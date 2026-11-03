import random

print("HERE COPMES THE DICE!")

while True:
	num1 = random.randint(1, 6)
	num2 = random.randint(1, 6)

	print()
	print(f"Roll #1: {num1}")
	print(f"Roll #2: {num2}")
	print(f"The total is {num1 + num2}")
	if num1 == num2:
		break

