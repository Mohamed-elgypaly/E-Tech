from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User
from app.repositories.base import BaseRepository
from app.core.security import get_password_hash

class UserRepository(BaseRepository[User]):
    def __init__(self, db: AsyncSession):
        super().__init__(User, db)

    async def get_by_email(self, email: str) -> User | None:
        query = select(self.model).where(self.model.email == email)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def create(self, *, obj_in: dict[str, Any]) -> User:
        if "password" in obj_in:
            obj_in["hashed_password"] = get_password_hash(obj_in.pop("password"))
        return await super().create(obj_in=obj_in)
