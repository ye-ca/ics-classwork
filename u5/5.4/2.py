numbers_string = input("Enter numbers seperated by comma, then a space: ")

string_list = numbers_string.split(", ")

numbers_list = []

for s in string_list:
    numbers_list.append(int(s))

for i in range(len(numbers_list)):
    print(f"{i}: {numbers_list[i]}")

