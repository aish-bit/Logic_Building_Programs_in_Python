# 1.Write a program which contains one class named as Demo.Demo class contains two instance variables as no1 ,no2.That class contains one class variable as Value.There are two instance methods of class as Fun and Gun which displays values of instance variables.Initialise instance variable in init method by accepting the values from user.

# After creating the class create the two objects of Demo class as
# Obj1 = Demo(11,21)
# Obj2 = Demo(51,101)
# Now call the instance methods as
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()

class Demo:

    Value = 51 #class variable

    def __init__(self,value1,value2): #constructor
        self.no1 = value1  #instance variable
        self.no2 = value2  #instance variable

    def fun(self): #instance method
        print("Inside fun values of instance variable no1 and no2 are:")    
        print("Value of no1:",self.no1)
        print("Value of no2:",self.no2)

    def gun(self): #instance method
        print("Inside gun values of instance variable no1 and no2 are:")    
        print("Value of no1:",self.no1)
        print("Value of no2:",self.no2)    


def main():

    print("Please enter first value for dobj1:")
    value1 = int(input())

    print("Please enter second value for dobj1:")
    value2 = int(input())

    dobj1 =  Demo(value1,value2)

    print("Please enter first value for dobj2:")
    value1 = int(input())

    print("Please enter second value for dobj2:")
    value2 = int(input()) 

    dobj2 =  Demo(value1,value2)
    
    dobj1.fun()
    dobj2.fun()
    dobj1.gun()
    dobj2.gun()

if __name__ == "__main__":
    main()    
