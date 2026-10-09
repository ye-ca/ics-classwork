cost = float(input("The cost of your item is how many dollars?\n$"))
if cost > 100:
	print("wow, that's expensive")

name = input("What's your name?: ")
my_name = "Jeffrey"

my_first = my_name[0].lower()
user_first = name[0].lower()
user_last = name[-1].lower()

if user_first == my_first:
	print(f"Woah, nice to meet you {name}, my name is Jeffrey and it stards with J too!")
elif user_last == my_first:
	print(name[-1])
	print(f"At least we can chain the names together! {name}effrey")
else:
	print(f"{name} is a cool name!")


