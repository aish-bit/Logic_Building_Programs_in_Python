# 4.Design python application which creates three threads as small, capital, digits. All 
# the threads accepts string as parameter. Small thread display number of small characters,
# capital thread display number of capital characters and digits thread display number of
# digits. Display id and name of each thread.

import threading
import os

class Demo:
    def __init__(self,str):
        self.str = str

    def countSmallChar(self):
        countSmall = 0
        for cnt in range(len(self.str)):
            if((self.str[cnt] <= 'z') and (self.str[cnt] >= 'a')):
                countSmall += 1
        print("PID is : {}  small characters in string : {}  Name of thread is : {}".format(os.getpid(),countSmall,threading.current_thread().name))

    def countCapitalChar(self):
        countCapital = 0
        for cnt in range(len(self.str)):
            if((self.str[cnt] <= 'Z') and (self.str[cnt] >= 'A')):
                countCapital += 1
        print("PID is : {}  capital characters in string : {}  Name of thread is : {}".format(os.getpid(),countCapital,threading.current_thread().name))      

    def countDigitChar(self):
        countDigit = 0
        for cnt in range(len(self.str)):
            if((self.str[cnt] < '9') and (self.str[cnt] > '0')):
                countDigit += 1
        print("PID is : {}  Digits in string : {} Name of thread is : {}".format(os.getpid(),countDigit,threading.current_thread().name))      

def main():
    print("Parent of main(Terminal): ",os.getppid())
    print("PID of main: {} Name of main thread is : {}".format(os.getpid(),threading.current_thread().name))

    str = input("Please enter string : ")

    dobj = Demo(str)

    small = threading.Thread(target =dobj.countSmallChar)
    capital = threading.Thread(target =dobj.countCapitalChar)
    digits = threading.Thread(target =dobj.countDigitChar)

    small.start()
    capital.start()
    digits.start()

    small.join()
    capital.join()
    digits.join()

    print("End of main")

if __name__ == "__main__":
    main()