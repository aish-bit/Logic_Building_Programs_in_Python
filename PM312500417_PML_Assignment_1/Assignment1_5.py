# 5.Write a program which display 10 to 1 on screen. 
# Output : 10 9 8 7 6 5 4 3 2 1

import BussinessLogic as BL

def execute():

    value = 0
        
    value = int(input("Enter number: "))

    BL.displayIntReverse(value)

    value = None

if __name__ =="__main__":
    execute()    