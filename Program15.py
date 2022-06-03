###############################################################################
# Q : 
# Accept no from user and display all numbers upto that n number on console
# in reverse.
# Input:5
# Output:5 4 3 2 1
# Input:-5
# Output:-5 -4 -3 -2 -1
# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          22/03/2022

###############################################################################

from ProblemOnNumber import displayUptoNRev


###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          22/03/2022

###############################################################################

def main():

    try:
        # accepting input from user
        iValue  = int(input("Please enter frequency to display numbers in revercse on console : "))

        # calling to user defined displayUptoNRev() method
        # from ProblemOnNumber module
        displayUptoNRev(iValue)

    except Exception as eobj:

        print("Exception occured : ",eobj)    


###############################################################################

# Description:   Starter of program
# Author:        Aishwarya Sunil Karande
# Date:          22/03/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    