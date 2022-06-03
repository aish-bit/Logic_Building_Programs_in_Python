# 3.Design python application which creates two threads as evenlist and oddlist. Both the
# threads accept list of integers as parameter. Evenlist thread add all even elements
# from input list and display the addition. Oddlist thread add all odd elements from input
# list and display the addition.
import os
import threading

class Arithmetics:

    def __init__(self,data):
        self.list = data

    def addEvenList(self):
        sum = 0
        for cnt in range(len(self.list)):
            if((self.list[cnt]%2)==0):
                sum += self.list[cnt]
        print("PID is : {}  Addition of all even elements from list: {}".format(os.getpid(),sum))

    def addOddList(self):
        sum = 0
        for cnt in range(len(self.list)):
            if((self.list[cnt]%2)!=0):
                sum += self.list[cnt]
        print("PID is : {}  Addition of all odd elements from list: {}".format(os.getpid(),sum))    

def main():

    print("Parent of main(Terminal): ",os.getppid())
    print("PID of main: ",os.getpid())

    list = []

    size = int(input("Enter number of elements required in list: "))
    
    print("Enter elements: ")
    for cnt in range(size):
        no = int(input())
        list.append(no)
    
    aobj = Arithmetics(list)

    evenlist = threading.Thread(target =aobj.addEvenList)
    oddlist  = threading.Thread(target =aobj.addOddList)

    evenlist.start()
    oddlist.start()

    evenlist.join()
    oddlist.join()

    print("End of main")

if __name__ == "__main__":
    main()    