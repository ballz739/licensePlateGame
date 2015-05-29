import os
import io
import time

from os.path import expanduser

class FileHelper():
    
    #check if file exists
    def fileExists(fileName):
        result = False
        try:
            result = os.path.exists(fileName)
        except IOError as e:
            print('I/O error({0}): {1}'.format(e.errno, e.strerror))
        return result

    #create file
    def createFile(fileName):
        with open(fileName, 'w') as logFile:
            logFile.write('File Created')

    #clear File
    def emptyFile(fileName):
        with open(fileName, 'w'):
            pass

    #get file size
    def getFileSize(fileName):
        return os.stat(fileName).st_size

    #get file modified date time
    def getFileModifiedDateTime(fileName):
        return time.ctime(os.path.getmtime(fileName))

    #get file created date time
    def getFileCreatedDateTime(fileName):
        return time.ctime(os.path.getctime(fileName))

    #combine paths
    def pathCombine(path1, path2):
        return os.path.join(os.getcwd() + path1, path2)

    #create Directory
    def createDirectory(directoryName):
        return os.mkdir(directoryName)

    #get working directory
    def getWorkingDirectory():
        return os.getcwd();

    #get home directory
    def getHomeDirectory():
        return expanduser('~')

    #get documents directory
    def getDocumentsDirectory():
        return expanduser('~/Documents')

    #get file name
    def getFileName(fileName):
        return os.path.basename(fileName)
