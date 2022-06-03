# 3. Write a program which accept one number from user and return its factorial.
# Input : 5 Output : 120

import BussinessLogic as BL

def execute():

    value  = 0
    ret    = 0
        
    value = int(input("Enter number: "))

    ret = BL.factorialInt(value)

    print("Factorial of number is: ",ret) 

    value  = None
    ret    = None  

if __name__ =="__main__":
    execute()    