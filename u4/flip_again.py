import random


# again = "y"

while True:
    flip = random.randrange(2)  # 0-1

    if flip == 1:
        coin = "HEADS"
    else:
        coin = "TAILS"

    print("You flip a coin and it is... " + coin)

    again = input("Would you like to flip again (y/n)? ")
    if again != "y":
       break

# 3. Now that we have changed the program to be post-testing instead of testing before, the program will still work because we define again before we try to check it. 
