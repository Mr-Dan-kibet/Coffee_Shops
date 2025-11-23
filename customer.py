# customer.py

class Customer:
    
    # Track all customer instances
    all = []

    # Initialize a new customer with a name.
    def __init__(self, name):
        self._name = None
        self.name = name  # Uses the property setter for validation
        Customer.all.append(self)

    # Name property with validation
    @property
    def name(self):
    # Get the customer's name
        return self._name

    @name.setter
    def name(self, value):
    # Set the customer's name with validation
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        
        value = value.strip()
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        
        self._name = value

    def orders(self):

    # Get all orders placed by this customer.

        from order import Order
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
    # Get all unique coffees ordered by this customer.

        # Get all coffees from this customer's orders
        ordered_coffees = [order.coffee for order in self.orders()]
        
        # Return unique coffees while preserving order
        unique_coffees = []
        seen_coffees = set()
        
        for coffee in ordered_coffees:
            if coffee not in seen_coffees:
                unique_coffees.append(coffee)
                seen_coffees.add(coffee)
                
        return unique_coffees

    def create_order(self, coffee, price):

    # Create a new order for this customer.
    
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        
    # Find the customer who spent the most on a specific coffee.
        
        if coffee is None:
            raise ValueError("Coffee cannot be None.")
            
        # Get all orders for this coffee
        from order import Order
        coffee_orders = [order for order in Order.all if order.coffee is coffee]
        
        # Return None if no one ordered this coffee
        if not coffee_orders:
            return None
        
        # Calculate total spent per customer
        customer_spending = {}
        for order in coffee_orders:
            customer = order.customer
            customer_spending[customer] = customer_spending.get(customer, 0.0) + order.price
        
        # Find customer with highest spending
        top_customer = max(customer_spending.items(), key=lambda item: item[1])[0]
        return top_customer

    def __repr__(self):
        return f"Customer name='{self.name}'"