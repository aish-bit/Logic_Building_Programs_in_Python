# 2. Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That class contains one class variable as ROI which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user.
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(),CalculateIntrest().
# Deposit() method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
# CalculateIntrest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI.
# And Display() method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects.

class BankAccount:
    __ROI = 10.5 #class variable

    def __init__(self,str): #constructor
        self.Name = str  #instance variable
        self.Amount = 0.0  #instance variable
    
    @classmethod
    def displayROI(cls):
        print("Rate of Interest of bank is:",cls.__ROI)

    def deposit(self,value): 
        self.Amount = self.Amount + value
        return True

    def withdraw(self,value):
        if(value <= self.Amount):
            self.Amount = self.Amount - value
            return True
        elif(value>self.Amount):
            print("Not sufficient balance available in account.Please enter amount less than entered value or first check amount available in your account")
            return False
        else:
            return False   
        
    def calculateIntrest(self):
        interest = 0.0
        interest = ((BankAccount.__ROI/100)*self.Amount)
        return interest

    def display(self):
        print("Dear user",self.Name,"Your current balance is:",self.Amount)

def main():
    # BankAccount.__ROI = 3.3 #error denar nhi pan badlun pan denar nhi which is neccessity
    
    name = None
    amount = 0.0
    ret = None

    print("Enter name of account holder:")
    name = input()

    bobj1 = BankAccount(name)

    print("Enter deposit amount:")
    amount = float(input())
    ret = bobj1.deposit(amount)
    if(ret == True):
        print("Amount",amount,"deposited successfully")
        bobj1.display() 
    else:
        print("Something went wrong!!!")
        print("Please try again...")    

    print("Enter amount to be withdrawn:")
    amount = float(input())
    ret = bobj1.withdraw(amount)
    if(ret == True):
        print("Amount",amount,"successfully withdrawn")
        bobj1.display() 
    else:
        print("Something went wrong!!!")
        print("Please try again...")    


    BankAccount.displayROI()
    ret = bobj1.calculateIntrest()    
    print("Your current available balance is:",bobj1.Amount)
    print("interest amount is:",ret)
    print("Total amount after adding ROI is:",float(bobj1.Amount+ret))

if __name__ == "__main__":
    main()    
