print("WELCOME TO JEFF'S TINY ADVENTURE!")
print()

# Room 1: The Entrance
print("You are in a creepy house! Would you like to go \"upstairs\" or into the \"kitchen\"?")
choice1 = input("> ").strip().lower()
print()

if choice1 == "kitchen":
    # Room 2: Kitchen
    print("There is a long countertop with dirty dishes everywhere. Off to one side")
    print("there is, as you'd expect, a refrigerator. You may open the \"refrigerator\"")
    print("or look in a \"cabinet\".")
    choice2 = input("> ").strip().lower()
    print()

    if choice2 == "refrigerator":
        # Room 4: Refrigerator
        print("Inside the refrigerator you see food and stuff. It looks pretty nasty.")
        print("Would you like to eat some of the food? (\"yes\" or \"no\")")
        choice3 = input("> ").strip().lower()
        print()

        if choice3 == "yes":
            # Ending 1
            print("You eat the mysterious glowing leftovers. You gain superpower-like energy and escape the house!")
        elif choice3 == "no":
            # Ending 2
            print("You die of starvation... eventually.")
        else:
            print("Invalid choice! You get confused and leave the house.")

    elif choice2 == "cabinet":
        # Room 5: Cabinet
        print("You open the wooden cabinet. Inside you find a mysterious glowing jar.")
        print("Do you want to \"open\" the jar or \"leave\" it alone?")
        choice3 = input("> ").strip().lower()
        print()

        if choice3 == "open":
            # Ending 3
            print("A friendly genie pops out and grants you three wishes! You win!")
        elif choice3 == "leave":
            # Ending 4
            print("You close the cabinet carefully, step backward onto a squeaky floorboard, and fall through a trapdoor!")
        else:
            print("Invalid choice! You trip and run away.")

    else:
        print("Invalid choice! You wandered into a wall.")

elif choice1 == "upstairs":
    # Room 3: Upstairs Hallway
    print("Upstairs you see a hallway. At the end of the hallway is the master")
    print("\"bedroom\". There is also a \"bathroom\" off the hallway. Where would you like to go?")
    choice2 = input("> ").strip().lower()
    print()

    if choice2 == "bedroom":
        # Room 6: Bedroom
        print("You are in a plush bedroom, with expensive-looking hardwood furniture. The")
        print("bed is unmade. In the back of the room, the closet door is ajar. Would you")
        print("like to open the door? (\"yes\" or \"no\")")
        choice3 = input("> ").strip().lower()
        print()

        if choice3 == "yes":
            # Ending 5
            print("You open the closet and find a secret exit that leads safely outside!")
        elif choice3 == "no":
            # Ending 6
            print("Well, then I guess you'll never know what was in there. Thanks for playing, I'm tired of making nested if statements.")
        else:
            print("Invalid choice! You fall asleep on the unmade bed.")

    elif choice2 == "bathroom":
        # Room 7: Bathroom
        print("You enter a dusty mirror-lined bathroom. The faucet is dripping gently into the sink.")
        print("Do you want to turn on the \"faucet\" or look in the \"mirror\"?")
        choice3 = input("> ").strip().lower()
        print()

        if choice3 == "faucet":
            # Ending 7
            print("Clean water flows out! You quench your thirst and find a hidden key in the sink drain.")
        elif choice3 == "mirror":
            # Ending 8
            print("Your reflection waves back at you on its own! Scared half to death, you bolt out the front door.")
        else:
            print("Invalid choice! You slip on a wet tile.")

    else:
        print("Invalid choice! You wandered into a wall.")

else:
    print("Invalid choice! You stood in the doorway forever.")