import math

print("SQUARE ROOT!")

number = float(input("Enter a number: "))

while True:
	if number < 0:
		print("You can't take the square root of a negative number, silly.")
		number = float(input("Try again: "))
		continue
	else:
		break

print(f"The square root of {number} is {math.sqrt(number)}.")
