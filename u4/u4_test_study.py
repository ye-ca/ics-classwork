# 1 
for i in range(55, 101, 2):
	print(i)

n = 55
while n <= 100:
	print(n)
	n += 2


# 2 
total = 0.0
iteration = 0 

# for i in range(0, 10):
# 	user_number = float(input("enter a number: "))
# 	total += user_number
# 	iteration += 1

# print(f"Your average is {total / iteration}, you did {iteration} averages")


# 3. 
print("Welcome the the Genetic Editing System (GES)")
print("Please use irresponsibly.\n")

sequence = input("Enter genetic sequence (letters a-g only): ")
print("Editing sequence...")

modified = ""
modifications = 0

for i in range(0, len(sequence)):
	if sequence[i] == "c":
		modified += "f"
		modifications += 1
	elif sequence[i] == "b":
		modified += "ag"
		modifications += 1
	else:
		modified += sequence[i]

print("... done!\n")

print(f"The edited sequence is: {modified}")
print(f"there were {modifications} modifications")


