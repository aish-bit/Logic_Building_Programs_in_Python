###############################################################################
# Q : 
# Accept no from user and check whether given no is pallindrome or not.
# by using user defined revDigitsFromInt() function from user defined ProblemOnDigits module
# Input : 7557
# Output: yes
# Input : -454
# Output: yes 
# Input : 2002
# Output: yes
# Input : 200
# Output: no
# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          30/03/2022

###############################################################################

from ProblemOnDigits import revDigitsFromInt

###############################################################################

# Function name: chkIntPalindrome
# Input:         Integer
# Output:        Boolean
# Description:   It is used to check provided integer is palindrome or not
# Author:        Aishwarya Sunil Karande
# Date:          30/03/2022

###############################################################################

def chkIntPalindrome(iNo):
    iRet = revDigitsFromInt(iNo)

    if(iRet == -1):
        return -1
    elif(iRet == iNo):
        return True
    else:
        return False

###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          30/03/2022

###############################################################################

def main():

    try:
        #Initialising variable to zero
        iValue = 0
        bRet   = 0

        # accepting input from user
        iValue  = int(input("Please enter integer to check its palindrome parity: "))

        # calling to user defined chkIntPalindrome method from ProblemOnDigits module
        bRet = chkIntPalindrome(iValue)

        if(bRet == -1):
            print("Please check.Provided input is zero")  
        elif(bRet == True):    
            print("{} is palindrome".format(iValue))
        else:    
            print("{} is not palindrome".format(iValue))       
    
    except Exception as eobj:

        #to catch and display exception if any occured during run time of program
        print("Exception occured : ",eobj)    


###############################################################################

# Description:   Starter of program
# Author:        Aishwarya Sunil Karande
# Date:          30/03/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    