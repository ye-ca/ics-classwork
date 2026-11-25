TICKET_PRICE = 13.95

def main():
    tickets = int(input("How many tickets\n> "))

    total_cost = tickets * TICKET_PRICE

    print(f"Your total cost is: {total_cost}")

if __name__ == "__main__":
    main()

