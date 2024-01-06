import time
from fastapi import Request, APIRouter


from src.auth.router import app_auth
from src.service import templates
from fastapi import FastAPI, HTTPException, Depends, Response, APIRouter
from redis import asyncio as aioredis


from src.warehouse.router import app_warehouse

app = FastAPI()
app.mount("/auth", app_auth)
app.mount("/warehouse", app_warehouse)

# @app.on_event("startup")
# async def startup_database():
#     redis = aioredis.from_url("redis://172.17.0.1", encoding="utf8", decode_responses=True)
#     FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
# @app.on_event("shutdown")
# async def shutdown_database():
#     pass

# @app.middleware("http")
# async def add_process_time(request: Request, call_next):
#     # end_point = StringEditor.find_last_word_from_url(request)
#     # will_check_tokens = Checker.will_check_tokens(end_point,request)
#     #
#     # if  will_check_tokens:
#     #     access_token = request.cookies.get("access-token")
#     #     access_token = Decoder.decode_jwt(access_token)
#     #     if access_token is None:
#     #         refresh_token = request.cookies.get("refresh-token")
#     #         if refresh_token is None:
#     #             return RedirectResponse("/auth/main")
#     #         access_token, refresh_token = refresh_tokens(refresh_token)
#     #         if access_token is None:
#     #             return RedirectResponse("/auth/main")
#
#     response = await call_next(request)
#     return response

