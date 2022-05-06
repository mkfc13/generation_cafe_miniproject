from logo import *
from option import user_input


def open_order_file():
    order_dict = {}
    with open('order.txt', 'r+') as file:
        for key, values in order_dict.items():
            file.write(f"{key}: {values}\n")

    # with open('order.txt', 'w+') as order_file:
    #     line = order_file.readlines()
    #     new_line = []
    #     for i in line:
    #         new_line.append(i.strip('\n'))
    #     order_dict = dict((name, new_line.count(name)) for name in new_line)
    #     print(dict_name)


order_dict = open_order_file()


def write_to_order_dict():
    with open('order.txt', 'w+') as write_to_order_file:
        for k, v in order_dict:
            write_to_order_file.write(f'{k}: {v}\n')


def enum_order_dict():
    for index, order in enumerate(order_dict):
        print(f"{index}. {order}")


def order_menu():
    while True:
        print_order_menu_message()
        num = input()
        print('................................................................\n')

        if num == '0':
            print('***Return to Main Menu.***\n')
            print_main_menu_logo()
            break

        elif num == '1':
            enum_order_dict()
            print('................................................................\n')

        elif num == '2':
            #     GET user input for customer name
            # GET user input for customer address
            # GET user input for customer phone number

            # PRINT couriers list with index value for each courier
            # GET user input for courier index to select courier
            # SET order status to be 'PREPARING'
            # APPEND order to orders list
            new_order = input('please type in your new order: \n')
            order_dict.append(new_order)
            print('................................................................\n')

        elif num == '3':
            # UPDATE existing order status

            # PRINT orders list with its index values
            # GET user input for order index value

            # PRINT order status list with index values
            # GET user input for order status index value
            # UPDATE status for order
            enum_order_dict()
            print(
                'Choose the corresponding index number for the order you want to update: \n')
            choice = user_input(order_dict)
            replace = input("What do you want to replace the order with: \n")
            print(
                f"***{order_dict[choice]} has been updated with {replace}.***\n")
            order_dict[choice] = replace
            print('................................................................\n')

        elif num == '4':
            #     # STRETCH - UPDATE existing order

            # PRINT orders list with its index values
            # GET user input for order index value

            # FOR EACH key-value pair in selected order:
            #     GET user input for updated property
            #     IF user input is blank:
            #         do not update this property
            #     ELSE:
            #         update the property value with user input
            print("Enter the corresponding index number to delete the order: \n")
            enum_order_dict()
            item = user_input(order_dict)
            print(f"***{order_dict[item]} has been deleted.***\n")
            del order_dict[item]
            print('................................................................\n')

        elif num == '5':
            # STRETCH GOAL - DELETE courier

            # PRINT orders list
            # GET user input for order index value
            # DELETE order at index in order list
            print("Enter the corresponding index number to delete the order: \n")
            enum_order_dict()
            item = user_input(order_dict)
            print(f"***{order_dict[item]} has been deleted.***\n")
            del order_dict[item]
            print('................................................................\n')

        else:
            print('Please choose only the following options:\n')
