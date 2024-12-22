import random


userwins=0
computerwins=0

options=["rock","paper","scissors"]


user_input=input("Type a Rock/Paper/Scissor or q to Quit: ").lower()
while True:
    if(user_input=="q"):
        break
    
    if user_input not in options:
        continue
random_number=random.randrange(0,2)
computer_pick=options[random_number]
print("Computer picked", computer_pick+".")
while True:
    if(user_input=="rock" and computer_pick=="scissor"):
            print("you won!")
            userwins+=1
            continue


    elif(user_input=="paper" and computer_pick=="rock"):
            print("you won!")
            userwins+=1
            continue

    elif(user_input=="scissor" and computer_pick=="paper"):
            print("you won!")
            userwins+=1
            break
    else:
            print("you lost!")
            computerwins+=1



# rock:0,paper:1,scissors:2

print("Goodbye!")


