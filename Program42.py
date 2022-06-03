###############################################################################
# Q : 
# Accept no from user and display its table.
# Input : 6 or -6
# Output: 6 12 18 24 30 36 42 48 54 60

# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          31/03/2022

###############################################################################

from ProblemOnNumber import displayTable

###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          31/03/2022

###############################################################################

def main():

    try:
        #Initialising variable to none
        iValue = None
        iRetList   = None

        # accepting input from user
        iValue  = int(input("Please number to display its table: "))

        # calling to user defined displayTable method from ProblemOnNumber module
        iRetList = displayTable(iValue)

        #updating negative input
        if(iValue < 0):
            iValue = -iValue
            
        if(iRetList == -1):
            print("Please check.Provided input is zero")
        else: 
            print("Table of {} : {}".format(iValue,iRetList))       
    
    except Exception as eobj:

        #to catch and display exception if any occured during run time of program execution
        print("Exception occured : ",eobj)    


###############################################################################

# Description:   Starter of program
# Author:        Aishwarya Sunil Karande
# Date:          31/03/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    