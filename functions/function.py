import pymysql
import os
from dotenv import load_dotenv

table_name = ['Product', 'Courier', 'Orders', 'Status','Customer']
column_name = [['ID', 'Product', 'Price'], ['ID', 'Courier', 'Phone'], ['Customer', 'Courier', 'Status', 'Product'], ['ID', 'order_status'], ['ID', 'Customer_Name',
                                                                                                                                                            'Customer_Address', 'Customer_Phone']]

# To-Do-List
# Add Unit Testing for my functions
# Stocks update
# fix phone list to be more viewable
# error handle Update Order function.
# make a product list so that the order show the product purchased rather than the ID.
# finish my README installation guide.


# Functions to ensuere that the user input is within the available list.
def string_input(new_list):
    while True:
        user_input = input()
        for x in new_list:
            if user_input == x:
                return user_input
            else:
                continue
        print(
            f'Invalid options.\nPlease choose from the following list:{new_list}')


# Establish connection to the database
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


# prints out the chosen table, currently only product and courier works, the others is weird
def select_table(choice):
    selected_table = table_name[int(choice)-1]
    selected_column = column_name[int(choice)-1]
    cursor.execute(f"SELECT * FROM {selected_table}")
    rows = cursor.fetchall()
    print(selected_table)
    print(selected_column)
    for row in rows:
        print(row)


# Show the current list of order with the customer's name, courier assigned, status and the product purchased and total to pay.
def view_current_order():
    sql = '''
            SELECT Orders.ID, Customer.Customer_Name, Courier.Courier, Status.order_status, Orders.Product, Orders.Total_Price
            FROM Orders
            LEFT JOIN Customer ON Customer.ID = Orders.Customer
            LEFT JOIN Courier ON Courier.ID = Orders.Courier
            LEFT JOIN Status ON Status.ID = Orders.Status WHERE Status.order_status != 'Completed' AND Status.order_status != 'Cancelled'
            ORDER BY Status
            '''
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(table_name[2])
    print("['ID', 'Customer', 'Courier', 'Status', 'Product', 'Total_Price']")
    for row in rows:
        print(row)


# Show the list of order with the customer's name, courier assigned, status and the product purchased and total to pay.
def view_order_table():
    while True:
        selection = input(
        "\n1: View a list of Current Orders.\n2: View a list of Completed Orders.\n3: View a list of Cancelled Orders.\n4: View a list of ALL Orders.\n")
        if selection == '1':
            view_current_order()
            break
        elif selection == '2':
            sql = '''
            SELECT Orders.ID, Customer.Customer_Name, Courier.Courier, Status.order_status, Orders.Product, Orders.Total_Price
            FROM Orders
            LEFT JOIN Customer ON Customer.ID = Orders.Customer
            LEFT JOIN Courier ON Courier.ID = Orders.Courier
            LEFT JOIN Status ON Status.ID = Orders.Status WHERE Status.order_status = 'Completed'
            ORDER BY Status
            '''
        elif selection == '3':
            sql = '''
            SELECT Orders.ID, Customer.Customer_Name, Courier.Courier, Status.order_status, Orders.Product, Orders.Total_Price
            FROM Orders
            LEFT JOIN Customer ON Customer.ID = Orders.Customer
            LEFT JOIN Courier ON Courier.ID = Orders.Courier
            LEFT JOIN Status ON Status.ID = Orders.Status WHERE Status.order_status = 'Cancelled'
            ORDER BY Status
            '''
        elif selection == '4':
            sql = '''
            SELECT Orders.ID, Customer.Customer_Name, Courier.Courier, Status.order_status, Orders.Product, Orders.Total_Price
            FROM Orders
            LEFT JOIN Customer ON Customer.ID = Orders.Customer
            LEFT JOIN Courier ON Courier.ID = Orders.Courier
            LEFT JOIN Status ON Status.ID = Orders.Status
            ORDER BY ID
            '''
        else:
            print('Invalid Option. Return to Order Menu.\n')
            break
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(table_name[2])
        print("['ID', 'Customer', 'Courier', 'Status', 'Product', 'Total_Price']")
        for row in rows:
            print(row)
        break


# Create a new row for product and courier table.
def create_new_row(choice):
    selected_table = table_name[int(choice)-1]
    selected_column = column_name[int(choice)-1]
    key = input(
        f"please type in your new {selected_table}'s {selected_column[1]}: \n")
    value = input(
        f"please type in your new {selected_table}'s {selected_column[2]}: \n")
    sql = f"INSERT INTO {selected_table} ({selected_column[1]}, {selected_column[2]}) VALUES (%s, %s)"
    val = (key, value)
    cursor.execute(sql, val)
    connection.commit()


# Update the row of product and courier table.
def update_row(choice):
    selected_table = table_name[int(choice)-1]
    selected_column = column_name[int(choice)-1]
    select_table(choice)
    selected_id = input(f"Choose the {selected_table} No. you want to update:\n")
    print(selected_column)
    print("Type in what you want to update.")
    update_column = string_input(selected_column)
    sql = f'''SELECT {selected_table}.{update_column}
            FROM {selected_table}
            WHERE {selected_column[0]} = {selected_id}
            '''
    cursor.execute(sql)
    selected_value = cursor.fetchone()
    selected_value = str(selected_value).strip("(),''")
    new_update = input(
        f"Type in the new detail you want to update {update_column} of {selected_value} with:\n")
    cursor.execute(
        f"UPDATE {selected_table} SET {update_column}= '{new_update}' WHERE {selected_column[0]} = {selected_id}")
    connection.commit()


