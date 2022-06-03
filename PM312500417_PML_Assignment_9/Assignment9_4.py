# 4.Write a program which accept two file names from user and compare contents of both the
# files. If both the files contains same contents then display success otherwise display failure.Accept names of both the files from command line.
# Input : demo.txt data.txt
# Compare contents of demo.txt and data.txt

import filecmp
import sys
import os

def compareContent(fileName1,fileName2):
    if (os.path.isfile(fileName1) and os.path.isfile(fileName2)):
        fobj = filecmp.cmp(fileName1,fileName2,shallow=False)
        return fobj
    # else:
    #     return False    

def main():
    try:
        fileName1 = sys.argv[1]
        fileName2 = sys.argv[2]

        ret = compareContent(fileName1,fileName2)
        # if(ret == True):
        #     print("Contents are same in both files")
        # else:
        #     print("Contents are not same in both files")
        print(ret)

    except Exception as eobj:
        print("Exception occured : ",eobj)

if __name__ == "__main__":
    main()    