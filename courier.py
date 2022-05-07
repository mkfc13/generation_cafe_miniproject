from logo import *
from option import user_input


def open_courier_file():
    courier_list = []
    with open('courier.txt', 'r+') as courier_file:
        line2 = courier_file.readlines()
        for i in line2:
            courier_list.append(i.strip('\n'))
    return courier_list


courier_list = open_courier_file()


def write_to_courier_list():
    with open('courier.txt', 'w+') as write_to_courier_file:
        for i in courier_list:
            write_to_courier_file.write(f'{i}\n')


def enum_courier_list():
    for index, courier in enumerate(courier_list):
        print(f"{index}. {courier}")


def courier_menu():
    while True:
        print_courier_menu_message()
        num = input()
        print('................................................................\n')

        if num == '0':
            print('***Return to Main Menu.***\n')
            print_main_menu_logo()
            break

        elif num == '1':
            enum_courier_list()
            print(
                '................................................................\n')

        elif num == '2':
            new_courier = input('please type in your new courier name: \n')
            courier_list.append(new_courier)
            write_to_courier_list()
            print(
                '................................................................\n')

        elif num == '3':
            enum_courier_list()
            print(
                "Choose the corresponding index number for the courier name you want to update: \n")
            choice = user_input(courier_list)
            replace = input(
                "What do you want to replace the courier name with: \n")
            print(
                f"***{courier_list[choice]} has been updated with {replace}.***\n")
            courier_list[choice] = replace
            write_to_courier_list()
            print(
                '................................................................\n')

        elif num == '4':
            print(
                "Enter the corresponding index number to delete the courier name: \n")
            enum_courier_list()
            item = user_input(courier_list)
            print(f"***{courier_list[item]} has been deleted.***\n")
            del courier_list[item]
            write_to_courier_list()
            print(
                '................................................................\n')

        else:
            print('Please choose only the following options:\n')
