###############################################################################
# Q : 
# Accept number from user and display that number of * on screen.
# Input : 4
# Output : * * * *
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          21/03/2022

###############################################################################

import DisplayPattern as dp


###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

def main():

    try:
        # take input from user
        iValue = int(input("Please enter frequency of * to display : "))

        # calling to user defined displayStarLinearOneRow function which we put in module named DisplayPattern
        iRet = dp.displayStarLinearOneRow(iValue) 

    except Exception as eobj:

        # Exception handled
        print("Exception occured: ",eobj)


###############################################################################

# Description:   Starter of program
# Date:          21/03/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    