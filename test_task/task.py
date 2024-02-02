import argparse

from sqlalchemy import func

from test_task.databases import sync_sessionmaker_1, sync_sessionmaker_2
from test_task.models import User, Post, Logs, EventType, SpaceType

# parser = argparse.ArgumentParser(description='Получение статистики')
# parser.add_argument('--login', type=str, help='Логин пользователя')
# args = parser.parse_args()
#
# user_login = args.login

user_login = "daniil228339"

with sync_sessionmaker_2() as session_1:
    # logs = session_1.query(Logs).filter(Logs.space_type_id.name == "global")

    # Возвращает список состоящий из кортежей (пост,кол-во комментов)
    # Пример: logs=[(0,5)] => Данный пользователь оставил 5 коментов только к одному посту c post_id = 0
    logs = session_1.query(Logs.post_id, func.count(Logs.id)). \
        join(EventType). \
        join(SpaceType). \
        filter(EventType.name == "comment", SpaceType.name == "post", Logs.user_id == 2). \
        group_by(Logs.post_id). \
        all()

    for tupl in logs:
        post_id = tupl[0]

with sync_sessionmaker_1() as session_1:
    user = session_1.query(User).filter(User.login == user_login).first()
    # user_posts = session.query(Post).filter(Post.author_id == user.id).all()

    with sync_sessionmaker_2() as session_2:
        # logs = session_1.query(Logs).filter(Logs.space_type_id.name == "global")

        # Возвращает список состоящий из кортежей (пост,кол-во комментов)
        # Пример: logs=[(0,5)] => Данный пользователь оставил 5 коментов только к одному посту c post_id = 0
        logs = session_2.query(Logs.post_id, func.count(Logs.id)). \
            join(EventType). \
            join(SpaceType). \
            filter(EventType.name == "comment", SpaceType.name == "post", Logs.user_id == user.id). \
            group_by(Logs.post_id). \
            all()

        print(logs)
        for tupl in logs:
            post_id = tupl[0]
            count_comments = tupl[1]
            post = session_1.query(Post).filter(Post.id == post_id).first()
            author = session_1.query(User).join(Post).filter(User.author_id == post.author_id).first()
            print(f"Логин пользователя: {user_login}\n"
                  f"Заголовок: {post.header}\n"
                  f"Логин автора: {author.login}\n"
                  f"Кол-во коментов: {count_comments}")


