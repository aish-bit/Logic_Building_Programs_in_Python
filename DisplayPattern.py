###############################################################################

# Function name: displayStarLinearOneRow
# Input:         interger
# Output:        -
# Description:   It is used to display given number of * on console in linear way  
#                single row
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################


def displayStarLinearOneRow(iNo):
    #filter in case if user provided zero value
    if(iNo == 0):
        print("Please check the provided input is zero. We cant display pattern")
        return

    #Updator in case if user provided negative value
    if(iNo < 0):
        iNo = -iNo

    #loop to display * on console
    for  iCnt in range(iNo):
        print("*",end = " ")
    
    print()


###############################################################################

# Function name: displayHashFiveTimesVerticalOneCol
# Input:         -
# Output:        -
# Description:   It is used to display five times # on console 
#                in vertical single column pattern
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

def displayHashFiveTimesVerticalOneCol():  

    iNo = 5

    for iCnt in range(iNo):
        print("#")

###############################################################################

# Function name: displayHashEightTimesVerticalOneCol
# Input:         -
# Output:        -
# Description:   It is used to display 8 times # on console 
#                in vertical single column pattern
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

def displayHashEightTimesVerticalOneCol():  

    iNo = 8

    for iCnt in range(iNo):
        print("#")


###############################################################################

# Function name: displayNumberStarInOneRow
# Input:         Integer
# Output:        -
# Description:   It is used to display n'th times number star single row 
#                linear pattern on console
# Author:        Aishwarya Sunil Karande
# Date:          08/05/2022

###############################################################################

def displayNumberStarInOneRow(iNo):

    # filter in case of input is zero
    if(iNo == 0):
        print("Entered input is zero.Please provide valid input.")
        return

    # updater in case of input is negative number
    if(iNo < 0):
        iNo = -iNo

    #loop to print pattern
    for iCnt in range(iNo):
        print(iCnt+1,"\t","*",end = "\t")        

    print()    


###############################################################################

# Function name: displayNumberInOneRowRev
# Input:         Integer
# Output:        -
# Description:   It is used to display n'th times number in reverse single row 
#                linear pattern on console
# Author:        Aishwarya Sunil Karande
# Date:          08/05/2022

###############################################################################

def displayNumberInOneRowRev(iNo):

    # filter in case of input is zero
    if(iNo == 0):
        print("Entered input is zero.Please provide valid input.")
        return

    # updater in case of input is negative number
    if(iNo < 0):
        iNo = -iNo

    #loop to print pattern
    for iCnt in range(iNo,0,-1):
        print(iCnt,end = "\t")

    print()


###############################################################################

# Function name: displayNTimesEvenNumberInSingleRow
# Input:         Integer
# Output:        -
# Description:   It is used to display n'th times even number in single row 
#                linear pattern on console
# Author:        Aishwarya Sunil Karande
# Date:          08/05/2022

###############################################################################

def displayNTimesEvenNumberInSingleRow(iNo):

    # filter in case of input is zero
    if(iNo == 0):
        print("Entered input is zero.Please provide valid input.")
        return

    # updater in case of input is negative number
    if(iNo < 0):
        iNo = -iNo

    #loop to print pattern
    for iCnt in range(2,(iNo*2)+1,2):
        print(iCnt,end = "\t")

    print()


###############################################################################

# Function name: displayNTimesStarHashInSingleRow
# Input:         Integer
# Output:        -
# Description:   It is used to display n'th times * # in single row 
#                linear pattern on console
# Author:        Aishwarya Sunil Karande
# Date:          08/05/2022

###############################################################################

def displayNTimesStarHashInSingleRow(iNo):

    # filter in case of input is zero
    if(iNo == 0):
        print("Entered input is zero.Please provide valid input.")
        return

    # updater in case of input is negative number
    if(iNo < 0):
        iNo = -iNo

    #loop to print pattern
    for iCnt in range(iNo):
        if(iCnt % 2 == 0):
            print("#",end = "\t")
        else:
            print("*",end = "\t")
            
    print()  

###############################################################################

# Function name: displayNTimesSmallAlphabetInSingleRow
# Input:         Integer
# Output:        -
# Description:   It is used to display n'th times small alphabets in single row 
#                linear pattern on console
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

