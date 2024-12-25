import random

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll

while True:
    players=input("enter the number for players (2-4): ")
    if(players.isdigit()):
        players=int(players)
        if(2 <= players <= 4):
            break
        else:
            print("Must be between 2 to 4 players !")
    else:
        print("invalid Try Again!")
        continue
max_score=50
players_score=[0 for _ in range(players)] # this is list comprehension where it will add 0 for score in total no.of players!
print(players_score)

current_score=0

while max(players_score)<max_score:

    for player_idx in range(players):
        current_score=0

    while True:
        should_roll=input("would you like to roll ? (Y)? ").lower()
        if(should_roll!="y"):
            break
        value=roll()
        if value == 1:
            print("you rolled the one! turned done")
        else:
            current_score+=value
            print("you rolled a: ",value)

        players_score[player_idx] += current_score
        print("your current scoire is :",player_idx[players_score])



