from services import *
from files import *

inventory = []


# -------------------------
# INPUT HELPERS
# -------------------------
def get_float(msg):
    while True:
        try:
            value = float(input(msg))
            if value >= 0:
                return value
            print("Must be positive")
        except:
            print("Invalid number")


def get_int(msg):
    while True:
        try:
            value = int(input(msg))
            if value >= 0:
                return value
            print("Must be positive")
        except:
            print("Invalid integer")


# -------------------------
# DISPLAY
# -------------------------
def show_menu():
    print("\n" + "=" * 35)
    print("      INVENTORY SYSTEM")
    print("=" * 35)
    print("1. Add product")
    print("2. Show inventory")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Statistics")
    print("7. Save CSV")
    print("8. Load CSV")
    print("9. Exit")
    print("=" * 35)


def show_stats(stats):
    print("\n" + "-" * 35)
    print("STATISTICS")
    print("-" * 35)
    print(f"Total units: {stats['total_units']}")
    print(f"Total value: {stats['total_value']}")
    print(f"Most expensive: {stats['most_expensive']['name']}")
    print(f"Highest stock: {stats['highest_stock']['name']}")
    print("-" * 35 + "\n")


# -------------------------
# MAIN LOOP
# -------------------------
while True:

    show_menu()
    option = input("Choose option: ")

    if option == "1":
        name = input("Name: ")
        price = get_float("Price: ")
        quantity = get_int("Quantity: ")

        add_product(inventory, name, price, quantity)
        print("✔ Product added\n")

    elif option == "2":
        show_inventory(inventory)

    elif option == "3":
        name = input("Search name: ")
        product = find_product(inventory, name)

        print(product if product else "Not found\n")

    elif option == "4":
        name = input("Update name: ")
        price = get_float("New price: ")
        quantity = get_int("New quantity: ")

        update_product(inventory, name, price, quantity)

    elif option == "5":
        name = input("Delete name: ")
        delete_product(inventory, name)

    elif option == "6":
        stats = calculate_statistics(inventory)

        if stats:
            show_stats(stats)
        else:
            print("No data\n")

    elif option == "7":
        path = input("File path: ")
        save_csv(inventory, path)

    elif option == "8":
        path = input("File path: ")
        new_data = load_csv(path)

        if new_data:
            choice = input("Overwrite? (Y/N): ")

            if choice.lower() == "y":
                inventory = new_data
                print("Inventory replaced\n")
            else:
                for new_p in new_data:
                    existing = find_product(inventory, new_p["name"])

                    if existing:
                        existing["quantity"] += new_p["quantity"]
                        existing["price"] = new_p["price"]
                    else:
                        inventory.append(new_p)

                print("Inventory merged\n")

    elif option == "9":
        print("Exiting...")
        break

    else:
        print("Invalid option\n")