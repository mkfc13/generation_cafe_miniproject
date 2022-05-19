import csv
import pandas as pd
import pymysql
import os
from dotenv import load_dotenv

from functions.option import user_input
table_name = ['Product', 'Courier', 'Orders']
column_name = [['product_id', 'Name', 'Price'], ['courier_id', 'Name', 'Phone'], ['order_id', 'Customer_Name',
                                                                                  'Customer_Address', 'Customer_Phone', 'Courier', 'Status', 'Items']]
status_list = ['Preparing', 'Ready, Awaiting Pickup',
               'Out for Delivery', 'Delivered']


def enum_status_list():
    print('Available Status')
    for index, status in enumerate(status_list):
        print(f"{index}. {status}")


load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=database)


cursor = connection.cursor()


def select_table(choice):
    selected_table = table_name[int(choice)-1]
    selected_column = column_name[int(choice)-1]
    cursor.execute(
        f"SELECT * FROM {selected_table}")
    rows = cursor.fetchall()
    print(selected_table)
    print(selected_column)
    for row in rows:
        print(row)


def old_select_table(choice):
    selected_table = table_name[int(choice)-1]
    selected_column = column_name[int(choice)-1]
    cursor.execute(f"SELECT * FROM {selected_table}")
    rows = cursor.fetchall()
    for row in rows:
        print(
            f"ID: {str(row[0])}, {selected_column[1]}: {row[1]}, {selected_column[2]}: {row[2]}")


def create_new_row(choice, column_name):
    selected_column_name = table_name[int(choice)-1]
    selected_column = column_name[int(choice)-1]
    key = input(
        f"please type in your new {selected_column_name}'s {selected_column[1]}: \n")
    value = input(
        f"please type in your new {selected_column_name}'s {selected_column[2]}: \n")
    sql = f"INSERT INTO {selected_column_name} ({selected_column[1]}, {selected_column[2]}) VALUES (%s, %s)"
    val = (key, value)
    cursor.execute(sql, val)
    connection.commit()


def delete_row(choice):
    selected_column_name = table_name[int(choice)-1]
    selected_row = column_name[int(choice)-1][0]
    select_table(int(choice))
    delete_id = input("please type in the id of what you wanted to delete.\n")
    sql = f"DELETE FROM {selected_column_name} WHERE {selected_row} = {delete_id}"
    cursor.execute(sql)
    connection.commit()


def order_table():
    order_list = []
    cursor.execute("SELECT * FROM Orders")
    rows = cursor.fetchall()
    for row in rows:
        print(
            f"Order No:{row[0]}\nCustomer Name: {row[1]}\nCustomer Address: {row[2]}\nCustomer Phone: {row[3]}\nCourier: {row[4]}\nStatus: {row[5]}\nItems: {row[6]}\n")


def create_new_order():
    name = input("please type in your new customer's name: \n")
    address = input("please type in your new customer's address: \n")
    phone = input("please type in your new customer's phone: \n")
    courier = input("please type in the assigned courier for the customer: \n")
    status = 'Preparing'
    item = input(
        "please type in product index the customer purchased(seperated each item with ,): \n")
    sql = "INSERT INTO Orders (Customer_Name, Customer_Address, Customer_Phone, Courier, Status, Item) VALUES (%s, %s, %s, %s, %s, %s)"
    val = name, address, phone, courier, status, item
    cursor.execute(sql, val)
    connection.commit()


def update_order_status():
    order_table()
    selected_order_id = input(
        'Choose the Order No. for the order status you want to update:\n')
    selected_order = int(selected_order_id)
    enum_status_list()
    print('\nChoose the corresponding index number for the status you want to update to the order with.\n')
    new_status = user_input(status_list)
    update_status = status_list[new_status]
    cursor.execute(
        f"UPDATE Orders SET Status= '{update_status}' WHERE order_id = {selected_order}")
    connection.commit()
