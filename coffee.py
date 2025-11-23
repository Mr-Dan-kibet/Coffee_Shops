# coffee.py

class Coffee:
    """
    Represents a coffee product in the shop.
    A coffee can be ordered by multiple customers and has order statistics.
    """
    
    # Track all coffee instances
    all = []

    # constructor to initalize a coffee name
    def __init__(self, name):
        self._name = None
        self.name = name 
        Coffee.all.append(self)

    # Name property with validation
    @property
    # Get the coffee's name
    def name(self):
        return self._name

    @name.setter
    # Set the coffee's name with validation.
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string.")
        
        value = value.strip()
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        
        self._name = value


    # Get all orders for this coffee.
    def orders(self):
        from order import Order
        return [order for order in Order.all if order.coffee is self]

    # Get all unique customers who ordered this coffee.
    def customers(self):
        # Get all customers from this coffee's orders
        ordering_customers = [order.customer for order in self.orders()]
        
        # Return unique customers while preserving order
        unique_customers = []
        seen_customers = set()
        
        for customer in ordering_customers:
            if customer not in seen_customers:
                unique_customers.append(customer)
                seen_customers.add(customer)
                
        return unique_customers

    #  Get the total number of times this coffee has been ordered.
    def num_orders(self):
        return len(self.orders())

    # Calculate the average price for this coffee across all orders.
    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0.0
            
        total_price = sum(order.price for order in orders)
        return total_price / len(orders)

    def __repr__(self):
        return f"Coffee name='{self.name}'"