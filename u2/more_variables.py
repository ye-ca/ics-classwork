store = "No Frills"
item = "Apples"
price = 0.47 
quantity = 8
subtotal = price * quantity
tax = subtotal * 0.13
total = tax + subtotal

# f-string
print(f"At {store} I bought some {item}.")
# concatenation
print("They sold for $" + str(price) + " each.")
# dot format
print("I wanted to purchase {} of them.".format(quantity))
# f-string
print(f"The total before tax was ${subtotal} and tax was {round(tax, 2)}")
# the f to indicate it is an f-string is missing
# f-string
print(f"The total price, with tax included, was ${round(total, 2)}.")
