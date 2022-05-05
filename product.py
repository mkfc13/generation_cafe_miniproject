from logo import *
from option import user_input


def open_product_file():
    product_list = []
    with open('product.txt', 'r+') as product_file:
        line = product_file.readlines()
        for i in line:
            product_list.append(i.strip('\n'))
    return product_list


product_list = open_product_file()


def write_to_product_list():
    with open('product.txt', 'w+') as write_to_product_file:
        for i in product_list:
            write_to_product_file.write(f'{i}\n')


def enum_product_list():
    for index, product in enumerate(product_list):
        print(f"{index}. {product}")


def product_menu():
    while True:
        print_product_menu_message()
        num = input()
        print('................................................................\n')

        if num == '0':
            print('***Return to Main Menu.***\n')
            print_main_menu_logo()
            break

        elif num == '1':
            enum_product_list()
            print('................................................................\n')

        elif num == '2':
            new_product = input('please type in your new product: \n')
            product_list.append(new_product)
            print('................................................................\n')

        elif num == '3':
            enum_product_list()
            print(
                'Choose the corresponding index number for the product you want to update: \n')
            choice = user_input(product_list)
            replace = input("What do you want to replace the product with: \n")
            print(
                f"***{product_list[choice]} has been updated with {replace}.***\n")
            product_list[choice] = replace
            print('................................................................\n')

        elif num == '4':
            print("Enter the corresponding index number to delete the product: \n")
            enum_product_list()
            item = user_input(product_list)
            print(f"***{product_list[item]} has been deleted.***\n")
            del product_list[item]
            print('................................................................\n')

        else:
            print('Please choose only the following options:\n')
