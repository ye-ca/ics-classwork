number = int(input("Number: "))
string = ""
total = 0


for i in range(1, number + 1):
    string += str(i) + " "
    total += i 

print(string)
print(f"The sum is {total}.")