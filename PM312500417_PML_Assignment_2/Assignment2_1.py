# 1.Create on module named as BussinessLogic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. Write on python program which call all the functions from BussinessLogic module by accepting the parameters from user.

import BussinessLogic as BL

def execute():

    ret = None
    value1 = 0
    value2 = 0

    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))
    
    ret = BL.addInt(value1,value2)
    print("Addition of two numbers is: ",ret)

    ret = BL.subInt(value1,value2)
    print("Substraction of two numbers is: ",ret)

    ret = BL.multInt(value1,value2)
    print("Multiplication of two numbers is: ",ret)
    
    ret = BL.divInt(value1,value2)
    if(ret == False):
        print("Cant do division;answer is undefined.")
    else:
        print("Division of two numbers is: ",ret)    

    ret = None
    value1 = None
    value2 = None
    
if __name__ =="__main__":
    execute()    