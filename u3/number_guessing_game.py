import random

random_number = random.randint(1, 10)
print("I'm thinking of a number from 1 to 10.")
guess = int(input("Your guess: "))

print()
if guess == random_number:
    print(f"That's right! My secret number was {random_number}!")
else:
    print(f"Sorry, but I was really thinking of {random_number}.")