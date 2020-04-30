import random


def print_players(players):
    for player in players:
        print(player["name"] + ":" + str(player["chips"]), end=" ")
    print()


dice_results = ["Left", "Right", "Center", ".", ".", "."]
center = 0
players = []

while True:
    # ask the user to enter the player names
    user = input("Please enter player name. ").lower()
    if user in ["done", "quit", "exit"]:
        break
    elif user.isalpha():
        # each player starts with 3 chips
        players.append({"name": user, "chips": 3})
    else:
        print("Not a valid entry.")

# while True:
# each player then takes turns rolling the dice
for i in range(len(players)):
    # if the player has less than 3 chips, they roll the same number of dice they have chips
    # roll 3 dice
    if players[i]["chips"] >= 3:
        num_dice = 3
    # roll number of dice
    elif players[i]["chips"] == 2 or players[i]["chips"] == 1:
        num_dice = players[i]["chips"]
    else:
        # don't roll any dice
        num_dice = 0
    print(f'{players[i]["name"]} rolled {num_dice} dice.')
    for die_i in range(num_dice):
        result = random.choice(dice_results)
        print(result)
        # if the die is L, move a chip to the player on the left (i-1)
        if result == "Left":
            players[i]["chips"] -= 1
            players[i-1]["chips"] += 1
        # if the die is R, move a chip to the player on the right (i+1)
        elif result == "Right":
            players[i]["chips"] -= 1
            if i == len(players)-1:
                players[0]["chips"] += 1
            else:
                players[i+1]["chips"] += 1
        # if the die is C, move a chip to the center pot
        elif result == "Center":
            players[i]["chips"] -= 1
            center += 1
    print_players(players)


# when only one player has chips, they won, ask the user if they want to play again