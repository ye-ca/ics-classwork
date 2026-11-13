numbers_string = input("Enter numbers seperated by comma, then a space: ")

numbers_list = [int(n) for n in numbers_string.split(", ")]

for i in range(len(numbers_list)):
    print(f"{i}: {numbers_list[i]}")

