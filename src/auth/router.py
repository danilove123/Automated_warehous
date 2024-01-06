import json

from fastapi import Request, APIRouter
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from starlette.responses import FileResponse, JSONResponse

from src.utils import IgnoreUrl, Checker
from src.auth.models import metadata, Base, Users
from src.service import templates, oauth2, refresh_tokens, put_token_to_redis, put_token_to_redis_test
from src.conf import DELTA_TIME, SECRET_KEY, ALGORITHM
from src.database import async_sessionmaker, sync_sessionmaker, async_engine, engine
from src.utils import Hasher, Decoder, StringEditor
from fastapi import FastAPI, HTTPException, Depends, Response, APIRouter
from sqlalchemy import create_engine, text, insert, select, delete
from starlette import status
from fastapi.responses import RedirectResponse

from src.auth.schemas import User
from src.auth.exceptions import CustomException
import src.auth.exceptions as exc

app_auth = FastAPI()

app_auth.add_exception_handler(RequestValidationError, exc.handler_input_params)


def check_user_full(username: str, password: str):
    try:
        with sync_sessionmaker() as session:
            statement = select(Users.username, Users.hash_password)
            names_column = session.execute(statement)
    except:
        raise CustomException(500, "Error with request to DB")
    for element in names_column:
        if username == element[0] and Hasher.verify_password(password, element[1]):
            return True
    return False


@app_auth.post("/create_user", tags=["Authentication"])
async def create_user(user: User, response: Response):
    hash_password = Hasher.get_password_hash(user.password)
    try:
        with sync_sessionmaker() as session:
            new_user = Users(username=user.username, age=user.age, email=user.email,
                             hash_password=hash_password, phone=user.phone)

            session.add_all([new_user])
            session.commit()
            response.status_code = 201

        return "User successfully created"

    except IntegrityError:
        raise CustomException(status_code=409, detail="User already registered")
    except Exception:
        raise CustomException(status_code=500, detail="Cant create USER")


@app_auth.post("/login")
async def login(username: str, password: str, response: Response, request: Request):
    registrate = check_user_full(username, password)
    if not registrate:
        raise CustomException(401, "Not registered user")
    refresh_token = Decoder.create_jwt({"sub": username})
    access_token = Decoder.create_jwt({"sub": username})
    put_token_to_redis(username, refresh_token)
    response.status_code = 200
    response.set_cookie(key='refresh-token', value=refresh_token, httponly=True, secure=True, max_age=3600 * 24 * 7)
    response.set_cookie(key='access-token', value=access_token, httponly=True, secure=True, max_age=1800)
    return response


@app_auth.delete("/delete_user")
async def delete_user(username: str, password: str, response: Response):
    registrate = check_user_full(username, password)
    if registrate:
        try:
            with sync_sessionmaker() as session:
                stm = delete(Users).where(
                    Users.username == username)
                session.execute(stm)
                session.commit()
        except Exception:
            raise CustomException(500, "Cant delete user")
    else:
        return "There no such user to delete"
    response.status_code = status.HTTP_200_OK
    return "User successfully deleted"


@app_auth.post("/update_user")
async def update_user(username: str, new_username: str):
    try:
        async with async_sessionmaker() as session:
            user_obj = await session.get(Users, username)
            user_obj.username = new_username
            session.commit()
    except Exception:
        raise CustomException(status_code=500, detail="Cant update USER")

@app_auth.get("/registration")
async def get_a(request: Request, response: Response):
    return templates.TemplateResponse("page_registration.html", {"request": request})


@app_auth.get("/login_warehouse")
async def get_d(request: Request, response: Response):
    return templates.TemplateResponse("page_login.html", {"request": request})


@app_auth.get("/static/{name}/{name1}")
async def get_styles_css(request: Request):
    file = StringEditor.find_path_to_files(request)
    return FileResponse(f"templates/{file}")


@app_auth.get("/get_all_users")
async def get_all(response: Response):
    try:
        with sync_sessionmaker() as session:
            statement = select(Users.username, Users.age, Users.email, Users.phone)
            atr = session.execute(statement)
            lst: list = []
            for i in atr:
                lst.append(i)
            return str(lst)

    except Exception:
        raise CustomException(500, "Error with request to DB")

@app_auth.post("/create_tables")
async def create_tb():
    tabl_1 = Base.metadata.tables.get("Users")
    Base.metadata.create_all(bind=engine, tables=[tabl_1])

# ------------How to create a TABLE or remove ONE or FEW tables
# @app_auth.get("/rem")
# async def rem():
#     tabl = Base.metadata.tables.get("Shelf")
#     tabl_1 = Base.metadata.tables.get("Producers")
#     tabl_2 = Base.metadata.tables.get("Cell")
#     tabl_3 = Base.metadata.tables.get("Staff")
#     Base.metadata.create_all(bind=engine, tables=[tabl,tabl_1,tabl_2,tabl_3])

# tabl = Base.metadata.tables.get("Shelf")
# Base.metadata.drop_all(bind=engine, tables=[tabl])

# one = Base.metadata.tables.get("Shelf")
# Base.matadata.create_all(binf=engine,tables=[table]
