# Mini Project Week 6Mini Project Week 6

Let's now maintain all our data in the database. We'll create an orders table and refactor our app to make use of it.

## GoalsGoals

As a user I want to:

```
create a product, courier, or order and add it to a list
view all products, couriers, or orders
update the status of an order
persist my data
```
## STRETCH delete or update a product, order, or courier

## BONUS list orders by status or courier

## BONUS CRUD a list of customers

## BONUS track my product inventory

## BONUS import/export my entities in CSV format

## SpecSpec

```
A product should be a dict, i.e:
```
### {

```
"id": 4,
"name": "Coke Zero",
"price": 0.
}
```
```
A courier should be a dict, i.e:
```
### {

```
"id": 2,
"name": "Bob",
"phone": "0789887889"
}
```
```
An order should be a dict, i.e:
```
### {

```
"id": 1,
"customer_name": "John",
"customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
"customer_phone": "0789887334",
"courier": 2, // Courier ID
"status": "preparing",
"items": [1, 3, 4] // Product IDs
}
```
```
# we are no longer reading products, couriers, orders and order statuses from files
# we are now reading data from database tables
```
```
CREATE order status list
```
```
PRINT main menu options
GET user input for main menu option
```
```
IF user input is 0:
SAVE products list to products.csv
SAVE couriers list to couriers.csv
SAVE orders list to order.csv
EXIT app
```
```
# products menu
ELSE IF user input is 1:
PRINT product menu options
GET user input for product menu option
```

GET user input for product menu option

IF user inputs 0:
RETURN to main menu

# WEEK 5 UPDATE
ELSE IF user input is 1:
GET all products from products table
PRINT products

# WEEK 5 UPDATE
ELSE IF user input is 2:
# CREATE new product

GET user input for product name
GET user input for product price
INSERT product into products table

# WEEK 5 UPDATE
ELSE IF user input is 3:
# STRETCH GOAL - UPDATE existing product

GET all products from products table
PRINT products with their IDs
GET user input for product ID

GET user input for product name
GET user input for product price

IF any inputs are empty, do not update them
UPDATE properties for product in product table

ELSE IF user input is 4:
# STRETCH GOAL - DELETE product

GET all products from products table
PRINT products with their IDs

GET user input for product ID
DELETE product in products table

# couriers menu
ELSE IF user input is 2:
PRINT courier menu options
GET user input for courier menu option

IF user inputs 0:
RETURN to main menu

ELIF user inputs 1:
PRINT couriers list

# WEEK 5 UPDATE
ELSE IF user input is 2:
# CREATE new courier

GET user input for courier name
GET user input for courier phone number
INSERT courier into couriers table

# WEEK 5 UPDATE
ELSE IF user input is 3:
# STRETCH GOAL - UPDATE existing courier

GET all couriers from couriers table
PRINT couriers with their IDs


PRINT couriers with their IDs
GET user input for courier ID

GET user input for courier name
GET user input for courier phone number

IF an input is empty, do not update its respective table property
UPDATE properties for courier in courier table

ELSE IF user input is 4:
# STRETCH GOAL - DELETE courier

GET all couriers from couriers table
PRINT courier with their IDs

GET user input for courier ID
DELETE courier in couriers table

# orders menu
ELSE IF user input is 3:
IF user input is 0:
RETURN to main menu

ELSE IF user input is 1:
PRINT orders dictionary

# WEEK 6 UPDATE
ELSE IF user input is 2:
# CREATE order

GET user input for customer name
GET user input for customer address
GET user input for customer phone number

GET all products from products table
PRINT products
GET user inputs for comma-separated list of product IDs
CONVERT above user input to list of integers

GET all couriers from couriers table
PRINT couriers
GET user input for courier ID

SET order status to be 1
INSERT order into orders table

# WEEK 6 UPDATE
ELSE IF user input is 3:
# UPDATE existing order status

GET all orders from orders table
PRINT orders with their IDs

GET all order statuses from order_status table
PRINT order statuses
GET user input for order status ID
UPDATE status for order

# WEEK 6 UPDATE
ELSE IF user input is 4:
# STRETCH - UPDATE existing order

GET all orders from orders table
PRINT orders with their IDs
GET user input for order ID

GET user input for customer name


GET user input for customer name
GET user input for customer address
GET user input for customer phone number

GET all products from products table
PRINT products
GET user inputs for comma-separated list of product IDs
CONVERT above user input to list of integers

GET all couriers from couriers table
PRINT couriers
GET user input for courier ID

UPDATE order in orders table

# WEEK 6 UPDATE
ELSE IF user input is 4:
# STRETCH GOAL - DELETE courier

GET all orders from orders table
PRINT orders with their IDs

GET user input for order ID
DELETE order in orders table


