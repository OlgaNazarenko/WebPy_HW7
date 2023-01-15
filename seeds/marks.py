from random import randint
from sqlalchemy import func
from datetime import datetime
import random as rand

from faker import Faker

from database.connect import session
from database.models import Marks


faker = Faker()


def create_marks():
    for _ in range(1, 21):
        mark = Marks(
            mark=rand.randint(1, 5),
            students_id=rand.randint(1, 3),
            professor_id=rand.randint(1, 30),
            discipline_id=rand.randint(1, 5),
            lesson_date=faker.date_between_dates(date_start=datetime(2022, 12, 1), date_end=datetime(2023, 1, 14))
            )
        session.add(mark)
    session.commit()


if __name__ == '__main__':
    # print(random, type(random))
    create_marks()
