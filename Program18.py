###############################################################################
# Q : 
# Accept no from user and and add all numbers upto that number and return addition 
# of all these numbers.
# If user provided negative number then still return addition of positive numbers
# Input : -3
# Output: 6 (3+2+1)
# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          22/03/2022

###############################################################################

from ProblemOnNumber import addAllPositiveNumUptoN

###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          22/03/2022

###############################################################################

def main():

    try:
        # accepting input from user
        iValue  = int(input("Please enter number to perform addition of all numbers upto that number: "))

        # calling to user defined addAllNumUptoN method
        # from ProblemOnNumber module
        iRet = addAllPositiveNumUptoN(iValue)

        if(iRet == "error"):
            print("Entered input is zero.Please provide valid input.")
        else:
            print("Addition of all numbers upto {} is : {}".format(iValue,iRet))
    
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