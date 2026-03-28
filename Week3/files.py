import csv


def save_csv(inventory, path):
    """Save inventory to CSV"""

    if not inventory:
        print("Nothing to save (empty inventory)\n")
        return

    try:
        with open(path, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["name", "price", "quantity"])

            for p in inventory:
                writer.writerow([p["name"], p["price"], p["quantity"]])

        print(f"✔ Saved at: {path}\n")

    except PermissionError:
        print("Permission denied\n")
    except Exception as e:
        print("Error saving file:", e, "\n")


def load_csv(path):
    """Load inventory from CSV"""

    inventory = []
    errors = 0

    try:
        with open(path, "r") as file:
            reader = csv.reader(file)

            header = next(reader)

            if header != ["name", "price", "quantity"]:
                print("Invalid CSV format\n")
                return []

            for row in reader:

                if len(row) != 3:
                    errors += 1
                    continue

                try:
                    name = row[0]
                    price = float(row[1])
                    quantity = int(row[2])

                    if price < 0 or quantity < 0:
                        errors += 1
                        continue

                    inventory.append({
                        "name": name,
                        "price": price,
                        "quantity": quantity
                    })

                except:
                    errors += 1

        print(f"✔ Loaded: {len(inventory)} products")
        print(f"⚠ Skipped rows: {errors}\n")

        return inventory

    except FileNotFoundError:
        print("File not found\n")
        return []

    except Exception as e:
        print("Error loading file:", e, "\n")
        return []