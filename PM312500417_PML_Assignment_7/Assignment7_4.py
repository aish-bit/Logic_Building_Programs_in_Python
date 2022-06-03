# 4.Write a recursive program which accept number from user and return summation of its digits.
# Input : 879
# Output : 24

def sumDigitsR(no):

    if(no == 0):
        return 0

    if(no != 0):
        return ((int(no%10))+sumDigitsR(int(no/10)))


def main():

    print("Please Enter number:")
    value = int(input())

    ret = sumDigitsR(value)

    print("Summation of digits of number",value,"are:",ret)


if __name__ == "__main__":
    main()    