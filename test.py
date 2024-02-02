from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Подключение к базе данных db1_scheme.png
db1_engine = create_engine('postgresql://username:password@host:port/db1')
db1_Session = sessionmaker(bind=db1_engine)
db1_session = db1_Session()

# Подключение к базе данных db2_scheme.png
db2_engine = create_engine('postgresql://username:password@host:port/db2')
db2_Session = sessionmaker(bind=db2_engine)
db2_session = db2_Session()

# Определение моделей для базы данных db1_scheme.png
db1_Base = declarative_base()


class Blog(db1_Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('author.id'))
    name = Column(String)
    description = Column(String)


class Author(db1_Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    login = Column(String)
    email = Column(String)


class Post(db1_Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    header = Column(String)
    text = Column(String)
    author_id = Column(Integer, ForeignKey('author.id'))
    blog_id = Column(Integer, ForeignKey('blog.id'))

    author = relationship("Author")
    blog = relationship("Blog")


# Определение моделей для базы данных db2_scheme.png
db2_Base = declarative_base()


class Logs(db2_Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    datetime = Column(String)
    user_id = Column(Integer)
    space_type_id = Column(Integer, ForeignKey('space_type.id'))
    event_type_id = Column(Integer, ForeignKey('event_type.id'))


class SpaceType(db2_Base):
    __tablename__ = 'space_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class EventType(db2_Base):
    __tablename__ = 'event_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)


# Получение статистики по пользователю и формирование CSV-файлов
def generate_statistics(user):
    # Поиск комментариев пользователя и формирование comments.csv
    comments = db1_session.query(Author.login, Post.header, Author.login, Post.header,
                                 db1_session.query(Comment).filter_by(author_id=user.id).count()) \
        .join(Post, Author, Comment) \
        .filter(Author.login == user.login) \
        .all()

    with open('comments.csv', 'w') as f:
        f.write("Author Login, Post Header, Author Login, Comment Count\n")
        for comment in comments:
            f.write(','.join(str(field) for field in comment) + '\n')

    # Поиск действий пользователя и формирование general.csv
    general_stats = db2_session.query(Logs.datetime,
                                      db2_session.query(Logs).filter_by(event_type_id=1).count(),
                                      db2_session.query(Logs).filter_by(event_type_id=2).count(),
                                      db2_session.query(Logs).join(SpaceType).filter(SpaceType.name == 'blog').count()) \
        .join(EventType, SpaceType) \
        .filter(Logs.user_id == user.id) \
        .all()

    with open('general.csv', 'w') as f:
        f.write("Datetime, Login Count, Logout Count, Blog Action Count\n")
        for stats in general_stats:
            f.write(','.join(str(field) for field in stats) + '\n')


# Пример использования
user_login = 'example_user'
user = db1_session.query(Author).filter_by(login=user_login).first()
generate_statistics(user)