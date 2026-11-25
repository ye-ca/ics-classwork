user_input = input("enter numbers seperated by a space: ")

string_list = user_input.split()

numbers = []

for s in string_list:
    numbers.append(int(s))

print(numbers)


found = []

for n in numbers:
    if n < 0:
        found.append(n)


print(found)
