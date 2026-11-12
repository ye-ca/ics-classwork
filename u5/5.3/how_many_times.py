import random

list = []

for i in range(10):
	list.append(random.randint(1,50))

print(f"List: {list}")
value = int(input("Value to find: "))

times_found = 0

for i in range(len(list)):
    if list[i] == value:
        times_found += 1

print(f"{value} was found {times_found} times. ")
