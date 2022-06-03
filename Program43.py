###############################################################################
# Q : 
# Accept 2 no's from user where first number is base and second one is its power.
# Write a program to display its power

# Input : -2^5
# Output: -32
# Input : -2^4
# Output: 16
# Input : 2^5
# Output: 32
# Input : 2^4
# Output: 16
# Input : 2^0
# Output: 1

# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          31/03/2022

###############################################################################

from ProblemOnNumber import powerOfInt

###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          31/03/2022

###############################################################################

def main():

    try:
        #Initialising variable to none
        iValue1 = None
        iValue2 = None
        iRet   = None

        # accepting input from user
        iValue1  = int(input("Please enter base value to display its power: "))
        iValue2  = int(input("Please enter power value: "))

        # calling to user defined powerOfInt method 
        # from user defined ProblemOnNumber module
        iRet = powerOfInt(iNo1=iValue1,iNo2=iValue2)

        if(iRet == -1):
            print("Please check input {} & {} both are zero.Result is undefined".format(iValue1,iValue2))
        else: 
            print("{} raised to {} : {}".format(iValue1,iValue2,iRet))       
    
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