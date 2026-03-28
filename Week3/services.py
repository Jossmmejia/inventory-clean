# =========================
# INVENTORY SERVICES
# =========================

def add_product(inventory, name, price, quantity):
    """Add a product to inventory"""
    inventory.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })


def show_inventory(inventory):
    """Display inventory"""
    if not inventory:
        print("Inventory is empty\n")
        return

    print("\n" + "-" * 40)
    print("INVENTORY")
    print("-" * 40)

    for p in inventory:
        print(f"{p['name']} | Price: {p['price']} | Qty: {p['quantity']}")

    print("-" * 40 + "\n")


def find_product(inventory, name):
    """Find product by name"""
    for p in inventory:
        if p["name"].lower() == name.lower():
            return p
    return None


def update_product(inventory, name, new_price=None, new_quantity=None):
    """Update product data"""
    product = find_product(inventory, name)

    if not product:
        print("Product not found\n")
        return

    if new_price is not None:
        product["price"] = new_price

    if new_quantity is not None:
        product["quantity"] = new_quantity

    print("✔ Product updated\n")


def delete_product(inventory, name):
    """Delete product"""
    product = find_product(inventory, name)

    if product:
        inventory.remove(product)
        print("✔ Product deleted\n")
    else:
        print("Product not found\n")


def calculate_statistics(inventory):
    """Calculate inventory stats"""

    if not inventory:
        return None

    total_units = 0
    total_value = 0

    most_expensive = inventory[0]
    highest_stock = inventory[0]

    for p in inventory:
        total_units += p["quantity"]
        total_value += p["price"] * p["quantity"]

        if p["price"] > most_expensive["price"]:
            most_expensive = p

        if p["quantity"] > highest_stock["quantity"]:
            highest_stock = p

    return {
        "total_units": total_units,
        "total_value": total_value,
        "most_expensive": most_expensive,
        "highest_stock": highest_stock
    }