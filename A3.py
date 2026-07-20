snack_name = "Candy"
price = 1.50
quantity = 10
is_available = True

print("Snack name: ",snack_name)
print("Price: ", price)
print("Quantity: ", quantity)
print("Is available: ", is_available)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))

total = price * quantity
print("Total value: $", total)
print("Sale price: $", price - 0.25)
print("Double stock:", quantity * 2)

print("Is price under $2?", price < 2)
print("More than 5 in stock?", quantity > 5)
print("Is price exactly $1.50?", price == 1.50)