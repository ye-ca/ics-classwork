def main():
    length = int(input("Enter a length: "))
    width = int(input("Enter a width: "))
    print()

    area = length * width

    print(f"The area is {area} units squared")

def greet():
    print("Welcome to the awesome area calculator!")
    print()

if __name__ == "__main__":
    greet()
    main()
