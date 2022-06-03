# Please follow below rules while designing automation script as
# • Accept input through command line or through file.
# • Display any message in log file instead of console.
# • For separate task define separate function.
# • For robustness handle every expected exception.
# • Perform validations before taking any action.
# • Create user defined modules to store the functionality.

# 4. Design automation script which accept directory name and delete all duplicate files from that directory. 
# Write names of duplicate files from that directory into log file named as Log.txt.
# Log.txt file should be created into current directory. Display execution time required for the script.
# Usage : DirectoryDuplicateRemovalTime.py “Demo”
# Demo is name of directory.

import os 
from sys import argv
import datetime
import csv
import hashlib
import time

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
                # print(type(fileName))
                completeName = os.path.join(root,fileName)
                # print(type(completeName))
                fileList.append(completeName)  
        # print(type(fileList[1]))    
        return fileList 
    else:
        fd = createLogFile()
        csvwriter = csv.writer(fd)  
        fd = createLogFile()
        csvwriter = csv.writer(fd)
        csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Duplicate File Automation Script-------------------------"],
            ["Script name : ",argv[0]]
        ])
        csvwriter.writerow(["Provided path is invalid","Recheck it","or contact developer"])   
        fd.close()    
        exit()    

    
def createFileHashList(directoryPath):
    fileList = createFilePathList(directoryPath)
    if(len(fileList) == 0):
        fd = createLogFile()
        csvwriter = csv.writer(fd)
        csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Duplicate File Automation Script-------------------------"],
            ["Script name : ",argv[0]]
        ])
        csvwriter.writerow(["There is no any file available at ",directoryPath," path"])
        fileList = None
        fd.close()
        exit()
    else:
        
        fileHashList = dict()
        # print(fileList)
        for fname in fileList:
            # print(type(fname))
            # print(type(os.path.basename(fname)))
            fileHash = hashOfFile(fname)

            if fileHash in fileHashList:
                # fileHashList[fileHash].append((os.path.basename(fname)))
                fileHashList[fileHash].append(fname)
            else:    
                # fileHashList[fileHash] = [os.path.basename(fname)]
                fileHashList[fileHash] = [fname]
        return fileHashList
###############################################################################
sortDup = lambda no1 :  len(no1) > 1
###############################################################################
def displayDupFile(directoryPath):
    dupFiles = createFileHashList(directoryPath) 
    fd = createLogFile()
    csvwriter = csv.writer(fd)
    csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Duplicate File Automation Script-------------------------"],
            ["Script name : ",argv[0]]
        ])
##################################Using Loop##################################    
    # cnt1 = 0
    # # cnt2 = 0
    # for key in dupFiles:
    #     cnt1 = 0
    #     # cnt2 = 0
    #     for cnt1 in range(len(dupFiles[key])):
    #         cnt1 += 1
    #         if(cnt1 > 1):
    #             csvwriter.writerow([dupFiles[key][cnt1]])
    #             # for cnt2 in range(len(dupFiles[key])):
    #                 # csvwriter.writerow([dupFiles[key][cnt2]])
    #                 # csvwriter.writerows([
    #                 #     ["Duplicate files are:"]
    #                 #     ,[dupFiles[key][cnt2]]
    #                 #     ])

    #################################Using Filter##################################   
    dups = list(filter(sortDup,dupFiles.values()))
    # print(dups) #list of list comes
    # [['Demo\\demo1.txt', 'Demo\\new_Dummy_1\\new_Dummy_2\\demo2.cpp', 'Demo\\new_Dummy_1\\new_Dummy_2\\demo6.txt'], ['Demo\\demo2.txt', 'Demo\\new_Dummy_1\\demo2.c']]
    # print(len(dups)) #2
    if (len(dups) > 0):
        csvwriter.writerow(["Duplicate files are : "]) 
        cnt = 1   
        for result in dups:
            csvwriter.writerow([cnt,result])
            cnt += 1
            # for sub_result in result:
            #     csvwriter.writerow([sub_result])
        # fd.close() 
        return fd,dups            
    else:
        csvwriter.writerow(["No duplicate file found."])
        fd.close() 
        exit() 
              

def deleteDupFiles(fd,dupFiles):
    # print(dupFiles) #list of list comes
    # [['Demo\\demo1.txt', 'Demo\\new_Dummy_1\\new_Dummy_2\\demo2.cpp', 'Demo\\new_Dummy_1\\new_Dummy_2\\demo6.txt'], ['Demo\\demo2.txt', 'Demo\\new_Dummy_1\\demo2.c']]
    # print(len(dupFiles)) #2
    csvwriter = csv.writer(fd)
    # csvwriter.writerow("")
    csvwriter.writerow(["List of duplicate files deleted from directory : "])
    cnt2 = 1
    for eachFileList in dupFiles:
        for cnt1 in range((len(eachFileList)-1)):
            os.remove(eachFileList[cnt1])
            csvwriter.writerow([cnt2,eachFileList[cnt1]])
            cnt2 += 1
            
    # fd.close()    


def main():
    # if((len(argv)<2) or (len(argv)>2)):
    if(len(argv) != 2):
        fd = createLogFile()
        csvwriter = csv.writer(fd)
        csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Duplicate File Automation Script-------------------------"],
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
            ["-----------------------Aishwarya Karande : Duplicate File Automation Script-------------------------"],
            ["Script name : ",argv[0]]
        ])
        csvwriter.writerows([
            ["Usage : Script accepts absolute directory path from user. Use to delete duplicate files from that directory and create log file which shows record of that deleted files"]
                               ]) 
        fd.close()                   
        exit()

    elif((argv[1] == "-h") or (argv[1] == "-H")):  
        fd = createLogFile()
        csvwriter = csv.writer(fd)
        csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Duplicate File Automation Script-------------------------"],
            ["Script name : ",argv[0]]
        ]) 
        csvwriter.writerows([
                    ["Help : python Name_of_Script.py First_Argument"],
                    ["First_Argument : Absolute path of directory on which we want to perform task"]
            ]) 
        fd.close() 
        exit()

    else:
        # csvwriter.writerows([["There is no such flag"]])
        # exit()
        
        try:
            # if(len(argv) == 2):
            startTime = time.time()
            directoryPath = argv[1]
            fd,dupFiles = displayDupFile(directoryPath)  
            deleteDupFiles(fd,dupFiles)
            endTime = time.time()
            csvwriter = csv.writer(fd)
            csvwriter.writerow(["Execution time required : ",endTime-startTime,"seconds"])
            fd.close()
            exit()
        except Exception as eobj:
            fd = createLogFile()
            csvwriter = csv.writer(fd)
            csvwriter.writerows([
            ["-----------------------Aishwarya Karande : Duplicate File Automation Script-------------------------"],
            ["Script name : ",argv[0]]
        ]) 
            csvwriter.writerow(["Exception occured : ",eobj])
            fd.close()
            exit()

if __name__ == "__main__":
    main()     








