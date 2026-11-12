import random

list = []

for i in range(10):
	list.append(random.randint(1,50))

print(f"List: {list}")
value = int(input("Value to find: "))
print()

for i in range(len(list)):
	if list[i] == value:
		print(f"{value} is in the list.")
