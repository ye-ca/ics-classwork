import random

number = random.randint(1,100)
print(number)
guess_index = 0
guess = ""

print("I'm thinking of a number between 1-100. You have 7 guesses.")

while guess != number and guess_index < 7:
	guess_index  += 1	

	if guess_index == 1:
		guess = int(input("First Guess: "))
	else: 
		guess = int(input(f"Guess # {guess_index}: "))
	if guess < number:
		print("Sorry, you are too low")
	elif guess > number:
		print("Sorry, you are too high")
	else:
		print("You guessed it! What are the odds?")
