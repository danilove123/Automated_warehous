from secrets import token_urlsafe

from dotenv import load_dotenv
import os

load_dotenv("config.env")

DB_HOST=os.environ.get("DB_HOST")
DB_PORT=os.environ.get("DB_PORT")
DB_NAME=os.environ.get("DB_NAME")
DB_USER=os.environ.get("DB_USER")
DB_PASS=os.environ.get("DB_PASS")

SECRET_KEY = token_urlsafe(16)
ALGORITHM = os.environ.get("ALGORITHM")
DELTA_TIME = os.environ.get("DELTA_TIME")

