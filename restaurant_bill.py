# Define the menu of the restaurant
menu = {
    "pizza": 150,
    "pasta": 70,
    "burger": 90,
    "salad": 60,
    "coffee": 80,
}

# Greet the customer
print("Welcome to Vikas Restaurant!\n")

# Display menu dynamically
print("Menu:")
for item, price in menu.items():
    print(f"{item.capitalize()}: Rs{price}")

# Initialize order total
order_total = 0

# First item order
item_1 = input("\nEnter the name of the item you want to order: ").strip().lower()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1.capitalize()}' has been added to your order.")
else:
    print(f"Sorry, the item '{item_1}' is not available in the restaurant.")

# Ask if the user wants to order another item
another_order = input("\nDo you want to add another item? (Yes/No): ").strip().lower()

if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").strip().lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2.capitalize()}' has been added to your order.")
    else:
        print(f"Sorry, the item '{item_2}' is not available!")
elif another_order == "no":
    print("\nThank you for coming! We hope to see you again.")

# Display total amount
print(f"\nThe total amount to pay is: Rs{order_total}")
