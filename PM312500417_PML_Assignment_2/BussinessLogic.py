def hello():

    str = "Hello"
    return str

def chkNumEvenOdd(no): 

    if(no < 0):
        no = -no

    if((no%2)==0):
        return True
    else:
        return False    

def addInt(no1,no2):
    
    ans = 0
    ans = no1 + no2
    return ans 

def subInt(no1,no2):
    
    ans = 0
    ans = no1 - no2
    return ans 

def multInt(no1,no2):
    
    ans = 0
    ans = no1 * no2
    return ans 

def divInt(no1,no2):
    
    if(no2 == 0):
        return False
    ans = 0
    ans = no1 / no2
    return ans                

def displayMarvellous(no):

    if(no < 0):
        no = -no

    cnt = 0
    
    for cnt in range(no):
        print("Marvellous")
    
    cnt = None

def displayIntReverse(no):
    
    if(no > 0):
        cnt = no

        for cnt in range(no,0,-1):       
            print(cnt,end = " ")
    elif(no < 0):
        cnt = no

        for cnt in range(no,0,1):       
            print(cnt,end = " ")        

    cnt = None

def chkIntType(no):

    if(no == 0):    
        return 0
    elif(no < 0):
        return -1
    elif(no > 0):
        return 1        

def chkIntDivisibleByFive(no):
    
    if((no%5)==0):
        return True
    elif((no%5)!=0):    
        return False

def displayStar(no):

    if(no < 0):
        no = -no

    cnt = 0

    for cnt in range(no):
        print("*",end =" ") 

def displayEvenNum(no):

    if(no > 0):
        cnt  = 1
        temp = 2
        while(cnt<=no):
            if((temp%2)==0):
                print(temp,end=" ")
                cnt = cnt + 1
            temp = temp + 1
    elif(no < 0):
        cnt  = no
        temp = -2
        while(cnt < 0):
            if((temp%2)==0):
                print(temp,end=" ")
                cnt = cnt + 1
            temp = temp - 1  

def stringLenX(str):

    # return (len(str))

    cnt = 0
    s = None
    
    for s in str:
        cnt = cnt + 1

    return cnt

def displaySqPattern(no):

    if(no < 0):
        no = -no 

    cnt1 = 0
    cnt2 = 0
    for cnt1 in range(no):
        cnt2 = 0
        for cnt2 in range(no):
            print("*",end=" ") 
        print()       

def factorialInt(no):

    if(no < 0):
        no = -no

    cnt = 0
    fact = 1
    for cnt in range(no,0,-1):
        fact = fact*cnt
        
    return fact

def addFactorsInt(no):

    if(no < 0):
        no = -no

    cnt = 0
    sum = 0
    end = (int((no/2)+1))
  
    for cnt in range(1,end,1):
        if((no%cnt)==0):
            # print(cnt,end=" ")
            sum = sum + cnt
   
    sum = sum + no
    return sum;        

def chkPrime(no):
    
    if(no < 0):
        return False

    cnt = 0
    end = (int((no/2)+1))
    flag = True
    # print(end)
    for cnt in range(2,end):
        if((no%cnt)==0):
            flag = False
            break
    # print(cnt)
    if(flag == True):
        return True
    else:
        return False 


def displayLeftLowerRightAngleTrianle(no):
    
    if(no < 0):
        no = -no
        
    cnt1 = 0
    cnt2 = 0
    temp = no

    for cnt1 in range(no):
        cnt2 = 0
        for cnt2 in range(temp):
            print("*",end=" ")        
        temp = temp - 1 
        print()    

def displaySqNumPattern(no):

    if(no > 0):
        cnt1 = 0
        cnt2 = 0

        for cnt1 in range(no):
            # cnt2 = 1
            for cnt2 in range(1,(no+1),1):
                print(cnt2,end = " ")
            print()   
    elif(no < 0):
        cnt1 = 0
        cnt2 = 0

        for cnt1 in range(no,0,1):
            # cnt2 = 1
            for cnt2 in range(-1,(no-1),-1):
                print(cnt2,end = " ")
            print()

def displayLeftUpperRightAngleTrianle(no):

    if(no > 0):

        cnt1 = 0
        cnt2 = 0
        temp = 2

        for cnt1 in range(1,(no+1),1):
            for cnt2 in range(1,temp,1):                         
                print(cnt2,end=" ")
            temp = temp + 1     
            print()    
    elif(no < 0):

        cnt1 = 0
        cnt2 = 0
        temp = -2

        for cnt1 in range(no,0,1):
            for cnt2 in range(-1,temp,-1):                         
                print(cnt2,end=" ")
            temp = temp - 1     
            print() 

def countIntDigit(no):

    cnt = 0
    temp = no

    while(temp != 0):  
        cnt = cnt + 1
        temp = (int(temp / 10))

    return cnt     

def addDigitFromInt(no):

    sum = 0
    digit = 0
    temp = no

    if(temp < 0):
        temp = -temp

    while(temp != 0):
        digit = (int(temp % 10))
        print(digit)       
        sum = sum + digit
        temp = (int(temp / 10))
    
    if(no < 0):
        sum = -sum
        return sum
    else:    
        return sum    







        

      








    