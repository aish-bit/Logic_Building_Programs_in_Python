# 4.Write a program which display 5 times Marvellous on screen. 
# Output : Marvellous
        #  Marvellous
        #  Marvellous
        #  Marvellous
        #  Marvellous

import BussinessLogic as BL

def execute():

    value = 0
        
    value = int(input("Enter frequency: "))

    BL.displayMarvellous(value)

    value = None

if __name__ =="__main__":
    execute()    