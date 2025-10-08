import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player = []
computer = []
player.append(random.choice(cards))
player.append(random.choice(cards))
computer.append(random.choice(cards))
computer.append(random.choice(cards))
print("player",player)
third_round = input("third_round?")
if third_round == "yes":
    player.append(random.choice(cards))
    print("player",player)
    print("sum(player): ", sum(player))

    if sum(player) > 21:
        print("bust")
        print(f"bust, computer: {sum(computer)}, player:{sum(player)}")

    elif sum(computer) > 17:
        computer.append(random.choice(cards))
        print("sum(computer): ",sum(computer))
        if sum(player) <=  21 < sum(computer):
            print(f"player win, computer: {sum(computer)}, player:{sum(player)}")
    elif sum(computer) < sum(player) <= 21:
        print(f"player win, computer: {sum(computer)}, player:{sum(player)}")
elif sum(computer) < sum(player) <= 21:
    print(f"player win, computer: {sum(computer)}, player:{sum(player)}")


else:
    print(f"player lose, computer: {sum(computer)}, player:{sum(player)}")

