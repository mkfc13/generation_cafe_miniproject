import csv
from venv import create
import pandas as pd
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             database='test',
                             charset='utf8mb4',
                             port=3306)

cursor = connection.cursor()


def create_new_product(new_product_name, new_product_price):
    new_product_name = input('please type in your new product name: \n')
    new_product_price = input('please type in your new product price: \n')
    sql = "INSERT INTO product (Product, Price) VALUES (%s, %s)"
    val = (new_product_name, new_product_price)
    cursor.execute(sql, val)
    connection.commit()



cursor.close()
connection.close()


def open_file(csv_file):
    new_list = []
    with open(csv_file, 'r') as infile:
        csv_reader = csv.DictReader(infile)
        for row in csv_reader:
            new_list.append(row)
        return new_list


def save_file(csv_file, header, new_list):
    with open(csv_file, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=header)
        writer.writeheader()
        for dict in new_list:
            writer.writerow(dict)
