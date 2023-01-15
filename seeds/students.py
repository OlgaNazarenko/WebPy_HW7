import random

from faker import Faker

from database.connect import session
from database.models import Students


fake = Faker("en_US")


def create_students():
    for _ in range(1, 31):
        student = Students(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            group_id=random.randint(1, 4)
        )
        session.add(student)
    session.commit()


if __name__ == '__main__':
    create_students()
