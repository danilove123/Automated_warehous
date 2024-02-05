import argparse
import csv
from sqlalchemy import func, case

from test_task.databases import sync_sessionmaker_1, sync_sessionmaker_2
from test_task.models import User, Post, Logs, EventType, SpaceType


def generate_statistics_comments(user_login):
    filename = "comments.csv"
    data = [
        ['user_login', 'post_header', 'author_login', 'comment_count']
    ]

    with sync_sessionmaker_1() as session_1:
        user = session_1.query(User).filter(User.login == user_login).first()

        with sync_sessionmaker_2() as session_2:
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

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def generate_statistics_events(user_login):
    filename = "general.csv"
    data = [
        ['date', 'count_login', 'count_logout', 'count_events']
    ]

    with sync_sessionmaker_1() as session_1:
        user = session_1.query(User).filter(User.login == user_login).first()

        with sync_sessionmaker_2() as session_2:

            date_list = session_2.query(func.date_trunc('day', Logs.datetime)). \
                filter(Logs.user_id == user.id). \
                group_by(func.date_trunc('day', Logs.datetime)). \
                order_by(func.date_trunc('day', Logs.datetime).desc()). \
                all()

            date_list = [date[0].strftime("%Y:%m:%d") for date in date_list]
            print(date_list)

            logs = session_2.query(func.date_trunc('day', Logs.datetime), func.count(Logs.id)). \
                join(EventType). \
                join(SpaceType). \
                filter(EventType.name == "login", SpaceType.name == "global", Logs.user_id == user.id). \
                group_by(func.date_trunc('day', Logs.datetime)). \
                all()

            dict_login = {}
            for e in logs:
                day = e[0].strftime("%Y:%m:%d")
                count_login = e[1]
                dict_login.update({day: count_login})

            logs_1 = session_2.query(Logs.datetime, func.count(Logs.id)). \
                join(EventType). \
                join(SpaceType). \
                filter(EventType.name == "logout", SpaceType.name == "global", Logs.user_id == user.id). \
                group_by(Logs.datetime). \
                all()

            dict_logout = {}
            for e in logs_1:
                day = e[0].strftime("%Y:%m:%d")
                count_login = e[1]
                dict_logout.update({day: count_login})

            logs_2 = session_2.query(Logs.datetime, func.count(Logs.id)). \
                join(EventType). \
                join(SpaceType). \
                filter(SpaceType.name == "blog", Logs.user_id == user.id). \
                group_by(Logs.datetime). \
                all()

            dict_events_blog = {}
            for e in logs_2:
                day = e[0].strftime("%Y:%m:%d")
                count_login = e[1]
                dict_events_blog.update({day: count_login})

            for date in date_list:
                count_login = dict_login.get(date)
                if count_login is None: count_login = 0

                count_logout = dict_logout.get(date)
                if count_logout is None: count_logout = 0

                count_events = dict_events_blog.get(date)
                if count_events is None: count_events = 0

                data.append([date, count_login, count_logout, count_events])

            print(data)


def gira():
    filename = "general.csv"
    data = [
        ['date', 'count_login', 'count_logout', 'count_events']
    ]
    with sync_sessionmaker_1() as session_1:
        user = session_1.query(User).filter(User.login == "ElenaRussia").first()

        with sync_sessionmaker_2() as session_2:

            logs = session_2.query(func.date_trunc('day', Logs.datetime),
                                 func.count(case((EventType.name == "login", Logs.id))),
                                 func.count(case((EventType.name == "logout", Logs.id))),
                                 func.count(case((SpaceType.name == "blog", Logs.id)))) \
                .join(EventType) \
                .join(SpaceType) \
                .filter(Logs.user_id == 1) \
                .group_by(func.date_trunc('day', Logs.datetime)) \
                .order_by(func.date_trunc('day', Logs.datetime).desc()) \
                .all()

            for log in logs:
                date = log[0].strftime("%Y:%m:%d")
                count_login = log[1]
                count_logout = log[2]
                count_events = log[3]
                data.append([date, count_login, count_logout, count_events])


            print(data)


def main():
    parser = argparse.ArgumentParser(description='Получение статистики')
    parser.add_argument('--login', type=str, help='Логин пользователя')
    args = parser.parse_args()

    user_login = args.login

    user_login = "ElenaRussia"

    if user_login is not None:
        # generate_statistics_comments(user_login)
        generate_statistics_events(user_login)
        gira()


if __name__ == "__main__":
    main()
