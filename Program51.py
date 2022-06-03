###############################################################################
# Q : 
# Accept 3 no's from user and display its average.
# Input : 3 + 6 + 9
# Output: 6 

# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          08/05/2022

###############################################################################

from ProblemOnNumber import averageOfThreeNumb

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
        iValue3 = None
        iRet   = None

        # accepting input from user
        print("To calculate average of three numbers : ")
        iValue1  = int(input("Please enter first number: "))
        iValue2  = int(input("Please enter second number: "))
        iValue3  = int(input("Please enter third number: "))

        # calling to user defined averageOfThreeNumb method from ProblemOnNumber module
        iRet = averageOfThreeNumb(iValue1,iValue2,iValue3)

        if(iRet == "error"):
            print("Please check.Provided input is zero")
        else: 
            print("Average of {},{} & {} is : {}".format(iValue1,iValue2,iValue3,iRet))      
    
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