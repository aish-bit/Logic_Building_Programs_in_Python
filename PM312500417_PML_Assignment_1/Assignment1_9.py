# 9. Write a program which display first 10 even numbers on screen.
# Output : 2 4 6 8 10 12 14 16 18 20

import BussinessLogic as BL

def execute():

    value = 0
        
    value = int(input("Enter how many even numbers you want to display: "))

    BL.displayEvenNum(value)

    value = None

if __name__ =="__main__":
    execute()    