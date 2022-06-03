###############################################################################
# Q : 
# Accept no from user and and (check whether the provided number is positive 
# or negative number) check parity of number

# Input : 1
# Output: 1 is Odd number

# Input : 3
# Output: 3 is Odd number

# Input : 10
# Output: 10 is Even number

# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          22/03/2022

###############################################################################

from ProblemOnNumber import  chkEvnOddInt

###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          22/03/2022

###############################################################################

def main():

    try:
        # accepting input from user
        iValue  = int(input("Please enter integer to check its parity: "))

        # calling to user defined addAllNumUptoN method
        # from ProblemOnNumber module
        iRet = chkEvnOddInt(iValue)

        if(iRet == True):
            print("{} is Even number".format(iValue))
        else:
            print("{} is Odd number".format(iValue))    
    
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