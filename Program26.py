###############################################################################
# Q : 
# Accept no from user and from that no Display each digit seperately.
# Input : 7521
# Output: 7 5 2 1
# Logic behind seperate out digits from number
###############################################################################

###############################################################################

# Function name: main
# Description:   Entry point function of program
# Author:        Aishwarya Sunil Karande
# Date:          27/03/2022

###############################################################################

def main():

    # accepting input from user
    iValue  = 7521

    iDigit  = 0   
    iNo     = iValue

    iDigit = iNo % 10    # 1
    print("The Digit is : ",iDigit)
    iNo    = int(iNo / 10)  # 752
    print("Current number is : ",iNo)

    iDigit = iNo % 10    # 2
    print("The Digit is : ",iDigit)
    iNo    = int(iNo / 10)  # 75
    print("Current number is : ",iNo) 

    iDigit = iNo % 10    # 5
    print("The Digit is : ",iDigit)
    iNo    = int(iNo / 10)  # 7
    print("Current number is : ",iNo)

    iDigit = iNo % 10    # 7
    print("The Digit is : ",iDigit)
    iNo    = int(iNo / 10)  # 0
    print("Current number is : ",iNo)


###############################################################################

# Description:   Starter of program
# Author:        Aishwarya Sunil Karande
# Date:          27/03/2022

###############################################################################

if __name__ == "__main__":
    
    # call to main function
    main()    