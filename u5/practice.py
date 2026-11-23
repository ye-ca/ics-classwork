# List:
# mutable collection of elements, denoted by square brackets

# Element:
# Individual item stored in a list(numbers, string, or other objects)

# Append:
# Add to the end of a list

# Index: 
# The position of an element within a list, represented with a number. 

# Slice:
# A portion of the list with slide notiation list[slice1:slice2]

# 1.
print("\n 1:")

list = []

for i in range(11):
    if i % 2 == 0:
        list.append(i)

print(list)

# 2.
print("\n 2:")

friends = ["John", "Jane", "Richard", "Maidenless", "Aiden"]
print(friends[1])

# 3.
print("\n 3:")

numbers = [2, 5, 6, 12, 85, 39, 9375, 8475, 1923]
print(numbers[-1])
print(numbers[len(numbers)-1])

# 4.
print("\n 4:")

numbers = [76, 55, 34, 24]

print(numbers[1:3])

#5.
print("\n 5:")

words = ["word", "there", "is", "a", "aiden"]

print(words[-3:])



