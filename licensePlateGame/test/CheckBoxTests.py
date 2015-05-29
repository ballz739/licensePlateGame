from CheckBox import *
import unittest

class CheckBoxTestCase(unittest.TestCase):

    def setUp(self):
        self.checkBox = CheckBox()

    def testDefaultIsChecked(self):
        self.assertFalse(self.checkBox.isChecked(), 'Default value of isChecked() should be False')

    def tearDown(self):
        print('Done')




suite = unittest.TestSuite()
suite.addTest(CheckBoxTestCase('testDefaultIsChecked'))






unittest.TextTestRunner().run(suite)
