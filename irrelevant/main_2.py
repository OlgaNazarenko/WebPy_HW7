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


# list_: dict = {
    # 'exit': {'func': func_exit},
    # 'help': {'func': assistance, 'params': []},
    # '1': select_1 ,
    # '2': {'func': my_select.select_2, 'params': []},
    # '3': {'func': my_select.select_3, 'params': ['discipline_value']},
    # '4': {'func': my_select.select_4, 'params': ['pr_id']},
    # '5': {'func': my_select.select_5},
    # '6': {'func': my_select.select_6, 'params': ['group_title']},
    # '7': {'func': my_select.select_7, 'params': ['group_title', 'discipline_name']},
    # '8': {'func': my_select.select_8, 'params': ['pr_id']},
    # '9': {'func': my_select.select_9, 'params': ['st_id']},
    # '10': {'func': my_select.select_10, 'params': ['st_id', 'pr_id']}
# }
