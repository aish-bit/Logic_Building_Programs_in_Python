###############################################################################

# Function name: displayOnetoFive()
# Input:         -
# Output:        -
# Description:   It is used to display 1 to 5 on screen
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

def displayOnetoFive():  
    
    # loop to print 1 to 5 on screen
    for iCnt in range(5):
        print(iCnt+1,end=" ")

    print()    


###############################################################################

# Function name: displayFiveTimesMarvellous()
# Input:         -
# Output:        -
# Description:   It is used to display 5 times Marvellous on Screen
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

def displayFiveTimesMarvellous():  
    
    str = "Marvellous"

    # loop to print Marvellous on screen
    for iCnt in range(5):
        print(str)
     

###############################################################################

# Function name: displayMarvellous()
# Input:         Integer
# Output:        -
# Description:   It is used to display n times Marvellous on Screen
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

def displayMarvellous(iNo):  
    #filter in case of provided input is zero
    if(iNo == 0):
        print("Entered input is zero.Please provide valid input.")
        return

    #updater in case of provided input is negative integer
    if(iNo < 0):
        iNo = -iNo    

    str = "Marvellous"

    # loop to print Marvellous on screen
    for iCnt in range(iNo):
        print(str)
    

###############################################################################

# Function name: displayUptoNInt()
# Input:         Integer
# Output:        -
# Description:   It is used to display n times integers on Screen
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

def displayUptoNInt(iNo):  
    # Filter in case of provided input is zero
    if(iNo == 0):
        print("Entered input is zero.Please provide valid input.")
        return

    # In case of provided input is negative integer
    if(iNo < 0):

    #     for iCnt in range(-1,iNo-1,-1):
    #         print(iCnt,end = " ")    

        iCnt = -1

        while(iCnt >= iNo):
            print(iCnt,end = " ")   
            iCnt -= 1

        print()    

    # In case of provided input is positive integer
    for iCnt in range(1,iNo+1,1):
        print(iCnt,end = " ")

    print()    


###############################################################################

# Function name: displayUptoNPositiveInt()
# Input:         Integer
# Output:        -
# Description:   It is used to display n times positive integers on Screen
# Author:        Aishwarya Sunil Karande
# Date:          21/03/2022

###############################################################################

def displayUptoNPositiveInt(iNo):  
    # Filter in case of provided input is zero
    if(iNo == 0):
        print("Entered input is zero.Please provide valid input.")
        return

    # Filter in case of provided input is negative integer
    if(iNo < 0):

        iNo = -iNo    

    # loop to display integers on console
    for iCnt in range(1,iNo+1,1):
        print(iCnt,end = " ")

    print() 


###############################################################################

# Function name: displayUptoNRev()
# Input:         Integer
# Output:        -
# Description:   It is used to display n times integers in reverse on console
# Author:        Aishwarya Sunil Karande
# Date:          22/03/2022

###############################################################################

def displayUptoNRev(iNo):  
    # Filter in case of provided input is zero
    if(iNo == 0):
        print("Entered input is zero.Please provide valid input.")
        return

    # In case of provided input is negative integer
    if(iNo < 0):

    #     for iCnt in range(iNo,0,1):
    #         print(iCnt,end = " ")    

        iCnt = iNo

        while(iCnt <= -1):
            print(iCnt,end = " ")   
            iCnt += 1

        print()    

    # In case of provided input is positive integer
    for iCnt in range(iNo,0,-1):
        print(iCnt,end = " ")

    print()    


###############################################################################

# Function name: displayUptoNPositiveIntRev()
# Input:         Integer
# Output:        -
# Description:   It is used to display integers upto n'th positive
#                integer in reverse on console
# Author:        Aishwarya Sunil Karande
# Date:          22/03/2022

###############################################################################

def displayUptoNPositiveIntRev(iNo):  
    # Filter in case of provided input is zero
    if(iNo == 0):
        print("Entered input is zero.Please provide valid input.")
        return

    # Filter in case of provided input is negative integer
    if(iNo < 0):

        iNo = -iNo   

    # Display numbers in loop in case of provided input is positive integer
    for iCnt in range(iNo,0,-1):
        print(iCnt,end = " ")

    print()    


###############################################################################

# Function name: addAllNumUptoN()
# Input:         Integer,Float,Double
# Output:        Integer,Float,Double
# Description:   It is used to add all numbers upto provided n'th number
# Author:        Aishwarya Sunil Karande
# Date:          22/03/2022

###############################################################################

def addAllNumUptoN(iNo):  
    # Filter in case of provided input is zero
    if(iNo == 0):
        return "error"

    
    iCnt = None
    iCnt = iNo
    iSum = 0

    # If provided input is negative number
    if(iNo < 0):

        while(iCnt < 0):
            iSum += iCnt
            iCnt += 1

    # If provided input is positive number
    if(iNo > 0):

        while(iCnt > 0):
            iSum += iCnt
            iCnt -= 1

    # returning result

    return iSum


###############################################################################

# Function name: addAllPositiveNumUptoN()
# Input:         Integer,Float,Double
# Output:        Integer,Float,Double
# Description:   It is used to add all positive numbers upto provided n'th number
# Author:        Aishwarya Sunil Karande
# Date:          22/03/2022

###############################################################################

def addAllPositiveNumUptoN(iNo):  
    # Filter in case of provided input is zero
    if(iNo == 0):
        return "error"

    # Updater in case of provided input is negative number
    if(iNo < 0):

        iNo = -iNo

    iCnt = None
    iCnt = iNo
    iSum = 0

    while(iCnt > 0):
        iSum += iCnt
        iCnt -= 1

    # returning result
    return iSum


