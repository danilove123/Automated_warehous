import json
import uuid

from datetime import datetime, timezone

from fastapi import Request, APIRouter
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from starlette.responses import FileResponse, JSONResponse

from src.utils import IgnoreUrl, Checker
from src.warehouse.models import metadata, Base, Producers, Staff
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
from src.warehouse.models import Shelf, Pallet

app_warehouse = FastAPI()

app_warehouse.add_exception_handler(RequestValidationError, exc.handler_input_params)


def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


@app_warehouse.get("/check")
async def check_cell(id_cell: str):
    async with async_sessionmaker() as session:
        someth = select(Shelf.id_cell)
        id_cells = await session.execute(someth)
        lst = []
        for element in id_cells:
            lst.append(element[0])
        if id_cell in lst:
            el_0 = '00'
            if el_0 not in lst:
                return el_0
            for i in range(1, 8, 1):
                el_3 = f'{i}{i}'
                if el_3 not in lst:
                    return el_3
                for k in range(1, i + 1):
                    el_1 = f'{i - k}{i}'
                    if el_1 not in lst:
                        return el_1
                    el_2 = f'{i}{i - k}'
                    if el_2 not in lst:
                        return el_2

        return id_cell


@app_warehouse.get("/get_html/{html_page}")
async def get_d(html_page:str,request: Request, response: Response):
    return templates.TemplateResponse(f"{html_page}.html", {"request": request})


@app_warehouse.post("/add_pallet")
async def add_pallet(unparsed: str):
    tabl_2 = Base.metadata.tables.get("Pallet")
    Base.metadata.create_all(bind=engine, tables=[tabl_2])
    array_parsed = StringEditor.unparsing_str(unparsed)
    id_pallet = str(uuid.uuid4())
    result = await check_cell("10")
    list_products = []
    async with async_sessionmaker() as session:
        for i in range(2, len(array_parsed), 1):
            new_product = Pallet(id_producer=array_parsed[0], type=array_parsed[1], id_product=array_parsed[i],
                                 id_pallet=id_pallet)
            list_products.append(new_product)

        list_products.append(Shelf(id_cell=result, id_pallet=id_pallet, id_producer=array_parsed[0],added_at=datetime.utcnow()))
        session.add_all(list_products)
        await session.commit()

    return result


@app_warehouse.delete("/drop_tables")
async def drop_tb():
    tabl_4 = Base.metadata.tables.get("Shelf")
    Base.metadata.drop_all(bind=engine, tables=[tabl_4])


@app_warehouse.post("/create_tables")
async def create_tb():
    tabl_0 = Base.metadata.tables.get("Producers")
    tabl_2 = Base.metadata.tables.get("Staff")

    lst_staff = []
    lst_producers = []
    try:
        with sync_sessionmaker() as session:
            lst_staff.append(Staff(id_staff='12345', name='Naruto Udzumaki', specification='Garden'))
            lst_staff.append(Staff(id_staff='12340', name='Gojo Satoru', specification='Wood'))
            lst_staff.append(Staff(id_staff='12341', name='Todo Urakadaki', specification='Wood'))
            lst_staff.append(Staff(id_staff='12342', name='Tanjiro Kamado', specification='Wood'))
            lst_staff.append(Staff(id_staff='12343', name='Gats Berserkovskyi', specification='Hardware products'))
            lst_staff.append(Staff(id_staff='12344', name='Sukuna Remen', specification='Сement'))
            lst_staff.append(Staff(id_staff='12346', name='Padme Amidala', specification='Hardware products'))
            lst_staff.append(Staff(id_staff='12347', name='Kopatych Smecharikovskiy', specification='Hardware products'))
            lst_staff.append(Staff(id_staff='12348', name='Genadiy bukin', specification='Open soft'))
            lst_staff.append(Staff(id_staff='12349', name='Gosha Kucenko', specification='Open soft'))

            lst_producers.append(Producers(id_producer='0000', name='Lerua', city='Vladivostok'))
            lst_producers.append(Producers(id_producer='0001', name='Freken Bok', city='Vladivostok'))
            lst_producers.append(Producers(id_producer='0002', name='Stroi DV', city='Vladivostok'))
            lst_producers.append(Producers(id_producer='0003', name='Zastroyshik', city='Artem'))
            lst_producers.append(Producers(id_producer='0004', name='Drom', city='Vladivostok'))
            lst_producers.append(Producers(id_producer='0005', name='Texnodrom', city='Khabarovsk'))
            lst_producers.append(Producers(id_producer='0006', name='Lerua_A', city='Vladivostok'))
            lst_producers.append(Producers(id_producer='0007', name='IKEA', city='Moscow'))
            lst_producers.append(Producers(id_producer='0008', name='IKEA_0', city='Vladivostok'))

            session.add_all(lst_staff)
            session.add_all(lst_producers)
            session.commit()

    except Exception:
        print("Cant add new shelf")

