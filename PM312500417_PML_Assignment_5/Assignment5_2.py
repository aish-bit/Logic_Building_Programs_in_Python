# 2. Write a program which contains one class named as Circle.
# Circle class contains three instance variables as Radius ,Area, Circumference.
# That class contains one class variable as PI which is initialise to 3.14.
# Inside init method initialise all instance variables to 0.0.
# There are three instance methods inside class as Accept(), CalculateArea(),
# CalculateCircumference(), Display().
# Accept method will accept value of Radius from user.
# CalculateArea() method will calculate area of circle and store it into instance variable Area.
# CalculateCircumference() method will calculate circumference of circle and store it into instance variable Circumference.
# And Display() method will display value of all the instance variables as Radius , Area,Circumference.
# After designing the above class call all instance methods by creating multiple objects.

class Circle:

    PI = 3.142 #class variable

    def __init__(self): #constructor
        self.Radius = 0.0  #instance variable
        self.Area = 0.0  #instance variable
        self.Circumference = 0.0  #instance variable

    def accept(self):
        print("Please enter radius of circle:")
        self.Radius = float(input())

    def calculateArea(self):
        self.Area = (Circle.PI * self.Radius**2)

    def calculateCircumference(self):
        self.Circumference = (2 * Circle.PI * self.Radius)

    def display(self):   
        print("Radius of circle is:",self.Radius)
        print("Area of circle is:",self.Area)
        print("Circumference of circle is:",self.Circumference)

def main():

    cobj1 = Circle()
    cobj1.accept()
    cobj1.calculateArea()
    cobj1.calculateCircumference()
    cobj1.display()

    cobj2 = Circle()
    cobj2.accept()
    cobj2.calculateArea()
    cobj2.calculateCircumference()
    cobj2.display()


if __name__ == "__main__":
    main()    
