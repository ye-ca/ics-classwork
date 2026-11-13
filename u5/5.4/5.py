input_string = input("Enter x locations seperated by: and ,: ")

input_list = input_string.split(",")

output_list = []

for i in range(len(input_list)):
    value_str = input_list[i].split(":")
    value = int(value_str[1])
    output_list.append(value)

print(output_list)
