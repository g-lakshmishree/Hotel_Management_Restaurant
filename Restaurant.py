def add_new_menu_item():
    try:
        item_name = input("Enter the name of the menu item: ")
        item_price = input("Enter the price of the menu item: ")
        item_category = input("Enter the category of the menu item: ")
        
        with open('menu.txt', 'a') as menu_file:
            menu_file.write(f"{item_name},{item_price},{item_category}\n")
        
        print("Menu item added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def update_menu_item():
    item_name = input("Enter the name of the menu item to update: ")
    updated = False
    menu_items = []

    with open("menu.txt", "r") as menu_file:
        menu_items = menu_file.readlines()

    for i, item in enumerate(menu_items):
        if item.startswith(item_name):
            new_price = input("Enter the new price: ")
            new_category = input("Enter the new category: ")
            menu_items[i] = f"{item_name},{new_price},{new_category}\n"
            updated = True
            break

    if updated:
        with open("menu.txt", "w") as menu_file:
            menu_file.writelines(menu_items)
        print("Menu item updated successfully.")
    else:
        print("Item not found.")

def view_menu():
    print("Current Menu:")
    try:
        with open("menu.txt", "r") as menu_file:
            for line in menu_file:
                print(line.strip())
    except FileNotFoundError:
        print("Menu file not found. Please add menu items first.")

def record_food_order():
    room_number = input("Enter the room number: ")
    order_items = input("Enter the items ordered (format: item_name:item_price, separated by commas): ")
    
    with open("orders.txt", "a") as orders_file:
        orders_file.write(f"{room_number},{order_items}\n")
    
    print("Order recorded successfully.")

def generate_sales_report():
    total_sales = 0
    item_count = {}
    
    try:
        with open("orders.txt", "r") as orders_file:
            for line in orders_file:
                # Split the line into room number and items
                room_number, items = line.strip().split(",", 1)
                for item in items.split(","):
                    try:
                        # Split each item into name and price
                        item_name, item_price = item.split(":")
                        total_sales += float(item_price)
                        item_count[item_name] = item_count.get(item_name, 0) + 1
                    except ValueError:                        
                        continue  # Skip this item and continue with the next

        print(f"Total Sales: RM{total_sales:.2f}")
        print("Most Popular Dishes:")
        for item, count in item_count.items():
            print(f"{item}: {count} orders")
    except FileNotFoundError:
        print("Orders file not found. Please record some orders first.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def restaurant_manager_menu():
    while True:
        print("\n--- Restaurant Manager Menu ---")
        print("1. Add New Menu Item")
        print("2. Update Menu Item")
        print("3. View Menu")
        print("4. Record Food Order")
        print("5. Generate Sales Report")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == '1':
            add_new_menu_item()
        elif choice == '2':
            update_menu_item()
        elif choice == '3':
            view_menu()
        elif choice == '4':
            record_food_order()
        elif choice == '5':
            generate_sales_report()
        elif choice == '6':
            print("Exiting the Restaurant Manager Menu.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Call the restaurant manager menu to start the program
if __name__ == "__main__":
    restaurant_manager_menu()