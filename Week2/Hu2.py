# =========================
# INVENTORY SYSTEM WITH MENU
# =========================

# list to store products
inventory = []


# =========================
# FUNCTION: ADD PRODUCT
# =========================
def add_product():

    name = input("Enter product name: ")

    # validate price
    while True:
        try:
            price = float(input("Enter price: "))
            if price >= 0:
                break
            else:
                print("Price cannot be negative")
        except:
            print("Error: enter a valid number")

    # validate quantity
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity >= 0:
                break
            else:
                print("Quantity cannot be negative")
        except:
            print("Error: enter a valid integer")

    # create product dictionary
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    # add to inventory list
    inventory.append(product)

    print("Product added successfully\n")


# =========================
# FUNCTION: SHOW INVENTORY
# =========================
def show_inventory():

    if len(inventory) == 0:
        print("Inventory is empty\n")
    else:
        print("----- INVENTORY -----")

        for product in inventory:
            print("Product:", product["name"],
                  "| Price:", product["price"],
                  "| Quantity:", product["quantity"])
        print()


# =========================
# FUNCTION: CALCULATE STATISTICS
# =========================
def calculate_statistics():

    if len(inventory) == 0:
        print("No products available\n")
        return

    total_value = 0
    total_products = 0

    for product in inventory:
        total_value += product["price"] * product["quantity"]
        total_products += product["quantity"]

    print("----- STATISTICS -----")
    print("Total inventory value:", total_value)
    print("Total quantity of products:", total_products)
    print()


# =========================
# MAIN MENU
# =========================
while True:

    print("===== MENU =====")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Calculate statistics")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        add_product()

    elif option == "2":
        show_inventory()

    elif option == "3":
        calculate_statistics()

    elif option == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid option\n")


# =========================
# END OF PROGRAM
# =========================
# This program allows the user to manage an inventory using a menu.
# The user can add products, view the inventory, and calculate statistics.
# It uses lists, dictionaries, loops, conditionals, and functions.