import random

enemy_health = 100

print("What attack would you like to do?")
print("1. Attack 1: 60% hitrate, 10-20 damage")
print("2. Attack 2: 80% hitrate, 5-10 damage")
print("3. Do nothing: 0% hitrate, 0 damage")

choice = input("Your choice(1, 2, or 3): ")

if choice == "1":
	hitrate = 60
	min_damage = 10
	max_damage = 20
elif choice == "2":
	hitrate = 80
	min_damage = 5
	max_damage = 10
elif choice == "3":
	hitrate = 80
	print("You did nothing...")
else:
	print("Invalid choice, turn skipped")

if choice == "1" or choice == "2":
	roll = random.randint(1, 100)
	
	if roll <= hitrate:
		damage = random.randint(min_damage, max_damage)
		enemy_health -= damage
		print(f"Hit! You dealt {damage} damage!")
	
	else:
		print("Miss! you didn't hit them...")

print(f"The enemy is at {enemy_health} health!")

