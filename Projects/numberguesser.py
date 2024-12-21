import random
toprange=input("enter A Range Number you want guess till: ")
if(toprange.isdigit()):
    toprange=int(toprange)
    if(toprange<=0):
        print("Enter a number higher than 0")
        quit()
    else:
        random_number=random.randint(1,toprange)
    guess_count=0
    while True:
        guess_count+=1
        user_guess=input("Guess the number: ")
        if(user_guess.isdigit()):
            user_guess=int(user_guess)
            
        else:
             print("please type a number next time")
             continue

        if(user_guess==random_number):
    
            print("Hurraay you guess it right! in ",guess_count, "guesses")
            break
        else:
            print("Try Again")
    






   
    
