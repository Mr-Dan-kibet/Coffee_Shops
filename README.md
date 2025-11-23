# Coffee Shop {Week 2 Code challenge}

This project models a Coffee Shop domain using Object-Oriented Programming principles in Python. It includes three core classes — Customer, Coffee, and Order — demonstrating initializers, validation, object relationships, and aggregation methods.

This repository satisfies the requirements of the Week 2 Python OOP Code Challenge.

## Project Structure
```
coffee_shop/
│
├── customer.py
├── coffee.py
├── order.py
├── debug.py
│
├── Pipfile
├── Pipfile.lock
└── README.md

```

## Domain Overview

The domain consists of three entities:

### 1.Customer

- Initialized with a validated name (1–15 chars)

- Can create multiple orders

- Can retrieve:

  > All orders the customer has made

  > All coffees the customer has ordered (unique)

Includes create_order(coffee, price)

Includes class method most_aficionado(coffee) → finds the customer who spent the most on a given coffee

### 2.Coffee

- Initialized with a validated name (≥ 3 chars)

- Can retrieve:

  > All orders for that coffee

  > All customers who ordered it (unique)

- Provides aggregation methods:

  > num_orders()

  > average_price()

### 3.Order

- Connects a Customer to a Coffee

- Stores:

     > customer (validated instance)

     > coffee (validated instance)

     > price (float between 1.0 and 10.0)

## Relationships

- A Customer can have many Orders

- A Coffee can have many Orders

- An Order belongs to one Customer and one Coffee

- Customers and Coffees have a many-to-many relationship through Orders

## Installation & Setup

1. Clone the Repository
```
git clone 
cd coffee_shop
```
2. Create Virtual Environment Using Pipenv

```
pipenv install
pipenv shell

```
3. Requirments

- Python 3.6+
- pipenv (for virtual environment management)


## Features Implemented

### Full OOP Design

- Separate class files (customer.py, coffee.py, order.py)

- Encapsulated attributes using properties

- Validation in setters & initializers

### Relationship Methods

Customer: ```orders(), coffees()```

Coffee: ``` orders(), customers()```

### Aggregate Methods

Coffee: ```num_orders(), average_price()```

Customer: ```most_aficionado(coffee)```

### Helper Methods & Validation

- Ensures single source of truth

- Raises exceptions for invalid input:

    > Wrong types

    > Illegal price values

    > Invalid names

### Debugging Script [Testing]

Use ``` debug.py``` to manually run and test your code:
```
python debug.py
```

The debug script demonstrates:

- Creating customers, coffees, and orders

- Testing all relationship methods

- Validating error handling

- Showing aggregation results

- Demonstrating the ```most_aficionado``` functionality

### Input Validation

This project raises exceptions for invalid input, such as:

- Customer name not a string or exceeds 15 characters

- Coffee name shorter than 3 characters

- Price not a float or outside range 1.0–10.0

- Order initialized with invalid customer/coffee instances



## Author

Dan Rotich,

Coffee Enthusiast & Python Developer

Dan's Coffee House
