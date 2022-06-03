###############################################################################
# Q : 
# Accept no from user and return addition of even digits from that number.
# Input : 7521
# Output: 2
# Input : 11134   
# Output: 4   
# Input : 2264
# Output: 14
# Input : 3357
# Output: 0
# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          30/03/2022

###############################################################################

from ProblemOnDigits import addEvenDigitsFromInt

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
        iValue  = int(input("Please enter integer to calculate addition of even digits from it : "))

        # calling to user defined addEvenDigitsFromInt method
        # from ProblemOnDigits module
        iRet = addEvenDigitsFromInt(iValue)

        if(iRet == -1):
            print("Please check.Provided input is zero")  
        else:    
            print("Addition of even digits from {} is : {}".format(iValue,iRet))   
    
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