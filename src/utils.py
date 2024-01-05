import json
from enum import Enum

from passlib.context import CryptContext
import datetime
import jwt
from starlette.requests import Request

from src.auth.exceptions import CustomException
from src.conf import SECRET_KEY, ALGORITHM, DELTA_TIME

pwd_contex = CryptContext(schemes=["bcrypt"], deprecated="auto")


class IgnoreUrl(Enum):
    login_window = "main"
    registration_window = "registration"

    swagger_utils_1 = "docs"
    swagger_utils_2 = "openapi.json"

    create_user = "create_user"
    get_user = "get_user"
    login = "login"

    css = ".css"
    js = ".js"
    gif = ".gif"



class Hasher:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_contex.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        return pwd_contex.hash(password)


class Decoder:
    @staticmethod
    def create_jwt(data: dict):
        data.update({"exp": datetime.datetime.now() + datetime.timedelta(seconds=int(DELTA_TIME))})
        return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def decode_jwt(token: str):
        try:
            return jwt.decode(token, SECRET_KEY, ALGORITHM).get("sub")
        except Exception:
            raise CustomException(504, "Error with decoding")


class StringEditor:
    @staticmethod
    def find_last_word_from_url(request: Request):
        url = request.url
        array = str(url).split("/")
        end_point = array[len(array) - 1]
        end_point = end_point.split("?")[0]
        return end_point
    @staticmethod
    def find_path_to_files(request: Request):
        url = str(request.url)
        try:
            return url.split("static", 1)[1]
        except IndexError:
            raise CustomException(404,"Cant download static")

    @staticmethod
    def unparsing_str(stroke:str):
        array_to_return = []
        try:
            stroke = stroke[1:-1]
            dict_format = json.loads(stroke)
            array_to_return.append(dict_format['id_producer'])
            array_to_return.append(dict_format['type'])
            del dict_format['id_producer']
            del dict_format['type']
            for element in dict_format:
                value = dict_format.get(element)
                array_to_return.append(value)
            return array_to_return

        except :
            print("Unparsing_str: Ну что за хуету ты мне сюда кидаешь?")





class Checker:
    @staticmethod
    def will_check_tokens(endpoint: str, request: Request):
        for element in IgnoreUrl:
            if endpoint == element.value or IgnoreUrl.swagger_utils_1.value in str(request.url) or IgnoreUrl.css.value in endpoint or IgnoreUrl.js.value in endpoint or IgnoreUrl.gif.value in endpoint:
                return False
        return True

