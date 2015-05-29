import os
import datetime
from enum import Enum
from FileHelper import *

class LogLevel(Enum):
    Err = 1
    Wrn = 2
    Inf = 3
    Dbg = 4

class Logger:
    def __init__(self, fileName, fileLocation='/log/', maxFiles=5, maxFileSize=200):
        self.fileName = fileName
        self.fileLocation = fileLocation
        self.maxFiles = maxFiles
        self.maxFileSize = maxFileSize 
        self.writeLog('Log file initialized', LogLevel.Inf)

    #write log        
    def writeLog(self, logEntry, logLevel):
        fileToWrite = self.getLogFile()
        #create if file doesn't exist
        if not FileHelper.fileExists(fileToWrite):
            print('Creating log file: ' + fileToWrite)
            self.createLog(fileToWrite)
        #clear if file is full
        fileSize = FileHelper.getFileSize(fileToWrite)
        if fileSize > self.maxFileSize:
            print('Clearing file: ' + fileToWrite)
            self.clearLog(fileToWrite)
        #print('Attempting to write to log file: ' + fileToWrite)
        with open(fileToWrite, 'a') as logFile:
            logFile.write(logLevel.name + '-' + str(datetime.datetime.now()) + '-' + logEntry + '\n')

    #create log
    def createLog(self, fileName):
        FileHelper.createFile(fileName)       



    #does the file exist
        #is it full
            #get next file


    #get log file
    def getLogFile(self):
        logIndex = 0
        while logIndex < self.maxFiles:            
            #check if file exists
            fileName = self.getLogFileName(logIndex)
            print(FileHelper.getFileName(fileName))
            if not FileHelper.fileExists(fileName):
                break
            else:
                #if over file limit, return next file
                fileSize = FileHelper.getFileSize(fileName)
                if fileSize < self.maxFileSize:
                    print('file has room')
                    break
                else:
                    print('file is full')
                    #if file is older, lets recycle
                    lastUpdated = FileHelper.getFileModifiedDateTime(fileName)
                    print(FileHelper.getFileName(fileName + ' ' + lastUpdated))
                    #check if the next file is older
                    nextFile = self.getLogFileName(self.getNextAvailableLog(logIndex))
                    nextFileDate = FileHelper.getFileModifiedDateTime(nextFile)
                    print(FileHelper.getFileName(nextFile) + ' ' + nextFileDate)
                    if FileHelper.fileExists(nextFile):
                        if lastUpdated > nextFileDate:
                            fileName = nextFile
                            print('next file is older')
                            break
            logIndex += 1
        return fileName

    #get next available log
    def getNextAvailableLog(self, logIndex):
        nextAvailableLogIndex = logIndex + 1
        if nextAvailableLogIndex == self.maxFiles:
            nextAvailableLogIndex = 0
        return nextAvailableLogIndex
        
    #get log file name
    def getLogFileName(self, count):
        if count == 0:
            return FileHelper.getWorkingDirectory() + self.fileLocation + self.fileName + '.log'
        else:
            return FileHelper.getWorkingDirectory() + self.fileLocation + self.fileName + str(count) + '.log'

    
    #empty file
    def clearLog(self, fileName):
        FileHelper.emptyFile(fileName)
