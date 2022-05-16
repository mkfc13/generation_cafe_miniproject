# Mini Project Week 4

Now that we've learned how to work with two-dimensional data, let's refactor our app to use dictionaries for both product and courier.

Building upon our use of a courier index within our order, let's create a list of product indexes now for order items.

We'll also need to refactor our storage layer to use `.csv` files rather than `.txt` to bring back our persistence functionality.

Unit-tests from previous weeks will need to be updated.

## Goals

As a user I want to:

- create a product, courier, or order and add it to a list
- view all products, couriers, or orders
- update the status of an order
- persist my data
- _STRETCH_ update or delete a product, order, or courier
- _BONUS_ list orders by status or courier

## Spec

- A `product` should be a `dict`, i.e:

```json
{
  "name": "Coke Zero",
  "price": 0.8 // Float
}
```

- A `courier` should be a `dict`, i.e:

```json
{
  "name": "Bob",
  "phone": "0789887889"
}
```

- An `order` should be a `dict`, i.e:

```json
{
  "customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "courier": 2, // Courier IDX
  "status": "preparing",
  "items": [1, 3, 4] // Product IDs
}
```

- Data should be persisted to a `.csv` file on a new line for each `courier`, `order`, or `product`, ie:

```csv
# ORDER
John,"Unit 2, 12 Main Street, LONDON, WH1 2ER",2,preparing,"1,3,4"
```

## Pseudo Code

```txt
LOAD products list from products.csv    # WEEK 4 UPDATE
LOAD couriers list from couriers.csv    # WEEK 4 UPDATE
LOAD orders list from orders.csv        # WEEK 4 UPDATE
CREATE order status list

PRINT main menu options
GET user input for main menu option

IF user input is 0:
    SAVE products list to products.csv
    SAVE couriers list to couriers.csv
    SAVE orders list to order.csv
    EXIT app

# products menu
ELSE IF user input is 1:
    PRINT product menu options
    GET user input for product menu option

    IF user inputs 0:
        RETURN to main menu

    ELSE IF user input is 1:
        PRINT products list

    # WEEK 4 UPDATE
    ELSE IF user input is 2:
        # CREATE new product

        GET user input for product name
        GET user input for product price
        CREATE new product dictionary with above properties
        APPEND product dictionary to products list

    # WEEK 4 UPDATE
    ELSE IF user input is 3: 
        # STRETCH GOAL - UPDATE existing product

        PRINT products with their index values
        GET user input for product index value

        FOR EACH key-value pair in selected product:
            GET user input for updated property
            IF user input is blank:
                do not update this property and skip
            ELSE:
                update the property value with user input

    ELSE IF user input is 4:
        # STRETCH GOAL - DELETE product
        
        PRINT products list
        GET user input for product index value
        DELETE product at index in products list

# couriers menu
ELSE IF user input is 2:
    PRINT courier menu options
    GET user input for courier menu option

    IF user inputs 0:
        RETURN to main menu

    ELIF user inputs 1:
        PRINT couriers list

    # WEEK 4 UPDATE
    ELSE IF user input is 2:
        # CREATE new courier

        GET user input for courier name
        GET user input for courier phone number
        CREATE new courier dictionary with above properties
        APPEND courier dictionary to courier list

    # WEEK 4 UPDATE
    ELSE IF user input is 3: 
        # STRETCH GOAL - UPDATE existing courier

        PRINT courier with their index values
        GET user input for courier index value

        FOR EACH key-value pair in selected courier:
            GET user input for updated property
            IF user input is blank:
                do not update this property and skip
            ELSE:
                update the property value with user input

    ELSE IF user input is 4:
        # STRETCH GOAL - DELETE courier
            
        PRINT courier list
        GET user input for courier index value
        DELETE courier at index in courier list

# orders menu
ELSE IF user input is 3:
    IF user input is 0:
        RETURN to main menu

    ELSE IF user input is 1:
        PRINT orders dictionary

    # WEEK 4 UPDATE
    ELSE IF user input is 2:
        GET user input for customer name
        GET user input for customer address
        GET user input for customer phone number

        PRINT products list with its index values
        GET user inputs for comma-separated list of product index values
        CONVERT above user input to list of integers

        PRINT couriers list with index value for each courier
        GET user input for courier index to select courier
        SET order status to be 'PREPARING'

        CREATE new order dictionary with above properties
        APPEND order to orders list

    ELSE IF user input is 3:
        # UPDATE existing order status

        PRINT orders list with its index values
        GET user input for order index value

        PRINT order status list with index values
        GET user input for order status index value
        UPDATE status for order

    ELSE IF user input is 4:
        # STRETCH - UPDATE existing order

        PRINT orders list with its index values
        GET user input for order index value

        FOR EACH key-value pair in selected order:
            GET user input for updated property
            IF user input is blank:
                do not update this property
            ELSE:
                update the property value with user input

    ELSE IF user input is 5:
        # STRETCH GOAL - DELETE courier
                    
        PRINT orders list
        GET user input for order index value
        DELETE order at index in order list
```
