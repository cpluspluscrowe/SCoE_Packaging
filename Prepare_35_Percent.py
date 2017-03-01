import os
import shutil
from xlwings import *
import xlwings as xw
from pprint import pprint
import re

def changeFileName(parentDirectory,file):
    if not "35%_" in file:
        if not "65%_" in file:
            newName = "35%_" + file
            shutil.move(os.path.join(parentDirectory,file),os.path.join(parentDirectory,newName))
        else:
            newName = file.replace("65%","35%")
            shutil.move(os.path.join(parentDirectory,file),os.path.join(parentDirectory,newName))


def changePdfNames():
    drawingsPdfPath = r"C:\Pkgs\Drawings"
    for root,dirs,files in os.walk(drawingsPdfPath):
        for file in files:
            if ".pdf" in file:
                changeFileName(root,file)

    drawingsDwgPath = r"C:\Pkgs\Drawings\DWG"
    for root,dirs,files in os.walk(drawingsDwgPath):
        for file in files:
            if ".dwg" in file:
                changeFileName(root,file)
    if os.path.isdir(r"C:\Pkgs\Drawings\DWG\Archive"):
        shutil.rmtree(r"C:\Pkgs\Drawings\DWG\Archive")

class TogManager():
    def __init__(self):
        self.facilityPath = r"C:\Pkgs\Facilities"
        self.togs = ['1212000AA', '1251000JB', '1251000JC', '1251000AA', '1263000AA', '1211000AA', '1211000AC', '1211000AB', '7301500ZL', '1211000GA', '1251000RA', '1263000AC', '1244100AA', '1251001AA', '1251000NB', '1251000LC', '1251000LB', '1251000LD', '1251000LJ', '1251000LK', '1251000LL', '1251000LM', '1416500EA', '1251000UA', '1251000EB', '1251000EA', '1251000CC', '1251000CA', '1251000CE', '1211000CA', '1211000CB', '1221000AA', '1248101AA', '1251000AC', '1248101AC', '1267000AA', '4113000GB', '1264000AD', '1264000AC', '1266000AA', '1266000AB', '1266000CB', '1266000CA', '1266000CC', '1266000CD', '4113000JA', '4113000EA', '4113000EB', '8341050BB', '4113000GA', '4113000AA', '4113000AC', '4113000AD', '4113000AB', '4113000CA', '4113000CE', '4113000CG', '4113000CD', '4113000CC', '4113000CB', '4215050AA', '4228100AA', '4115000AB', '4311000CB', '4115000AA']
        self.togs.remove('1251000LC')
        self.togs.remove('1251000LJ')
        self.togs.remove('1251000LK')
        self.togFolder = r"C:\JCMS\DATA_FILES\TOGS"
        self.copyTogs = self.togs
        self.cnt = 0
        self.additionalFolder = r"C:\Pkgs\Additional 35% Design"
        self.vettingFolder = r"C:\Pkgs\Vetting"
        self.facilityPath = r"C:\Pkgs\Facilities"
    def moveTogFolder(self):
        destination = r"C:\Pkgs\TOGS"
        if os.path.isdir(destination):
            shutil.rmtree(destination)
        shutil.copytree(self.togFolder,destination)

    def getTogInFile(self,file):
        for tog in self.togs:
            if tog in file:
                return tog

    def InTogs(self,file):
        return any([s for s in self.togs if s in file])

    def fcount(self,path, map = {}):
      count = 0
      for f in os.listdir(path):
        child = os.path.join(path, f)
        if os.path.isdir(child):
          child_count = self.fcount(child, map)
          count += child_count + 1 # unless include self
      map[path] = count
      return count

    def deleteExtraFacilities(self):
        for section in os.listdir(self.facilityPath):
            for folder in os.listdir(os.path.join(self.facilityPath,section)):
                if not self.InTogs(folder):
                    shutil.rmtree(os.path.join(self.facilityPath,section,folder))
            if self.fcount(os.path.join(self.facilityPath,section)) == 0:
                shutil.rmtree(os.path.join(self.facilityPath,section))
    def changeTogNames(self):
        pathToTOGS = r"C:\Pkgs\TOGS"
        docPath = os.path.join(pathToTOGS,"DOC")
        for file in os.listdir(docPath):
            changeFileName(docPath,file)
        pdfPath = os.path.join(pathToTOGS,"PDF")
        for file in os.listdir(pdfPath):
            changeFileName(pdfPath,file)
        specPath = os.path.join(pathToTOGS,"SPEC")
        for file in os.listdir(specPath):
            changeFileName(specPath,file)

    def getFacilityList(self):
        self.facList = []
        self.facPath = r"C:\Pkgs\Facilities"
        for section in os.listdir(self.facPath):
            for folder in os.listdir(os.path.join(self.facPath,section)):
                facName = folder.split(" - ")[0]
                self.facList.append(facName)

    def isDirectoryAFacility(self,directory):
        return any([s for s in self.togs if s in directory])

    def moveAdditionalCoverSheets(self):
        for coverSheet in self.coverSheetPaths:
            parent = re.sub(' (.+)|_Empty', '', os.path.basename(os.path.dirname(coverSheet)))
            #.split(" (")[0]
            coverSheetPdfName = os.path.basename(coverSheet)
            facilityPath = r"C:\Pkgs\Facilities"
            for root,dirs,files in os.walk(facilityPath):
                for d in dirs:
                    if self.isDirectoryAFacility(d):
                        if parent in d:
                            shutil.copyfile(coverSheet,os.path.join(root,d,coverSheetPdfName))
        
    def getCoverSheets(self,additionalFolder = r"C:\Pkgs\Additional 35% Design"):
        self.getFacilityList()#Creates a list of facilities
        self.coverSheetPaths = []
        for root,dirs,files in os.walk(additionalFolder):
            for file in files:
                if "Cover Sheet.pdf" in file:
                    self.coverSheetPaths.append(os.path.join(root,file))

    def getAndStoreConceptFolderList(self):
        self.conceptFolderList = set()
        self.appendConceptFolderList(self.additionalFolder)
        self.appendConceptFolderList(self.vettingFolder)

    def appendConceptFolderList(self,path):
        for root,dirs,files in os.walk(path):
            for d in dirs:
                if d == "Concept Drawings":
                    self.conceptFolderList.add(os.path.join(root,d))

    def moveConceptualDrawingFolders(self):
        """
        Moves concept drawings from their additional/vetting folder to the correct corresponding
            facility location
        self.conceptFolderList should be empty at the completion of the function
        """
        for conceptFolderPath in list(self.conceptFolderList):
            parent = re.sub(' (.+)|_Empty', '', os.path.basename(os.path.dirname(conceptFolderPath)))
            fileName = os.path.basename(conceptFolderPath)
            for root,dirs,files in os.walk(self.facilityPath):
                for d in dirs:
                    if self.isDirectoryAFacility(d):
                        if parent in d:
                            if not os.path.isdir(os.path.join(root,d,fileName)):
                                shutil.copytree(conceptFolderPath,os.path.join(root,d,fileName))
                            self.conceptFolderList.remove(conceptFolderPath)
                            
