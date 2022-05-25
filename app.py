from functions.function import *
from functions.logo import *
import pymysql


def selected_menu(choice):
    while True:
        if choice == 1:
            print_product_menu_message()
        elif choice == 2:
            print_courier_menu_message()
        elif choice == 3:
            print_order_menu_message()
        else:
            print("You shouldn't be here\n")

        num = input()
        print('................................................................\n')

        if num == '0':
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


def order_menu(choice):
    while True:
        print_order_menu_message()
        num = input()
        print('................................................................\n')

        if num == '0':
            print_main_menu_logo()
            break

        elif num == '1':
            view_order_table()
            print('................................................................\n')

        elif num == '2':
            create_new_order()
            print('................................................................\n')

        elif num == '3':
            update_order_status()
            print('................................................................\n')

        elif num == '4':
            update_order_row(choice)
            print('................................................................\n')

        elif num == '5':
            delete_row(choice)
            print('................................................................\n')
        else:
            print('Please choose only the following options:\n')


print_cafe_logo()
print_main_menu_logo()
while True:
    print_main_menu_message()
    choice = input()
    if choice == '0':
        print_exit_message()
        cursor.close()
        connection.close()
        break
    elif choice == '1':
        print_product_menu_logo()
        selected_menu(int(choice))
    elif choice == '2':
        current_menu = 2
        print_courier_menu_logo()
        selected_menu(int(choice))
    elif choice == '3':
        print_order_menu_logo()
        order_menu(int(choice))
    elif choice == '4':
        select_table(int(choice))
    elif choice == '5':
        select_table(int(choice))
    else:
        print('Please choose only the following options:\n')
