# 5. Accept file name and one string from user and return the frequency of that string from file.
# Input : Demo.txt Marvellous
# Search “Marvellous” in Demo.txt
import sys

def chkFreqStr(fileName,str):
    fd = open(fileName,"r")
    data = fd.read()
    occurrences = data.count(str)
    return occurrences

def main():
    try:
        fileName = sys.argv[1]
        str = sys.argv[2]

        ret = chkFreqStr(fileName,str)

        print("Freq of {} in {} is {}.".format(str,fileName,ret))
    except Exception as eobj:
        print("Exception occured : ",eobj)

if __name__ == "__main__":
    main()    