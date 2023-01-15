from faker import Faker

from database.connect import session
from database.models import Professor


fake = Faker("en_US")


def create_professors():
    for _ in range(1, 5):
        professor = Professor(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(professor)
    session.commit()


if __name__ == '__main__':
    create_professors()
