string = input("input: ")
n = int(input("n: "))

final = ""

for i in range(n):
    final += string[-n:]

print(final)