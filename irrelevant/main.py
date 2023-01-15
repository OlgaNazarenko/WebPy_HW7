import my_select
import run_seed


def assistance():
    menu = """Commands line:
    help - help
    exit - exit
    create tables - create_table
    from 1 - 10 - choose any query-requests: 

        0) Інформація про студентів, викладачів та предмети
        1) Інформація про студентів, викладачів та предмети
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


def the_list():
    list_: dict = {
        '1': {'func': my_select.select_1, 'params': []},
        '2': {'func': my_select.select_2, 'params': []},
        '3': {'func': my_select.select_3, 'params': ['discipline_value']},
        '4': {'func': my_select.select_4, 'params': ['pr_name']},
        '5': {'func': my_select.select_5},
        '6': {'func': my_select.select_6, 'params': ['group_title']},
        '7': {'func': my_select.select_7, 'params': ['group_title', 'discipline_name']},
        '8': {'func': my_select.select_8, 'params': ['pr_name']},
        '9': {'func': my_select.select_9, 'params': ['st_name']},
        '10': {'func': my_select.select_10, 'params': ['st_name', 'pr_name']}
    }


def main():
    value: str = input("Choose from the 'help'")
    while True:

        if value == 'exit':
            print('Good bye)')
            break
        if value == 'help':
            print(assistance())

        else:
            x = []
            # for x in  the_list()['params']

        # if not command == int:
        #     return 'Send number of query!'
        create_tables()


def command(value):
    if value not in the_list():
        print("Incorrect")
        return

    list_cmd = []
    for key, value in the_list[value]['input_']:
        input_ = input(key)
        list_cmd.append(input_)



COMMANDS: dict = {
        select_1: '1',
        select_2: '2',
        select_3: '3',
        select_4: '4',
        select_5: '5',
        select_6: '6',
        select_7: '7',
        select_8: '8',
        select_9: '9',
        select_10: '10'
    }


def unknown_command():
    print('Unknown command! Enter again!\n')


def command_parser(user_command: str):
    for key, value in COMMANDS.items():
        if user_command.lower() == value:
            print(f"{key=}")
    else:
        return unknown_command()


if __name__ == "__main__":
    assistance()
    main()
    # main()
    # create_tables()
    while True:
        user_command = input("Please enter the query number, from 1 to 10: ")
        if user_command==11:
            print("Incorrect number")
            break
        print(f"{command_parser(user_command)=}")
