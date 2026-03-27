# create shopping cart using loop and remove 1 item from total
# shopping_cart.py

cart = []
total = 0

# Add items to cart using loop
for i in range(3):  # you can change 3 to any number of items
    item = input("Enter item name: ")
    price = float(input(f"Enter price of {item}: "))
    cart.append((item, price))
    total += price

print("\nShopping Cart Items:")
for item, price in cart:
    print(f"{item} - Rs.{price}")

print("Total =", total)

# Remove one item
remove_item = input("\nEnter the name of the item to remove: ")

for item, price in cart:
    if item == remove_item:
        total -= price
        cart.remove((item, price))
        break

print("\nUpdated Cart Items:")
for item, price in cart:
    print(f"{item} - Rs.{price}")

print("Updated Total =", total)