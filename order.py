from logo import *
from courier import *
from option import *
import json
import io
import yaml


with open('order.json') as order_file:
    order_list = json.load(order_file)

order_list = order_list


def save_order():
    with io.open('order.json', 'w', encoding='utf-8') as outfile:
        save_data = json.dumps(order_list, indent=4, sort_keys=False,
                               separators=(",", ":"), ensure_ascii=False)
        outfile.write(save_data)


def enum_order_list():
    for index, orders in enumerate(order_list):
        print(f"{index}. {yaml.dump(order_list[index], sort_keys=False)}")


def new_order():
    customer_name = input("Please input the new customer's name.\n")
    customer_address = input("Please input the new customer's address.\n")
    customer_phone = input("Please input the new customer's phone number.\n")
    enum_courier_list()
    print(
        f"Please input the relevant courier number to assigned the courier for {customer_name}.\n")
    courier_no = user_input(courier_list)
    status = "Preparing"
    orders = {"customer_name": customer_name, "customer_address": customer_address,
              "customer_phone": customer_phone, "courier": courier_list[courier_no], "status": status}
    order_list.append(orders)
    print(yaml.dump(order_list[len(order_list) - 1], sort_keys=False))
    print("***New Order been added to the Order List.***\n")


def update_order_status():
    print(
        '\nChoose the corresponding index number for the order status you want to update:')
    choice = user_input(order_list)
    order_dict = dict(order_list[choice])
    print(f"Current Order Status: {order_dict['status']}\n")
    replace = input(
        "Please input the new status.\n")
    chose_status = order_dict.get('status', [])
    print(
        f"\n***Status: {chose_status} has been updated to {replace}.***\n")
    order_dict.pop('status')
    new_status = {"status": replace}
    order_dict.update(new_status)
    order_list[choice] = order_dict


def update_order():
    print('\nChoose the corresponding index number for the order you want to update:')
    choice = user_input(order_list)
    order_dict = dict(order_list[choice])
    new_order_dict = {}
    new_customer_name = input(
        "Please input the new customer's name or Enter to skip.\n")
    if new_customer_name == '':
        print("No update to Customer's Name.\n")
        new_order_dict['customer_name'] = order_dict.get('customer_name')
    else:
        print(
            f"***{order_dict.get('customer_name')} has been updated to {new_customer_name}.***\n")
        new_order_dict['customer_name'] = new_customer_name
    new_customer_address = input(
        "Please input the new customer's address or Enter to skip.\n")
    if new_customer_address == '':
        print("No update to Customer's Address.\n")
        new_order_dict['customer_address'] = order_dict.get('customer_address')
    else:
        print(
            f"***{order_dict.get('customer_address')} has been updated to {new_customer_address}.***\n")
        new_order_dict['customer_address'] = new_customer_address
    new_customer_phone = input(
        "Please input the new customer's phone number or Enter to skip.\n")
    if new_customer_phone == '':
        print("No update to Customer's Phone Number.\n")
        new_order_dict['customer_phone'] = order_dict.get('customer_phone')
    else:
        print(
            f"***{order_dict.get('customer_phone')} has been updated to {new_customer_phone}.***\n")
        new_order_dict['customer_phone'] = new_customer_phone
    print('Courier List')
    enum_courier_list()
    courier_no = input(
        "Please input the new number of the assigned courier or Enter to skip.\n")
    new_courier = courier_list[int(courier_no)]
    if 0 <= int(courier_no) < len(courier_list):
        print(
            f"***{order_dict.get('courier')} has been updated to {new_courier}.***\n")
        new_order_dict['courier'] = new_courier
    elif new_courier == "":
        print("No update to Assigned Courier.\n")
        new_order_dict['courier'] = order_dict.get('courier')
    else:
        print("Invalid option, therefore no update to Assigned Courier.\n")
        new_order_dict['courier'] = order_dict.get('courier')
    new_status = input(
        "Please input the new order status or Enter to skip.\n")
    if new_status == '':
        print("No update to Order's Status.\n")
        new_order_dict['status'] = order_dict.get('status')
    else:
        print(
            f"***{order_dict.get('status')} has been updated to {new_status}.***\n")
        new_order_dict['status'] = new_status
    order_list[choice] = new_order_dict
    print('Order has been updated to:')
    print(new_order_dict)


def delete_order():
    print("Enter the corresponding index number to delete the order: \n")
    item = user_input(order_list)
    print(f"***{order_list[item]} has been deleted.***\n")
    del order_list[item]


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
            enum_order_list()
            print('................................................................\n')

        elif num == '2':
            new_order()
            save_order()
            print('................................................................\n')

        elif num == '3':
            enum_order_list()
            update_order_status()
            save_order()
            print('................................................................\n')

        elif num == '4':
            enum_order_list()
            update_order()
            save_order()
            print('................................................................\n')

        elif num == '5':
            enum_order_list()
            delete_order()
            save_order()
            print('................................................................\n')
        else:
            print('Please choose only the following options:\n')
