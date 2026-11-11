input1 = input("String 1: ")
input2 = input("String 2: ")

string1 = str.lower(input1)
string2 = str.lower(input2)

len1 = len(input1)
len2 = len(input2)

if string1 == string2[-len1:] or string2 == string1[-len2:]:
    print(True)
else:
    print(False)