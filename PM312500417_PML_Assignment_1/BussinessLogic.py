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






    