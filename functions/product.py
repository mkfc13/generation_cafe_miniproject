from random import choice
from functions.function import *
from functions.logo import *


def product_menu(choice):
    while True:
        print_product_menu_message()
        num = input()
        print('................................................................\n')

        if num == '0':
            print('***Return to Main Menu.***\n')
            print_main_menu_logo()
            break

        elif num == '1':
            select_table(choice)
            print('................................................................\n')

        elif num == '2':
            create_new_row(choice)
            print('................................................................\n')

        elif num == '3':
            update_row(choice)
            print('................................................................\n')

        elif num == '4':
            delete_row(choice)
            print('................................................................\n')

        else:
            print('Please choose only the following options:\n')
