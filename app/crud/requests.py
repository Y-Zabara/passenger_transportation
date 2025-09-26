from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy  import select, Result

from core.schemas.requests import RequestCreate, RequestBase
from core.models.requests import Requests

async def get_requests(session: AsyncSession) -> list[Requests]:
    stmt = select(Requests).order_by(Requests.id)
    result: Result = await session.execute(stmt)
    requests = result.scalars().all()
    return list(requests)


async def get_request_by_id(
    session: AsyncSession,
    id: int,
    ) -> Requests | None:

    return await session.get(Requests, id)


async def create_request(
    session: AsyncSession,
    request_in: RequestCreate,
    ) -> Requests:

    request = Requests(**request_in.model_dump())
    session.add(request)
    await session.commit()
    await session.refresh(request)
    return request


async def update_request(
    session: AsyncSession,
    request: Requests,
    request_update: RequestBase,
) -> Requests:
    for name, value in request_update.model_dump().items():
        setattr(request, name, value)
    await session.commit()
    return request


async def delete_request(
    session: AsyncSession,
    request: Requests,
) -> None:
    await session.delete(request)
    await session.commit()

