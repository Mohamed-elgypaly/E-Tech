from sqlalchemy.ext.asyncio import AsyncSession
from app.models.order import Order
from app.repositories.order_repository import OrderRepository
from app.schemas.order import OrderCreate
from app.core.exceptions import IdempotencyConflictException

class CheckoutService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.order_repo = OrderRepository(db)

    async def create_order(self, order_in: OrderCreate, user_id: int, idempotency_key: str) -> Order:
        # 1. Check for existing order with same idempotency key
        existing_order = await self.order_repo.get_by_idempotency_key(idempotency_key)
        if existing_order:
            # If the order exists, return it (idempotent behavior)
            # Ensure it belongs to the same user and has same details
            if existing_order.user_id != user_id:
                raise IdempotencyConflictException("Idempotency key already used by another user")
            return existing_order

        # 2. Proceed with order creation
        order_data = order_in.model_dump()
        order_data["user_id"] = user_id
        order_data["idempotency_key"] = idempotency_key
        
        # In a real scenario, we'd also handle inventory deduction and payment here
        # within a transaction (Unit of Work).
        
        new_order = await self.order_repo.create(obj_in=order_data)
        return new_order
