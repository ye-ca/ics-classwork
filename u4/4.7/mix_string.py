a = input("a: ")
b = input("b: ")

if len(a) > len(b):
    max_len = len(a)
else:
    max_len = len(b)

final = ""

for i in range(max_len):
    if i < len(a):
        final += a[i]

    if i < len(b):
        final += b[i]

print(final)