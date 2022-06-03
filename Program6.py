###############################################################################
# Q : 
# Display 1 to 5 on screen.
# Output : 1 2 3 4 5 

# Wrong way of implementation-2 => (using loop but inside main function due to 
# which code is not reusable)
###############################################################################


###############################################################################

# Function name: main
# Description:   Entry point function of program.Used to display 1 to 5 on Console.
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

def main():

    #for loop implementation
    iValue = 5

    for iCnt in range(iValue):
        print(iCnt+1,end = " ")


###############################################################################

# Description:   Starter of program
# Date:          21/03/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    