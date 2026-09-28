# Ask the user for their name, include their name in a greeting string and output it. 
name = input("What is your name? ")
print(f"Hello, {name}!")
print()

# Ask the user for the cost of an item, add tax and display the total to the user in a string like Your total is $15.67.
cost = float(input("What is the cost of the item? "))
tax_rate = 0.13  # Assuming a tax rate of 13%
total_cost = cost + (cost * tax_rate)
print(f"Your total is ${total_cost:.2f}.")
print()

# Ask the user for their name. Output a message telling them what letter their name starts with and ends with. If their name is Jeff, then you would say it starts with "J" and ends with "f".
name = input("What is your name? ")
print(f"Your name starts with '{name[0]}' and ends with '{name[-1]}'.")
print()

# Ask the user for a word and output the word excluding the first and last letter. Use a "slice" for this. You can use the builtin function len() to give you the length of the word, or use -1 in the slice.
word = input("Please enter a word: ")
# Using slicing to exclude the first and last letter
sliced_word = str(word[1:-1])
print(f"The word excluding the first and last letter is: {sliced_word}")
print()
