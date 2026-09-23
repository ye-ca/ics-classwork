print("Enter the following information about an item you wish to purchase..\n")
print()


name = input("The name of the item: ")
price = float(input("The price: $"))
quantity = int(input("How many do you want? "))

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to ${total}")

# 1. The difference between input for price and input for name is that the price input is converted to a float, while the name input is stored as a string. The quantity input is converted to an integer. This is important because price and quantity are numerical values that will be used in calculations, while name is a text(string) datatype that does not require conversion to use.
# 3. A prompt is a text message shown to the user that tells the user what to type, changing the order of the below causes a usability issue because if the input() function comes before the print() function, the use will not know what to type in and will be confused. The prompt should always come before the input() function so that the user knows what to type in:
# name = input()
# print("Enter the name of the item:")
# 4 int() and float() functions are used to convert the input from a string to a numerical value. The int() function turns the input to an integer, while the float() function turns the input to a float datatype. This is important because it allows for calculations to be done on the input values, such as calculating the subtotal, tax, and total cost of the items being purchased.

