class Student: #class
    name = "Humaid Siddiqui"

s1=Student()
print(s1.name) #object



class Stud:
    def __init__(self): #this one gets call by itself and invoke by itself 
        print(self)
        print("Adding a new student!")

s1=Stud()
print(s1) #both s1 and self are same 

class Stud:
    def __init__(self,fullname,marks): 
        print("adding a new name in database")
        self.fullname=fullname
        self.marks=marks


s1=Stud("mohammed humaid siddiqui",98.0)
print(s1.fullname,s1.marks)

s2=Stud("Anwar",55.0)
print(s2.fullname,s2.marks)


wap to take name,marks as arguements and cal sum of avg marks by using self constructor
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def score(self):
        Sum=0
        for val in self.marks:
            Sum+=val #ADD ALL THE VALUES IN THE MARKS
        print("HI",self.name,"your avg score is",Sum/3)

s1=Student("Mohammed Humaid Siddiqui",[90,90,90])
s1.score()

        