import random
from sys import displayhook

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# a while loop to let the user guess again.
game_over = False
matched_before = []

while game_over == False:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:

        if letter == guess:
            display += letter
            matched_before.append(letter)

        elif  letter in matched_before:
            display += letter

        else:
            display += "_"

    print(display)
    if "_" not in display:
        game_over = True
        print("You won")