###############################################################################

# Function name: factorialOfInt()
# Input:         Integer
# Output:        Integer
# Description:   It is used to calculate factorial of number
# Author:        Aishwarya Sunil Karande
# Date:          22/03/2022

###############################################################################

def factorialOfInt(iNo):  
  
    # Updater in case of provided input is negative number
    if(iNo < 0):

        iNo = -iNo

    iCnt = None
    iCnt = iNo
    iFact = 1

    while(iCnt > 0):
        iFact *= iCnt
        iCnt -= 1

    # returning result
    return iFact


###############################################################################

# Function name: chkEvnOddInt()
# Input:         Integer
# Output:        Boolean
# Description:   It is used to check even odd parity of integer
# Author:        Aishwarya Sunil Karande
# Date:          22/03/2022

###############################################################################

def chkEvnOddInt(iNo):  
  
    # Updater in case of provided input is negative number
    if(iNo < 0):

        iNo = -iNo

    iFlag = False

    if(iNo % 2 == 0):
        iFlag = True

    # returning result
    return iFlag    


###############################################################################

# Function name: findFactorsInt()
# Input:         Integer
# Output:        list
# Description:   It is used to find factors of provided integer
# Author:        Aishwarya Sunil Karande
# Date:          22/03/2022

###############################################################################

def findFactorsInt(iNo):  
    # Filter in case of provided input is zero
    if(iNo == 0):
        return -1

    # Updater in case of provided input is negative number
    if(iNo < 0):

        iNo = -iNo

    iFactorList = list()

    # looping to find factors of provided integer
    for iCnt in range(1,(int(iNo/2)+1),1):
        if(iNo % iCnt == 0):
            iFactorList.append(iCnt)

    iFactorList.append(iNo)        

    # returning result
    return iFactorList


###############################################################################

# Function name: chkIntPerfect()
# Input:         Integer
# Output:        Boolean
# Description:   It is used to check whether number is perfect or not
# Author:        Aishwarya Sunil Karande
# Date:          31/03/2022

###############################################################################

def  chkIntPerfect(iNo):  
    # Filter in case of provided input is zero
    if(iNo == 0):
        return -1

    # Updater in case of provided input is negative number
    if(iNo < 0):

        iNo = -iNo

    iFactorList = list()
    iSum = 0

    # looping to find factors of provided integer
    for iCnt in range(1,(int(iNo/2)+1),1):
        if(iNo % iCnt == 0):
            iFactorList.append(iCnt)

    for factor in iFactorList:
        iSum += factor

    # returning result
    if(iNo == iSum):
        return True
    else:
        return False    


###############################################################################

# Function name: displayTable()
# Input:         Integer
# Output:        List
# Description:   It is used to display table of provided number
# Author:        Aishwarya Sunil Karande
# Date:          31/03/2022

###############################################################################

def  displayTable(iNo):  
    # Filter in case of provided input is zero
    if(iNo == 0):
        return -1

    # Updater in case of provided input is negative number
    if(iNo < 0):

        iNo = -iNo

    iTable = list()

    # looping to create table of provided integer
    for iCnt in range(1,11,1):
        iTable.append(iCnt*iNo)

    # returning result
    return iTable 


###############################################################################

# Function name: powerOfInt()
# Input:         Integer
# Output:        Integer
# Description:   It is used to calculate power of integer
# Author:        Aishwarya Sunil Karande
# Date:          31/03/2022

###############################################################################

def  powerOfInt(iNo1,iNo2):  
    # Filter in case of both provided inputs are zero
    if((iNo1 == 0) and (iNo2 == 0)):
        return -1

    # Filter in case if iNo2 power is zero
    if(iNo2 ==0):
        return 1
    

    iPower = None

    # if(iNo1 > 0):
    #     iPower = iNo1 ** iNo2

    # if(iNo1 < 0):
    #     if(iNo2 % 2 == 0):
    #         iPower = (iNo1 ** iNo2)  
    #     else:
    #         iPower =  iNo1 ** iNo2     
    iPower = iNo1 ** iNo2
    
    # returning result
    return iPower


###############################################################################

# Function name: averageOfThreeNumb()
# Input:         Integer/Float/Double
# Output:        Integer/Float/Double
# Description:   It is used to calculate average of three numbers
# Author:        Aishwarya Sunil Karande
# Date:          31/03/2022

###############################################################################

def  averageOfThreeNumb(iNo1,iNo2,iNo3):  
    # Filter in case of all provided inputs are zero
    if((iNo1 == 0) and (iNo2 == 0) and (iNo3 == 0)):
        return "error"

    # Creating local variable
    iAvg = None

    iAvg = ((iNo1 + iNo2 + iNo3)/3)

    # returning result
    return iAvg


###############################################################################

# Function name: smallNumb()
# Input:         Integer/Float/Double
# Output:        Integer/Float/Double
# Description:   It is used to show smallest number from provided 2 numbers
# Author:        Aishwarya Sunil Karande
# Date:          31/03/2022

###############################################################################

def  smallNumb(iNo1,iNo2):  
    # Filter in case of all provided inputs are zero
    if((iNo1 == 0) and (iNo2 == 0)):
        return "error"

    if(iNo1 > iNo2):
        return iNo2
    elif(iNo1 < iNo2):
        return iNo1  
    elif(iNo1 == iNo2):
        return "equal"      
