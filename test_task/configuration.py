from dotenv import load_dotenv
import os

load_dotenv("configuration.env")

DB1_NAME=os.environ.get("DB1_NAME")
DB2_NAME=os.environ.get("DB2_NAME")

DB_HOST=os.environ.get("DB_HOST")
DB_PORT=os.environ.get("DB_PORT")
DB_PASS=os.environ.get("DB_PASS")
DB_USER=os.environ.get("DB_USER")


