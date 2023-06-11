#Copyright©2023 Vishal Ahirwar. All rights reserved.
import os
import datetime
while True:
    input_=input("Enter Security Password ??")
    if(input_.lower()=="quit" or input_=="exit"):
            break
    pwd=str(datetime.datetime.now().time())
    temp=pwd.split(":")
    pwd=""
    for i in temp:
         pwd+=str(int(float(i)))
    print(pwd)    
    if(__name__=="__main__" and input_==pwd):
        print("Success!\nAre you sure you want delete items on desktop??")
        user_input= input("")
        if(user_input.lower()=="yes"):
            try:
                if(os.remove("C:\\Users\\Vishal Ahiwar\\Desktop\\")):
                    print("Success!")
                else:
                    print("Failed!")
            except:
                 print("You  do not have permission to delete the directory!")
                 break
        else:
            print("okay!")
    else:
        print("Sorry Incorrect Security Password!")



