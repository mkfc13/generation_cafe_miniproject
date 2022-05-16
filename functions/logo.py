def print_cafe_logo():
    cafe_logo = ("""
 _______                                               ______           ___        
|_   __ \                                            .' ___  |        .' ..]       
  | |__) | .--.   _ .--.   ______  __   _  _ .--.   / .'   \_| ,--.  _| |_  .---.  
  |  ___// .'`\ \[ '/'`\ \|______|[  | | |[ '/'`\ \ | |       `'_\ :'-| |-'/ /__\\ 
 _| |_   | \__. | | \__/ |         | \_/ |,| \__/ | \ `.___.'\// | |, | |  | \__., 
|_____|   '.__.'  | ;.__/          '.__.'_/| ;.__/   `.____ .'\'-;__/[___]  '.__.' 
                 [__|                     [__|                                     
                        """)
    print(cafe_logo + '\n')


def print_main_menu_logo():
    main_menu_logo = '''         
 ______        _          ______                    
|  ___ \      (_)        |  ___ \                   
| | _ | | ____ _ ____    | | _ | | ____ ____  _   _ 
| || || |/ _  | |  _ \   | || || |/ _  )  _ \| | | |
| || || ( ( | | | | | |  | || || ( (/ /| | | | |_| |
|_||_||_|\_||_|_|_| |_|  |_||_||_|\____)_| |_|\____|                      
'''
    print(main_menu_logo + '\n')


def print_main_menu_message():
    main_menu = '\n 0: Save Changes and Exit the app. \n 1: Product Menu.\n 2: Courier Menu. \n 3: Order Menu. \n'
    print(main_menu)


def print_product_menu_logo():
    product_menu_logo = ('''
     ______               _                     ______                    
    (_____ \             | |            _      |  ___ \                   
     _____) )___ ___   _ | |_   _  ____| |_    | | _ | | ____ ____  _   _ 
    |  ____/ ___) _ \ / || | | | |/ ___)  _)   | || || |/ _  )  _ \| | | |
    | |   | |  | |_| ( (_| | |_| ( (___| |__   | || || ( (/ /| | | | |_| |
    |_|   |_|   \___/ \____|\____|\____)\___)  |_||_||_|\____)_| |_|\____|
    ''')
    print(product_menu_logo + '\n')


def print_product_menu_message():
    product_menu_message = '0: to return to main menu. \n1: for your product list. \n2: create a new product. \n3: update an existing product. \n4: delete an existing product.\n'
    print(product_menu_message)


def print_courier_menu_logo():
    courier_menu_logo = ('''
  ______                  _                ______                    
 / _____)                (_)              |  ___ \                   
| /      ___  _   _  ____ _  ____  ____   | | _ | | ____ ____  _   _ 
| |     / _ \| | | |/ ___) |/ _  )/ ___)  | || || |/ _  )  _ \| | | |
| \____| |_| | |_| | |   | ( (/ /| |      | || || ( (/ /| | | | |_| |
 \______)___/ \____|_|   |_|\____)_|      |_||_||_|\____)_| |_|\____|
    ''')
    print(courier_menu_logo + '\n')


def print_courier_menu_message():
    courier_menu_message = '0: to return to main menu. \n1: Check you current Courier list. \n2: enter a NEW Courier name. \n3: update an existing Courier name. \n4: delete an existing Courier name.\n'
    print(courier_menu_message)


def print_order_menu_logo():
    order_menu_logo = ('''
  _____           _                ______
 / ___ \         | |              |  ___ \                   
| |   | | ____ _ | | ____  ____   | | _ | | ____ ____  _   _ 
| |   | |/ ___) || |/ _  )/ ___)  | || || |/ _  )  _ \| | | |
| |___| | |  ( (_| ( (/ /| |      | || || ( (/ /| | | | |_| |
 \_____/|_|   \____|\____)_|      |_||_||_|\____)_| |_|\____|
    ''')
    print(order_menu_logo + '\n')


def print_order_menu_message():
    order_menu_message = "0: to return to main menu. \n1: Print you current Orders Dictionary. \n2: enter a NEW order. \n3: update an existing order's status. \n4: update an existing order. \n5: delete an order.\n"
    print(order_menu_message)


def print_exit_message():
    exit_message = (''' 
................................................................
.%%%%%%..%%..%%..%%%%%%..%%%%%%...........%%%%...%%%%%...%%%%%..
.%%.......%%%%.....%%......%%............%%..%%..%%..%%..%%..%%.
.%%%%......%%......%%......%%............%%%%%%..%%%%%...%%%%%..
.%%.......%%%%.....%%......%%............%%..%%..%%......%%.....
.%%%%%%..%%..%%..%%%%%%....%%............%%..%%..%%......%%.....
................................................................
        ''')
    print(exit_message)
