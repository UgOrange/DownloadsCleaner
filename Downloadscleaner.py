#!/user/bin/env python
# -*- coding:utf-8 -*-
# Author：UgOrange
# Date：2020-07-30

import sys
import os
import shutil
dirList=['Documents','compressed','photo','installer','movies','music','others']

def classifier(directory):
    files=os.listdir(directory)
    mkdir(directory)
    for filename in files:
        if not os.path.isdir(directory+filename):
            fileType=getType(filename)
            desDir=directory+fileType
            srcDir=directory+filename
            shutil.move(srcDir,desDir)
            print("move a "+fileType+"file to "+desDir+"!")

def getType(filename):
    docList=['chm','rtf','tex','ltx','doc','docx','ppt','pptx','wps','odf','mht','pdf','mhtml']
    compressList=['7z','zip','rar','001','cab','']
    photoList=['bmp','gif','jpg','jpeg','png','psd','tif','tiff','webp']
    installerList=['exe','dmg','iso','apk']
    moviesList=['avi','wmv','mpeg','mov','mkv','mp4']
    musicList=['mp3','wma','wav','flac']
    suffix=os.path.splitext(filename)[-1][1:]
    if suffix in docList:
        return dirList[0]
    elif suffix in compressList:
        return dirList[1]
    elif suffix in photoList:
        return dirList[2]
    elif suffix in installerList:
        return dirList[3]
    elif suffix in moviesList:
        return dirList[4]
    elif suffix in musicList:
        return dirList[5]
    else:
        return dirList[6]    
def mkdir(directory):
    
    for dirname in dirList:
        dirname=directory+dirname
        dirnameExist=os.path.exists(dirname)
        if not dirnameExist:
            os.mkdir(dirname)
            print("Create "+dirname+" directory")

# def cleaner(directory):

if __name__ == "__main__":
    if(len(sys.argv)==1 or len(sys.argv)==2):
        print("Usage:Downloadscleaner ～/Download classify/clean")
    else:
        directory=sys.argv[1]
        selectType=sys.argv[2]
        if(directory[-1]!='/'):
            directory=directory+'/'
        if(selectType=='classify'):
            classifier(directory)
        elif(selectType=='clean'):
            cleaner(directory)
        

    