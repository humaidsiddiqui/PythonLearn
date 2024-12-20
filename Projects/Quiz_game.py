print("Welcome to my game!!!")
playing=input("do you want to play game? ")
if playing.lower() != "yes":
    quit()
print("Okay let's play :) ")
score=0
answer=input("what is CPU Stands For? ")
if (answer.lower()=="central processing unit"):
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What is GPU stands for? ")
if (answer.lower()=="graphics processing unit"):
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What is RAM Stands for? ")
if (answer.lower()=="random access memory"):
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print(f"your score is {score} out of 4")
print("the percentage is "+ float(score)/3*100,"%")





