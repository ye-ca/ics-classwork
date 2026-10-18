print("TWO MORE QUESTIONS, BABY!")
print()

print("Think of something and I'll try to guess it!")
print() 

q1 = input("Question 1) Does it stay inside or outside or both? ").lower().strip()
q2 = input("Question 2) Is it a living thing? ").lower().strip()

print()
if q1 == "inside" and q2 == "yes":
    print("Hmm, the alive thing inside is probably a houseplant!")
if q1 == "inside" and q2 == "no":
    print("Something that is inside but not alive is definately a shower curtain!")
if q1 == "outside" and q2 == "yes":
    print("Hmm, the alive thing outside is most definately a bison!")
if q1 == "outside" and q2 == "no":
    print("Something that is outside but not alive is most definately a mailbox!")
if q1 == "both" and q2 == "yes":
    print("Hmm, the alive thing that is both inside and outside is most definately a dog!")
if q1 == "both" and q2 == "no":
    print("Something that is both inside and outside but not alive is most definately a car!")


