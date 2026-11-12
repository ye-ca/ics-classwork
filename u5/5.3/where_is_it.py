import random

list = []

for i in range(10):
    list.append(random.randint(1,50))


print(f"List: {list}")

value = int(input("Value to find: "))
is_there = False

for i in range(len(list)):
    current_num = list[i]
    if current_num == value:
        is_there = True
        print(f"{value} is at index {i}. ")

if False == is_there:
    print(f"{value} is not in the list.")
