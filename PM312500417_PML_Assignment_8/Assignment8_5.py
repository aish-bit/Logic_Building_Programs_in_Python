# 5.Design python application which contains two threads named as thread1 and thread2.
# Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
# screen. After execution of thread1 gets completed then schedule thread2.
import threading
import os

def displayNum(no,lock):
    lock.acquire()
    print("PID of displayNum is : {}  name is: {}".format(os.getpid(),threading.current_thread().name))
    for cnt in range(1,no+1,1):
        print(cnt,end = " ")
    print()
    lock.release()

def displayNumRev(no,lock):
    lock.acquire()
    print("PID of displayNumRev is : {}  name is: {}".format(os.getpid(),threading.current_thread().name))
    for cnt in range(50,0,-1):
        print(cnt,end = " ")
    print()
    lock.release()    

def main():
    
    print("Parent of main(Terminal): ",os.getppid())
    print("PID of main: {} Name of main thread is : {}".format(os.getpid(),threading.current_thread().name))

    lock = threading.Lock()

    thread1 = threading.Thread(target = displayNum,args = (50,lock,) )
    thread2 = threading.Thread(target = displayNumRev,args = (50,lock,) )

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join() 

if __name__ == "__main__":
    main()    