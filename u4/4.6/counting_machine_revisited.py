min = int(input("Count from: "))
max = int(input("Count to: "))
step = int(input("Count by: "))

total = ""

for i in range(min, max + 1, step):
    total =  total + str(i) + " "

print(total) 