from functions.function import *
from functions.logo import *
# from functions.courier import *
# from functions.product import *
# from functions.option import *


# def short_update_order():
#     choice = menu_input(order_list)
#     for key, value in dict(order_list)[choice].items():
#         print("Do you want to change the value\n")
#         print(f"{key}: {value}")
#         replace = input('')
#         if len(replace) == 0:
#             print("No update has been done.")
#         else:
#             dict(order_list)[choice][key] = replace


# def update_order():
#     print('\nChoose the corresponding index number for the order you want to update:')
#     choice = menu_input(order_list)
#     order_dict = dict(order_list[choice])
#     new_order_dict = {}
#     new_customer_name = input(
#         "Please input the new customer's name or Enter to skip.\n")
#     if new_customer_name == '':
#         print("No update to Customer's Name.\n")
#         new_order_dict['customer_name'] = order_dict.get('customer_name')
#     else:
#         print(
#             f"***{order_dict.get('customer_name')} has been updated to {new_customer_name}.***\n")
#         new_order_dict['customer_name'] = new_customer_name
#     new_customer_address = input(
#         "Please input the new customer's address or Enter to skip.\n")
#     if new_customer_address == '':
#         print("No update to Customer's Address.\n")
#         new_order_dict['customer_address'] = order_dict.get('customer_address')
#     else:
#         print(
#             f"***{order_dict.get('customer_address')} has been updated to {new_customer_address}.***\n")
#         new_order_dict['customer_address'] = new_customer_address
#     new_customer_phone = input(
#         "Please input the new customer's phone number or Enter to skip.\n")
#     if new_customer_phone == '':
#         print("No update to Customer's Phone Number.\n")
#         new_order_dict['customer_phone'] = order_dict.get('customer_phone')
#     else:
#         print(
#             f"***{order_dict.get('customer_phone')} has been updated to {new_customer_phone}.***\n")
#         new_order_dict['customer_phone'] = new_customer_phone
#     print('Courier List')
#     enum_courier_list()
#     only_courier_list = pd_courier_list()
#     print("Please input the new number of the assigned courier or Enter to skip.\n")
#     courier_no = user_input(only_courier_list)
#     if courier_no == "":
#         print("No update to Assigned Courier.\n")
#         new_order_dict['courier'] = order_dict.get('courier')
#     elif 0 <= courier_no < len(only_courier_list):
#         print(
#             f"***{order_dict.get('courier')} has been updated to {only_courier_list[courier_no]}.***\n")
#         new_order_dict['courier'] = only_courier_list[courier_no]
#     print('Available Status')
#     enum_status_list()
#     print("Please input the corresponding index number for a new order status or Enter to skip.\n")
#     new_status = user_input(status_list)
#     if new_status == '':
#         print("No update to Order's Status.\n")
#         new_order_dict['status'] = order_dict.get('status')
#     elif 0 <= int(new_status) < len(status_list):
#         print(
#             f"***{order_dict.get('status')} has been updated to {status_list[int(new_status)]}.***\n")
#         new_order_dict['status'] = status_list[int(new_status)]
#     new_purchased_list = []
#     while True:
#         enum_product_list()
#         print("Please input the new product to be updated or Enter to skip.\n")
#         new_purchased_item = user_input(product_list)
#         if new_purchased_item == '':
#             print("No update to Customer's Purchased Items.\n")
#             new_order_dict['items'] = order_dict.get('items')
#             break
#         elif 0 <= int(new_purchased_item) < len(product_list):
#             only_product_list = pd_product_list()
#             new_purchased_list.append(only_product_list[new_purchased_item])
#             print(f"purchases so far: {new_purchased_list}")
#             more_purchase = input(
#                 "Do you want to purchase more item? Enter 'Y'es to continue, or just press Enter or 'N'o to stop.\n").lower()
#             if more_purchase == '' or more_purchase == 'n' or more_purchase == 'no':
#                 new_order_dict['items'] = new_purchased_list
#                 break
#             elif more_purchase == 'y' or more_purchase == 'yes':
#                 continue
#             else:
#                 print("Invalid option, assuming you don't want to add more purchase")
#                 new_order_dict['items'] = new_purchased_list
#                 break
#         else:
#             print("Invalid option, assuming you don't want to add more purchase")
#             new_order_dict['items'] = new_purchased_list
#             break
#     order_list[choice] = new_order_dict
#     print('Order has been updated to:')
#     print(new_order_dict)


# # def delete_order():
# #     print("Enter the corresponding index number to delete the order: \n")
# #     item = user_input(order_list)
# #     print(f"***{order_list[item]} has been deleted.***\n")
# #     del order_list[item]

# def delete_courier():
#     print("Enter the corresponding index number to delete courier from the fulfilled order: \n")
#     item = menu_input(order_list)
#     del_courier = order_list[item]
#     print(f"***{del_courier['courier']} has been deleted.***\n")
#     del_courier["courier"] = "Deleted"
#     del_courier["status"] = "Completed"


def order_menu(choice):
    while True:
        print_order_menu_message()
        num = input()
        print('................................................................\n')

        if num == '0':
            print('***Return to Main Menu.***\n')
            print_main_menu_logo()
            break

        elif num == '1':
            select_table(choice)
            print('................................................................\n')

        elif num == '2':
            create_new_order()
            print('................................................................\n')

        elif num == '3':
            update_order_status()
            print('................................................................\n')

        elif num == '4':
            update_row(choice)
            print('................................................................\n')

        elif num == '5':
            delete_row(choice)
            print('................................................................\n')
        else:
            print('Please choose only the following options:\n')
