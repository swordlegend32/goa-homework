shopping_cart = []

while True:
    item = input("Add item to the shopping cart: ")
    shopping_cart.append(item)
    Input = input()
    if Input == "Exit":
        break

print(shopping_cart)