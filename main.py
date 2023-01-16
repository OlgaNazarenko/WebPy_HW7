from my_select import select_1, select_2, select_3, select_4, select_5, select_6, \
    select_7, select_8, select_9, select_10
import run_seed


def assistance():
    menu: str = """Commands line:
    help - help
    exit - exit
    from 0 - 9 - choose any query-requests: 

        0) 5 студентів з найбільшим середнім балом з усіх предметів
        1) Студенти з найвищим середнім балом з певного предмету
        2) Середній бал у групах з певного предмету
        3) Середній бал на потоці
        4) Курси певного викладача
        5) Список студентів певної групи
        6) Оцінки студентів у окремій группі з певного предмету
        7) Середній бал, який ставив певний викладач зі своїх предметів
        8) Список курсів, які відвідував студент
        9) Список курсів, які певний викладач читає певному студенту
    """
    print(menu)


def create_tables():
    return run_seed


def command_parser():
    create_tables()
    assistance()
    while True:
        choose_query = input('Enter command: ')

        if choose_query == 'exit':
            print('Good bye)')
            break

        func_list: list = [select_1, select_2, select_3, select_4, select_5,
                           select_6, select_7, select_8, select_9, select_10]

        func_list[int(choose_query) - 1]()


if __name__ == "__main__":
    command_parser()
