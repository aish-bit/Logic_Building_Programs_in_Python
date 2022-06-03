# 2. Write a program which contains one function named as ChkNumEvenOdd() which accept one parameter as number. If number is even then it should display “Even number” otherwise display “Odd number” on console. 
# Input : 11 Output : Odd Number
# Input : 8 Output : Even Number

import BussinessLogic as BL

def execute():

    value = 0
    ret   = None

    value = int(input("Enter number to check: "))

    ret = BL.chkNumEvenOdd(value)

    if(ret == True):
        print("Number is even")
    else:
        print("Number is odd")   

    value = None
    ret   = None    

if __name__ =="__main__":
    execute()    