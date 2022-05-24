<h1 align="center">
    <img src="https://i.imgur.com/WdCQeRa.gif" width="256" height="256"/>
</h1>

# Pop-up Cafe
A simple cafe app that allows the user to interact with his/her data in the database. 

## How to Use
The app starts at the main menu, with the following options:

    0: Save Changes and Exit the app.
    1: Product Menu.
    2: Courier Menu.
    3: Order Menu.

User must input the corresponding value, otherwise user will be prompt to input a valid option.

### 0: Save Changes and Exit the app.
User will save all changes and exit the app.

### 1: Product Menu.
In the product menu, user are given the following options:

    0: to return to main menu.
    1: View your product list.
    2: create a new product.
    3: update an existing product details.
    4: delete an existing product.

The Product Menu's options are relatively self-explanatory.

As always user must input the corresponding value, otherwise user will be prompt to input a valid option.


### 2: Courier Menu.
In the product menu, user are given the following options:

    0: to return to main menu.
    1: Check you current Courier list.
    2: enter a new Courier details.
    3: update an existing Courier details.
    4: delete an existing Courier.
    

The Courier Menu's options are relatively self-explanatory.

As always user must input the corresponding value, otherwise user will be prompt to input a valid option.

Lastly.

### 3: Order Menu.

    0: to return to main menu.
    1: View your Orders.
    2: enter a new order details.
    3: update an existing order's status.
    4: update an existing order's details.
    5: delete an order.
   

An input of **0** will return the user back to the main menu.

Within the **View your Orders** option user will be yet prompted with the following options.

    1: View a list of Current Orders.
    2: View a list of Completed Orders.
    3: View a list of Cancelled Orders.
    4: View a list of ALL Orders.

In this menu user may enter the corresponding value to view different list of Orders, any other input and the user will be prompt with an **Invalid Option. Return to Order Menu.**

### Option 2
in the Order menu allows the user to create a new order. 

User will first be prompted with this:

    Is it a [N]ew or [E]xisting customer?

User can only enter either **n/new** for a new customer or **e/existing** for existing customer, any other input will result in the app prompting the user to reenter a valid option.

Afterward user will be given a list of current Courier and as always user need to input the corresponding Courier's ID to assigned the Courier to the customer.

Lastly, the user have to input the corresponding ID of the product the customer purchased seperating each product with a **,**  . The total price of all the product will be automatically added to the order, this will also be printed out for the user to see.

### Option 3
in the Order Menu is a quick menu for the user to quickly update the status of the current order. Orders that are completed or cancelled will not appear in this list for edit.

As usual a list of Status with index will be given to the user to choose from, and only the corresponding value is accepted, any other input will be invalid, and user will be prompted to reenter a valid option.

### Option 4 (WIP)
in the Order Menu allows the user more control on what to edit in the Order details.

User may input the corresponding Order ID to choose which Order the user wanted to update.

Once an order is selected, user will be prompted to type in the **exact** detail the user want to edit as below. 

- ID
- Customer
- Courier
- Status
- Product
- Total_Price

User are allowed to edit all of the above.
>ID, User can change the ID of the Order, but duplicated will result in an error.

>Customer, User can change the customer of the order to another existing customer. Allowing the user to input a new customer will be implemented in future version.

>Courier, User can change the courier of the other to another courier.

>Status, User can also chagne the status of the order here.

>Product, User can change the product purchased by the customer in here, this will also update the Total Price of the order.

>Total_Price, User can change the value of the order's total price. Maybe it's an additional tip from the customer. Or maybe you are overcharging the customer, you evil bugger.

As mentioned Option 4 is Work-in-Progress and little to none error handling was made here, and it will be implemented in future version.

Therefore user must input the **exact** value otherwise the app will crash.

Lastly,
### Option 5

User will be able to delete unwanted order.

# Installation
1. Start by downloading the following link:
https://github.com/mkfc13/generation_cafe_miniproject/archive/refs/heads/main.zip

2. Extract the zip into your desired destination.

3. You need the following program.


    python = https://www.python.org/downloads/

    docker = https://www.docker.com/products/docker-desktop/


4. Install python and docker.

5. Start a docker server.

6. Start a venv in python.

7. Open the app.py.

# To do list
- [ ] Add Unit Testing for my functions
- [ ] Stocks update
- [ ] fix phone list to be more viewable
- [ ] error handle Update Order function.
- [ ] make a product list so that the order show the product purchased rather than the ID.
- [ ] finish my README installation guide.


