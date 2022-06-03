# 3. Write a program which contains one function named as addInt() which accepts two numbers from user and return addition of that two numbers. 
# Input : 11 5 Output : 16

import BussinessLogic as BL

def execute():

    value1 = 0
    value2 = 0
    ret    = 0
        
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    ret = BL.addInt(value1,value2)

    print("Addition of two numbers is: ",ret) 

    value1 = None
    value2 = None
    ret    = None  

if __name__ =="__main__":
    execute()    