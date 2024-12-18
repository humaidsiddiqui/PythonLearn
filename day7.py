
def check_for_word():
    count=1
    word="learning"
    data=True
    with open("c:/Users/User/OneDrive/Desktop/PythonProgramming/PythonLearn/file123.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(count)
                return
            count+=1
        return -1





    
