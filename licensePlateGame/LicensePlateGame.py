import os
from LicensePlateState import *
from FileHelper import *
from Config import *
from Logger import *
from TimerThread import *

'''
TODO:
    Sample out parameters and messaging
    Add graphics
    Add xml parsing
    review pythong basic logger
    restructure for distribution
    check and create directories in setup
'''

class LicensePlateGame:
    def __init__(self):
        #name of the application
        self.name = 'License Plate Game'

        #filename prefix
        self.filename = 'licenseplategame'
        
        self.configFile = self.filename + '.cfg'

        #self.logger.writeLog('Checking config file', LogLevel.Inf)
        self.config = Config(self.configFile)
        self.dataFile = ''
        self.dataFileLocation = '/data/'
        self.logFileMax = 5
        self.logFileMaxByteSize = 200
        self.logFileLocation = '/log/'
        
        self.logger = Logger(self.filename, self.logFileLocation, self.logFileMax, self.logFileMaxByteSize)
        
        #initialize Game
        self.logger.writeLog('Initializing Game', LogLevel.Inf)
        
        self.checkFiles()
        


        #file
        
        #states
        self.states = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
        }

        #list of LicensePlateStates
        self.licensePlateStates = []
        
        #initialize data file
        self.initializeFile()

        #initialize list
        self.initializeList()
      

    #initialize file
    def initializeFile(self):
        #if file is empty or doesn't exist, create file with all states
        if not FileHelper.fileExists(self.dataFile):
            self.logger.writeLog('Data file doesn''t exist', LogLevel.Inf)
            self.loadFile()
        if FileHelper.getFileSize(self.dataFile) == 0:
            self.logger.writeLog('Data file empty', LogLevel.Inf)
            self.loadFile()
        else:
            self.logger.writeLog('Data exists in current data file', LogLevel.Inf)
            self.logger.writeLog('Current data file size: ' + str(os.stat(self.dataFile).st_size) + ' bytes', LogLevel.Inf)

    #load file with states
    def loadFile(self):
        file = open(self.dataFile, 'a')
        for key in self.states:
            licensePlateState = LicensePlateState(key,self.states[key])
            stringToWrite = licensePlateState.checkBox.getText() + ' ' + key + '\n'
            file.write(stringToWrite)
            #might as well ad to the list
            self.licensePlateStates.append(licensePlateState)
        file.close
        self.logger.writeLog('Data file loaded', LogLevel.Inf)
 
    #initialize list
    def initializeList(self):
        if len(self.licensePlateStates) == 0:
            self.logger.writeLog('License Plate State List is empty', LogLevel.Inf)
            self.loadList()
        else:
            self.logger.writeLog('License Plate State List preloaded with existing data', LogLevel.Inf)

    #load list with states from file
    def loadList(self):
        lines = self.getStatesFromFile()
        for line in lines:
            licensePlateState = self.getLicensePlateState(line)
            if licensePlateState.stateName != '':
                self.licensePlateStates.append(licensePlateState)
        self.logger.writeLog('License Plate State List loaded: ' + str(len(self.licensePlateStates)) + ' states', LogLevel.Inf)        

    #parse string to get License Plate State
    def getLicensePlateState(self,line):
        licensePlateState = LicensePlateState('','')
        if line[0] == 'X':
            licensePlateState.setComplete(True)
        state = line[2:4]
        if self.isValidState(state):
            licensePlateState.setState(state)
            licensePlateState.setStateName(self.states[state])
        return licensePlateState

    #check to see if state is valid
    def isValidState(self, state):
        for key in self.states:
            if key == state:
                return True
        return False
    
    #returns the number of states remaining
    def remainingStateCount(self):
        stateCount = 0
        for licensePlateState in self.licensePlateStates:
            if not licensePlateState.checkBox.isChecked():
                stateCount += 1
        print('States remaining: ' + str(stateCount))

    #add state
    def addState(self, state, show=False):
        print('Adding ' + state)
        if self.updateState(state, 'a', show):
            self.logger.writeLog('Request to add ' + state + ' : Success', LogLevel.Inf)
        else:
            self.logger.writeLog('Request to add ' + state + ' : Failure', LogLevel.Inf)

    #remove state
    def removeState(self,state, show=False):
        print("Removing " + state)
        if self.updateState(state, 'd', show):
            self.logger.writeLog('Request to remove ' + state + ' : Success', LogLevel.Inf)
        else:
            self.logger.writeLog('Request to remove ' + state + ' : Failure', LogLevel.Inf)

    #update state
    def updateState(self, state, action, show):
        result = False
        for licensePlateState in self.licensePlateStates:
            if licensePlateState.state == state:
                if action == 'a':
                    licensePlateState.setComplete(True)
                    if licensePlateState.checkBox.isChecked():
                        result = True
                if action == 'd':
                    licensePlateState.setComplete(False)
                    if not licensePlateState.checkBox.isChecked():
                        result = True
        #clear data on file            
        with open(self.dataFile, 'w'):
            pass
        
        #rewrite data to file with state            
        file = open(self.dataFile, 'a')
        for licensePlateState in self.licensePlateStates:
            file.write(licensePlateState.checkBox.getText() + ' ' + licensePlateState.state.upper() + '\n')
        file.close

        if show is True:
            self.showStateList()

        return result

    #get states from data file                           
    def getStatesFromFile(self):
        file = open(self.dataFile, 'r')
        lines = file.readlines()
        file.close
        return lines

    #show list of states and completion
    def showStateList(self):
        sortedLicensePlateStates = sorted(self.licensePlateStates, key=lambda x:x.stateName)
        for licensePlateState in sortedLicensePlateStates:
            licensePlateState.showState()

        #notify number of states remaining count
        print('\n')
        self.remainingStateCount()
    
    #show help
    def showHelp(self):
        print('\n')
        print('License Plate Game v1.0.0.0')
        print('Author: Robert Balala')
        print('Copyright: 2015')
        print('\n')
        print('add [State Abbreviation]')
        print('  Example: To mark the state ''Alabama'' as completed: add AL')
        print('rem [State Abbreviation]')
        print('  Example: To revert the state ''Alabama'' as completed: rem AL')
        print('sho')
        print('  Example: To show the state list: sho')
        print('hel')
        print('  Example: To show help: hel')
        print('\n')

    #check game files
    def checkFiles(self):
        #check config file
        if not FileHelper.fileExists(self.configFile):
            self.logger.writeLog('Config file does not exist', LogLevel.Inf)
            self.config.setConfigSection('Settings')
            self.config.setConfigValue('Settings', 'appName', 'License Plate Game')
            self.config.setConfigValue('Settings', 'version', '1.0.0.0')
            self.config.setConfigValue('Settings', 'dataFileType', '.dat')
            self.config.setConfigValue('Settings', 'dataFileLocation', '/data/')
            self.config.setConfigValue('Settings', 'logFileMax', '5')
            self.config.setConfigValue('Settings', 'logFileMaxByteSize', '200')
            self.config.setConfigValue('Settings', 'logFileLocation', '/log/')
        else:
            self.logger.writeLog('Config file exists', LogLevel.Inf)
            self.appName = self.config.getConfigValue('Settings', 'appName')
            self.version = self.config.getConfigValue('Settings', 'version')
            self.dataFileType = self.config.getConfigValue('Settings', 'dataFileType')
            self.dataFileLocation = self.config.getConfigValue('Settings', 'dataFileLocation')
            self.logFileMax = self.config.getConfigValue('Settings', 'logFileMax')
            self.logFileMaxByteSize = self.config.getConfigValue('Settings', 'logFileMaxByteSize')
            self.logFileLocation = self.config.getConfigValue('Settings', 'logFileLocation')
            self.dataFile = FileHelper.getWorkingDirectory() + self.dataFileLocation + self.filename + self.dataFileType
        #check data file
        datFile = FileHelper.getDocumentsDirectory() + '/' + self.filename + self.dataFileLocation + self.filename + '.dat'
        if not FileHelper.fileExists(datFile):
            self.logger.writeLog('Dat file does not exist', LogLevel.Inf)
        else:
            print('Dat file exists')
        xmlFile = FileHelper.getDocumentsDirectory() + '/' + self.filename + self.dataFileLocation + self.filename + '.xml'
        if not FileHelper.fileExists(xmlFile):
            self.logger.writeLog('Xml file does not exist', LogLevel.Inf)
        else:
            self.logger.writeLog('Xml file exists', LogLevel.Inf)

    def run(self):
        self.showHelp()
        t = TimerThread('Timer', 10, self.logger)
        t.start()
        while True:
            i = input('Type in command (or Press Enter to quit): ')
            if not i:
                break
            #print('your input:', i)
            action = i[0:3]
            #print(action)
            state = i[4:6]
            #print(state)
            if action == 'add':
                 self.addState(state)
            if action == 'rem':
                self.removeState(state)
            if action == 'sho':
                self.showStateList()
            if action == 'hel':
                self.showHelp()
        
        print('Thank you for playing the License Plate Game, GoodBye!')
        t.stop()

#this will allow the game to execute if you execute this file
if __name__ == '__main__':
    LicensePlateGame().run()
