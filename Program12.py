###############################################################################
# Q : 
# Accept n numbers from user and display Marvellous on screen n number of times
# Input  : -5 
# or 
# Input  : 5 
# Output : Marvellous
#          Marvellous
#          Marvellous
#          Marvellous
#          Marvellous

# POP way implementation => (function is reusable outside of this file also)
###############################################################################


###############################################################################

# Description:   importing modules required
# Date:          21/03/2022

###############################################################################

from ProblemOnNumber import displayMarvellous


###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

def main():

    try:
        # accepting input from user
        iValue  = int(input("Please enter frequency to display marvellous on console : "))

        # calling to user defined displayMarvellous() method
        # from ProblemOnNumber module
        displayMarvellous(iValue)

    except Exception as eobj:

        print("Exception occured : ",eobj)    


###############################################################################

# Description:   Starter of program
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    