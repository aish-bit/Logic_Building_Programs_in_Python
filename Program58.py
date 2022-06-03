###############################################################################
# Q : 
# Display below pattern on console.
# Input : 6
# Output : abcdef
# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          09/05/2022

###############################################################################

from DisplayPattern import nTimesSmallAlphabetNoSpaceInOneRow

###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

def main():

    try:
        #Initialising variable to none
        iValue = None

        # accepting input from user
        print("Used to display n'th times small alphabets with no space in between in single row")
        iValue  = int(input("Please enter number: "))

        # calling to user defined nTimesSmallAlphabetNoSpaceInOneRow
        # method from DisplayPattern module
        nTimesSmallAlphabetNoSpaceInOneRow(iValue)   
    
    except Exception as eobj:

        #to catch and display exception if any occured during run time of program execution
        print("Exception occured : ",eobj)    


###############################################################################

# Description:   Starter of program
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    