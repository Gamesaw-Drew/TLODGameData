import hashlib
import os
jsonString = '{\n"data": ['
rootDir = 'D:\Users\Drew\Documents\LegendofDiamondbackBuild\WindowsNoEditor'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        filename = "%s\\%s"%(dirName.replace("D:\\Users\\Drew\\Documents\\LegendofDiamondbackBuild\\WindowsNoEditor\\" ,""), fname)
        jsonString = jsonString + '{"Filename": "%s", "sha256" : "%s"},\n' %(filename, hashlib.sha256(open("%s" %"%s\\%s" %(dirName, fname), 'rb').read()).hexdigest())
    
jsonString = jsonString[:-2] + '\n]}'
jsonString = jsonString.replace("\\", "/").replace("D:/Users/Drew/Documents/LegendofDiamondbackBuild/WindowsNoEditor/", "")
print(jsonString)
file = open("lotamanifest.json", "w")
file.write(jsonString)