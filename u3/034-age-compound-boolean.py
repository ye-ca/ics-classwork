name = input("Your name:")
age = int(input("Your age:"))

if age < 16:
	print(f"You can't drive, {name}")
if age >= 16 and age <= 17:
	print(f"You can drive but not vote, {name}")
if age >= 18 and age <= 24:
	print(f"")
