# Please follow below rules while designing automation script as
# • Accept input through command line or through file.
# • Display any message in log file instead of console.
# • For separate task define separate function.
# • For robustness handle every expected exception.
# • Perform validations before taking any action.
# • Create user defined modules to store the functionality.
# 1.Design automation script which accept directory name and file extension from user. 
# Display all files with that extension.
# Usage : DirectoryFileSearch.py “Assignment10_1” “.txt”
# Assignment10_1 is name of directory and .txt is the extension that we want to search.

import os 
from sys import argv
import datetime
import fnmatch
import csv

def createLogFile():
    current_time = str(datetime.datetime.now().strftime("%d_%m_%Y-%I.%M.%S_%p"))
    # print(current_time) 
    # print(type(current_time))   
    extension = ".csv"
    fileName = "logFile_" + current_time + extension
    # print(fileName)
    fd = open(fileName,"a",newline="")
    # fd.close() 
    return fd


def recordAllFileWithExt(directoryPath,fileExt):
    if os.path.isdir(directoryPath):
        #to get only files present in path
        # fileList = os.listdir(directoryPath)
        # for file in fileList:
        #     if fileExt not in file:
        #         fileList.remove(file)
        # print(fileList)
    ##########################################
        all_files = list()
        # all_dirs = list()
        # Iterate for each dict object in os.walk()
        for root, dirs, files in os.walk(directoryPath):
            # Add the files list to the the all_files list
            all_files.extend(files)
            # Add the dirs list to the all_dirs list
            # all_dirs.extend(dirs)
        # print(all_dirs)    
        fd = createLogFile()
        csvwriter = csv.writer(fd)
        csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Automation Script-------------------------"],
            ["Script name : ",argv[0]]
        ])
        fileList = list()
        for file in all_files:
            if file.endswith(fileExt):
                fileList.append(file)
        if(len(fileList) == 0):
            csvwriter.writerow(["There is no such file available with ",fileExt,"extension"])
            fd.close()
        else:
            csvwriter.writerow(["Files from directory and its sub directories with extension ",fileExt," is : "])         
            csvwriter.writerow(fileList)
            fd.close()
    else:
        fd = createLogFile()
        csvwriter = csv.writer(fd)  
        csvwriter.writerow(["Provided path is invalid","Recheck it","or contact developer"])   
        fd.close()

def main():
    
    if((len(argv)<2) or (len(argv)>3)):
        fd = createLogFile()
        csvwriter = csv.writer(fd)
        csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Automation Script-------------------------"],
            ["Script name : ",argv[0]]
        ])
        msgs = [
                    ["Invalid number of arguments"],
                    ["Use -u or -U flag for usage"],
                    ["Use -h or -H flag for help"],
                    ["use command : ","python Name_of_Script.py flag_name"]
                ]
        csvwriter.writerows(msgs)
        fd.close()
        exit()

    if(len(argv) == 2):
        fd = createLogFile()
        csvwriter = csv.writer(fd)
        csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Automation Script-------------------------"],
            ["Script name : ",argv[0]]
        ])
        if (argv[1] == "-u" or argv[1] == "-U"):
            csvwriter.writerows([
            ["Usage : Script accepts directory path and file extension from user. And create log file which shows all files with that extension"]
                               ]) 
            exit()

        elif((argv[1] == "-h") or (argv[1] == "-H")):   
            csvwriter.writerows([
                    ["Help : python Name_of_Script.py First_Argument Second_argument"],
                    ["First_Argument : Directory path which is continuous string"],
                    ["Second_Argument : extension of file (including '.' eg.(.txt)) which is continuous string"]
            ]) 
            exit()
        else:
            csvwriter.writerows([["There is no such flag"]])
            exit()

    if(len(argv) == 3):
        directoryPath = argv[1]
        fileExt = argv[2]
        recordAllFileWithExt(directoryPath,fileExt)  
        exit()

if __name__ == "__main__":
    main()     









