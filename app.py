from functions.function import *
from functions.product import *
from functions.courier import *
from functions.order import *
from functions.option import *
import pymysql

# Make it pretty with pandas after everything works.


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
        product_menu(int(choice))
    elif choice == '2':
        current_menu = 2
        print_courier_menu_logo()
        courier_menu(int(choice))
    elif choice == '3':
        print_order_menu_logo()
        order_menu(int(choice))
    else:
        print('Please choose only the following options:\n')
