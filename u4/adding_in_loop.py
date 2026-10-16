print("I will add up the numbers you give me.")

number = -1
total = 0 

while number != 0:
	number = int(input("Number: "))
	
	total += number

	print(f"The total so far is {total}")

print()
print(f"The total is {total}.")
