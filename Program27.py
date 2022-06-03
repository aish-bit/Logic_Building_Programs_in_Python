###############################################################################
# Q : 
# Accept no from user and from that no Display each digit seperately.
# Input : 7521
# Output: 7 5 2 1
# POP way implementation => (function is reusable inside the same file only)
###############################################################################


###############################################################################

# Function name: displayDigits
# Input:         Integer
# Output:        List of Integers
# Description:   It is used to display digits from positive number
# Author:        Aishwarya Sunil Karande
# Date:          24/03/2022

###############################################################################

def displayDigits(iNo):  
      
    resultList = list()

    iDigit = 0
    iNum   = iNo
    
    # seperating each digit from list by iterating over integer
    while(iNum != 0):
        
        iDigit = iNum % 10
        
        resultList.append(iDigit)
        
        iNum = int(iNum / 10)
        

    # reversing result list
    resultList.reverse()

    # returning result
    return resultList


###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          27/03/2022

###############################################################################

def main():

    # accepting input from user
    iValue  = 7521

    iRetList = list()

    #call to displayDigits() function
    iRetList = displayDigits(iValue)
    
    #displaying answer on console
    print("Digits from {} are : {}".format(iValue,iRetList))

###############################################################################

# Description:   Starter of program
# Author:        Aishwarya Sunil Karande
# Date:          27/03/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    