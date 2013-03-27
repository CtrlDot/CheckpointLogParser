
import os

class CheckpointLog:
    
    logFileName = ""
    headers = []
    logFile = None
    linesRead = 0
    
    def __init__(self,logFileName):
        self.logFileName = logFileName
        if not os.path.isfile(self.logFileName):
             raise IOException("File does not exist")
        
        self.logFile = open(self.logFileName,'r')
        firstLine = self.logFile.readline()
        
        self.headers = self.ParseLine(firstLine)
    
    def HasHeader(self,header):
        if header in self.headers:
            return True
        return False
    
    def GetFileSize(self):
        statinfo = os.stat(self.logFileName)
        return statinfo.st_size
       
    def GetLineByHeader(self,headers):
        currentLine = self.logFile.readline()
        if currentLine == '':
            return []
        self.linesRead += 1
        currentLineSplit = self.ParseLine(currentLine)
        retValue = []
        for header in headers:
            if header in self.headers:
                index = self.headers.index(header)
                if len(currentLineSplit) <= index:
                    retValue.append('')
                else:
                    retValue.append(currentLineSplit[index])
            else:
                retValue.append('')
        return retValue 
            
    def ParseLine(self,line):
        lineSplit = line.split('"')
        retValue = []
        for element in lineSplit:
            if not (element.isspace()):
                retValue.append(element)
        return retValue
    
    def GetLinesRead(self):
        return self.linesRead