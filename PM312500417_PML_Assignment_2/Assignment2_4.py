# 4.Write a program which accept one number form user and return addition of its factors.
# Input : 12 Output : 28 (1+2+3+4+6+12)

import BussinessLogic as BL

def execute():

    value = 0
    ret   = 0
        
    value = int(input("Enter number: "))

    ret = BL.addFactorsInt(value)

    print("Addition of factors of number is: ",ret)

    value = None
    ret   = None

if __name__ =="__main__":
    execute()    