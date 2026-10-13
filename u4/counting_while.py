print("Type in a message, and I'll display it five times.")

message = input("Message: ")
print()

repeat = int(input("How many times? "))

n = 0
while n < repeat:
    print(f"{n * 10 + 10}. {message}")
    n += 1
