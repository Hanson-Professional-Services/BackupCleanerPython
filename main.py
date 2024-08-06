# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:32:20 2024

@author: pearc02338
"""

import os
import zipfile
from datetime import datetime, timedelta
import traceback

def main():
    try:
        with open('test.txt', 'r') as f:
            lines = f.readlines()
            
            for line in lines:
                line = line[:len(line)-1]
                print(line)
                checkFile(line)
    except:
        traceback.print_exc()
        
def checkFile(parent):
    print("Checking File")
    if os.path.isdir(parent) and containsDirectories(parent):
        for file in os.listdir(parent):
            file = parent + "\\" + file
            checkFile(file)     
    elif "Historic" not in parent:
        deleteFiles(parent)
   
    
def containsDirectories(parent):
    if os.path.isdir(parent):
        for file in os.listdir(parent):
            print(file)
            file = parent + "\\" + file
            print(file)
            if os.path.isdir(file):
                return True
    return False
   

def deleteFiles(parent):
    cutoff_date = datetime.now() - timedelta(days=29)
 
  
    for filename in os.listdir(parent):
        filePath = os.path.join(parent, filename)
        if os.path.isfile(filePath):
            fileModtime = datetime.fromtimestamp(os.path.getmtime(filePath))
 
 
            if fileModtime <= cutoff_date:
                os.remove(filePath)
            elif "zip" not in filename:
                print(f"Need to zip: {filePath}")
                zipFiles(filePath)
                os.remove(filePath)
 
def zipFiles(originalFile):
    zipFilePath = f"{originalFile}.zip"
    try:
        with zipfile.ZipFile(zipFilePath, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(originalFile, os.path.basename(originalFile))
            
        
            
            
    except Exception as e:
        print(f"Error while zipping file {originalFile}: {e}")
        

main()










