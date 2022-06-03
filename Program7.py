###############################################################################
# Q : 
# Display 1 to 5 on screen.
# Output : 1 2 3 4 5 

# POP way implementation => (function is reusable but inside the same file only)
###############################################################################


###############################################################################

# Function name: displayOnetoFive
# Input:         -
# Output:        -
# Description:   It is used to display 1 to 5 on screen
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

def displayOnetoFive():

    iNo = 5
    iCnt = 1
    # for loop implementation 
    # for iCnt in range(iValue):
    #     print(iCnt+1,end = " ")

    #while loop implementation
    while(iCnt <= iNo):
        print(iCnt,end = " ")
        iCnt += 1

    print()    


###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

def main():

    # calling to user defined displayOnetoFive() method
    displayOnetoFive()


###############################################################################

# Description:   Starter of program
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    