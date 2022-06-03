# 6. Write a program which accept one number and display below pattern.
# Input : 5
# Output : 
# * * * * *
# * * * *
# * * *
# * *
# *

import BussinessLogic as BL

def execute():

    value = 0
        
    value = int(input("Enter number: "))

    BL.displayLeftLowerRightAngleTrianle(value)

    value = None

if __name__ =="__main__":
    execute()    