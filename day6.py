# leaning of function
def calc_sum(a,b):
    sum=a+b
    print(sum)
    return(sum)
calc_sum(2,10)
calc_sum(4,12)
calc_sum(6,5)

# another way!!
def calculate(a,b):
    return a+b

sum=calculate(12,4)
print(sum)


# you can make no return and no paramters functions in coding too!
def helloworld():
    print("hello world!")

helloworld()
helloworld()
helloworld()
helloworld()


# the function who doesn't return any output will display none 
def hi():
    print("hi")

output=print(hi)
print(output) #None 


def avg(a,b,c):
    avg=(a+b+c)/3
    print(avg)
    return avg

avg(10,12,3)


cities=["hyderabad","mumbai","delhi","noida"]
heros=["batman","superman","thor","ironman"]

def list_count(list):
    print(len(list))

list_count(cities)
list_count(heros)

def list_print(list):
    for item in list:
        print(f"the items are : ",{item}, end="")


list_print(cities)
list_print(heros)




def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact *= i
    print(fact)

factorial(5)

def convert(cad_value):
    inr_value=cad_value*61
    usd_value=print(cad_value,"CAD = ",inr_value, "INR")
    return(usd_value)
convert(100)

# WAP To input from user and return whether it is true or not
def Even_or_odd(num):
    if (num%2==0):
        print("EVEN")
    else:
        print("ODD")
userinput=int(input("enter the number: "))
Even_or_odd(userinput)


# recursion: When a function calls itself repeateadly
# prints n to 1 backwards
def show (n):
    if (n==0): #base case which decide when the functions needs to stop!!
        return
    print(n)
    show(n-1)

show(6)
#show(n=5)-> (n-1)->(n=4) call again for 4, same goes till 0


def fact(n):
   if (n==0 or n==1):#base condition
      return 1
   return fact(n-1)*n
print(fact(2)) 

def calc_sum(n):
   if (n==0):
      return 0 
   return calc_sum(n-1)+n
   print(sum)


sum=calc_sum(5)
print(sum)



def print_list(list,index=0):
    if (index==len(list)):
        return
    print(list[index])
    print_list(list,index+1)

cities=["hyderabad","mumbai","delhi","noida"]
print(len(cities))
print_list(cities)
# how this work fist index 0 pe call gayi, check kiya 0=length hai (nahi hai), phir print karwadiya "hyderabad" phir index+1 hogayi
# again index 1 is == to length of list (no), again same , till index 4 == length(which is 4) now it returns and breaks the recursive function


# FILE I/0  IN PYTHON

f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()


f=open("demo.txt","r")
data=f.read()
print(data)

line1=f.readline()
line2=f.readline()

f=open("demo.txt","a")
data=f.write("\n I want to learn AWS now ")
print(data)
f.close



# it's easier with with syntax as it doesn't need to close the file
with open("demo.txt","r") as f:
    data=f.read()
    print(data)


# Deleting a file : using a OS module: Module (like a code library) is a file written by another programmer that generally has a functions we can use
# import os
# os.remoe(filename)

import os
os.remove("Sample.txt")

with open ("practice.txt","w") as f:
    data=f.write("Hi Everyone\n we arlearning File I/0\n using java \n I like programming in Python")
    print(data)
    f.close()

with open ("practice.txt","r") as f:
    data=f.read()

    new_data=data.replace("java","python")
    print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data=f.read()
        if(data(word)!= -1):
            print("found")
        else:
            print("not found")












