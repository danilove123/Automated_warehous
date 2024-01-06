import asyncio
import datetime
import time
import jwt
from fastapi.security import OAuth2PasswordBearer
from starlette.templating import Jinja2Templates
import redis

from src.auth.exceptions import CustomException
from src.conf import SECRET_KEY, ALGORITHM, DELTA_TIME
from src.utils import Decoder

templates = Jinja2Templates(directory="templates")
oauth2 = OAuth2PasswordBearer("sdd")


r = redis.StrictRedis(
    host='localhost',
    port=6379,
    charset="utf-8",
    decode_responses=True
)


def put_token_to_redis(username: str, refresh_token: str):
    try:
        r.set(username, refresh_token)
    except Exception:
        raise CustomException(504, "Error with set value to Redis")


def refresh_tokens(refresh_token: str):
    username = Decoder.decode_jwt(refresh_token)
    if username is None: return None, None
    try:
        refresh_in_redis = r.get("username")
    except Exception:
        raise CustomException(504, "Error with get value from Redis")

    if refresh_in_redis == refresh_token:
        refresh_token = Decoder.create_jwt({"sub": username})
        access_token = Decoder.create_jwt({"sub": username})
        return access_token, refresh_token

    return None, None


async def put_token_to_redis_test(username: str, refresh_token: str):
    try:
        r.set(username, refresh_token)
    except Exception:
        raise CustomException(504, "Error with set value to Redis")