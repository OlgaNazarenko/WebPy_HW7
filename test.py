# Lets say you have 10 programs or functions:
from my_select import select_1, select_2, select_3, select_4, select_5, select_6

func_list = [select_6, select_5]

choose_program = int(input('Please Choose a program: ')) # input function number

func_list[choose_program - 1]()


