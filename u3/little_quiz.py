correctQ = 0

input("Are you ready for a quiz? ")
print("Okay, here it comes!")
print()

q = input("""Q1) What is the capital of Alaska?
          1) Melbourne
          2) Anchorage
          3) Juneau

> """)

print()
if q == "3":
	print("That's right!")
	correctQ += 1
elif q == "1" or q == "2":
	print("Sorry, the capital of Alaska is Juneau")
else: 
	print("Error, please enter one of the NUMBER options")
print()

q = input("""Q2) In Python, the way you get keyboard input is the keyobard_input function.
          1) true
          2) false

> """)

print()
if q == "2":
        print("That's right!")
        correctQ += 1
elif q == "1":
        print('Sorry, in Python, you would use the "input" function to get keyboard input.')
else:
	print("Error, please enter one of the NUMBER options")
print()

q = input("""Q3) What is the result of 9 + 6 / 3?
          1) 5
          2) 11
          3) 15/3

> """)

print()
if q == "2":
        print("That's correct!")
        correctQ += 1
elif q == "1" or q == "3":
        print("Sorry, it's 11.")
else:
        print("Error, please enter one of the NUMBER options")
print()
print()

print(f"Overall, you got {correctQ} out of 3 correct.")
print("Thanks for playing!")
