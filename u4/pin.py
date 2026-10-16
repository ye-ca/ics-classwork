PIN = "12345"

print("WELCOME TO THE BANK OF GALLO.")
# entry = input("ENTER YOUR PIN: ")

while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")


print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")

# 1 A while loop is similar to an if statement in the way that it compares, and it runs if the statement inside the while or if is true (boolean)

# 2 A while loop is different to an if statement in the way that it loops until the boolean statement inside it is false. 

# 3, we would first need to convert the entry into an int using int()

# 4. It produces a namerror when running the while loop, because variable entry is not defined yet, but its trying to compare it to something. 

# 5 ok. 
