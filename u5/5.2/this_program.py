import random

a = []
b = []

for i in range(10):
	a.append(random.randint(1,100))

for n in a:
	b.append(n)

a[-1] = -7

print(a)
print(b)


# this does not work because when you set lista = listb, it only creates a symbolic link aka a refrence to the link, not actually copying it over to two difference places in memory. This means that when you change a, b changes too. 
