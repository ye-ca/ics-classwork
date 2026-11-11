import random

list = []

for i in range(1000):
	list.append(random.randint(10, 99))

output = ""

for i in range(1000):
	output += str(list[i]) + "  "

print(output)
