import csv
from unittest.mock import Mock
from unittest.mock import patch
import pytest


def open_product_file():
    product_list = []
    with open('Unit_Test/test_stuff.csv', 'r') as infile:
        csv_reader = csv.DictReader(infile)
        for row in csv_reader:
            product_list.append(row)
        return product_list


product_list = open_product_file()


def test_open_product_file():
    result = open_product_file()
    expected = [{'Product': 'Espresso', 'Price': '1.25'}, {'Product': 'Double Espresso', 'Price': '2.89'}, {
        'Product': 'Macchiato', 'Price': '2.25'}, {'Product': 'Latte', 'Price': '3.50'}]

    assert result == expected


test_open_product_file()


def enumerate_new_list(new_list):
    for index, value in enumerate(new_list):
        print(f"{index}. {value}")


def menu_input(new_list):
    while True:
        num = input()
        try:
            num = int(num)
            if 0 <= num < len(new_list):
                num = num
            else:
                raise ValueError
            break
        except Exception as e:
            print("Please choose a valid option")
            print(enumerate_new_list(new_list))
    return num


# @patch('builtins.input', side_effect=[3])
# def test_menu_input(mock_input):
#     menu_input(mock_input)


def add_new_product_list():
    new_product_name = input('please type in your new product name: \n')
    new_product_price = input('please type in your new product price: \n')
    new_product = {"Product": new_product_name, "Price": new_product_price}
    product_list.append(new_product)


@patch('builtins.input', side_effect=['7up', '1.00'])
@patch('builtins.print')
def test_add_new_product_list(mock_print, mock_input):
    add_new_product_list()
    mock_print.assert_called_with("{'Product': 7up, 'Price': 1.00}")
    assert mock_input.call_count == 2
    assert mock_print.call_count == 1
