import os
import shutil
import sys
import unittest

class Packaging(unittest.TestCase):
    def setUp(self):
        self.packagePath = r"C:\Pkgs"
        self.checkIfDrawingFolderIsPresent()
        self.assertEqual(3,4)
    def checkIfDrawingFolderIsPresent(self):
        self.drawingsPath = os.path.join(self.packagePath,"Drawings")
        try:
            self.assertTrue(os.path.isdir(self.drawingsPath))
        except Exception as e:
            print(e)
            print("Drawings folder does not exist within C:\Pkgs")
            




