# 3. Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),Factors().
# ChkPrime() method will returns true if number is prime otherwise return false.
# ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method as a helper method if required.
# After designing the above class call all instance methods by creating multiple objects.

class Numbers:

    def __init__(self,value): #constructor
        self.no1 = value #instance variable
        if(self.no1 < 0):
            self.no1 = -self.no1
    
    def sumFactors(self): #instance method
        fact = 0
        temp = int(((self.no1)/2)+1)

        for cnt in range(1,temp):
            if((self.no1 % cnt)==0):
                fact = fact + cnt
        # fact = fact + self.no1    
        return fact

    def factors(self): #instance method
        print("Factors of number",self.no1,"is:")

        temp = int(((self.no1)/2)+1)

        for cnt in range(1,temp):
            if((self.no1 % cnt)==0):
                print(cnt,end = " ")
        print(self.no1)    
        print()

    def chkPerfect(self): #instance method
        perfect = 0
        perfect = self.sumFactors() #instance method call
        if(perfect == self.no1):
            return True
        else:
            return False 

    def chkPrime(self):  #instance method

        flag = True
        temp = int(((self.no1)/2)+1)

        for cnt in range(2,temp):
            if((self.no1 % cnt)==0):
                flag = False

        return flag  
        

def main():

    print("Please enter number:")
    value = int(input())

    nobj1 = Numbers(value)

    nobj1.factors()

    ret = 0

    ret = nobj1.sumFactors()
    print("Addition of all factors of number",value,"excluding itself is:",ret)

    ret = nobj1.chkPerfect()
    if(ret == True):
        print(value,"is a perfect number")
    elif(ret == False):
        print(value,"is not a perfect number")   

    ret = nobj1.chkPrime()
    if(ret == True):
        print(value,"is a prime number")
    elif(ret == False):
        print(value,"is not a prime number")        


if __name__ == "__main__":
    main()    
