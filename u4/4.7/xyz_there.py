input = input("input: ")

answer = False 

for i in range(0, len(input)):
	if input[i] == "x" and input[i+1] == "y" and input[i+2] == "z" and not input[i-1] == ".":
		answer = True
	else:
		continue

print(answer)
            