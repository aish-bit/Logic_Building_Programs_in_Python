# 1. Write a recursive program which display below pattern.
# Input : 5
# Output : * * * * *

def displayLinearStarR(no):

    if(no < 0):
        no = -no
        
    if(no > 0):
        print("*",end = " ")
        no = no - 1
        displayLinearStarR(no)


def main():
    print("-:Program to display stars in Linear Pattern Single Row:-")
    print("Please Enter Frequency")
    value = int(input())

    displayLinearStarR(value)


if __name__ == "__main__":
    main()    