gender = input("What is your gender? (M or F): ")
first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))

married = False
if gender == "F" and age >= 20:
    married = input("Are you married? (Y or N): ").upper() == "Y"

if gender == "M":
    if age >= 20:
        print(f"Then I shall call you Mr. {last_name}.")
    else:
        print(f"Then I shall call you {first_name} {last_name}.")

elif gender == "F":
    if age >= 20:
        if married:
            print(f"Then I shall call you Mrs. {last_name}.")
        else:
            print(f"Then I shall call you Ms. {last_name}.")
    else:
        print(f"Then I shall call you {first_name} {last_name}.")