import argparse
import sys
from sqlalchemy.exc import SQLAlchemyError


from run_seed import create_groups, create_professors, create_students, create_marks, create_disciplines


parser = argparse.ArgumentParser(description='The list')
parser.add_argument('--action', help='Command: create_groups, create_professors, create_students, create_marks, '
                                     'create_disciplines')
parser.add_argument('--groups')
parser.add_argument('--professors')
parser.add_argument('--students')
parser.add_argument('--marks')
parser.add_argument('--disciplines')

arguments = parser.parse_args()
my_arg = vars(arguments)


action = my_arg.get('action')
groups = my_arg.get('groups')
professors = my_arg.get('professors')
students = my_arg.get('students')
marks = my_arg.get('marks')
disciplines = my_arg.get('disciplines')


def main():
    match action:
        case 'create':
            create_info(groups=groups, professors=professors, students=students, marks=marks, disciplines=disciplines)


# if __name__ == "__main__":
#     main()