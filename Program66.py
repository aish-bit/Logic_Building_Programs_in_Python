###############################################################################
# Q : 
# Display below pattern on console.
# input = 6 6 (row column)
# Output =
#           $ # # # # #
#           * $ # # # #
#           * * $ # # #
#           * * * $ # #
#           * * * * $ #
#           * * * * * $

# POP way implementation => (function is reusable outside of this file also)
###############################################################################

###############################################################################

# Description:   importing modules required
# Date:          09/05/2022

###############################################################################

from DisplayPattern import dlrDiagStrLtHshUtSq


###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

def main():

    try:
        #Initialising variable to none
        iRow = None
        iCol = None

        # accepting input from user
        print("Used to display dollar-Diagonal-StarLowerTriangle-HashUpperTriangle-Box pattern on console")
        iRow  = int(input("Please enter row required: "))
        iCol  = int(input("Please enter col required: "))

        # calling to user defined dlrDiagStrLtHshUtSq method 
        # user defined DisplayPattern module
        dlrDiagStrLtHshUtSq(iRow,iCol)   
    
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