
# working on file word searching
def check_for_word():
    count=1
    word="learning"
    data=True
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(count)
                return
            count+=1
        return -1





    
