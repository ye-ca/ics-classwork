import random
die1 = -68
die2 = -69

print("HERE COMES THE DICE!")


while die1 != die2:
	die1 = random.randint(1, 6)
	die2 = random.randint(1, 6)
	
	print(f"Roll #1: {die1}")
	print(f"Roll #2: {die2}")
	print(f"The total is {die1+die2}")

