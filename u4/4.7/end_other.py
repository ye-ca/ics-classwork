input1 = input("String 1: ")
input2 = input("String 2: ")

string1 = str.lower(input1)
string2 = str.lower(input2)

if string1 in string2 or string2 in string1:
	print(True)
else:
	print(False) 
