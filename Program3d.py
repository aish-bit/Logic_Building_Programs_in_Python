# Additon of two numbers
# POP way of programming- 4 (better than prvious three programs)
# but still not perfect yet

def addition(no1,no2):
    ans = 0
    ans = no1 + no2
    return ans

def main():

    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))

    ret = addition(value1,value2)

    print("Addition of two numbers is : ",ret)

if __name__ == "__main__":
    main()    