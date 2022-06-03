###############################################################################
# Q : 
# Accept no from user and display below pattern

# Input:4
# Output : 1 * 2 * 3 * 4 *

# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          08/05/2022

###############################################################################

from DisplayPattern import displayNumberStarInOneRow


###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          08/05/2022

###############################################################################

def main():
    try:
        # Initialising variable to none
        iValue = None

        # accepting input from user
        iValue = int(input("Please enter number to print pattern : "))

        # calling to user defined displayNumberStarInOneRow method 
        # from user defined DisplayPattern module
        displayNumberStarInOneRow(iValue)

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