# 5.Write a program which accept one number for user and check whether number is prime or not.
# Input : 5 Output : It is Prime Number

import BussinessLogic as BL

def execute():

    value = 0
    ret   = None
        
    value = int(input("Enter number to check: "))

    ret = BL.chkPrime(value)

    if(ret == True):
        print(value," is prime number")
    elif(ret == False):
        print(value," is not prime number")    

    value = None
    ret   = None

if __name__ =="__main__":
    execute()    
    