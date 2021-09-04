from starlette.config import Config
from starlette.datastructures import Secret


config = Config(".env")

PROJECT_NAME = "Househeld Budget"
VERSION = "1.0.0"
API_PREFIX = "/api"
SECRET_KEY = config("SECRET_KEY", cast=Secret)
ACCESS_TOKEN_EXPIRE_MINUTES = config(
    "ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=7 * 24 * 60  # one week
)
JWT_ALGORITHM = config("JWT_ALGORITHM", cast=str, default="HS256")
JWT_AUDIENCE = config("JWT_AUDIENCE", cast=str, default="househeld-budget:auth")
JWT_TOKEN_PREFIX = config("JWT_TOKEN_PREFIX", cast=str, default="Bearer")


DEBUG_MODE: bool = False
HOST: str = "0.0.0.0"
PORT: int = 8000

MONGODB_DB = config("MONGODB_DB")
MONGODB_DB_TEST = config("MONGODB_DB_TEST")
MONGODB_HOST = config("MONGODB_HOST")
MONGODB_PORT = config("MONGODB_PORT", int)  ###49156
MONGODB_USERNAME = config("MONGODB_USERNAME")
MONGODB_PASSWORD = config("MONGODB_PASSWORD")
MONGODB_AUTH_SOURCE = config("MONGODB_DB")

##connect(host="mongodb://my_user:my_password@127.0.0.1:27017/my_db?authSource=my_db")
## MONGODB_URI = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}/{MONGODB_DB}?authSource={MONGODB_DB}"
## MONGODB_URI_TEST = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}/{MONGODB_DB_TEST}?authSource={MONGODB_DB_TEST}"

MONGODB_URI = (
    f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}"
)
MONGODB_URI_TEST = (
    f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}"
)


##MONGODB_URI = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.tksut.mongodb.net/{MONGODB_DB}?retryWrites=true&w=majority"
##MONGODB_URI_TEST = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.tksut.mongodb.net/{MONGODB_DB_TEST}?retryWrites=true&w=majority"
