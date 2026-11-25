import random
import os
import time


def main():
    for i in range(100000):
        r = random.randrange(1, 6)

        if r == 1:
            first()
        if r == 2:
            second()
        if r == 3:
            third()
        if r == 4:
            fourth()
        if r == 5:
            fifth() 
        # Write five if statements here.
        # If r is 1, then call the function named 'first'.
        # If r is 2, then call the function named 'second', and so on.
        
        # Optional: after the if statements are over, add in a slight delay.
        time.sleep(0.1)
        os.system("clear")  # clear console

    print("I pledge allegiance to the flag.");


def first():
    print("I                               ");


def second():
    print("  pledge                        ");


def third():
    print("         allegiance             ");


def fourth():
    print("                    to the      ");


def fifth():
    print("                           flag.");


if __name__ == "__main__":
    main()
