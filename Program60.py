###############################################################################
# Q : 
# Display below pattern on console.
# input = 3 4 (row column)
# Output = 
#           * * * *
#           * * * *
#           * * * *
# POP way implementation => (function is reusable inside the same file also)
###############################################################################


###############################################################################

# Function name: starBoxPattern
# Input:         Integer,Integer
# Output:        -
# Description:   It is used to display * box pattern on console
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

def starBoxPattern(iRow,iCol):

    #loop to print pattern
    for iCnt1 in range(iRow):
        for iCnt2 in range(iCol):
            print("*",end = "\t")
        print()    

    print() 

###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

def main():

    try:
        #Initialising variable to none
        iRow = 3
        iCol = 4

        # calling to user defined starBoxPattern method
        starBoxPattern(iRow,iCol)   
    
    except Exception as eobj:

        #to catch and display exception if any occured during run time of program execution
        print("Exception occured : ",eobj)    


###############################################################################

# Description:   Starter of program
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    