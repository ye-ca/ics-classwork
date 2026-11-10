input = input("input: ")

answer = False

for i in range(0, len(input)):
    if input[i] == "b" and input[i+2] == "b" :
        answer = True
        break
        


print(answer)