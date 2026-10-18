guess = ""

print("TWO QUESTIONS!")
print("Think of an object, and I'll try to guess it.")
print()

print("Question 1) Is it animal, vegetable, or mineral?")
q1 = input("> ").lower().strip()

print("Question 2) Is it bigger than a breadbox?")
q2 = input("> ").lower().strip()

if q2 == "yes":
	if q1 == "animal":
		guess = "Moose"
	elif q1 == "vegetable":
        	guess = "watermelon"
	elif q1 == "mineral":
      		guess = "Camaro"
	else:
		guess = "something that I can't guess because YOU didn't answer the questions properly."
elif q2 == "no":
	if q1 == "animal":
        	guess = "squirrel"
	elif q1 == "vegetable":
        	guess = "carrot"
	elif q1 == "mineral":
        	guess = "paper clip"
	else:
		guess = "something that I can't guess because YOU didn't answer the questions properly."
else:
	guess = "something that I can't guess because YOU didn't answer the questions properly."

print(f"My guess is that you are thinking of a {guess}")
