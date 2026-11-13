r_list = ["L", "T", "W"]

given = input("Enter string of win losssssssssssss: ")

given_list = given.split()

output_list = []

for i in range(len(given_list)):
    number = r_list.index(given_list[i])
    output_list.append(number)

print(output_list)
