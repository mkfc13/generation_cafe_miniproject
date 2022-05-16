from functions.logo import *
from functions.option import *
import csv
import pandas as pd


def open_product_file():
    product_list = []
    with open('data\product.csv', 'r') as infile:
        csv_reader = csv.DictReader(infile)
        for row in csv_reader:
            product_list.append(row)
        return product_list


product_list = open_product_file()


def enum_product_list():
    df = pd.read_csv('data\product.csv')
    print(df.round(2))


def pd_product_list():
    df = pd.read_csv('data\product.csv')
    only_product_list = df['Product'].tolist()
    return only_product_list


def pd_price_list():
    df = pd.read_csv('data\product.csv')
    only_product_price = df['Price'].tolist()
    return only_product_price


def write_to_product_list():
    with open('data\product.csv', 'w', newline='') as outfile:
        fieldnames = ['Product', 'Price']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in product_list:
            writer.writerow(row)


def purchase_product():
    purchased_list = []
    while True:
        enum_product_list()
        print('What items do you want to purchase?')
        purchase = menu_input(product_list)
        only_product_list = pd_product_list()
        purchased_list.append(only_product_list[purchase])
        print(f"purchases so far: {purchased_list}")
        more_purchase = input(
            "Do you want to purchase more item? Enter 'Y'es to continue, or just press Enter or 'N'o to stop.\n").lower()

        if more_purchase == '' or more_purchase == 'n' or more_purchase == 'no':
            break
        elif more_purchase == 'y' or more_purchase == 'yes':
            continue
        else:
            print("Invalid option, assuming you don't want to add more purchase")
            break
    return purchased_list


def add_new_product_list():
    new_product_name = input('please type in your new product name: \n')
    new_product_price = input('please type in your new product price: \n')
    new_product = {"Product": new_product_name, "Price": new_product_price}
    product_list.append(new_product)


def update_product_list():
    # perhaps add a string so user can input the product index or the product name, probably need .title() somewhere
    print('Choose the corresponding index number for the product you want to update: \n')
    choice = menu_input(product_list)
    product_dict = dict(product_list[choice])
    new_product_dict = {}
    new_product_name = input(
        "Please input the new product's name or Enter to skip.\n")
    if new_product_name == '':
        print("No update to Product's Name.\n")
        new_product_dict['Product'] = product_dict.get('Product')
    else:
        print(
            f"***{product_dict.get('Product')} has been updated to {new_product_name}.***\n")
        new_product_dict['Product'] = new_product_name
    new_product_price = input(
        "Please input the new product's price or Enter to skip.\n")
    if new_product_price == '':
        print("No update to Product's Price.\n")
        new_product_dict['Price'] = product_dict.get('Price')
    else:
        print(
            f"***{product_dict.get('Price')} has been updated to {new_product_price}.***\n")
        new_product_dict['Price'] = float(new_product_price)
    product_list[choice] = new_product_dict


def delete_product_list():
    print("Enter the corresponding index number to delete the product: \n")
    item = menu_input(product_list)
    print(f"***{product_list[item]} has been deleted.***\n")
    del product_list[item]


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
            add_new_product_list()
            write_to_product_list()
            print('................................................................\n')

        elif num == '3':
            enum_product_list()
            update_product_list()
            write_to_product_list()
            print('................................................................\n')

        elif num == '4':
            enum_product_list()
            delete_product_list()
            write_to_product_list()
            print('................................................................\n')

        else:
            print('Please choose only the following options:\n')
