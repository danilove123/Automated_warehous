import argparse
import csv
from sqlalchemy import func, and_, or_, case

from test_task.databases import sync_sessionmaker_1, sync_sessionmaker_2
from test_task.models import User, Post, Logs, EventType, SpaceType

parser = argparse.ArgumentParser(description='Получение статистики')
parser.add_argument('--login', type=str, help='Логин пользователя')
args = parser.parse_args()

user_login = args.login

user_login = "daniil228339"


def generate_statistics_comments():
    filename = "comments.csv"
    data = [
        ['user_login', 'post_header', 'author_login', 'comment_count']
    ]

    with sync_sessionmaker_1() as session_1:
        user = session_1.query(User).filter(User.login == user_login).first()

        with sync_sessionmaker_2() as session_2:
            # Возвращает список состоящий из кортежей (пост,кол-во комментов)
            # Пример: logs=[(0,5)] => Данный пользователь оставил 5 коментов к посту c post_id = 0
            logs = session_2.query(Logs.post_id, func.count(Logs.id)). \
                join(EventType). \
                join(SpaceType). \
                filter(EventType.name == "comment", SpaceType.name == "post", Logs.user_id == user.id). \
                group_by(Logs.post_id). \
                all()

            for tupl in logs:
                post_id = tupl[0]
                count_comments = tupl[1]
                post = session_1.query(Post).filter(Post.id == post_id).first()
                author = session_1.query(User).join(Post).filter(User.author_id == post.author_id).first()
                data.append([user_login, post.header, author.login, count_comments])

                # print(f"Логин пользователя: {user_login}\n"
                #       f"Заголовок: {post.header}\n"
                #       f"Логин автора: {author.login}\n"
                #       f"Кол-во коментов: {count_comments}")

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def generate_statistics_events():

    with sync_sessionmaker_1() as session_1:
        user = session_1.query(User).filter(User.login == user_login).first()

        with sync_sessionmaker_2() as session_2:

            date_list = session_2.query(Logs.datetime).filter(Logs.user_id == 1).order_by(Logs.datetime.desc()).all()

            logs = session_2.query(Logs.datetime, func.count(Logs.id)). \
                join(EventType). \
                join(SpaceType). \
                filter(EventType.name == "login", SpaceType.name == "global", Logs.user_id == 1). \
                group_by(Logs.datetime). \
                all()

            logs_1 = session_2.query(Logs.datetime, func.count(Logs.id)). \
                join(EventType). \
                join(SpaceType). \
                filter(EventType.name == "logout", SpaceType.name == "global", Logs.user_id == 1). \
                group_by(Logs.datetime). \
                all()

            logs_2 = session_2.query(Logs.datetime, func.count(Logs.id)). \
                join(EventType). \
                join(SpaceType). \
                filter(SpaceType.name == "blog", Logs.user_id == 1). \
                group_by(Logs.datetime). \
                all()

            print(date_list)



            #
            # print(logs_1)

            # for tupl in logs:
            #     date = tupl[0]
            #     count_comments = tupl[1]
            #     post = session_1.query(Post).filter(Post.id == post_id).first()
            #     author = session_1.query(User).join(Post).filter(User.author_id == post.author_id).first()
            #     data.append([user_login,post.header,author.login,count_comments])




generate_statistics_events()
