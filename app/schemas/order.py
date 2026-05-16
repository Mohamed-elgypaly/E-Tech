from pydantic import BaseModel, Field

class OrderBase(BaseModel):
    total_amount: float = Field(..., gt=0)

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    user_id: int
    status: str
    idempotency_key: str

    class Config:
        from_attributes = True
