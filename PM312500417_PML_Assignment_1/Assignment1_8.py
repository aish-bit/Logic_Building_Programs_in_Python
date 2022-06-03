# 8. Write a program which accept number from user and print that number of “*” on screen.
# Input : 5 Output : * * * * *

import BussinessLogic as BL

def execute():

    value = 0
        
    value = int(input("Enter frequency: "))

    BL.displayStar(value)

    value = None

if __name__ =="__main__":
    execute()    