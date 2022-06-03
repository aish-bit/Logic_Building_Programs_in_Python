###############################################################################
# Q : 
# Accept no from user and check whether given no is perfect number or not.
# Input : 6 or -6
# Output: 6 is a perfect number
# Input : 3 or -3
# Output: 3 is not a perfect number

# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          31/03/2022

###############################################################################

from ProblemOnNumber import chkIntPerfect

###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          31/03/2022

###############################################################################

def main():

    try:
        #Initialising variable to zero
        iValue = 0
        bRet   = 0

        # accepting input from user
        iValue  = int(input("Please enter integer to check whether number is perfect number or not: "))

        # calling to user defined chkIntPerfect method from ProblemOnNumber module
        bRet = chkIntPerfect(iValue)

        #updating negative input
        if(iValue < 0):
            iValue = -iValue
            
        if(bRet == -1):
            print("Please check.Provided input is zero")  
        elif(bRet == True):    
            print("{} is a perfect number".format(iValue))
        else:    
            print("{} is not a perfect number".format(iValue))       
    
    except Exception as eobj:

        #to catch and display exception if any occured during run time of program
        print("Exception occured : ",eobj)    


###############################################################################

# Description:   Starter of program
# Author:        Aishwarya Sunil Karande
# Date:          31/03/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    