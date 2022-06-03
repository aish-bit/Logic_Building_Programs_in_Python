# 3.Write a recursive program which display below pattern.
# Input : 5
# Output : 5 4 3 2 1

def displayLinearIntRevPatternR(no):

    if(no < 0):
        no = -no

    if(no > 0):
        print(no,end = " ")
        no = no - 1
        displayLinearIntRevPatternR(no)



def main():
    print("-:Program to display integer in Reverse Order Linear Pattern Single Row:-")
    print("Please Enter Frequency")
    value = int(input())

    displayLinearIntRevPatternR(value)


if __name__ == "__main__":
    main()    