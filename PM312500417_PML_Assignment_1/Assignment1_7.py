# 7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
# Input : 8 Output : False
# Input : 25 Output : True

import BussinessLogic as BL

def execute():

    value = 0
    ret   = False
        
    value = int(input("Enter number to check: "))

    ret = BL.chkIntDivisibleByFive(value)

    print(ret)
    if(ret == True):
        print("Number is divisible by 5")
    elif(ret == False):
        print("Number is not divisible by 5")    

    value = None
    ret   = None

if __name__ =="__main__":
    execute()    