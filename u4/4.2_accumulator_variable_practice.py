# 1
i = 1 
total = 0

while i <= 10:
	total += i 
	i +=1

print(total)

# 2
i = 100
total = 0

while i <= 200:
        total += i 
        i +=1

print(total)

# 3
i = 100 
total1 = 0

while i <= 200:
        total1 += i 
        i +=1

i = 200
total2 = 0 

while i <= 300:
	total2 += i 
	i += 1

print(total2-total1)

# 4
i = 1000
total = 0
 
while i <= 10000:
	total += i
	i += 5

print(total)

# 5

i = 1
total = 0

while i <= 100:
	if i % 3 != 0 and i % 5 == 0:
		total += i
	i += 1

print(total)
