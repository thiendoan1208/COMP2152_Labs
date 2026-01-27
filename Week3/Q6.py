print("=" * 50)
print("Question 6: Inventory Management System")
print("=" * 50)

inventory = {
"Laptop": (999.99, 5),
"Mouse": (29.99, 15),
"Keyboard": (79.99, 10),
"Monitor": (299.99, 8)
}

electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}

priceList = []

print("=== Current Inventory ===")
for key, value in inventory.items():
    print(f"{key} - Price: ${value[0]}, Quantity: {value[1]}")

print("                ")
print("All product category: ", electronics | accessories)
print("                ")

for key, value in inventory.items():
    priceList.append(value[0])

print("                ")
print("Price list: ", priceList)

priceList.sort()
print("Sorted list: ", priceList)
print("Lowest price: ", priceList[0])
print("Highest price: ", priceList[-1])

inventory.update({"Headphones": (49.99, 20)})
inventory.update({"Mouse": (29.99, 12)})
del inventory["Monitor"]

print("=== Final Inventory ===")
for key, value in inventory.items():
    print(f"{key} - Price: ${value[0]}, Quantity: {value[1]}")
