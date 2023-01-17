import sys

import run_seed
from my_select import select_1, select_2, select_3, select_4, select_5, select_6, \
    select_7, select_8, select_9, select_10


def assistance():
    menu: str = """Commands line:
    exit - exit
    from 1 - 10 - choose any query-requests: 

        1) 5 студентів з найбільшим середнім балом з усіх предметів
        2) Студенти з найвищим середнім балом з певного предмету
        3) Середній бал у групах з певного предмету
        4) Середній бал на потоці
        5) Курси певного викладача
        6) Список студентів певної групи
        7) Оцінки студентів у окремій группі з певного предмету
        8) Середній бал, який ставив певний викладач зі своїх предметів
        9) Список курсів, які відвідував студент
        10) Список курсів, які певний викладач читає певному студенту
    """
    print(menu)


def create_tables():
    return run_seed


def command_parser():
    create_tables()
    assistance()
    while True:
        choose_query: str = input('Enter command: ')

        func_list: dict = {'1': select_1,
                           '2': select_2,
                           '3': select_3,
                           '4': select_4,
                           '5': select_5,
                           '6': select_6,
                           '7': select_7,
                           '8': select_8,
                           '9': select_9,
                           '10': select_10
                           }

        if choose_query == 'exit':
            sys.exit("Good bye")

        if choose_query in func_list:
            print(func_list[choose_query]())

        elif choose_query >= str(10):
            print('You can enter up to 10, try again: ')


if __name__ == "__main__":
    command_parser()
