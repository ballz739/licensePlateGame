from CheckBox import *

class LicensePlateState:

    def __init__(self, state='', stateName=''):
        self.checkBox = CheckBox(False)
        self.state = state
        self.stateName = stateName

    def setComplete(self,complete):
        self.checkBox.check(complete)

    def setState(self, state):
        self.state = state

    def setStateName(self, stateName):
        self.stateName = stateName
        
    def showState(self):
        print(self.checkBox.getText() + ' ' + self.stateName)
