from sqlalchemy.exc import ProgrammingError, IntegrityError
from sqlalchemy import create_engine
from test_task.configuration import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB1_NAME, DB2_NAME
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import create_database
from datetime import datetime, timedelta

from test_task.models import Base_1, Base_2, Blog, Post, Logs, SpaceType, EventType, User

sync_engine_1 = create_engine(
    url=f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB1_NAME}",
    echo=False
)
sync_sessionmaker_1 = sessionmaker(bind=sync_engine_1, autocommit=False, autoflush=False, class_=Session)

sync_engine_2 = create_engine(
    url=f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB2_NAME}",
    echo=False
)
sync_sessionmaker_2 = sessionmaker(bind=sync_engine_2, autocommit=False, autoflush=False, class_=Session)


def create_db():
    try:
        create_database(sync_engine_1.url)
        # create_database(sync_engine_2.url)
    except ProgrammingError:
        print("Одна или все БД уже есть на сервере Postgres")


def create_tables():
    Base_1.metadata.create_all(sync_engine_1)
    # Base_2.metadata.create_all(sync_engine_2)


def fill_tables_db1():
    try:
        with sync_sessionmaker_1() as session:

            user_0 = User(id=0, email="makintosh@mail.ru", login="daniil228339", author_id=0)
            user_1 = User(id=1, email="RonaldoMakluny@gmail.ru", login="ElenaRussia")
            user_2 = User(id=2, email="GogoStatoru@mail.ru", login="VladimirPizza")
            user_3 = User(id=3, email="vlru2024@yandex.com", login="Evgeniy_malachov", author_id=1)
            user_4 = User(id=4, email="NarutoUdzumaki@mail.ru", login="Vasiliy_Voronzov", author_id=2)
            user_5 = User(id=5, email="DaniilDanilov@gmail.ru", login="OLEKSEY", author_id=3)

            blog_0 = Blog(id=0, author_id=0, name="Materials", description="Blog_about_materials")
            blog_1 = Blog(id=1, author_id=0, name="Biology", description="Blog_about_biology")
            blog_2 = Blog(id=2, author_id=2, name="Box", description="Blog_about_box")
            blog_3 = Blog(id=3, author_id=2, name="Games", description="Blog_about_games")
            blog_4 = Blog(id=4, author_id=3, name="Diving", description="Blog_about_diving")
            blog_5 = Blog(id=5, author_id=3, name="Jinja", description="Blog_about_jinja")

            post_0 = Post(id=0, header="History Materials", text="History materials contains a lot off....",
                          author_id=0, blog_id=0)
            post_1 = Post(id=1, header="Intresting biology", text="Biology it is....", author_id=0, blog_id=1)
            post_2 = Post(id=2, header="History of box industry", text="World box records starts with....", author_id=0,
                          blog_id=2)
            post_3 = Post(id=3, header="Gamse 2024", text="The newest game Last of us....", author_id=0, blog_id=3)
            post_4 = Post(id=4, header="What is DIVING LICENCE?", text="Diving licence....", author_id=0, blog_id=4)
            post_5 = Post(id=5, header="JINJA", text="Jinja templates allow you....", author_id=0, blog_id=5)

            session.add_all([user_0, user_1, user_2, user_3, user_4, user_5])
            session.commit()
            session.add_all([blog_0, blog_1, blog_2, blog_3, blog_4, blog_5])
            session.commit()
            session.add_all([post_0, post_1, post_2, post_3, post_4, post_5])
            session.commit()

    except IntegrityError:
        print("Один или несколько объектов уже существуют в таблицах БД-db1")


def fill_tables_db2():
    time_0 = datetime.now()
    time_1 = time_0 + timedelta(hours=1)
    time_2 = time_1 + timedelta(hours=1)
    time_3 = time_2 + timedelta(hours=1)
    time_4 = time_3 + timedelta(hours=1)
    time_5 = time_4 + timedelta(hours=1)
    time_6 = time_5 + timedelta(hours=1)
    time_7 = time_6 + timedelta(hours=1)

    with sync_sessionmaker_2() as session:
        space_type_0 = SpaceType(id=0, name="global")
        space_type_1 = SpaceType(id=1, name="blog")
        space_type_2 = SpaceType(id=2, name="post")

        event_type_0 = EventType(id=0, name="login")
        event_type_1 = EventType(id=1, name="comment")
        event_type_2 = EventType(id=2, name="create_post")
        event_type_3 = EventType(id=3, name="delete_post")
        event_type_4 = EventType(id=4, name="logout")

        log_0 = Logs(id=0, datetime=time_0, user_id=0, space_type_id=0, event_type_id=4)
        log_1 = Logs(id=1, datetime=time_1, user_id=1, space_type_id=0, event_type_id=0)
        log_2 = Logs(id=2, datetime=time_2, user_id=1, space_type_id=1, event_type_id=2)
        log_3 = Logs(id=3, datetime=time_5, user_id=1, space_type_id=1, event_type_id=2)
        log_4 = Logs(id=4, datetime=time_6, user_id=2, space_type_id=1, event_type_id=3)
        log_5 = Logs(id=5, datetime=time_3, user_id=1, space_type_id=1, event_type_id=2)
        log_6 = Logs(id=6, datetime=time_2, user_id=2, space_type_id=2, post_id=0, event_type_id=1)
        log_7 = Logs(id=7, datetime=time_0, user_id=3, space_type_id=2, post_id=0, event_type_id=1)
        log_8 = Logs(id=8, datetime=time_2, user_id=4, space_type_id=2, post_id=0, event_type_id=1)
        log_9 = Logs(id=9, datetime=time_0, user_id=0, space_type_id=2, post_id=0, event_type_id=1)
        log_10 = Logs(id=10, datetime=time_7, user_id=0, space_type_id=2, post_id=0, event_type_id=1)
        log_11 = Logs(id=11, datetime=time_2, user_id=1, space_type_id=2, post_id=0, event_type_id=1)
        log_12 = Logs(id=12, datetime=time_7, user_id=2, space_type_id=2, post_id=0, event_type_id=1)
        log_13 = Logs(id=13, datetime=time_2, user_id=2, space_type_id=2, post_id=0, event_type_id=1)
        log_14 = Logs(id=14, datetime=time_7, user_id=5, space_type_id=2, post_id=0, event_type_id=1)
        log_15 = Logs(id=15, datetime=time_0, user_id=3, space_type_id=2, post_id=0, event_type_id=1)
        log_16 = Logs(id=16, datetime=time_7, user_id=2, space_type_id=2, post_id=1, event_type_id=1)

        session.add_all([space_type_0, space_type_1, space_type_2])
        session.add_all([event_type_0, event_type_1, event_type_2, event_type_3, event_type_4])
        session.commit()
        session.add_all(
            [log_0, log_1, log_2, log_3, log_4, log_5, log_6, log_7, log_8, log_9, log_10, log_11, log_12, log_13,
             log_14, log_15, log_16])
        session.commit()


def drop_all_tables():
    Base_2.metadata.drop_all(sync_engine_2)


# create_db()
# create_tables()
# fill_tables_db1()
# drop_all_tables()


'''
user = session.query(User).filter(User.name == "John").first()
if user:
    session.delete(user)
    session.commit()'''

''' 
comments = db1_session.query(Author.login, Post.header, Author.login, Post.header,
                                db1_session.query(Comment).filter_by(author_id=user.id).count()) \
                    .join(Post, Author, Comment) \
                    .filter(Author.login == user.login) \
                    .all()
                    
                    '''
