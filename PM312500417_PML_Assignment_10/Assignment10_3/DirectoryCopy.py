# Please follow below rules while designing automation script as
# • Accept input through command line or through file.
# • Display any message in log file instead of console.
# • For separate task define separate function.
# • For robustness handle every expected exception.
# • Perform validations before taking any action.
# • Create user defined modules to store the functionality.

# 3. Design automation script which accept two directory names. Copy all files from first directory
# into second directory. Second directory should be created at run time.
# Usage : DirectoryCopy.py “Demo” “Temp”
# Demo is name of directory which is existing and contains files in it. We have to create new
# Directory as Temp and copy all files from Demo to Temp.

import os 
from sys import argv
import datetime
import csv
import shutil

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

def mkDir(NewDirectoryPath,NewDirectoryName):
    try:
        path = os.path.join(NewDirectoryPath,NewDirectoryName)
        os.mkdir(path)
        return path
    except Exception as eobj:
        fd = createLogFile()
        csvwriter = csv.writer(fd)
        csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Automation Script-------------------------"],
            ["Script name : ",argv[0]],
            ["Check the path provided by you or check may the directory already exists on given path or contact developer"],
            ["Exception occured during new directory making: ",eobj]
                            ])
        fd.close() 
        exit()                   


def copyDirectory(OldDirectoryPath,NewDirectoryPath,NewDirectoryName):
    fd = createLogFile()
    csvwriter = csv.writer(fd)
    csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Automation Script-------------------------"],
            ["Script name : ",argv[0]]
                            ])
    if os.path.isdir(OldDirectoryPath):
        ####################################################################
        # newPath = mkDir(NewDirectoryPath,NewDirectoryName)
        
        # fileList = list()
        # for (root,dirs,files) in os.walk(OldDirectoryPath, topdown=True):
        #     # print(root)            
        #     # print(dirs)
        #     # print(files)
        #     # print("--------------------------")
        #     for fileName in files:
        #         completeName = os.path.join(root,fileName)
        #         fileList.append(completeName)

        # for fname in fileList:
        #     shutil.copy2(fname,newPath)        
        ####################################################################
        destPath = os.path.join(NewDirectoryPath,NewDirectoryName)
        # Copy the content of source to destination 
        destination = shutil.copytree(OldDirectoryPath,destPath, copy_function = shutil.copy) 
        ####################################################################
        csvwriter.writerow([
            "All files get copied from ",OldDirectoryPath, " to ",destPath," successfully..!!!"
                            ])

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
            ["Usage : Script accepts two directories path and name from user respectively.Copy all files from first directory into second directory. Second directory should be created at run time."]
                               ]) 
            exit()

        elif((argv[1] == "-h") or (argv[1] == "-H")):   
            csvwriter.writerows([
                    ["Help : python Name_of_Script.py First_Argument Second_Argument Third_Argument"],
                    ["First_Argument : Directory path of existing directory"],
                    ["Second_Argument : Path where you want to create directory at run time))"],
                    ["Third_Argument : New directory name which you want to create))"]
            ]) 
            exit()
        else:
            csvwriter.writerows([["There is no such flag"]])
            exit()

    if(len(argv) == 4):
        OldDirectoryPath = argv[1]
        NewDirectoryPath = argv[2]
        NewDirectoryName = argv[3]
        copyDirectory(OldDirectoryPath,NewDirectoryPath,NewDirectoryName)  
        exit()

if __name__ == "__main__":
    main()     
