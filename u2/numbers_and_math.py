print("I have a class of 33 students.")
print("There are 11 girls, so that means..")
# This calculates the expression of 33 - 11 which is the amount of boys(22), this works because it splits the sentence, and places an expression formatted in string in the middle so it works
print(f"there are {33 - 11} boys.")
print()
# This f-string expression prints the quotient of 11 / 33, which is .3 repeating , this works because it processes python code directly in the curly bracket
print(f"That means {round((11 / 33) * 100, 2)} % are girls...")
# this dot format expression prints the result of (33 - 11) / 33, which is .6 repeating, it works because the .format injects the values of the expression here into the curly brackets
print(f"and {round((33 - 11) / 33 * 100, 2)} % are boys.")
print()
print("If we made groups of six...")
# this f-string expression prints the floor division of 33/6, which is 5, because it truncates the decimal(s). 
print(f"There would be {33 // 6} groups of six.")
# this f-string expression prints the mod/remainder of 33/6, which is 3, because it takes the remaining after 33/6 
print(f"And then a smaller group of {33 % 6} people.")
# this prints the character "-" multiplied by 30
print(f"-" * 30)
print("If we had 17 apples and 3 people...")
# this f-string expression prints the floor division of 17 // 3,  which is 5
print(f"Each person would get {17 // 3} whole apples.")
# this calculates the expression of 17 mod/remainder 3, which is 2, this works because it splits the string and completes it still with the str() function
print(f"There would be {17 % 3} apples remaining.")
print()
print("If we charged each person $2 each for their 5 apples..")
# this dot format expression inserts the calculate of 2 * 5 in the curly brackets, which is 10 
print(f"they would each pay ${2 * 5}.")

