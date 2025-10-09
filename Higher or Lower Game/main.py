# break down the problem
# print logos DONE
# get 2 random name from dictionary
# get their followers
# make a retrieval function
# make a compare function

# start with the easiest
# get 2 random name from dictionary
# player choose

# Turn the problem / task into comments in my code

from art import logo, vs
from random import choice
from game_data import data

first_choice = (choice(data))
f_name = first_choice['name']
f_followers = first_choice['follower_count']
f_description = first_choice['description']
f_country = first_choice['country']

second_choice = (choice(data))
if second_choice == first_choice:
    second_choice = (choice(data))

s_name = second_choice['name']
s_followers= second_choice['follower_count']
s_description = second_choice['description']
s_country = second_choice['country']


def compare(score):
    print(f"Compare A: {f_name}, {f_description},{f_country}")
    print(vs)
    print(f"Against B: {s_name}, {s_description},{s_country}")
    player_choice = input("Who has the most followers? 'A' or 'B': ").lower()
    if f_followers > s_followers and player_choice == 'a':
        print(f"Correct! {f_name} has more followers")
        score +=1
        print(f"Your score is {score}")
    elif f_followers < s_followers and player_choice == 'b':
        print(f"Correct! {s_name} has more followers")
        score += 1
        print(f"Your score is {score}")
    else:
        print(f"Incorrect! {player_choice} doesn't has more followers!")
        score -= 1
        print(f"Your score is {score}")
print(logo)
score = 0
should_continue = True
while should_continue:
    compare(score)
    choice = input("continue?").lower()
    print(choice)
    if choice == "no" or "n":
        should_continue = True
        print("Good bye")
    else:
        print("compare")

        compare()



