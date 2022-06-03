###############################################################################
# Q : 
# Find factorial of number using "while loop"
# Input : 1
# Output: 1 (1)

# Input : 3
# Output: 6 (3*2*1)

# Input : 5
# Output: 120 (5*4*3*2*1)

# POP way implementation => (function is reusable inside of this file only)
###############################################################################


###############################################################################

# Function name: factorialOfIntWhileLoop
# Input:         Integer
# Output:        Integer
# Description:   It is used to display factorial of integer
# Author:        Aishwarya Sunil Karande
# Date:          22/03/2022

###############################################################################
def factorialOfIntWhileLoop(iNo):
    #Input Updater
    if(iNo < 0):
        iNo = -iNo

    iFact = 1
    iCnt = 1
    #Calculating factorial of integer by iterating over number
    while(iCnt <= iNo):

        iFact *= iCnt
        iCnt += 1
        
    return iFact

###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          22/03/2022

###############################################################################

def main():

    try:
        # accepting input from user
        iValue  = int(input("Please enter integer to find its factorial: "))

        # calling to factorialOfIntWhileLoop function
        iRet = factorialOfIntWhileLoop(iValue)

        print("Factorial of {} is : {}".format(iValue,iRet))  
    
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