import random
random.seed(401)  

x = random.randrange(10)  # 0-9
print(f"My random number is {x}.")

print()
print("Here are some random numbers from 1 to 5...")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5))

print()
print("Here are some random numbers from 1 to 100...")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101))

print()
print("Will these next two random number be the same?")
a = random.randrange(10)  # 0-9
b = random.randrange(10)

if a == b:
    print(f"Wow! Both numbers were {a}!")
else:
    print("The two random numbers were different. Not too surprising.")

# 1 If we change random.randrange(1, 6) to random.randrange(1, 5), the numbers will be from 1-4 instead of 1-5 since the upper bound is exclusive. 

# 2 adding random.seed(401) at the top of the file will make the random numbers generated the same each time the program is run.

# 3 changing the random seed makes the random numbers generated different.

# 4 Games use seeds to make random numbers predictable for testing and debugging purposes. It allows developers to reproduce the same sequence of random numbers, which is useful for identifying and fixing issues in the game logic. It can also be used to create consistent experiences for players, such as generating the same level layout or enemy behavior across different playthroughs. 