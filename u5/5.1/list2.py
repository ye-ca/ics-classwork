import random

list = []

for i in range(10):
	list.append(random.randint(1,100))

for i in range(10):
	print(f"Slot {i} contains a {list[i]}")
