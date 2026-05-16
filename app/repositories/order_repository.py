from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.order import Order
from app.repositories.base import BaseRepository

class OrderRepository(BaseRepository[Order]):
    def __init__(self, db: AsyncSession):
        super().__init__(Order, db)

    async def get_by_idempotency_key(self, key: str) -> Order | None:
        query = select(self.model).where(self.model.idempotency_key == key)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
