# traffic light using if-elif and else statement
light = input ("what is color of the light : ")
if (light=="red"):
    print("STOP!")
elif (light=="green"):
    print("GO!")
elif (light=="yellow"):
    print("LOOKUP!")
else:
    print("the light is broken")


# if-elif-else statement in one line
food = input ("enter the food you want to eat : ")
eat = "yes" if food == "cake" else "no"
print(eat)


# clever if / ternary operator
age = int(input("enter your age = "))
vote = ("yes", "no") [age >= 18] 
print(vote)


sal=int(input("enter your salary"))
tax = sal*(0.1, 0.2) [sal<=50000] 
print(tax)

