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
        self.IsDirectoryAFacilityTest()
        self.getAdditionalCoverSheets()
        self.moveCoverSheetsAdditionalTest()
        self.moveCoverSheetsVettingTest()
        self.eachFileHasCoverSheet()
        print("Done!")
        sys.exit(0)
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
    def eachFileHasCoverSheet(self):
        self.facilityPath = r"C:\Pkgs\Facilities"
        for section in os.listdir(self.facilityPath):
            for folder in os.listdir(os.path.join(self.facilityPath,section)):
                foundCoverSheet = False
                for file in os.listdir(os.path.join(self.facilityPath,section,folder)):
                    if file == "Cover Sheet.pdf":
                        foundCoverSheet = True
                try:
                    self.assertTrue(foundCoverSheet == True)
                except Exception as e:
                    print(e)
                    print("Cover Sheet not found in folder:",section,folder)

    def IsDirectoryAFacilityTest(self):
        tm = TogManager()
        for tog in tm.togs:
            self.assertTrue(tm.isDirectoryAFacility(tog))
        self.assertTrue(not tm.isDirectoryAFacility(''))

    def moveCoverSheetTest(self):
        coverSheetPath = r"C:\Users\CCrowe\Documents\AFCS Folder\Tests\Cover Sheet.pdf"
        getAdditionalCoverSheets(r"C:\Users\CCrowe\Documents\AFCS Folder\Tests")

    def getAdditionalCoverSheets(self):
        tm = TogManager()
        tm.getCoverSheets()
        try:
            self.assertTrue(len(tm.coverSheetPaths) > 0)
        except Exception as e:
            print(e)
            print("additionalCoverSheetPaths list is empty, was not filled from getAdditionalCoverSheets")
        for coverSheetPath in tm.coverSheetPaths:
            file = os.path.basename(coverSheetPath)
            try:
                self.assertTrue(file == "Cover Sheet.pdf")
            except Exception as e:
                print(e)
                print("Cover Sheet name is wrong:",file)

    def moveCoverSheetsAdditionalTest(self):
        tm = TogManager()
        tm.getCoverSheets()
        tm.moveAdditionalCoverSheets()

    def moveCoverSheetsVettingTest(self):
        tm = TogManager()
        tm.getCoverSheets(r"C:\Pkgs\Vetting")
        tm.moveAdditionalCoverSheets()

        

testIfReadyToPackage = Packaging()
testIfReadyToPackage.setUp()



















