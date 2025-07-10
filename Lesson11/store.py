import random

def display_menu():
    print("\n **WELCOME TO THE FUTURISTIC STORE INVENTORY SYSTEM**")
    print("1. View Store Inventory ")
    print("2. Add A New Product")
    print("3. Remove Products")
    print("4. Exit\n")

def display_inventory():
    for product in store_inventory:
        print(f"id: {product.id}, name: {product.productName}, type: {product.type}, price: {product.price}, stock: {product.total}")
        pass

def exit_inventory():
    exit()

def add_item():
    print("\nadding new product")
    itemName = input("enter product name: ")
    itemType = input("enter product type: ")
    price = float(input("enter product price: "))
    total = int(input("enter number in stock: "))
    item_id = random.randint(1000, 9999)

    new_item = Product(item_id, itemName, price, total, itemType)
    store_inventory.append(new_item)
    print(f"\nProduct '{itemName}' added with the following ID: {item_id}.\n")
    
def remove_item():
    try:
        user_removal = int(input("enter ID of item you want removed: "))
        for item in store_inventory:
            if item.id == user_removal:
                store_inventory.remove(item)
                break
    except ValueError:
        print("type an integer instead.")




def user_selection():
    user_choice = int(input("Enter a number between 1-4: "))
    if user_choice == 1:
        display_inventory()
    elif user_choice == 2:
        add_item()
    elif user_choice == 3:
        remove_item()
    elif user_choice == 4:
        print("Program ends.")
        exit_inventory()
    else:
        print("\nSorry, Not a Valid Choice. Please try again!")

class Product:
    def __init__(self, product_id, productName, price, total, type):
        self.id = product_id  
        self.productName = productName
        self.price = price
        self.total = total
        self.type = type


base_inventory = [
    {'product_id': 4327, 'type': 'LASER GUN',   'price': 100.0,  'total': 20},
    {'product_id': 3915, 'type': 'a little propeller heat', 'price': 43.5,   'total': 32},
    {'product_id': 2119, 'type': 'HOVERBOARD',   'price': 34.0,   'total': 19},
    {'product_id': 1194, 'type': 'ASTRONAUT FOOD', 'price': 250.0,  'total': 5},
    {'product_id': 1300, 'type': 'JETPACK',  'price': 24.76,  'total': 3},
    {'product_id': 1118, 'type': 'H20',   'price': 50.0,   'total': 10},
    {'product_id': 1664, 'type': 'SPACESUITS',   'price': 250.0,  'total': 5}
]

store_inventory = []
for item in base_inventory:
    product = Product(item['product_id'], item['type'], item['price'], item['total'], item['type'])
    store_inventory.append(product)

print(store_inventory[0].productName)

while True:
    display_menu()
    user_selection()