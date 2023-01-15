import random
from random import choice

from faker import Faker

from database.connect import session
from database.models import Group

NAME: list = ['A', 'B', 'C', 'D']


def create_groups():
    for _ in range(1, 5):
        groups = Group(
            title=random.choice(['A', 'B', 'C', 'D'])
        )
        session.add(groups)
    session.commit()


if __name__ == '__main__':
    create_groups()
