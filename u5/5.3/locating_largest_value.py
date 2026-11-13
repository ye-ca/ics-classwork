import random

list = []

for i in range(10):
    list.append(random.randint(1,100))

print(f"Array: {list}")

largest_value = 0
largest_index = 0

for i in range(len(list)):
    if list[i] > largest_value:
        largest_value = list[i]
        largest_index = i

print(f"The largest value is {largest_value}")
print(f"It is at index {largest_index}")
