word_number_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

input_string = input("Enter numbers in word for seperated by jsut comma: ")

input_list = input_string.split(",")

output_list = []

for i in range(len(input_list)):
    number = word_number_list.index(input_list[i]) # find the index of where the i of input_list is, then  set it to that, because the index of the word number list is equal to the number it represents. 
    output_list.append(number) # append it. 

print(output_list)
