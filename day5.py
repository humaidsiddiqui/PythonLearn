# working on IF-ELIF CONDITIONS
a = input("enter first number: ")
b = input("enter second number: ")
c = input("enter third number: ")
d = input("enter fourth number: ")
if (a>=b and a>=c and a>=d):
    print("A is the greatest",a )
elif(b>=c and b>=d ):
    print("b is greatest: ",b)
elif(c>=d):
    print("c is greatest", c)
else:
    print("d is greatest", d)

# Working on Loop Condition 
# while condition
i=1
while i<=5:
    print("humaid",i)
    i+=1
print(i)

i = int(input("enter the number : "))
while i>=50:
    print("the number is ",i)
    i-=1

i= 1
while (i<=100):
    print(i)
    i+=1
print("loop ended")


i = 100
while (i>=1):
    print(i)
    i-=1
print("loop ended")

i=1
num=int(input("enter the number pls : "))
while (i<=10):
    sum=num*i
    print("Multiplication is :", sum)
    i+=1
print("loop ended")


numbers = [1,4,9,16,25,36,49,81,100]
index=0
while(index<len(numbers)):
    print(numbers[index])
    index+=1
print("loop ended")


numbers = (1,4,9,16,25,36,49,81,100)
x = int(input("enter the number you want to search: "))
index = 0
found = False
while(index<len(numbers)):
    if numbers[index] == x:
        found = True
        break
    index +=1
    
if found:
    print("the number is founded")
else : 
    print("the number is not found in the list sorry")

# a second way of solving this while loop
num = (1,4,9,16,25,36,49,81,100)
index = 0
x = 36
while index<len(num):
    if (x==num[index]):
        print("x is found at location", index)
    else:
        print("finding")
    index+=1
print("loop ended")

# working with break
i=0
while (i<=5):
    print(i)
    if(i==5):
        break
    i+=1
print("end loop")

i=0
while i<=10:
    if(i%2!=0):
        i+=1
        continue #skip
    print(i)
    i+=1
print("end of loop")

cars = ["porsche","acura","mercedes","bmw"]
for i in cars:
    print(i)
else:
    print("loop is ended")
# this means pure cars i mai ajayae and sequential execution is done"
# we use while for working in iterator such variable you want to update or you have condition
# and if you want to traverse in a datatype such as tuples, string, list by using for loops


nums=[1,4,9,16,25,36,49,81,100]
for el in nums:
    print(el)


index=0
nums=(1,4,9,16,25,36,49,81,100,49)
x=49
for el in nums:
    if (el==x):
        print(el)
        print("number found at index",index)
    index+=1

seq=range(5)
for i in seq:
    print(i)

for i in range(10):
    print (i)



# LOGIC BUILDING
students=[] 
while True:
    name=input("enter the name of the student (or done to finish and interrupt : ")
    if(name.lower()=="done"):
        break

    grade=float(input(f"enter {name} grade : "))
    students.append({"name ":name, "grade ":grade})
    print(students)

total_grades = sum(student["grade"] for student in students)

    





    


    
