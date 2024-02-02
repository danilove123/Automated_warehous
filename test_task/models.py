from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base_1 = declarative_base()


class User(Base_1):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    email = Column(String, unique=True)
    author_id = Column(Integer, nullable=True, unique=True)


class Blog(Base_1):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.author_id'),nullable=False)
    name = Column(String)
    description = Column(String)


class Post(Base_1):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    header = Column(String)
    text = Column(String)
    author_id = Column(Integer, ForeignKey('user.author_id'),nullable=False)
    blog_id = Column(Integer, ForeignKey('blog.id'),nullable=False)

    author = relationship("User")
    blog = relationship("Blog")


Base_2 = declarative_base()


class Logs(Base_2):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime)
    user_id = Column(Integer)
    post_id = Column(Integer, nullable=True)
    space_type_id = Column(Integer, ForeignKey('space_type.id'))
    event_type_id = Column(Integer, ForeignKey('event_type.id'))


class SpaceType(Base_2):
    __tablename__ = 'space_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class EventType(Base_2):
    __tablename__ = 'event_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)
