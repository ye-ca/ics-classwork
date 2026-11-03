import random

print("I have chosen a number between 1 and 10. Try to guess it.")

number = random.randint(1, 10)
tries = 0

while True:
	tries += 1
	guess = int(input("Your Guess: "))
	if guess == number:
		print("That's right! You're a good guesser.")
		break
	else:
		print("That is incorrect. Guess again")

print(f"It only took you {tries} tries.")
