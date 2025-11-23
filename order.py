# order.py

class Order:
    
    # Track all order instances
    all = []

    #  Initialize a new order.
    def __init__(self, customer, coffee, price):

        # Import here and not in circular imports to avoid conflicts in debug.py 
        from customer import Customer as CustomerClass
        from coffee import Coffee as CoffeeClass

        # Validate customer type
        if not isinstance(customer, CustomerClass):
            raise TypeError("Customer must be a Customer instance.")
            
        # Validate coffee type  
        if not isinstance(coffee, CoffeeClass):
            raise TypeError("Coffee must be a Coffee instance.")
        
        # Validate price
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
            
        price = float(price)
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0 inclusive.")

        # Set the order properties
        self._customer = customer
        self._coffee = coffee
        self._price = price

        Order.all.append(self)

    # Read-only properties (no setters to maintain data integrity)
    @property
    def customer(self):
    # Get the customer who placed this order.
        return self._customer

    @property
    def coffee(self):
    # Get the coffee that was ordered
        return self._coffee

    @property
    def price(self):
    # Get the price of this order
        return self._price

    def __repr__(self):
        return f"Order customer='{self.customer.name}' coffee='{self.coffee.name}' price={self.price:.2f}"