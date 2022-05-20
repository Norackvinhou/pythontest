import random

guess = random.randint(1,100)

user=input("A number, or q/Q to quit:")
count=0
while(True):
    if (user =="q" or user == "Q"):
        print("program exit")
        break
    if (int(user)>100 or int(user)<1):
        print("number can only between 1 and 100")
        user=input("A number, or q/Q to quit:")
        count+=1
    if(int(user)==guess):
        print(f"congrant you guessed it in {count} tried")
        break
    elif(int(user)<guess):
        print("guess heiger")
        user=(input("A number, or q/Q to quit:"))
        count+=1
    elif(int(user)>guess):
        print("lower")
        user=(input("A number, or q/Q to quit:"))
        count+=1

        
