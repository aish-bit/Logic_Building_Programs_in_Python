# 9. Write a program which accept number from user and return number of digits in that number.
# Input : 5187934 Output : 7

import BussinessLogic as BL

def execute():

    value = 0
    ret   = 0
        
    value = int(input("Enter number: "))

    ret = BL.countIntDigit(value)

    print("Count of digits in ",value," is: ",ret)

    value = None
    ret   = None

if __name__ =="__main__":
    execute()    