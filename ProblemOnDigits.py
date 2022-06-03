###############################################################################

# Function name: displayDigitsFromInt
# Input:         Integer
# Output:        List of Integers
# Description:   It is used to display digits from positive number
# Author:        Aishwarya Sunil Karande
# Date:          24/03/2022

###############################################################################

def displayDigitsFromInt(iNo):  
    
    # filter in case of input is zero
    if(iNo ==  0):
        return -1

    resultList = list()

    if(iNo < 0):
        iDigit = 0
        iNum   = -iNo
        # seperating each digit from list by iterating over integer
        while(iNum != 0):
        
            iDigit = -(iNum % 10)
            resultList.append(iDigit)
            iNum = int(iNum / 10)
    
    if(iNo > 0):
        iDigit = 0
        iNum   = iNo
        # seperating each digit from list by iterating over integer
        while(iNum != 0):
        
            iDigit = iNum % 10
        
            resultList.append(iDigit)
        
            # iNum = int(iNum / 10)
            iNum = iNum // 10
        

    # reversing result list
    resultList.reverse()

    # returning result
    return resultList


###############################################################################

# Function name: sumDigitsFromInt
# Input:         Integer
# Output:        Integer
# Description:   It is used to calculate addition of digits from integer
# Author:        Aishwarya Sunil Karande
# Date:          30/03/2022

###############################################################################

def sumDigitsFromInt(iNo):  
    
    # filter in case of input is zero
    if(iNo ==  0):
        return -1

    iSum   = 0
    iDigit = 0
    iNum   = iNo

    if(iNo < 0):
        iNum   = -iNo

        # seperating each digit from list by iterating over integer
        while(iNum != 0): 

            iDigit = -(iNum % 10)

            iSum   += iDigit

            iNum = int(iNum / 10)

            
    
    if(iNo > 0):

        # seperating each digit from list by iterating over integer
        while(iNum != 0):
        
            iDigit = iNum % 10
        
            iSum   += iDigit
        
            # iNum = int(iNum / 10)
            iNum = iNum // 10
    
    # returning result
    return iSum

###############################################################################

# Function name: countDigitsFromInt
# Input:         Integer
# Output:        Integer
# Description:   It is used to count digits from integer
# Author:        Aishwarya Sunil Karande
# Date:          30/03/2022

###############################################################################

def countDigitsFromInt(iNo):  
    
    # filter in case of input is zero
    if(iNo ==  0):
        return 1

    iNum   = iNo
    iCnt   = 0

    if(iNo < 0):
        iNum   = -iNo
       
    # seperating each digit from list by iterating over integer
    while(iNum != 0):

        iCnt += 1
        
        iNum = int(iNum / 10)
    
    # returning result
    return iCnt       


###############################################################################

# Function name: countEvenDigitsFromInt
# Input:         Integer
# Output:        Integer
# Description:   It is used to count even digits from integer
# Author:        Aishwarya Sunil Karande
# Date:          30/03/2022

###############################################################################

def countEvenDigitsFromInt(iNo):  
    
    # filter in case of input is zero
    if(iNo ==  0):
        return 1

    iDigit = 0
    iNum   = iNo
    iCnt   = 0

    if(iNo < 0):
        iNum   = -iNo
       
    # seperating each digit from list by iterating over integer
    while(iNum != 0):
        
        iDigit = iNum % 10

        if(iDigit % 2 == 0):
            iCnt += 1
        
        iNum = int(iNum / 10)
    
    # returning result
    return iCnt    


###############################################################################

# Function name: addEvenDigitsFromInt
# Input:         Integer
# Output:        Integer
# Description:   It is used to calculate addition of even digits from integer
# Author:        Aishwarya Sunil Karande
# Date:          30/03/2022

###############################################################################

def addEvenDigitsFromInt(iNo):  
    
    # filter in case of input is zero
    if(iNo ==  0):
        return -1

    iSum   = 0
    iDigit = 0
    iNum   = iNo

    if(iNo < 0):
        iNum   = -iNo

        # seperating each digit from list by iterating over integer
        while(iNum != 0): 

            iDigit = iNum % 10

            if(iDigit % 2 == 0):
                iSum   += (-iDigit)

            iNum = int(iNum / 10)
    
    if(iNo > 0):

        # seperating each digit from list by iterating over integer
        while(iNum != 0):
        
            iDigit = iNum % 10

            if(iDigit % 2 == 0):
                iSum   += iDigit
        
            iNum = int(iNum / 10)
    
    # returning result
    return iSum    


###############################################################################

# Function name: revDigitsFromInt
# Input:         Integer
# Output:        Integer
# Description:   It is used to reverse a given integer and form new reversed number
# Author:        Aishwarya Sunil Karande
# Date:          30/03/2022

###############################################################################

def revDigitsFromInt(iNo):  
    
    # filter in case of input is zero
    if(iNo ==  0):
        return -1

    iRev   = 0
    iDigit = 0
    iNum   = iNo

    if(iNo < 0):
        iNum   = -iNo

    # seperating each digit from list by iterating over integer
    while(iNum != 0): 

        iDigit = iNum % 10

        iRev   = (iRev * 10) + iDigit

        iNum   = int(iNum / 10)

    if(iNo < 0):
        iRev = -iRev
    
    # returning result
    return iRev


###############################################################################

# Function name: chkIntPalindrome
# Input:         Integer
# Output:        Boolean
# Description:   It is used to check provided integer is palindrome or not
# Author:        Aishwarya Sunil Karande
# Date:          30/03/2022

###############################################################################

def chkIntPalindrome(iNo):  
    
    # filter in case of input is zero
    if(iNo ==  0):
        return -1

    iRev   = 0
    iDigit = 0
    iNum   = iNo

    if(iNo < 0):
        iNum   = -iNo

    # seperating each digit from list by iterating over integer
    while(iNum != 0): 

        iDigit = iNum % 10

        iRev   = (iRev * 10) + iDigit

        iNum   = int(iNum / 10)

    if(iNo < 0):
        iRev = -iRev

    # returning result
    if(iRev == iNo):
        return True
    else:
        return False        

###############################################################################

# Function name: countDigitGreaterFive()   
# Input:         Integer
# Output:        Integer
# Description:   It is used to count digits which are greater than and equal to 5
# Author:        Aishwarya Sunil Karande
# Date:          08/05/2022

###############################################################################

def countDigitGreaterFive(iNo): 
    # Filter in case of input is zero
    if(iNo == 0):
        return -1

    # Initialising local variable
    iNum   = iNo
    iDigit = None
    iCount = 0

    # updater in case of number is negative
    if(iNo < 0):
        iNum = -iNo

    #loop to count number >= 5
    while(iNum != 0):
        iDigit = iNum % 10
        if(iDigit >= 5):
            iCount += 1
        iNum   = iNum // 10

    # returning result
    return iCount    


 