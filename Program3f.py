###############################################################################
# Q : 
# Additon of two numbers
# POP way of programming- 6 (better than previous 5 programs)
# the code is reusable as we seperate out logic function so we can reuse it anywhere we needed
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          21/03/2022

###############################################################################

import Arithmetics as arith


###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

def main():

    try:
        # take input from user
        iValue1 = int(input("Enter first number : "))
        iValue2 = int(input("Enter second number : "))

        # calling to user defined addition function which we put in module named Arithmetics
        iRet = arith.addition(iNo1 = iValue1,iNo2 = iValue2) #keyword arguments

        # display addition on console
        print("Addition of {} and {} is : {}".format(iValue1,iValue2,iRet))

    except Exception as eobj:

        # Exception handled
        print("Exception occured: ",eobj)


###############################################################################

# Description:   Starter of program
# Date:          21/03/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    