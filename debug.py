# debug.py
from customer import Customer
from coffee import Coffee
from order import Order

def main():
    # Demonstration script to test the coffee shop domain model.
    # Creates sample data and tests all functionality.
    
    # Clear any previous data (helpful for testing)
    Customer.all.clear()
    Coffee.all.clear()
    Order.all.clear()

    print("1. CREATING COFFEE SHOP DATA\n")

    # Create customers
    print("Creating customers...")
    alice = Customer("Alice")
    bob = Customer("Bob")
    charlie = Customer("Charlie")
    print(f"Created: {[c.name for c in Customer.all]}")

    # Create coffees
    print("\nCreating coffees...")
    latte = Coffee("Latte")
    mocha = Coffee("Mocha")
    espresso = Coffee("Espresso")
    americano = Coffee("Americano")
    print(f"Created: {[c.name for c in Coffee.all]}")

    # Create orders
    print("\nCreating orders...")
    alice.create_order(latte, 5.0)
    alice.create_order(mocha, 7.0)
    bob.create_order(latte, 4.5)
    bob.create_order(latte, 6.0)  # Bob orders Latte twice
    charlie.create_order(espresso, 3.5)
    print(f"Created {len(Order.all)} orders")

    # Display all orders
    print("\n2. ALL ORDERS")
    for order in Order.all:
        print(f"  {order}")

    # Show customer-coffee relationships
    print("\n3. CUSTOMER COFFEE PREFERENCES")
    for customer in Customer.all:
        coffee_names = [coffee.name for coffee in customer.coffees()]
        print(f"  {customer.name}: {coffee_names}")

    # Show coffee statistics
    print("\n4. COFFEE STATISTICS")
    for coffee in Coffee.all:
        num_orders = coffee.num_orders()
        avg_price = coffee.average_price()
        customer_names = [customer.name for customer in coffee.customers()]
        
        print(f"  {coffee.name}:")
        print(f"    Orders: {num_orders}")
        print(f"    Average Price: ${avg_price:.2f}")
        print(f"    Customers: {customer_names}")

    # Test the most_aficionado method
    print("\n5. COFFEE AFICIONADOS")
    latte_lover = Customer.most_aficionado(latte)
    print(f"  Biggest Latte lover: {latte_lover.name if latte_lover else 'None'}")
    
    # Test with coffee that has no orders
    americano_lover = Customer.most_aficionado(americano)
    print(f"  Biggest Americano lover: {americano_lover.name if americano_lover else 'None'}")


if __name__ == "__main__":
    main()