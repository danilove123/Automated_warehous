import argparse

from test_task.databases import sync_sessionmaker_1
from test_task.models import Author, Post

# parser = argparse.ArgumentParser(description='Получение статистики')
# parser.add_argument('--login', type=str, help='Логин пользователя')
# args = parser.parse_args()
#
# user_login = args.login

user_login = "daniil228339"
with sync_sessionmaker_1() as session:
    user = session.query(Author).filter(Author.login == user_login).first()
    user_posts = session.query(Post).filter(Post.author_id == user.id).all()

    print(user_posts)
