###############################################################################
# Q : 
# Accept no from user and display thier factors

# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          22/03/2022

###############################################################################

from ProblemOnNumber import  findFactorsInt

###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          22/03/2022

###############################################################################

def main():

    try:
        # accepting input from user
        iValue  = int(input("Please enter integer to find its factors: "))

        iRetList = list()

        # calling to user defined findFactorsInt method
        # from ProblemOnNumber module
        iRetList = findFactorsInt(iValue)

        if(iRetList == -1):
            print("Entered input is zero.Please provide valid input.")
        else:  
            if(iValue < 0):
                iNewValue = -iValue
                print("Factors of {} are = {}".format(iNewValue,iRetList))   
            print("Factors of {} are = {}".format(iValue,iRetList))       
    
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