import sys
import os
from xml.dom import minidom
import xml.etree.ElementTree as ET

def getpardict(legendpar):    
    list = []
    tree = ET.parse(legendpar)
    root = tree.getroot()
    for element in root.findall('element'):
        afbname = element.find('AfbName').text
        instance = element.find('instanceNumber').text
        parxml = element.find('parXml').text        
        partuple = (afbname, instance, parxml)
        list.append(partuple)
        print(afbname + " " + instance + " " + parxml)
        print(partuple[0] + " " + partuple[1] + " " + partuple[2])        
    return list        

def getfilenames(dir):
    print('getfilenames')
    returnlist = []            
    filenames = os.listdir(dir)
    for filename in filenames:
        returnlist.append(filename)
    return returnlist     

def renameparfiles(partuples, folderpath):
    print('renameparfiles')
    for partuple in partuples:        
        print(partuple[0] + " " + partuple[1] + " " + partuple[2])        
        print(folderpath + "\\" + partuple[2])
        print(folderpath + "\\" + partuple[0] + ".par")
        if partuple[1] == '1':            
            if os.path.isfile(folderpath + "\\" + partuple[2]):
                os.rename(folderpath + "\\" + partuple[2], folderpath + "\\" + partuple[0] + ".par")
        else:
            if os.path.isfile(folderpath + "\\" + partuple[2]):
                os.rename(folderpath + "\\" + partuple[2], folderpath + "\\" + partuple[0] + "_" + partuple[1] + ".par")
            
def main():
    if len(sys.argv[1]) == 2:
        parfilenames = getfilenames(sys.argv[1])
    
        legendpar = ''
        for parfile in parfilenames:
            if parfile.endswith('.par'):
                legendpar = sys.argv[1] + "\\" + parfile    

        # print(legendpar)
    
        partuples = getpardict(legendpar)   
        renameparfiles(partuples, sys.argv[1])       
    else:
        prin('need folder path')

if __name__ == '__main__':
    main()