# 5. Write a recursive program which accept number from user and return its factorial.
# Input : 5
# Output : 120 (5*4*3*2*1)

def factorialR(no):

    if(no == 0):
        return 1
        
    if(no > 0):
        return(no*factorialR(no-1))
   


def main():

    print("Please Enter number:")
    value = int(input())

    ret = factorialR(value)

    print("Factorial of number",value,"is:",ret)


if __name__ == "__main__":
    main()    