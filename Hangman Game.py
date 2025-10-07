import random
word_list = ["aardVark", "babVoon", "Vcamel"]

myWord = random.choice(word_list).lower()
print(myWord)

userGuess = input("Guess the letter: ").lower()
print(f"userGuess is {userGuess}")

for letter in myWord:
    print(f"letter is {letter}")
    if userGuess != letter:
        print("Wrong")
    else:
        print("Right")
