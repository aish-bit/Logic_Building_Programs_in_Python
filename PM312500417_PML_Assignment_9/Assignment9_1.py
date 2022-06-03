# 1.Write a program which accepts file name from user and check whether that file exists in
# current directory or not.
# Input : Demo.txt
# Check whether Demo.txt exists or not.

import os 

def chkFileExist(fileName):
    if os.path.isfile(fileName):
        return True
    else:
        return False    


def main():

    fileName = input("Enter file name to check : ")
    try: 
        ret = chkFileExist(fileName)
        if(ret == True):
            print("File is exists")
        else:
            print("File is not exists")    
    except Exception as eobj:
        print("Exception occured : ",eobj)

if __name__ == "__main__":
    main()    