# Please follow below rules while designing automation script as
# • Accept input through command line or through file.
# • Display any message in log file instead of console.
# • For separate task define separate function.
# • For robustness handle every expected exception.
# • Perform validations before taking any action.
# • Create user defined modules to store the functionality.

# 2. Design automation script which accept directory name and two file extensions from user.
# Rename all files of first file extension with the second file extension.
# Usage : DirectoryRename.py “Demo” “.txt” “.doc”
# Demo is name of directory and .txt is the extension that we want to search and rename
# with .doc.
# After execution this script each .txt file gets renamed as .doc.

import os 
from sys import argv
import datetime
import fnmatch
import csv
from pathlib import Path


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

def renameAllFileWithExt(directoryPath,fileExt1,fileExt2):
    fd = createLogFile()
    csvwriter = csv.writer(fd)
    csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Automation Script-------------------------"],
            ["Script name : ",argv[0]]
                            ])
    if os.path.isdir(directoryPath):
        #to get only files present in top directory path 
        # fileList = os.listdir(directoryPath)
        # for file in fileList:
        #     if fileExt1 not in file:
        #         fileList.remove(file)
        # print(fileList)
    ##########################################
        
        fileList = list()
        for (root,dirs,files) in os.walk(directoryPath, topdown=True):
            # print(root)            
            # print(dirs)
            # print(files)
            # print("--------------------------")
            for fileName in files:
                if fileName.endswith(fileExt1):
                    completeName = os.path.join(root,fileName)
                    fileList.append(completeName)
        
        if(len(fileList) == 0):
            csvwriter.writerow(["There is no such file available with ",fileExt1,"extension"])
            fd.close()
        else:
            csvwriter.writerow(["Files from directory and its sub directories with existing extension ",fileExt1," : "])         
            csvwriter.writerow(fileList)
            ######################################################################
            csvwriter.writerow(["Files from directory and its sub directories with new changed extension ",fileExt2," : "]) 
            ##############Only renames top dir files and not subdir##############
            # files = os.listdir(directoryPath)
            # # files = os.listdir(os.curdir)
            # # print(files)
            # newFileList = list()
            # for fi in files:
            #     if fi.endswith(fileExt1):
            #         completeName = os.path.join(directoryPath,fi)
            #         newfile = completeName.replace(fileExt1,fileExt2)
            #         os.rename(completeName, newfile)
            #         newFileList.append(newfile)
            # csvwriter.writerow(newFileList)        
            ######################################################################
            ##############Only renames top dir files and not subdir##############
            # for path in Path(directoryPath).iterdir():
            #     if path.is_file():
            #         old_name = path.stem #original filename
            #         old_extension = path.suffix #original file extension
            #         directory = path.parent #current file location
            #         if (old_extension == fileExt1):
            #             new_name = old_name + fileExt2
            #             path.rename(Path(directory, new_name)) #rename `path` to `new_name`
            ######################################################################
            ##############renamed thru all files in top and sub dir##############
            newFileList = list()
            for (root,dirs,files) in os.walk(directoryPath, topdown=True):
                # print(root)            
                # print(dirs)
                # print(files)
                # print("--------------------------")
                for fileName in files:
                    if fileName.endswith(fileExt1):
                        completeName = os.path.join(root,fileName)
                        newfile = completeName.replace(fileExt1,fileExt2)
                        os.rename(completeName, newfile)
                        newFileList.append(newfile)
            csvwriter.writerow(newFileList)    
                
            ###################################################################### 
            fd.close()
    else:
          
        csvwriter.writerow(["Provided path is invalid","Recheck it","or contact developer"])   
        fd.close()

def main():
    
    if((len(argv)<2) or (len(argv)>4) or (len(argv) == 3)):
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
                    ["use command : ","python Name_of_Script.py -flag_name"]
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
            ["Usage : Script accepts from user directory path,file extension to find files which we want to rename and one another file extension to change that file's extension.It is used to create log file which shows all renamed files with that new extension"]
                               ]) 
            exit()

        elif((argv[1] == "-h") or (argv[1] == "-H")):   
            csvwriter.writerows([
                    ["Help : python Name_of_Script.py First_Argument Second_Argument Third_Argument"],
                    ["First_Argument : Directory path which is continuous string"],
                    ["Second_Argument : Extension of existing files (including '.' eg.(.txt))"],
                    ["Third_Argument : New extension of file (including '.' eg.(.docx))"]
            ]) 
            exit()
        else:
            csvwriter.writerows([["There is no such flag"]])
            exit()

    if(len(argv) == 4):
        directoryPath = argv[1]
        fileExt1 = argv[2]
        fileExt2 = argv[3]
        renameAllFileWithExt(directoryPath,fileExt1,fileExt2)  
        exit()

if __name__ == "__main__":
    main()     
