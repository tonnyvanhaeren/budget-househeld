from typing import Callable
from fastapi import FastAPI
from app.db.tasks import init_database_async, shut_down_db_client


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await init_database_async(app)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await shut_down_db_client(app)

    return stop_app
