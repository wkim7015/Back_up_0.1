#-*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.realpath('..'))
from log_function import text_log
## Need to import text_log         (1)


#change the log.describe to specific function >> log.describe()

class security_byte():


    ''' It uses full paths of originalDirectory,copiedDirectory( new directory) and log. 
    '''
    
    
    ''' This function to calculate the contents of the files..######not completed yet.It requires to the full paths of the directories wyou whish to copy
    '''
    totaLfileCounter = 0
    fileCounter = 0
    def get_size(self,startPath):
        totalSize = 0
        for dirPath, dirnames, fileNames in os.walk(startPath):
            for f in fileNames:
                fp = os.path.join(dirPath, f)
                totalSize += os.path.getsize(fp)
        return totalSize    
    
    
    @staticmethod  #require the conversion?
    def loss_byte(Constant2,text): 

        log = text_log()
        if (Constant2 <1e3):
            log.describe(str(Constant2 +("\t바이트\n")),text)
        elif (1e3<Constant2< 1e6):
            log.describe(str(Constant2*1e-3) +("\t킬로바이트\n"),text)
        elif (1e6<Constant2<1e9):
            log.describe(str(Constant2*1e-6) +u("\t메가바이트\n"),text)
        elif (1e9<Constant2<1e12):
            log.describe(str(Constant2*1e-9) +("\t기가바이트\n"),text)    

    #Reporting on nominal bytes and other folders which may have discreted.    
    def file_check(self,originalDirectory,
                   newDirectory,text):  # only for directory.
        #if str(e).find("not a directory")  !=-1:
        #        return 1 #flag
        if os.path.isdir(originalDirectory) == False:  #Debugg it
            return 1
        ''' return flag when newDirectory or originalDirectory does not exist: can we use the commandline isexist() for this?
        '''
        
        ''' It needs to have another command which supports the txt file; the addresses are required.
        '''
        #======================================================================= initialization
        olDfiles = os.listdir(originalDirectory)
        neWfiles = os.listdir(newDirectory)
        olDname = []
        neWname = []
        log = text_log()
        olDfilesSize = self.get_size(originalDirectory)
        neWfilesSize = self.get_size(newDirectory)
        #=======================================================================
        #======================================================================= Process #1

        olDfilesSize = self.get_size(originalDirectory)
        neWfilesSize = self.get_size(newDirectory)
        for i in range(0,len(olDfiles)):
            global totaLfileCounter
            totaLfileCounter = i
            olDname.append( originalDirectory+"\\"+str(olDfiles[i]))
        for i in range(0, len(neWfiles)):
            global fileCounter
            fileCounter = i
            neWname.append( newDirectory+"\\"+str(neWfiles[i]))
        #======================================================================= Process #2
        log.describe("\n\n해당되는 주소:",text)
        log.write(originalDirectory,text)
        log.describe("\n%%"+"전체 파일 " +str(len(olDfiles))+"중"+str(len(neWfiles))+"파일 또는 폴더 복사 완료"+"%%\n",text)
        difference = list(set(olDfiles)-set(neWfiles))
        if( difference == []):
             for i in range(0, len(olDname)):
                 constant = abs(os.stat(olDname[i]).st_size-os.stat(neWname[i]).st_size)
                 if(constant !=0):
                      log.describe("실패한 파일:\t",text)
                      log.write(olDname[i],text)
                      log.describe("\n 잃어버린 바이트 :\t",text)
                      self.loss_byte(constant,text)
    
        else: 
             for i in range(0,len(difference)):
                  constant = os.stat(originalDirectory+"\\"+str(difference[i])).st_size
                  log.describe("\n\n실패한폴더 또는 파일:\t"+((difference[i]))+"\n",text) #cannot calculate when there is a permission lock on the file. .
                  if(constant !=0):
        #            draw the line.
                     log.describe(("잃어버린자료 용량 :\t"),text)
                     self.loss_byte(constant,text)

        #======================================================================= Termination

def unicode_conversion(string):
    #If the file is None, then return string "None"
    if string ==None or '':
        string = "None"
    return str(unicode(string,"utf-8").encode('cp949'))
    #return string.decode('utf-8','replace').encode('euc-kr','replace')