# delete the row of product, courier and order table.
def delete_row(choice):
    selected_table = table_name[int(choice)-1]
    selected_row = column_name[int(choice)-1][0]
    while True:
        confirmation = input("ARE YOU SURE YOU WANT TO DELETE {selected_table}? (y/n)").lower()
        if confirmation == 'y':
            select_table(int(choice))
            delete_id = input("please type in the id of what you wanted to delete.\n")
            sql = f"DELETE FROM {selected_table} WHERE {selected_row} = {delete_id}"
            cursor.execute(sql)
            connection.commit()
            break
        else:
            print("Nothing has been deleted.\n")
            break


# A function to add a new customer, and return the latest customer_id for new order
def new_customer():
    selected_table = table_name[4]
    selected_column = column_name[4]
    name = input("please type in your new customer's name: \n")
    address = input("please type in your new customer's address: \n")
    phone = input("please type in your new customer's phone: \n")
    sql = f"INSERT INTO {selected_table} ({selected_column[1]}, {selected_column[2]}, {selected_column[3]}) VALUES (%s, %s, %s)"
    val = (name, address, phone)
    cursor.execute(sql, val)
    connection.commit()
    cursor.execute("SELECT MAX(ID) FROM Customer")
    latest_customer_id = cursor.fetchone()
    return latest_customer_id


# create a new order. Need to fix
def create_new_order():
    while True:
        which_customer = input(f"Is it a [N]ew or [E]xisting customer?\n").lower()
        if which_customer == 'new' or which_customer == 'n':
            customer = new_customer()
            break
        elif which_customer == 'existing' or which_customer == 'e':
            select_table(5)
            customer = input("Select the existing customer's ID.\n")
            break
        else:
            print("Invalid options. Please type in 'new' or 'existing'.")
    customer = customer
    select_table(2)
    courier = input("please type in the assigned courier for the customer: \n")
    status = 1
    select_table(1)
    product = input(
        "please type in product index the customer purchased(seperated each product with ,): \n")
    price = total_price(product)
    print(f"The total price of the Order is £{price}.\n")
    sql = "INSERT INTO Orders (Customer, Courier, Status, Product, Total_Price) VALUES (%s, %s, %s, %s, %s)"
    val = customer, courier, status, product, price
    cursor.execute(sql, val)
    connection.commit()


# print out a list of order id
def list_order_id():
    order_id = []
    cursor.execute("SELECT ID FROM Orders WHERE Status !=4 AND Status !=5")
    rows = cursor.fetchall()
    for row in rows:
        order_id.append(str(row).strip("(),''"))
    while True:
        user_input = input(
            'Choose the Order No. for the order status you want to update:\n')
        for x in order_id:
            if user_input == x:
                return user_input
            else:
                continue
        print(
            f'Invalid options.\nPlease choose from the following list:{order_id}')


# update an order's status. need to fix
def update_order_status():
    view_current_order()
    selected_order_id = list_order_id()
    select_table(4)
    new_status = input(
        "Choose the corresponding index number for the status you want to update to the order with.\n")
    cursor.execute(
        f"UPDATE Orders SET Status= {new_status} WHERE ID = {selected_order_id}")
    connection.commit()


# function to add all the total price of user input product.
def total_price(input_list):
    cursor.execute("SELECT * from Product")
    products = cursor.fetchall()
    connection.commit()
    x = input_list.split(',')
    new_price = 0
    for price in products:
        for i in x:
            if int(i) == price[0]:
                new_price += price[2]
    return new_price


# function to update the order
def update_order_row(choice):
    view_current_order()
    selected_order_id = int(input(
       '\nChoose the Order No. for the Order you want to update:\n'))
    print(column_name[2])
    print("Type in what you want to update.")
    update_column = string_input(column_name[2])
    if update_column == 'Status':
        selected_column = 'order_status'
    elif update_column == 'Customer':
        selected_column = 'Customer_Name'
    else:
        selected_column = update_column
    sql = f'''SELECT {update_column}.{selected_column}
            FROM Orders
            LEFT JOIN {update_column} ON {update_column}.ID = Orders.{update_column}
            WHERE Orders.ID = {selected_order_id}
            '''
    cursor.execute(sql)
    selected_value = str(cursor.fetchone()).strip("(),''")
    cursor.execute(f"SELECT * FROM {update_column}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    new_update = input(
        f"Type in the index of the new detail you want to update {update_column} of {selected_value} with:\n")
    if update_column == 'Product':
        new_price = total_price(new_update)
        cursor.execute(
            f"UPDATE Orders SET {update_column}= '{new_update}', Total_Price = {new_price} WHERE ID = {selected_order_id}")
        connection.commit()
    else:
        new_update
        cursor.execute(f"UPDATE Orders SET {update_column}= '{new_update}' WHERE ID = {selected_order_id}")
        connection.commit()


# function that can make phone into +44 00000 00000 format
def sort_phone(phone_num):
    if phone_num == "":
        return ""
    else:
        return "+44" + " " + phone_num[-10:-5] + " " + phone_num[-5:]
