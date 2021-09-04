import os
from fastapi import FastAPI
import logging
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)
from odmantic.engine import AIOEngine


from app.core.config import MONGODB_DB_TEST, MONGODB_URI, MONGODB_DB, MONGODB_URI_TEST


logger = logging.getLogger(__name__)


async def init_database_async(app: FastAPI) -> None:
    MONGO_URI = f"{MONGODB_URI_TEST}" if os.environ.get("TESTING") else MONGODB_URI
    MONGO_DATABASE = f"{MONGODB_DB_TEST}" if os.environ.get("TESTING") else MONGODB_DB

    try:
        mongodb_client: AsyncIOMotorClient = AsyncIOMotorClient(MONGO_URI)
        mongodb_engine = AIOEngine(motor_client=mongodb_client, database=MONGO_DATABASE)

        logger.info("Initialize mongodb client connection")

        mongodb_database: AsyncIOMotorDatabase = mongodb_client[MONGODB_DB]
        mongodb_user_collection: AsyncIOMotorCollection = mongodb_database["users"]

        logger.info("Initialize mongodb user collection indexes")
        # create user indexes

        await mongodb_user_collection.create_index(
            "email", unique=True, name="unique_index_email"
        )
        await mongodb_user_collection.create_index("lastname", name="index_last_name")

        app.state._mongo_client = mongodb_client
        app.state._mongo_engine = mongodb_engine

    except Exception as e:
        logger.warn("--- Mongo db connection ERROR ---")
        logger.warn(e)
        logger.warn("--- Mongo db connection ERROR ---")


def shut_down_db_client(app: FastAPI) -> None:
    logging.info("Close mongodb client connection")
    app.state._mongo_client.close()


# async def connect_to_db(app: FastAPI) -> None:
#     DB_URL = f"{DATABASE_URL}_test" if os.environ.get("TESTING") else DATABASE_URL
#     database = Database(DB_URL, min_size=2, max_size=10)

#     try:
#         await database.connect()
#         app.state._db = database
#     except Exception as e:
#         logger.warn("--- DB CONNECTION ERROR ---")
#         logger.warn(e)
#         logger.warn("--- DB CONNECTION ERROR ---")


# async def close_db_connection(app: FastAPI) -> None:
#     try:
#         await app.state._db.disconnect()
#     except Exception as e:
#         logger.warn("--- DB DISCONNECT ERROR ---")
#         logger.warn(e)
#         logger.warn("--- DB DISCONNECT ERROR ---")
