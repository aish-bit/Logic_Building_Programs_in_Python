###############################################################################
# Q : 
# Accept no from user and return its reverse.
# Input : 253
# Output: 352
# Input : 1278
# Output: 8721  
# Input : 5610
# Output: 165
# Input : 7000
# Output: 7
# Input : -56
# Output: -65
# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          30/03/2022

###############################################################################

from ProblemOnDigits import revDigitsFromInt

###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          30/03/2022

###############################################################################

def main():

    try:
        #Initialising variable to zero
        iValue = 0
        iRet   = 0

        # accepting input from user
        iValue  = int(input("Please enter integer to reverse its digits and form new reversed number: "))

        # calling to user defined revDigitsFromInt method
        # from ProblemOnDigits module
        iRet = revDigitsFromInt(iValue)

        if(iRet == -1):
            print("Please check.Provided input is zero")  
        else:    
            print("Reversal of {} is : {}".format(iValue,iRet))   
    
    except Exception as eobj:

        #to catch and display exception if any occured during run time of program
        print("Exception occured : ",eobj)    


###############################################################################

# Description:   Starter of program
# Author:        Aishwarya Sunil Karande
# Date:          30/03/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    