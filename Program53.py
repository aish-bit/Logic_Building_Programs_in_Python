###############################################################################
# Q : 
# Accept 2 no's from user and show small number from it.
# Input : 3 6
# Output: 3
# Input : -3 -9
# Output: -9
# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          08/05/2022

###############################################################################

from ProblemOnNumber import smallNumb

###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          08/05/2022

###############################################################################

def main():

    try:
        #Initialising variable to none
        iValue1 = None
        iValue2 = None
        iRet   = None

        # accepting input from user
        print("To show smallest number from provided 2 numbers: ")
        iValue1  = int(input("Please enter first number: "))
        iValue2  = int(input("Please enter second number: "))

        # calling to user defined smallNumb method from ProblemOnNumber module
        iRet = smallNumb(iValue1,iValue2)

        if(iRet == "error"):
            print("Please check.Provided input is zero")
        elif(iRet == "equal"):
            print("Numbers are equal")    
        else: 
            print("Smallest number from {} & {} is : {}".format(iValue1,iValue2,iRet))      
    
    except Exception as eobj:

        #to catch and display exception if any occured during run time of program execution
        print("Exception occured : ",eobj)    


###############################################################################

# Description:   Starter of program
# Author:        Aishwarya Sunil Karande
# Date:          08/05/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    