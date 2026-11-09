print("Type in a message, and I'll display it ten times.")

message = input("Message: ")

for n in range(2, 21, 2):
    print(f"{n}. {message}")

# 1. Nothing happens when you change the variable n to another one, becase it's arbitraty and can be anything. I suppose you chose it as n because it can be a short form for "number"

# 2. It defines the start and stop, but not including the stop number, so 0, 5, goes 0, 1, 2, 3, 4. 

# 3. the third number is step. 

# 4. if you only do it with one number, it will start at 0 and go up to that number, not including it.

# 5. when you use the range function with only two numbers, it will start at the first number and go up to the second number, not including it. incrementing by one

# 6. ok

# 7 ok