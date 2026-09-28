# Be able to trace a program using a variable table
x = 5       # x = 5
x = x + 3   # x = 8
y = x * 2   # x = 8, y = 16
x = y - 4   # x = 12, y = 16
print(x, y)
print()

# Know your data types 
x = 5        # x is an integer
y = 3.2      # y is a float
z = "Hello"  # z is a string
t = True     # t is a boolean

print("x is of type:", type(x))
print("y is of type:", type(y))
print("z is of type:", type(z))
print("t is of type:", type(t))
print()

# Order of operations
print("Order of operations examples:")
print(2 + 3 * 4)
print((2 + 3) * 4)
print()

# Operators 
print("Operator examples:")
print(10 + 5)   # Addition
print(10 - 5)   # Subtraction
print(10 * 5)   # Multiplication
print(10 / 5)   # Division
print(10 // 3)  # Floor Division
print(10 % 3)   # Modulus
print(10 ** 2)  # Exponentiation
print()

# Assignment operators
x = 10
x += 5  # x = x + 5
print("x after += 5:", x)
x -= 3  # x = x - 3
print("x after -= 3:", x)
x *= 2  # x = x * 2
print("x after *= 2:", x)
x /= 4  # x = x / 4
print("x after /= 4:", x)
x //= 3  # x = x // 3
print("x after //= 3:", x)
x %= 2  # x = x % 2
print("x after %= 2:", x)
x **= 3  # x = x ** 3
print("x after **= 3:", x)
print()

# Input and Output 
# print and input
name = input("What is your name? ")
print(f"Hello, {name}!")
print()

# Input is a string

age = input("How old are you? ")
print("in 5 years you will be ", int(age) + 5, "years old.")
print(f"2.5 years ago you were {float(age) - 2.5} years old.") # note, you don't have to convert to float, but it is good practice to do so when doing math with floats
print()

# Strings
# How to slice a string
text = "Hello, World!"
print(text[0:5])  # Output: "Hello"
print(text[7:12])  # Output: "World"
print(text[:5])  # Output: "Hello"
print(text[7:])  # Output: "World!"
print(text[-6:-1])  # Output: "World"
print(text[-6:])  # Output: "World!"
print()

# How to get a single character
print(text[0])  # Output: "H"
print(text[7])  # Output: "W"
print(text[-1])  # Output: "!"
print(text[-2])  # Output: "d"
print()

