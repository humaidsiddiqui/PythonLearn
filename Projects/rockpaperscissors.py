import random

user_wins=0
computer_wins=0
draw=0

options=["rock","paper","scissors"]

while True:
    user_input=input("Type ROCK/PAPER/SCISSOR or Q to quit: ").lower()
    if(user_input=="q"):
        break
    
    if user_input not in options:
        print("thats not valid to game rules!")
        continue
    randomnumber=random.randint(0,2)
    # rock:0    paper:1    scissors:2
    computer_picks=options[randomnumber]
    print("computer picked",computer_picks + ".")
    

    if(user_input=="rock" and computer_picks=="scissors"):
        print("You Won!")
        user_wins+=1
        continue
    elif(user_input=="paper" and computer_picks=="rock"):
        print("You Won!")
        user_wins+=1
        continue
    elif(user_input=="scissors" and computer_picks=="paper"):
        print("You Won!")
        user_wins+=1
        continue
    elif(user_input=="rock" and computer_picks=="rock"):
        print("It is a Draw")
        draw+=1
        
    elif(user_input=="scissors" and computer_picks=="scissors"):
        print("It is a Draw")
        draw+=1
        
    elif(user_input=="paper" and computer_picks=="paper"):
        print("It is a Draw")
        draw+=1
       
    else:
        print("Computer Won!")
        computer_wins+=1
        continue


print("the number of times you won",user_wins)
print("the number of times computer won",computer_wins)
print("the number of draws are: ",draw)
print("goodbye!")



