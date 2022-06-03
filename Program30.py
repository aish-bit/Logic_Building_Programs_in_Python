###############################################################################
# Q : 
# Accept no from user and return count of digits from that number.
# Input : 7521
# Output: 4
# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          30/03/2022

###############################################################################

from ProblemOnDigits import countDigitsFromInt

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
        iValue  = int(input("Please enter integer to calculate count of digits from it : "))

        # calling to user defined countDigitsFromInt method
        # from ProblemOnDigits module
        iRet = countDigitsFromInt(iValue)

        if(iRet == 1):
            print("Number of digits in {} is : {}".format(iValue,1))  
        else:    
            print("Number of digits in {} is : {}".format(iValue,iRet))   
    
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