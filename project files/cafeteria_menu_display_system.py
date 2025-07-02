
# Cafeteria Menu Display System

# Menu storage
menu = {
    "Breakfast": [],
    "Lunch": [],
    "Beverages": [],
    "Specials": []
}

def display_menu():
    print("\n------ Cafeteria Menu ------")
    for category, items in menu.items():
        print(f"\n{category}:")
        if items:
            for item in items:
                print(f"- {item['name']} : ₹{item['price']} (Available: {item['available']})")
        else:
            print("No items available.")
    print("-----------------------------\n")

def add_item():
    category = input("Enter category (Breakfast/Lunch/Beverages/Specials): ")
    if category in menu:
        name = input("Enter item name: ")
        price = input("Enter item price: ")
        available = input("Is the item available? (Yes/No): ")
        menu[category].append({"name": name, "price": price, "available": available})
        print("Item added successfully!")
    else:
        print("Invalid category.")

def update_item():
    category = input("Enter category to update item in: ")
    if category in menu:
        name = input("Enter item name to update: ")
        for item in menu[category]:
            if item['name'] == name:
                item['price'] = input("Enter new price: ")
                item['available'] = input("Is the item available? (Yes/No): ")
                print("Item updated successfully!")
                return
        print("Item not found.")
    else:
        print("Invalid category.")

def delete_item():
    category = input("Enter category to delete item from: ")
    if category in menu:
        name = input("Enter item name to delete: ")
        for item in menu[category]:
            if item['name'] == name:
                menu[category].remove(item)
                print("Item deleted successfully!")
                return
        print("Item not found.")
    else:
        print("Invalid category.")

def main():
    while True:
        print("1. Display Menu")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_menu()
        elif choice == '2':
            add_item()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
