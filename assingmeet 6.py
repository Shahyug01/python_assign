class MenuItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name}: ${self.price} (Quantity: {self.quantity})"

menu_items = []

def add_item(name, price, quantity):
    menu_items.append(MenuItem(name, price, quantity))

def update_item(name, price, quantity):
    for item in menu_items:
        if item.name == name:
            item.price = price
            item.quantity = quantity
            break

def delete_item(name):
    global menu_items
    menu_items = [item for item in menu_items if item.name != name]

def display_menu():
    for item in menu_items:
        print(item)

def read_menu_from_file():
    global menu_items
    menu_items = []
    try:
        with open("menu.txt", "r") as file:
            for line in file:
                name, price, quantity = line.strip().split(",")
                menu_items.append(MenuItem(name, float(price), int(quantity)))
    except FileNotFoundError:
        pass

def write_menu_to_file():
    with open("menu.txt", "w") as file:
        for item in menu_items:
            file.write(f"{item.name},{item.price},{item.quantity}\n")

read_menu_from_file()

class CustomException(Exception):
    pass

class InvalidMenuItemError(CustomException):
    pass

class InsufficientQuantityError(CustomException):
    pass

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, name, quantity):
        for item in menu_items:
            if item.name == name:
                if item.quantity >= quantity:
                    self.items.append((item, quantity))
                    item.quantity -= quantity
                    break
                else:
                    raise InsufficientQuantityError(f"Insufficient quantity of {name}")
        else:
            raise InvalidMenuItemError(f"{name} is not in the menu")

    def calculate_total(self):
        return sum(item.price * quantity for item, quantity in self.items)

    def generate_receipt(self):
        print(f"Receipt for {self.customer_name}:")
        for item, quantity in self.items:
            print(f"{item.name} x {quantity}: ${item.price * quantity}")
        print(f"Total: ${self.calculate_total()}")

def take_order():
    customer_name = input("Enter your name: ")
    order = Order(customer_name)
    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            quantity = int(input("Enter quantity: "))
            order.add_item(name, quantity)
        except (InvalidMenuItemError, InsufficientQuantityError) as e:
            print(e)
    return order

orders = []

def read_orders_from_file():
    global orders
    orders = []
    try:
        with open("orders.txt", "r") as file:
            for line in file:
                customer_name, *items = line.strip().split(",")
                order = Order(customer_name)
                for item in items:
                    if item:
                        name, quantity = item.split(":")
                        order.add_item(name, int(quantity))
                orders.append(order)
    except FileNotFoundError:
        pass

def write_orders_to_file():
    with open("orders.txt", "w") as file:
        for order in orders:
            items = [f"{item.name}:{quantity}" for item, quantity in order.items]
            file.write(f"{order.customer_name}," + ",".join(items) + "\n")

read_orders_from_file()

def main():
    while True:
        print("Restaurant Management System")
        print("1. Manage Menu")
        print("2. Place Order")
        print("3. View Orders")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                print("Menu Management")
                print("1. Add Item")
                print("2. Update Item")
                print("3. Delete Item")
                print("4. Display Menu")
                print("5. Back")
                choice = input("Enter your choice: ")

                if choice == "1":
                    name = input("Enter item name: ")
                    price = float(input("Enter item price: "))
                    quantity = int(input("Enter item quantity: "))
                    add_item(name, price, quantity)
                    write_menu_to_file()
                elif choice == "2":
                    name = input("Enter item name: ")
                    price = float(input("Enter new price: "))
                    quantity = int(input("Enter new quantity: "))
                    update_item(name, price, quantity)
                    write_menu_to_file()
                elif choice == "3":
                    name = input("Enter item name: ")
                    delete_item(name)
                    write_menu_to_file()
                elif choice == "4":
                    display_menu()
                elif choice == "5":
                    break
        elif choice == "2":
            order = take_order()
            orders.append(order)
            write_orders_to_file()
            order.generate_receipt()  
        elif choice == "3":
            for order in orders:
                order.generate_receipt()
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
