###############################################################################
# Q : 
# Accept no from user and from that no Display each digit seperately.
# Input : 7521
# Output: 7 5 2 1
# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          24/03/2022

###############################################################################

from ProblemOnDigits import displayDigitsFromInt

###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          24/03/2022

###############################################################################

def main():

    try:
        # accepting input from user
        iValue  = int(input("Please enter integer to display digits from it : "))

        iRetList = list()

        # calling to user defined displayDigitsFromInt method
        # from ProblemOnDigits module
        iRetList = displayDigitsFromInt(iValue)

        if(iRetList == -1):
            print("Provided value is zero")
        else:    
            print("Digits from {} are : {}".format(iValue,iRetList))   
    
    except Exception as eobj:

        print("Exception occured : ",eobj)    


###############################################################################

# Description:   Starter of program
# Author:        Aishwarya Sunil Karande
# Date:          24/03/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    