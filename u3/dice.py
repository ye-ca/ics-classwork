import random

print("HERE COMES THE DICE!")
print()

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print(f"Roll #1: {dice1}")
print(f"Roll #2: {dice2}")
print(f"The total is {dice1 + dice2}!")