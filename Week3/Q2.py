print("=" * 50)
print("Question 2: Shopping List")
print("=" * 50)

cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

print("Number of apples: ", cart.count("apple"))
print("Position of milk: ", cart.index("milk"))

cart.remove("apple")
print("Removed item using pop: ", cart.pop())

if "banana" in cart:
    print("Is banana in cart?", True)

print("Final cart: ", cart)