def displayNTimesSmallAlphabetInSingleRow(iNo):

    # filter in case of input is zero
    if(iNo == 0):
        print("Entered input is zero.Please provide valid input.")
        return

    # updater in case of input is negative number
    if(iNo < 0):
        iNo = -iNo

    # Initialising local variables
    ch = 97

    #loop to print pattern
    for iCnt in range(0,iNo,1):
        print(chr(ch),end="\t")
        ch += 1

    print()    


###############################################################################

# Function name: displayNTimesSmallAlphabetInSingleCol
# Input:         Integer
# Output:        -
# Description:   It is used to display n'th times small alphabets in single column 
#                linear pattern on console
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

def displayNTimesSmallAlphabetInSingleCol(iNo):

    # filter in case of input is zero
    if(iNo == 0):
        print("Entered input is zero.Please provide valid input.")
        return

    # updater in case of input is negative number
    if(iNo < 0):
        iNo = -iNo

    # Initialising local variables
    ch = 97

    #loop to print pattern
    for iCnt in range(0,iNo,1):
        print(chr(ch),end="\n")
        ch += 1

    print()


###############################################################################

# Function name: nTimesSmallAlphabetNoSpaceInOneRow
# Input:         Integer
# Output:        -
# Description:   It is used to display n'th times small alphabets in single row 
#                with no space in between linear pattern on console
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

def nTimesSmallAlphabetNoSpaceInOneRow(iNo):

    # filter in case of input is zero
    if(iNo == 0):
        print("Entered input is zero.Please provide valid input.")
        return

    # updater in case of input is negative number
    if(iNo < 0):
        iNo = -iNo

    # Initialising local variables
    ch = 97

    #loop to print pattern
    for iCnt in range(0,iNo,1):
        print(chr(ch),end="")
        ch += 1

    print()


###############################################################################

# Function name: nTimesCapAlphabetInOneRow
# Input:         Integer
# Output:        -
# Description:   It is used to display n'th times capital alphabets in single row 
#                linear pattern on console
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

def nTimesCapAlphabetInOneRow(iNo):

    # filter in case of input is zero
    if(iNo == 0):
        print("Entered input is zero.Please provide valid input.")
        return

    # updater in case of input is negative number
    if(iNo < 0):
        iNo = -iNo

    # Initialising local variables
    ch = 65

    #loop to print pattern
    for iCnt in range(0,iNo,1):
        print(chr(ch),end="\t")
        ch += 1

    print() 
    
###############################################################################

# Function name: starBoxPattern
# Input:         Integer,Integer
# Output:        -
# Description:   It is used to display * box pattern on console
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

def starBoxPattern(iRow,iCol):

    # filter in case of input is zero
    # if((iRow == 0) and (iCol == 0)):
    #     print("Entered input is zero.Please provide valid input.")
    #     return

    if((iRow == 0) or (iCol == 0)):
        print("Entered input is zero.Please provide valid input.")
        return    

    # updater in case of input is negative number
    if((iRow < 0)):
        iRow = -iRow

    if((iCol < 0)):
        iCol = -iCol    

    #loop to print pattern
    for iCnt1 in range(iRow):
        for iCnt2 in range(iCol):
            print("*",end = "\t")
        print()    

    print()     


###############################################################################

# Function name: intBoxPattern
# Input:         Integer,Integer
# Output:        -
# Description:   It is used to display integer-box pattern on console
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

def intBoxPattern(iRow,iCol):

    # filter in case of input is zero
    if((iRow == 0) or (iCol == 0)):
        print("Entered input is zero.Please provide valid input.")
        return    

    # updater in case of input is negative number
    if((iRow < 0)):
        iRow = -iRow

    if((iCol < 0)):
        iCol = -iCol    

    #loop to print pattern
    for iCnt1 in range(iRow):
        for iCnt2 in range(iCol):
            print(iCnt2+1,end = "\t")
        print()    

    print() 


###############################################################################

# Function name: sameIntInRowBoxPattern()
# Input:         Integer,Integer
# Output:        -
# Description:   It is used to display same integer in one row-box pattern on console
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

