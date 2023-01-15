import random
from random import choice, randint

from database.connect import session
from database.models import Disciplines


def create_disciplines():
    for _ in range(1, 5):
        discipline = Disciplines(
            discipline=random.choice(['Python', 'Java', 'Korean', 'Japanese', 'QA']),
            group_id=random.randint(1, 3),
            professor_id=random.randint(1, 5)
        )
        session.add(discipline)
    session.commit()


if __name__ == '__main__':
    create_disciplines()
