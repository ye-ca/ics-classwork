name = input("Hey, what's your name? (Sorry I keep forgetting): ")
age = int(input(f"Ok, {name}, how old are you?"))
print()

if age < 16:
	print(f"You can't drive, {name}.")
elif age < 18:
	print(f"You can drive, but you can't vote, {name}.")
elif age < 21:
	print(f"You can vote, drive, but can't rent a car, {name}.")
else:
	print(f"You can pretty much do anything, {name}.")
