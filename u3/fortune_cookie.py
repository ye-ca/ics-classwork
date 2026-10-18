import random

fortunes = [
    "You will have a great day!",
    "Something good will happen to you soon.",
    "You are a kind and generous person.",
    "Your hard work will pay off.",
    "You will find happiness in unexpected places."
    "You have a friend in need."
    "You will achieve your goals if you stay focused."
    "You will have a pleasant surprise soon."
]

random_fortune = random.choice(fortunes)
print(f'Fortune cookies says: "{random_fortune}"')

number = [random.randint(10, 99) for _ in range(6)]
print(f"    {number[0]} - {number[1]} - {number[2]} - {number[3]} - {number[4]} - {number[5]}")