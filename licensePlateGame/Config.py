import configparser

class Config:
    def __init__(self, filename):
        self.config = configparser.RawConfigParser()
        self.fileName = filename

    #set Section
    def setConfigSection(self, section):
        self.config.add_section(section)
        self.writeToConfig()

    #set Value
    def setConfigValue(self, section, key, value):
        try:
            self.config.set(section, key, value)
            #print('Setting section: ' + section + ' key: ' + key + ' value: ' + value)
        except:
            print('Error: unable to set value')
        self.writeToConfig()
    
    #read config
    def getConfigValue(self, section, key):
        self.config.read(self.fileName)
        try:
            configValue = self.config.get(section, key)
            #print('Getting section: ' + section + ' key: ' + key + ' value: ' + configValue)
        except:
            print('Error: unable to get value')
        return configValue

    #write config
    def writeToConfig(self):
        with open(self.fileName, 'w') as configFile:
            self.config.write(configFile)
