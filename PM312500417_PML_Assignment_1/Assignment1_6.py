# 6.Write a program which accept number from user and check whether that number is positive or negative or zero.
# Input : 11 Output : Positive Number
# Input : -8 Output : Negative Number
# Input : 0  Output : Zero

import BussinessLogic as BL

def execute():

    value = 0
    ret   = 0
        
    value = int(input("Enter number to check: "))

    ret = BL.chkIntType(value)

    if(ret == 1):
        print("Number is positive")
    elif(ret == -1):    
        print("Number is negative")
    elif(ret == 0):   
        print("Number is zero")

    value = None
    ret   = None

if __name__ =="__main__":
    execute()    