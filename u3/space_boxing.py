earth_weight = float(input("Please enter your current earth weight: "))

print("""I have information about the following planets:
         1. Venus     2. Mars     3. Jupiter
         4. Saturn    5. Uranus   6. Neptune """)

planet = int(input("Which planet are you visiting? \n#")) 

if planet == 1:
	target_weight = earth_weight * 0.78
	print(f"Your weight would be {target_weight:.2f} pounds on that planet")

if planet == 2:
        target_weight = earth_weight * 0.39
        print(f"Your weight would be {target_weight:.2f} pounds on that planet")

if planet == 3:
        target_weight = earth_weight * 2.65
        print(f"Your weight would be {target_weight:.2f} pounds on that planet")

if planet == 4:
        target_weight = earth_weight * 1.17
        print(f"Your weight would be {target_weight:.2f} pounds on that planet")

if planet == 5:
        target_weight = earth_weight * 1.05
        print(f"Your weight would be {target_weight:.2f} pounds on that planet")

if planet == 6:
        target_weight = earth_weight * 1.23
        print(f"Your weight would be {target_weight:.2f} pounds on that planet")
