import random

chosen = random.randint(1, 10)
guesses = 0

print("I have chosen a number between 1 and 10. Try to guess it.")

guess = int(input("Your guess: "))
guesses += 1

while guess != chosen:
    print("That is incorrect. Guess again.")
    guess = int(input("Your guess: "))
    guesses += 1

print("That's right! You're a good guesser.")
print(f"It only took you {guesses} tries.")
