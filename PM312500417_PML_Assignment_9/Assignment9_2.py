# 2. Write a program which accept file name from user and open that file and display the contents of that file on screen.
# Input : Demo.txt
# Display contents of Demo.txt on console.

import os 

def displayContent(fileName):
    if(os.path.isfile(fileName)):
        fd = open(fileName,"r")
        data  = fd.read()
        print(data)
        fd.close()
        return True
    else:
        return False    


def main():

    fileName = input("Enter file name to read : ")
    try: 
        ret = displayContent(fileName)
        if(ret == True):
            print("File get read successfully!!!")
        else:
            print("There is no such file exixts")    
    except Exception as eobj:
        print("Exception occured : ",eobj)

if __name__ == "__main__":
    main()    