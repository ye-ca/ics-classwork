import random

name = input("Name (first last): ")
filename = input("Filename: ")


grades = []

for i in range(5):
    grades.append(random.randint(1,100))

print("Here are your randomly-selected grades (hope you pass): ")
for i in range(len(grades)):
    print(f"Grade {i+1}: {grades[i]}")


data = ""
for n in grades:
    data += str(n)
    data += " "

with open(filename, "w", encoding = "utf-8") as file:
    file.write(name)
    file.write(data)

print()
print(f'Data saved in "{filename}".')
