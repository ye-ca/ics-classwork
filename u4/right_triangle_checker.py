print("Enter three integers:")
a = int(input("Side 1: "))

while True:
	b = int(input("Side 2: "))
	if a > b:
		print(f"{b} is smaller than {a}. Try again.")
		continue
	else:
		break

while True:
	c = int(input("Side 3: "))
	if b > c:
		print(f"{c} is smaller than {b}. Try again.")
		continue
	else:
		break

print()
print(f"Your three sides are {a} {b} {c}")

if a ** 2 + b ** 2 == c ** 2:
	print("These sides *do* make a right triangle.  Yippy-skippy!")
else:
	print("NO!  These sides do not make a right triangle!")
