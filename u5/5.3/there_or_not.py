import random

list = []

for i in range(10):
    list.append(random.randint(1,50))

print(f"List: {list}")
value = int(input("Value to find: "))
print()

is_in = " not"

for i in range(len(list)):
    if value == list[i]:
        is_in = ""

print(f"{value} is{is_in} in the list. ")
