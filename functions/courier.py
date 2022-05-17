from functions.function import *
from functions.logo import *
from functions.option import *
import csv
import pandas as pd
header = ['Courier', 'Phone']

courier_list = open_file('data\courier.csv')


def enum_courier_list():
    df = pd.read_csv('data\courier.csv', dtype={'Phone': 'str'})
    print(df)


def pd_courier_list():
    df = pd.read_csv('data\courier.csv')
    only_courier_list = df['Courier'].tolist()
    return only_courier_list


def pd_phone_list():
    df = pd.read_csv('data\courier.csv')
    only_courier_phone = df['Phone'].tolist()
    return only_courier_phone


def add_new_courier_list():
    new_courier_name = input('please type in your new courier name: \n')
    new_courier_phone = input('please type in your new courier phone: \n')
    new_courier = {"Courier": new_courier_name,
                   "Phone": (f"{new_courier_phone}")}
    courier_list.append(new_courier)


def update_courier_list():
    print('Choose the corresponding index number for the courier you want to update: \n')
    choice = menu_input(courier_list)
    courier_dict = dict(courier_list[choice])
    new_courier_dict = {}
    new_courier_name = input(
        "Please input the new courier's name or Enter to skip.\n")
    if new_courier_name == '':
        print("No update to courier's Name.\n")
        new_courier_dict['Courier'] = courier_dict.get('Courier')
    else:
        print(
            f"***{courier_dict.get('Courier')} has been updated to {new_courier_name}.***\n")
        new_courier_dict['Courier'] = new_courier_name
    new_courier_phone = input(
        "Please input the new courier's phone or Enter to skip.\n")
    if new_courier_phone == '':
        print("No update to courier's Phone.\n")
        new_courier_dict['Phone'] = courier_dict.get('Phone')
    else:
        print(
            f"***{courier_dict.get('Phone')} has been updated to {new_courier_phone}.***\n")
        new_courier_dict['Phone'] = (f"{new_courier_phone}")
    courier_list[choice] = new_courier_dict


def delete_courier_list():
    print("Enter the corresponding index number to delete the courier: \n")
    item = user_input(courier_list)
    print(f"***{courier_list[item]} has been deleted.***\n")
    del courier_list[item]


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
            save_file('data\courier.csv', header, courier_list)
            print('................................................................\n')

        elif num == '2':
            add_new_courier_list()
            save_file('data\courier.csv', header, courier_list)
            print('................................................................\n')

        elif num == '3':
            enum_courier_list()
            update_courier_list()
            save_file('data\courier.csv', header, courier_list)
            print('................................................................\n')

        elif num == '4':
            enum_courier_list()
            delete_courier_list()
            save_file('data\courier.csv', header, courier_list)
            print('................................................................\n')

        else:
            print('Please choose only the following options:\n')
