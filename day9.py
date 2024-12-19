class Student():
    university="Fairleigh dickinson University"
    print(university)
    def __init__(self,name,marks,rollno):
        self.name=name #self method used for objects such that it stores differnet values
        self.marks=marks
        self.rollno=rollno
        print(f"The marks for the: {name} with rol no: {rollno} are {marks} ")

    def Hello(self):
        print("Hello")
    def get_marks(self):
        return self.marks

s1=Student("Humaid",98,2098230)
s1.Hello()
print(s1.get_marks())


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print(f"The name of Student is {name} and the marks are {marks} ")

    def get_marks(self):
        sum=0
        for val in self.marks:
            sum += val #ad all the values in marks
            print(f"the average of marks of the {self.name} is",sum/3)

s1=Student("humaid",[98,99,97])
s1.get_marks()
