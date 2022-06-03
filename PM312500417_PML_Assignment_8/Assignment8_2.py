# 2.Design python application which creates two threads as evenfactor and oddfactor.
# Both the thread accept one parameter as integer. Evenfactor thread will display
# addition of even factors of given number and oddfactor will display addition of odd
# factors of given number. After execution of both the thread gets completed main
# thread should display message as “exit from main”.

import os
import threading

def sumEvenFactors(no):
    if(no < 0):
        no = -no

    if((no % 2) == 0):
        sum = no
    else:
        sum = 0   
        
    for cnt in range(1,((int(no/2))+1),1):
        if((no % cnt)==0):
            if((cnt % 2)==0):
                sum = sum + cnt

    print("PID is : {}  Sum of even factors of {} is : {}".format(os.getpid(),no,sum))
         
def sumOddFactors(no):
    if(no < 0):
        no = -no

    if((no % 2) != 0):
        sum = no
    else:
        sum = 0    

    for cnt in range(1,((int(no/2))+1),1):
        if((no % cnt)==0):
            if((cnt % 2)!=0):
                sum = sum + cnt

    print("PID is : {}  Sum of odd factors of {} is : {}".format(os.getpid(),no,sum))

def main():

    print("Parent of main(Terminal): ",os.getppid())
    print("PID of main: ",os.getpid())

    value = int(input("Please enter number: "))
    evenfactor = threading.Thread(target =sumEvenFactors,args =(value,))
    oddfactor  = threading.Thread(target =sumOddFactors,args =(value,))

    evenfactor.start()
    oddfactor.start()

    evenfactor.join()
    oddfactor.join()

    print("End of main")

if __name__ == "__main__":
    main()    