@app_warehouse.post("/add_pallets")
async def add_pallets():
    tabl = Base.metadata.tables.get("Shelf")
    Base.metadata.create_all(bind=engine, tables=[tabl])

    try:
        with sync_sessionmaker() as session:
            pallet_0 = Shelf(id_cell='00', id_pallet='12234544', id_producer='123322112M')
            pallet_1 = Shelf(id_cell='01', id_pallet='12234543', id_producer='123322112M')
            pallet_2 = Shelf(id_cell='10', id_pallet='12234542', id_producer='123322112M')
            pallet_3 = Shelf(id_cell='11', id_pallet='12234540', id_producer='123322112K')
            pallet_4 = Shelf(id_cell='20', id_pallet='12234549', id_producer='123322112L')
            pallet_5 = Shelf(id_cell='02', id_pallet='12234546', id_producer='123322112R')
            pallet_6 = Shelf(id_cell='60', id_pallet='12234545', id_producer='23322112T')

            session.add_all([pallet_0,pallet_1,pallet_2,pallet_3,pallet_4,pallet_5,pallet_6])
            session.commit()

    except Exception:
        print("Cant add new shelf")


@app_warehouse.get("/get_shelfs")
async def get_all(response: Response):
    try:
        with sync_sessionmaker() as session:
            statement = select(Shelf.id_cell, Shelf.id_pallet, Shelf.id_producer, Shelf.added_at)
            atr = session.execute(statement)
            lst: list = []
            lst_0: list = []
            k = 0
            for i in atr:
                for l in range(len(i)):
                    if l == 3:
                        date = utc_to_local(i[l])
                        date_time = (str(date.date()) + " " + str(i[3].time().strftime('%H:%M:%S')))
                        lst_0.append(date_time)
                    else:
                        lst_0.append(i[l])
                lst.append(lst_0)
                k = k + 1
                lst_0 = []

            return str(lst)

    except Exception:
        raise CustomException(500, "Error with request to DB")

@app_warehouse.get("/get_producers")
async def get_all(response: Response):
    try:
        with sync_sessionmaker() as session:
            statement = select(Producers.id_producer,Producers.name)
            atr = session.execute(statement)
            lst: list = []
            for i in atr:
                lst.append(i)
            return str(lst)

    except Exception:
        raise CustomException(500, "Error with request to DB")

@app_warehouse.get("/get_staff")
async def get_all(response: Response):
    try:
        with sync_sessionmaker() as session:
            statement = select(Staff.id_staff,Staff.name)
            atr = session.execute(statement)
            lst: list = []
            for i in atr:
                lst.append(i)
            return str(lst)

    except Exception:
        raise CustomException(500, "Error with request to DB")





@app_warehouse.get("/get_staff")
async def get_all(response: Response):
    try:
        with sync_sessionmaker() as session:
            statement = select(Shelf.id_cell, Shelf.id_pallet, Shelf.id_producer, Shelf.added_at)
            atr = session.execute(statement)
            lst: list = []
            lst_0: list = []
            k = 0
            for i in atr:
                for l in range(len(i)):
                    if l == 3:
                        date = utc_to_local(i[l])
                        date_time = (str(date.date()) + " " + str(i[3].time().strftime('%H:%M:%S')))
                        lst_0.append(date_time)
                    else:
                        lst_0.append(i[l])
                lst.append(lst_0)
                k = k + 1
                lst_0 = []

            return str(lst)

    except Exception:
        raise CustomException(500, "Error with request to DB")




@app_warehouse.get("/get_html/static/{name}/{name1}")
async def get_styles_css(request: Request):
    file = StringEditor.find_path_to_files(request)
    return FileResponse(f"templates/{file}")

# ------------How to create a TABLE or remove ONE or FEW tables
# @app_warehouse.get("/rem")
# async def rem():
#     #tabl = Base.metadata.tables.get("Sorting")
#     tabl_2 = Base.metadata.tables.get("Cell")
#     Base.metadata.create_all(bind=engine, tables=[tabl_2])

# tabl = Base.metadata.tables.get("Shelf")
# Base.metadata.drop_all(bind=engine, tables=[tabl])

# one = Base.metadata.tables.get("Shelf")
# Base.matadata.create_all(binf=engine,tables=[table]
