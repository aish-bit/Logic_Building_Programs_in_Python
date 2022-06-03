###############################################################################
# Q : 
# Additon of two numbers
# POP way of programming- 5 (better than previous four programs)
# We handled exception and labled everything
#local variables names are proper
###############################################################################


###############################################################################

# Function name: Addition
# Input:         interger,interger
# Output:        interger
# Description:   It is used to add 2 integers
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

def addition(iNo1,iNo2):

    # local variable to store result
    iAns = None

    # performing addition
    iAns = iNo1 + iNo2 

    # returning addition of two numbers
    return iAns


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

        # calling to user defined addition function
        iRet = addition(iNo1 = iValue1,iNo2 = iValue2) #keyword arguments

        # display addition on console
        print("Addition of {} and {} is : {}".format(iValue1,iValue2,iRet))

    except Exception as eobj:

        # Exception handled
        print("Exception occured: ",eobj)


###############################################################################

# Description:   Starter of program
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    