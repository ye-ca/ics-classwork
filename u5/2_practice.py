list = ["hello", "there", "world"]

searched = input("What's the word you want to search for?: ")

if searched in list:
    word_i = list.index(searched)
else:
    word_i = -1

print(f"Your word is at {word_i}")
