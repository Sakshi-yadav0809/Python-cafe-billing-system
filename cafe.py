
Menu = {
    'Espresso': 40,
    'Cappuccino': 80,
    'Latte': 100,
    'Pizza': 120,
    'Pasta': 150,
    'Salad': 60,
    'Sandwich': 70,
    'Noodles': 90,
    'Pancakes': 100
}

# Greet
print("Welcome to our Cafe!")
print("Espresso - Rs.40\nCappuccino - Rs.80\nLatte - Rs.100\nPizza - Rs.120\nPasta - Rs.150\nSalad - Rs.60\nSandwich - Rs.70\nNoodles - Rs.90\nPancakes - Rs.100")

order_total = 0

# First Item
item_1 = input("Enter the name of the item you want to order: ")

if item_1 in Menu:
    order_total += Menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Sorry, {item_1} is not available in our menu.")

# Second Item
another_order = input("Do you want to order another item? (yes/no): ")

if another_order.lower() == "yes":
    item_2 = input("Enter the name of the second item: ")

    if item_2 in Menu:
        order_total += Menu[item_2]
        print(f"Your item {item_2} has been added to your order.")
    else:
        print(f"Sorry, {item_2} is not available in our menu.")

print(f"\nYour total amount to pay is Rs.{order_total}")