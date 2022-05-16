from functions.product import *
from functions.courier import *
from functions.order import *

# refactoring these code into OOP

print_cafe_logo()
print_main_menu_logo()
while True:
    print_main_menu_message()
    choice = input()
    if choice == '0':
        print_exit_message()
        write_to_product_list()
        write_to_courier_list()
        save_order()
        break
    elif choice == '1':
        print_product_menu_logo()
        product_menu()
    elif choice == '2':
        print_courier_menu_logo()
        courier_menu()
    elif choice == '3':
        print_order_menu_logo()
        order_menu()
    else:
        print('Please choose only the following options:\n')
