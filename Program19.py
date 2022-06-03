###############################################################################
# Q : 
# Accept no from user and and return its factorial.

# Input : 1
# Output: 1 (1)

# Input : 3
# Output: 6 (3*2*1)

# Input : 5
# Output: 120 (5*4*3*2*1)

# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          22/03/2022

###############################################################################

from ProblemOnNumber import  factorialOfInt

###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          22/03/2022

###############################################################################

def main():

    try:
        # accepting input from user
        iValue  = int(input("Please enter integer to find its factorial: "))

        # calling to user defined addAllNumUptoN method
        # from ProblemOnNumber module
        iRet = factorialOfInt(iValue)

        print("Factorial of {} is : {}".format(iValue,iRet))
    
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