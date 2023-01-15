from random import random

from seeds.professors import create_professors
from seeds.students import create_students
from seeds.group import create_groups
from seeds.marks import create_marks
from seeds.disciplines import create_disciplines


if __name__ == '__main__':
    create_groups()
    create_professors()
    create_students()
    create_disciplines()
    create_marks()
