# 10. Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934 Output : 37

import BussinessLogic as BL

def execute():

    value = 0
    ret   = 0
        
    value = int(input("Enter number: "))

    ret = BL.addDigitFromInt(value)

    print("Addition of digits in ",value," is: ",ret)

    value = None
    ret   = None

if __name__ =="__main__":
    execute()    