def sameIntInRowBoxPattern(iRow,iCol):

    # filter in case of input is zero
    if((iRow == 0) or (iCol == 0)):
        print("Entered input is zero.Please provide valid input.")
        return    

    # updater in case of input is negative number
    if((iRow < 0)):
        iRow = -iRow

    if((iCol < 0)):
        iCol = -iCol    

    #loop to print pattern
    for iCnt1 in range(iRow):
        for iCnt2 in range(iCol):
            print(iCnt1+1,end = "\t")
        print()    

    print() 


###############################################################################

# Function name: dollarDiagonalStarSq()
# Input:         Integer,Integer
# Output:        -
# Description:   It is used to display same integer in one row-box pattern on console
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

def dollarDiagonalStarSq(iRow,iCol):

    # updater in case of input is negative number
    if((iRow < 0)):
        iRow = -iRow

    if((iCol < 0)):
        iCol = -iCol

    # filter in case of input is zero
    if((iRow == 0) or (iCol == 0)):
        print("Entered input is zero.Please provide valid input.")
        return    

    if(iRow!=iCol):   
        print("provided no. of rows and no. of columns are not equal.Provide valid inputs for square.")
        return 

    #loop to print pattern
    for iCnt1 in range(iRow):
        for iCnt2 in range(iCol):
            if(iCnt1 == iCnt2):
                print("$",end = "\t")  
            else:
                print("*",end = "\t")    
        print()        

    print() 


###############################################################################

# Function name: hashStarOneByOneRowBox()
# Input:         Integer,Integer
# Output:        -
# Description:   It is used to display hash-star-OneByOneRow-Box pattern on console
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

def hashStarOneByOneRowBox(iRow,iCol):

    # filter in case of input is zero
    if((iRow == 0) or (iCol == 0)):
        print("Entered input is zero.Please provide valid input.")
        return    

    # updater in case of input is negative number
    if((iRow < 0)):
        iRow = -iRow

    if((iCol < 0)):
        iCol = -iCol    

    #loop to print pattern
    for iCnt1 in range(iRow):
        for iCnt2 in range(iCol):
            if((iCnt1+1) % 2 == 0):
                print("*",end = "\t")        
            else:
                print("#",end = "\t")    
        print()        

    print() 


###############################################################################

# Function name: dlrDiagStrLtHshUtSq()
# Input:         Integer,Integer
# Output:        -
# Description:   It is used to display dollar-Diagonal-StarLowerTriangle-
#                HashUpperTriangle-Box pattern on console
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

def dlrDiagStrLtHshUtSq(iRow,iCol):

    # updater in case of input is negative number
    if((iRow < 0)):
        iRow = -iRow

    if((iCol < 0)):
        iCol = -iCol 

    # filter in case of input is zero
    if((iRow == 0) or (iCol == 0)):
        print("Entered input is zero.Please provide valid input.")
        return    

    if(iRow!=iCol):   
        print("provided no. of rows and no. of columns are not equal.Provide valid inputs for square.")
        return 

    #loop to print pattern
    for iCnt1 in range(iRow):
        for iCnt2 in range(iCol):
            if(iCnt1 == iCnt2):
                print("$",end="\t")        
            elif(iCnt1 > iCnt2):
                print("*",end = "\t")    
            else:     
                print("#",end = "\t")
        print() 

    print()


###############################################################################

# Function name: starLeftDownSideRightAngledTriangle()
# Input:         Integer,Integer
# Output:        -
# Description:   It is used to display dollar-Diagonal-StarLowerTriangle-
#                HashUpperTriangle-Box pattern on console
# Author:        Aishwarya Sunil Karande
# Date:          09/05/2022

###############################################################################

def starLeftDownSideRightAngledTriangle(iRow,iCol):

    # updater in case of input is negative number
    if((iRow < 0)):
        iRow = -iRow

    if((iCol < 0)):
        iCol = -iCol 

    # filter in case of input is zero
    if((iRow == 0) or (iCol == 0)):
        print("Entered input is zero.Please provide valid input.")
        return    

    if(iRow!=iCol):   
        print("Please provide both inputs equal number for right angled trianle.")
        return 

    #loop to print pattern
    for iCnt1 in range(iRow):
        for iCnt2 in range(iCol):
            if(iCnt2<=iCnt1):
                print("*",end="\t")
            else:
                break
        print()   

    print()