class Group():
    def __init__(self,name,facilityList):
        self.name = name
        self.facilityList = facilityList
        self.folderPath = r"C:\Pkgs\Facilities"
        self.createGroupFolder()
        self.removeEmptyFolders()
    def createGroupFolder(self):
        if not os.path.isdir(os.path.join(self.folderPath,self.name)):
            os.makedirs(os.path.join(self.folderPath,self.name))
        for facility in self.facilityList:
            self.findAndMoveFacility(facility)
    def findAndMoveFacility(self,folder):
        for root,dirs,files in os.walk(self.folderPath):
            for d in dirs:
                if folder in d:
                    if not os.path.isdir(os.path.join(self.folderPath,self.name,d)):
                        shutil.copytree(os.path.join(root,d),os.path.join(self.folderPath,self.name,d))
                    if os.path.isdir(os.path.join(root,d)):
                        if os.path.join(root,d) != os.path.join(self.folderPath,self.name,d):
                            shutil.rmtree(os.path.join(root,d))
    def removeEmptyFolders(self):
        tm = TogManager()
        for folder in os.listdir(self.folderPath):
            if tm.fcount(os.path.join(self.folderPath,folder)) == 0:
                shutil.rmtree(os.path.join(self.folderPath,folder))
def createGroups():
    groupList = []
    app1 = xw.App()
    wb = xw.apps.active.books.open(r'C:\Users\CCrowe\Documents\AFCS Folder\SCoE Facility List for Chad.xlsx')
    sheets = ['Group 1 Fuels','Group 1 Ammo Storage','Group 1 Mortuary Affairs']
    for sheetName in sheets:
        facilityList = []
        sht = wb.sheets[sheetName]
        rowcnt = 3
        while(sht.range('A' + str(rowcnt)).value != None):
            facilityList.append(sht.range('A' + str(rowcnt)).value)
            rowcnt += 1
        group = Group(sheetName.replace("Group 1 ",""),facilityList)
        groupList.append(group)
    wb.close()
    app1.quit()

def changeDrawingStructure():
    drawingFolder = r"C:\Pkgs\Drawings"
    pdfPath = r"C:\Pkgs\Drawings\PDF"
    if not os.path.isdir(pdfPath):
        os.mkdir(pdfPath)
    for root,dirs,files in os.walk(drawingFolder):
        for file in files:
            if ".pdf" in file and not ".lnk" in file:
                if os.path.join(root,file) != os.path.join(pdfPath,file):
                    shutil.copyfile(os.path.join(root,file),os.path.join(pdfPath,file))
                

def main():
    """
    Prepares the folders for packaging
    """
    changePdfNames()
    togManager = TogManager()
    togManager.moveTogFolder()
    togManager.deleteExtraFacilities()
    togManager.changeTogNames()
    createGroups()
    togManager.getCoverSheets()
    togManager.moveAdditionalCoverSheets()
    togManager.getCoverSheets(r"C:\Pkgs\Vetting")
    togManager.moveAdditionalCoverSheets()
    togManager.getAndStoreConceptFolderList()
    togManager.moveConceptualDrawingFolders()
    changeDrawingStructure()

def AfterPackagingCode35Percent():
    facilityPath = r"C:\Pkgs\Facilities"
    for root,dirs,files in os.walk(facilityPath):
        for d in dirs:
            if d == "Drawings":
                animationPath = os.path.join(root,d,"Animations")
                dwgPath = os.path.join(root,d,"DWG")
                if os.path.isdir(animationPath):
                    shutil.rmtree(animationPath)
                if os.path.isdir(dwgPath):
                    shutil.rmtree(dwgPath)
            if d == "TOGS":
                secPath = os.path.join(root,d,"SEC")
                pdfPath = os.path.join(root,d,"PDF")
                if os.path.isdir(secPath):
                    shutil.rmtree(secPath)
                if os.path.isdir(pdfPath):
                    shutil.rmtree(pdfPath)
    

if __name__ == "__main__":
    main()









