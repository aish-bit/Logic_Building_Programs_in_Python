# 7. Write a program which accept one number and display below pattern.
# Input : 5
# Output : 
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

import BussinessLogic as BL

def execute():

    value = 0
        
    value = int(input("Enter number: "))

    BL.displaySqNumPattern(value)

    value = None

if __name__ =="__main__":
    execute()   