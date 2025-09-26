#!/usr/bin/env python
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI

from api import router as api_router
from settings import config
from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    #create table
    #async with db_helper.engine.begin() as conn:
        #await conn.run_sync(Base.metadata.create_all)
    yield
    await db_helper.dispose()


app = FastAPI(
    lifespan=lifespan,
)
app.include_router(
    api_router,
    prefix="/api",
)


def main():
    uvicorn.run(
        "main:app",
        host=config.run.host,
        port=config.run.port,
        reload=True,
    )


if __name__ == "__main__":
    main()
