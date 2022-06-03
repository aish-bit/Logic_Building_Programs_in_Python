# 10. Write a program which accept name from user and display length of its name.
# Input : Marvellous  Output : 10

import BussinessLogic as BL

def execute():

    data = None
    ret = 0
        
    data = (input("Enter name: "))

    ret = BL.stringLenX(data)

    print("Length of string is: ",ret)
    
    ret = None
    data = None

if __name__ =="__main__":
    execute()    