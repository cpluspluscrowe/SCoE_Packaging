import os
import shutil
import sys
import unittest
from Prepare_35_Percent import changeFileName
from Prepare_35_Percent import changePdfNames
from Prepare_35_Percent import TogManager
from Prepare_35_Percent import Group
from Prepare_35_Percent import createGroups

class Packaging(unittest.TestCase):
    def setUp(self):
        self.packagePath = r"C:\Pkgs"
        self.checkIfDrawingFolderExists()
        self.checkIfFacilityFolderExists()
        self.checkIfExeIsPresentWithinTheFile()
        self.checkIfTOGSFolderExists()
        self.checkIfAnimationsFolderExistsOrHasBeenCreated()
        self.checkchangeFileNameFunction()
        self.checkchangeFileNameFunction65Percent()
        print("Done!")
        self.assertEqual(3,4)
    def checkIfDrawingFolderExists(self):
        self.drawingsPath = os.path.join(self.packagePath,"Drawings")
        try:
            self.assertTrue(os.path.isdir(self.drawingsPath))
        except Exception as e:
            print(e)
            print("Drawings folder does not exist within C:\Pkgs")
    def checkIfFacilityFolderExists(self):
        self.facilitiesPath = os.path.join(self.packagePath,"Facilities")
        try:
            self.assertTrue(os.path.isdir(self.facilitiesPath))
        except Exception as e:
            print(e)
            print("Facilities folder does not exist within C:\Pkgs")
    def checkIfExeIsPresentWithinTheFile(self):
        self.exePath = os.path.join(self.packagePath,"SCoE Packaging.exe")
        try:
            self.assertTrue(os.path.isfile(self.exePath))
        except Exception as e:
            print(e)
            print("exe 'SCoE Packaging.exe' is not present within C:\Pkgs")
    def checkIfTOGSFolderExists(self):
        self.togsPath = r"C:\JCMS\DATA_FILES\TOGS"
        try:
            self.assertTrue(os.path.isdir(self.togsPath))
        except Exception as e:
            print(e)
            print("TOGS folder is not present at C:\JCMS\DATA_FILES\TOGS")
    def checkIfAnimationsFolderExistsOrHasBeenCreated(self):
        self.togsPath = r"C:\Pkgs\Drawings\Animations"
        try:
            self.assertTrue(os.path.isdir(self.togsPath))
        except Exception as e:
            print(e)
            print("Animations folder needs to be created at C:\Pkgs\Drawings\Animations")
    def checkchangeFileNameFunction(self):
        file = open(r"C:\Pkgs\test.txt","w")
        file.close()
        changeFileName(r"C:\Pkgs","test.txt")
        newPath = r"C:\Pkgs\35%_test.txt"
        try:
            self.assertTrue(os.path.isfile(newPath))
        except Exception as e:
            print(e)
            print("35% file conversion failed, look at checkchangeFileNameFunction")
        os.remove(newPath)
    def checkchangeFileNameFunction65Percent(self):
        file = open(r"C:\Pkgs\65%_test.txt","w")
        file.close()
        changeFileName(r"C:\Pkgs","65%_test.txt")
        newPath = r"C:\Pkgs\35%_test.txt"
        try:
            self.assertTrue(os.path.isfile(newPath))
        except Exception as e:
            print(e)
            print("65% to 35% file conversion failed, look at checkchangeFileNameFunction")
        os.remove(newPath)

testIfReadyToPackage = Packaging()
testIfReadyToPackage.setUp()

