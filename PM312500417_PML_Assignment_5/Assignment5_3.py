# 3. Write a program which contains one class named as Arithmetic.
# Arithmetic class contains two instance variables as Value1 ,Value2.
# Inside init method initialise all instance variables to 0.0
# There are three instance methods inside class as Accept(), Addition(), Subtraction(),Multiplication(), Division().
# Accept method will accept value of Value1 and Value2 from user.
# Addition() method will perform addition of Value1 ,Value2 and return result.
# Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
# Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
# Division() method will perform division of Value1 ,Value2 and return result.
# After designing the above class call all instance methods by creating multiple objects.

class Arithmetic:
    def __init__(self): #constructor
        self.no1 = 0.0  #instance variable
        self.no2 = 0.0  #instance variable

    def accept(self):
        print("Please enter first number:")
        self.no1 = float(input())
        print("Please enter second number:")
        self.no2 = float(input())

    def addition(self):
        ans = 0.0
        ans = self.no1 + self.no2
        return ans

    def substraction(self):
        ans = 0.0
        ans = self.no1 - self.no2
        return ans

    def multiplication(self):
        ans = 0.0
        ans = self.no1 * self.no2
        return ans

    def division(self):   
        ans = 0.0
        ans = self.no1 / self.no2
        return ans     

def main():

    aobj1 = Arithmetic()
    aobj2 = Arithmetic()
    ret = 0.0

    aobj1.accept()
    ret = aobj1.addition()
    print("Addition of two numbers is:",ret)
    ret = aobj1.substraction()
    print("Substraction of two numbers is:",ret)
    ret = aobj1.multiplication()
    print("Multiplication of two numbers is:",ret)
    ret = aobj1.division()
    print("Division of two numbers is:",ret)

    aobj2.accept()
    ret = aobj2.addition()
    print("Addition of two numbers is:",ret)
    ret = aobj2.substraction()
    print("Substraction of two numbers is:",ret)
    ret = aobj2.multiplication()
    print("Multiplication of two numbers is:",ret)
    ret = aobj2.division()
    print("Division of two numbers is:",ret)


if __name__ == "__main__":
    main()    
