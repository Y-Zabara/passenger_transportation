#!/usr/bin/env python
import uvicorn
from fastapi import FastAPI

from api import router as api_router
from settings import config


app = FastAPI()
app.include_router(
    api_router,
    # prefix="/api",
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
