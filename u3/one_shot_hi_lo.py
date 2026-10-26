import random
random_number = random.randint(1, 100)

print("I'm thinking of a number between 1-100.  Try to guess it.")
guess = int(input(">  "))

if guess == random_number:
    print("You guessed it! what are the odds?!?")
elif guess < random_number:
    print("Sorry, you are too low.  I was thinking of", random_number)
elif guess > random_number:
    print("Sorry, you are too high.  I was thinking of", random_number)
