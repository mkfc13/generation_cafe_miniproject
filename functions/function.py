import pymysql
import os
from dotenv import load_dotenv

table_name = ['Product', 'Courier', 'Orders', 'Status','Customer']
column_name = [['product_id', 'Product', 'Price'], ['courier_id', 'Courier', 'Phone'], ['order_id', 'Customer', 'Courier', 'Status', 'Product'], ['status_id', 'order_status'], ['customer_id', 'Customer_Name',
                                                                                                                                                            'Customer_Address', 'Customer_Phone']]

# To-Do-List
# Need to fix ORDER, joining with other table so ORDER don't print numbers.
# pull product from table to local and add the total amount of price and what the customer need to pay.
# Add Unit Testing for my functions


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


#need to add if order is cancelled or completed, ommited from showing.
# Show the list of order with the customer's name, courier assigned, status and the product purchased
def join_table():
    sql = '''
    SELECT Orders.order_id, Customer.Customer_Name, Courier.Courier, Status.order_status, Product.Product
    FROM Orders
    LEFT JOIN Customer ON Customer.customer_id = Orders.Customer
    LEFT JOIN Courier ON Courier.courier_id = Orders.Courier
    LEFT JOIN Status ON Status.status_id = Orders.Status
    LEFT JOIN Product ON Product.product_id = Orders.Product
    ORDER BY Status
    '''
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(table_name[2])
    print(column_name[2])
    for row in rows:
        print(row)


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
    new_update = input(
        f"Type in the new detail you want to update {update_column} with:\n")
    cursor.execute(
        f"UPDATE {selected_table} SET {update_column}= '{new_update}' WHERE {selected_column[0]} = {selected_id}")
    connection.commit()


#need to change the delete function for order, so the old order is archived instead of being deleted.
# delete the row of product, courier and order table.
def delete_row(choice):
    selected_table = table_name[int(choice)-1]
    selected_row = column_name[int(choice)-1][0]
    select_table(int(choice))
    delete_id = input("please type in the id of what you wanted to delete.\n")
    sql = f"DELETE FROM {selected_table} WHERE {selected_row} = {delete_id}"
    cursor.execute(sql)
    connection.commit()


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
    cursor.execute("SELECT MAX(customer_id) FROM Customer")
    latest_customer_id = cursor.fetchone()
    return latest_customer_id


# create a new order. Need to fix
def create_new_order():
    while True:
        which_customer = input(f"Is it a [N]ew or [E]xisting customer? (y/n)\n").lower()
        if which_customer == 'new' or which_customer == 'y' or which_customer == 'n':
            customer = new_customer()
            break
        elif which_customer == 'existing' or which_customer == 'n' or which_customer == 'e':
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
    sql = "INSERT INTO Orders (Customer, Courier, Status, Product) VALUES (%s, %s, %s, %s)"
    val = customer, courier, status, product
    cursor.execute(sql, val)
    connection.commit()


# update an order's status. need to fix
def update_order_status():
    join_table()
    selected_order_id = int(input(
        'Choose the Order No. for the order status you want to update:\n'))
    select_table(4)
    new_status = input(
        "Choose the corresponding index number for the status you want to update to the order with.\n")
    cursor.execute(
        f"UPDATE Orders SET Status= {new_status} WHERE order_id = {selected_order_id}")
    connection.commit()
