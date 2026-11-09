vowels = "aAeEiIoOuU"

message = input("What is your message? ")

print()
print(f"Your message is {len(message)} characters long.")
print(f"The first character is at position 0 and is '{message[0]}'.")
lastpos = len(message) - 1
print(f"The last character is at position {lastpos} and is '{message[lastpos]}'.")
print()
print("Here are all the characters, one at a time:\n")

for i in range(len(message)):
    print(f"\t{i} - '{message[i]}'")

vowel_count = 0
for i in range(len(message)):
    if message[i] in vowels: # this works because it checks if message index of i is inside vowels
        vowel_count += 1

print(f"\nYour message contains {vowel_count} vowels.")
