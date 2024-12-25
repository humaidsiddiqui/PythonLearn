master_pwd = input("what is the master password? ")

def view():
    with open ("password.txt","r") as f:
       for line in f.readlines():
           data=line.rstrip()#when we read the file we acctually read that \n character too. so we need to strip that character by using rstrip
           user, passw = data.split("|")
           #hello|tim|20|hi
           #["hello","tim",20,"hi"] will return in the form of list
           print("user: ",user,"password: ",passw)
        
def add():
    name= input("account name: ")
    password=input("password: ")
    with open ("password.txt","a") as f:
        f.write(name + "|"+ password+"\n")



while True:
    mode = input("what you like to add a new or view existing ones (view,add) or press q to quit ?").lower()
    if mode=="q":
        break
    
    if mode == "view":
        view()
    elif mode=="add":
        add()
    else:
        print("invalid mode")
        continue