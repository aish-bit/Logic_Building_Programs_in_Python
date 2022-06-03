# Please follow below rules while designing automation script as
# • Accept input through command line or through file.
# • Display any message in log file instead of console.
# • For separate task define separate function.
# • For robustness handle every expected exception.
# • Perform validations before taking any action.
# • Create user defined modules to store the functionality.
# 1.Design automation script which accept directory name and display checksum of all files.
# Usage : DirectoryChecksum.py “Demo”
# Demo is name of directory.

import os 
from sys import argv
import datetime
import csv
import hashlib

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

def hashOfFile(fname,blockSize = 1024):
    md5_hash = hashlib.md5() #to create an MD5 hash object
    fd = open(fname, "rb") #to read file in binary mode
    buffer = fd.read(blockSize)
    while((len(buffer)) > 0):
        md5_hash.update(buffer) #to update its contents with the file contents 
        buffer = fd.read(blockSize)
    hash = md5_hash.hexdigest() #save the hash into a hexadecimal string
    fd.close()
    return hash

def createFilePathList(directoryPath):
    flag = os.path.isabs(directoryPath)
    if flag == False:
        path = os.path.abspath(directoryPath)

    if os.path.isdir(directoryPath):
        fileList = list()
        for (root,dirs,files) in os.walk(directoryPath, topdown=True):
            # print(root)            
            # print(dirs)
            # print(files)
            # print("--------------------------")
            for fileName in files:
                # if fileName.endswith(fileExt1):
                completeName = os.path.join(root,fileName)
                fileList.append(completeName)  
        return fileList 
    else:
        fd = createLogFile()
        csvwriter = csv.writer(fd)  
        fd = createLogFile()
        csvwriter = csv.writer(fd)
        csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Automation Script-------------------------"],
            ["Script name : ",argv[0]]
        ])
        csvwriter.writerow(["Provided path is invalid","Recheck it","or contact developer"])   
        fd.close()    
        exit()    

    
def displayChecksumFile(directoryPath):
    fileList = createFilePathList(directoryPath)
    fd = createLogFile()
    csvwriter = csv.writer(fd)
    csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Automation Script-------------------------"],
            ["Script name : ",argv[0]]
        ])
        
    if(len(fileList) == 0):
        csvwriter.writerow(["There is no any file available at ",directoryPath," path"])
        fileList = None
        fd.close()
    else:
        csvwriter.writerow(["Checksum of files :  "])
        # fileChecksum = dict()
        # hasherList = list()
        for fname in fileList:
            hasher = hashOfFile(fname)
            # fileChecksum[hasher] = fname 
            # hasherList.append(hasher)
            csvwriter.writerow(["Checksum of ",fname," is : ",hasher]) 
        ###################################################################
        # something wrong:
        # for hash in hasherList:
        #     # for fname in fileList:
        #         fileChecksum.setdefault(hash, [])
        #         # .append(fname)     
        # print(fileChecksum)
        # print(hasherList)
        ###################################################################
        fd.close()



def main():
    # if((len(argv)<2) or (len(argv)>2)):
    if(len(argv) != 2):
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


    # if(len(argv) == 2):
        
    if (argv[1] == "-u" or argv[1] == "-U"):
        fd = createLogFile()
        csvwriter = csv.writer(fd)
        csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Automation Script-------------------------"],
            ["Script name : ",argv[0]]
        ])
        csvwriter.writerows([
            ["Usage : Script accepts directory path from user. And create log file which shows checksum of all files from whole directory tree"]
                               ]) 
        fd.close()                   
        exit()

    elif((argv[1] == "-h") or (argv[1] == "-H")):  
        fd = createLogFile()
        csvwriter = csv.writer(fd)
        csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Automation Script-------------------------"],
            ["Script name : ",argv[0]]
        ]) 
        csvwriter.writerows([
                    ["Help : python Name_of_Script.py First_Argument"],
                    ["First_Argument : Directory absolute path"]
            ]) 
        fd.close() 
        exit()

    else:
        # csvwriter.writerows([["There is no such flag"]])
        # exit()
        try:
            # if(len(argv) == 2):
            directoryPath = argv[1]
            displayChecksumFile(directoryPath)  
            exit()
        except Exception as eobj:
            fd = createLogFile()
            csvwriter = csv.writer(fd)
            csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Automation Script-------------------------"],
            ["Script name : ",argv[0]]
        ]) 
            csvwriter.writerow([["Exception occured : ",eobj]])
            fd.close()
            exit()

if __name__ == "__main__":
    main()     








