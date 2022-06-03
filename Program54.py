###############################################################################
# Q : 
# Accept no from user and return count of digits which are greater than and equal to 5.
# Input : 127894
# Output : 3

# Input : -561750
# Output : 4
# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          08/05/2022

###############################################################################

from ProblemOnDigits import countDigitGreaterFive

###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          08/05/2022

###############################################################################

def main():

    try:
        #Initialising variable to none
        iValue = None
        iRet   = None

        # accepting input from user
        print("To count digits which are greater than and equal to 5 : ")
        iValue  = int(input("Please enter number: "))

        # calling to user defined countDigitGreaterFive method from ProblemOnNumber module
        iRet = countDigitGreaterFive(iValue)

        if(iRet == -1):
            print("Entered input is zero.Please provide valid input.")
        else: 
            print("Digits greater than and equal to 5 are : {}".format(iRet))      
    
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