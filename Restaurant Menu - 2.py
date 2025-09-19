print("🍽️ Welcome to Taste Delight Restaurant 🍽️")

# Get customer name
name = input("Enter your name: ")

# Menu items with prices
menu = {
    1: ["Margherita Pizza", 400],
    2: ["Butter with Naan", 320],
    3: ["Veg Biryani", 200],
    4: ["Chocolate Brownie with Ice Cream", 150]
}

# Display the menu
print("\nToday's Menu:")
for key in menu:
    print(f"{key}. {menu[key][0]} - ₹{menu[key][1]}")

# Store order details
order = []
total = 0

while True:
    choice = int(input("\nEnter item number to order (0 to finish): "))

    if choice == 0:
        break
    elif choice in menu:
        qty = int(input(f"Enter quantity for {menu[choice][0]}: "))
        item_name = menu[choice][0]
        price = menu[choice][1]
        amount = price * qty
        order.append((item_name, qty, price, amount))
        total += amount
        print(f"Added {qty} x {item_name} - ₹{amount}")
    else:
        print("Invalid choice. Please choose from the menu.")

# Print the bill
print("\n🧾 Final Bill")
print(f"Customer Name: {name}")
print("-------------------------------")
print(f"{'Item':25} {'Qty':>3} {'Price':>6} {'Total':>7}")
print("-------------------------------")
for item in order:
    print(f"{item[0]:25} {item[1]:>3} ₹{item[2]:>5} ₹{item[3]:>6}")
print("-------------------------------")
print(f"{'Total Bill':>38}: ₹{total}")
print("Thank you for dining with us! 🍴")
