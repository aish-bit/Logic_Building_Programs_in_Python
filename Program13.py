###############################################################################
# Q : 
# Accept no from user and display all numbers upto that no number on console
# Input  : 5 
# Output:  1 2 3 4 5

# Input  : -5 
# Output:  -1 -2 -3 -4 -5

# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          21/03/2022

###############################################################################

from ProblemOnNumber import displayUptoNInt


###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

def main():

    try:
        # accepting input from user
        iValue  = int(input("Please enter frequency to display numbers on console : "))

        # calling to user defined displayUptoNInt() method
        # from ProblemOnNumber module
        displayUptoNInt(iValue)

    except Exception as eobj:

        print("Exception occured : ",eobj)    


###############################################################################

# Description:   Starter of program
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    