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

def createLogFile():
    current_time = str(datetime.datetime.now().strftime("%d_%m_%Y-%I.%M.%S_%p"))
    print(current_time) 
    print(type(current_time))   
    extension = ".csv"
    fileName = "logFile_" + current_time + extension
    print(fileName)
    fd = open(fileName,"a")
    fd.close() 

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
        all_dirs = list()
        # Iterate for each dict object in os.walk()
        for root, dirs, files in os.walk(directoryPath):
            # Add the files list to the the all_files list
            all_files.extend(files)
            # Add the dirs list to the all_dirs list
            # all_dirs.extend(dirs)
  
        print("All files from directory and its sub directories : ",all_files)
        # print(all_dirs)
        print("file with {} are : ".format(fileExt))
        for file in all_files:
            if file.endswith(fileExt):
                print(file)

def main():
    # try: 
    # createLogFile()
    # except Exception as eobj:
    #     print("Exception Occured : ",eobj)  
    directoryPath = argv[1]
    fileExt = argv[2]

    recordAllFileWithExt(directoryPath,fileExt)  

if __name__ == "__main__":
    main()     









