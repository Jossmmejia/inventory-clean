# Simple inventory program
# This program allows registering a product with its name, price, and quantity
# Then it calculates the total cost of the product in the inventory

# Ask the user for the product name
name = input("Enter the product name: ")

# Validate that the entered price is a valid number
while True:
    try:
        price = float(input("Enter the product price: "))
        if price < 0:
            print("The price cannot be negative.")
        else:
            break
    except:
        print("Error: You must enter a valid number.")

# Validate that the quantity is a valid integer
while True:
    try:
        quantity = int(input("Enter the product quantity: "))
        if quantity < 0:
            print("The quantity cannot be negative.")
        else:
            break
    except:
        print("Error: You must enter a valid integer.")

# Calculate the total cost of the inventory
total_cost = price * quantity

# Display the results in the console
print("\n--- Product Information ---")
print(f"Product: {name} | Price: {price} | Quantity: {quantity} | Total: {total_cost}")

# End of the program
# This program asks for product data, validates numeric values,
# and calculates the total cost by multiplying price by quantity