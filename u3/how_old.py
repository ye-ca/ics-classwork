name = input("Why hello there, What's your name? \n")
age = int(input(f"Hi {name}, how old are you? \n"))

print()
if age < 16:
	print(f"You can't drive, {name}.")
if age < 18:
	print(f"You can't vote, {name}.") 
if age < 21:  
	print(f"You can't rent a car, {name}.")
else:
	print(f"You can do anything that's legal, {name}.")
