# 3.Write a program which accept file name from user and create new file named as Demo.txt 
# and copy all contents from existing file into new file. Accept file name through command line
# arguments.
# Input : data.txt
# Create new file as Demo.txt and copy contents of data.txt in Demo.txt

import os 
import sys
import shutil

def createFile(fileName):
    if os.path.isfile(fileName):
        return False
    else:    
        fd = open(fileName,"x")
        fd.close()
        return True

def copyContent(fileName):
    if os.path.isfile('data.txt'):
        shutil.copyfile('data.txt',fileName)
        return True
    else:
        return False    

def main():
    try:
        fileName = sys.argv[1]
     
        ret = createFile(fileName)
        if(ret == True):

            print("File gets successfully created!!!")
        else:
            print("File with this name is already exists")  

        ret = copyContent(fileName)
        if(ret == True):

            print("Contents get copied successfully from one file to another file!!!")
        else:
            print("There is some issue.Contents not get copied from one file to another file.Or check whether there is file containing data is present or not")

    except Exception as eobj:
        print("Exception occured : ",eobj)

        
if __name__ == "__main__":
    main()    