# 2. Write a recursive program which display below pattern.
# Input : 5
# Output : 1 2 3 4 5

def displayLinearIntRevPatternR(no):

    if(no >= 1):
        displayLinearIntRevPatternR(no - 1)
        print(no,end = " ")

def main():
    print("-:Program to display integer in Reverse Order Linear Pattern Single Row:-")
    print("Please Enter Frequency")
    value = int(input())

    displayLinearIntRevPatternR(value)


if __name__ == "__main__":
    main()    


