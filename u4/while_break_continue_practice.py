# 1
x = -1

while x < 10:
	x += 1
	if x == 7:
		continue
	print(x)

# 2
i = 4
total = 0
while i < 20:
	i += 1
	if i % 3 == 0:
		continue
	else:
		total += i
	print(total)

# 3:
starting = int(input("Starting number: "))
ending = int(input("Ending number: "))

total = 0

while (starting - 1) < ending:
	i += 1
	if i == 13 or i == 31:
		break
	total += i
print(total)

while True:
	word = input("What is your word?\n> ")
	if word.lower().strip() == "stop":
		print("Goodbye!")
		break
	print(f"Your word: {word}")
