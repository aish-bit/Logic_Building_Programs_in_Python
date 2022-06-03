# 1.Design python application which creates two thread named as even and odd. Even
# thread will display first 10 even numbers and odd thread will display first 10 odd
# numbers.

import os
import threading

def DisplayEven(no):
    num = 0
    while(no > 0):
        if((num % 2 )==0):
            print("PID is : {}  Even number is : {}".format(os.getpid(),num))
            no = no - 1
            num = num + 1
        else:
            num = num + 1    

def DisplayOdd(no):
    num = 0
    while(no > 0):
        if((num % 2 )!=0):
            print("PID is : {}  Odd number is : {}".format(os.getpid(),num))
            no = no - 1
            num = num + 1
        else:
            num = num + 1
        

def main():

    print("Parent of main(Terminal): ",os.getppid())
    print("PID of main: ",os.getpid())
    value = 10
    thread1 = threading.Thread(target = DisplayEven,args = (value,))
    thread2 = threading.Thread(target = DisplayOdd,args = (value,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End of main")

if __name__ == "__main__":
    main()    