import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


guess = input("Guess a letter: ").lower()
placeholder = ""
for letter in chosen_word:
    placeholder += "_"

print(placeholder)

display = ""

for letter in chosen_word:
    if letter == guess:
        display += guess
    else:
        display += "_"

print(display)


