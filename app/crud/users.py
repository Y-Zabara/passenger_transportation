from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy  import select, Result

from core.schemas.users import UserCreate, UserBase
from core.models.users import Users

async def get_users(session: AsyncSession) -> list[Users]:
    stmt = select(Users).order_by(Users.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def get_user_by_id(
    session: AsyncSession,
    id: int,
    ) -> Users | None:
    return await session.get(Users, id)


async def create_user(
    session: AsyncSession,
    user_in: UserCreate,
    ) -> Users:

    user = Users(**user_in.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def update_user(
    session: AsyncSession,
    user: Users,
    user_update: UserBase,
) -> Users:
    for name, value in user_update.model_dump().items():
        setattr(user, name, value)
    await session.commit()
    return user


async def delete_user(
    session: AsyncSession,
    user: Users,
) -> None:
    await session.delete(user)
    await session.commit()


