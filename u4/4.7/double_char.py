final = ""

string = input("Enter a string: ")

for i in range(0, len(string), 1):
	final += string[i] * 2

print(final)

