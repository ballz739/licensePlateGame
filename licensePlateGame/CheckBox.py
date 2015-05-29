class CheckBox:

    #initialize
    def __init__(self, checked=False):
        self.checked = checked
        self.text = ' '

    def setText(self):
        if self.checked:
            self.text = 'X'
        else:
            self.text = ' '

    def getText(self):
        return self.text

    #set checked value
    def check(self,checked):
        if checked:
            self.checked = True
        else:
            self.checked = False
        self.setText()


    #get checked value
    def isChecked(self):
        return self.checked
            
    #draw checkbox
    def showCheckBox(self):
        print(self.text)
