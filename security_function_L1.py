<<<<<<< HEAD
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
    text = text_log()    

    #Reporting on nominal bytes and other folders which may have discreted.    
    def file_check(self,originalDirectory,
                   newDirectory,log):  # only for directory.
        #if str(e).find("not a directory")  !=-1:
        #        return 1 #flag
        if os.isdir(unicode_conversion(originalDirectory)) == False:  #Debugg it
            return 1
        ''' return flag when newDirectory or originalDirectory does not exist: can we use the commandline isexist() for this?
        '''
        
        ''' It needs to have another command which supports the txt file; the addresses are required.
        '''

            
        #======================================================================= initialization
=======



class security_byte():
''' This function to calculate the contents of the files..######not completed yet.
'''
        
    def process_check(copiedFolder,originalFolder,log):
        
        if( copiedFolder == originalFolder):
                log.write( "\t #복사 성공#" + "\t :)")
                log.write("\n")
                log.write("\t\t\t\t\t\t\t"+(str(len(os.listdir(toDirectory)))+"파일 복사 완료")+"("+str(copiedFolder*100/originalFolder)+"%)")
                star(log)
        #else:
                #log.write('\t #!!복사 실패!!#' +"\tX(\n")
                #file_check(fromDirectory,toDirectory,log)



    #Reporting on nominal bytes and other folders which may have discreted.    
    def file_check(self,originalDirectory,
                   newDirectory,log,e):
        if str(e).find("not a directory")  !=-1:
##                log.write("\n\n이유: \t" + str(e).decode('cp949').encode('cp949')+"\n");
##                suggestion.append(str(originalDirectory).decode('cp949').encode('cp949')+"\n")
##                internalError.append(str(originalDirectory).decode('cp949').encode('cp949')+"\n")
##                error_writing(str(e).decode('cp949').encode('cp949'),log);
##                error_reports(str(e).decode('cp949').encode('cp949'))
                return None
>>>>>>> refs/remotes/origin/master
        olDfiles = os.listdir(originalDirectory)
        neWfiles = os.listdir(newDirectory)
        olDname = []
        neWname = []
<<<<<<< HEAD
        olDfilesSize = _get_size(originalDirectory)
        neWfilesSize = get_size(newDirectory)
        #=======================================================================
        #======================================================================= Process #1
=======
        olDfilesSize = get_size(originalDirectory)
        neWfilesSize = get_size(newDirectory)
>>>>>>> refs/remotes/origin/master
        for i in range(0,len(olDfiles)):
            global totaLfileCounter
            totaLfileCounter = i
            olDname.append( originalDirectory+"\\"+str(olDfiles[i]))
        for i in range(0, len(neWfiles)):
            global fileCounter
            fileCounter = i
            neWname.append( newDirectory+"\\"+str(neWfiles[i]))
<<<<<<< HEAD
        #======================================================================= Process #2
        log.describe(unicode_conversion("전체 파일 ") +str(totaLfileCounter)+unicode_conversion("중")+str(fileCounter)+unicode_conversion("파일 복사 완료"))
        difference = list(set(olDfiles)-set(neWfiles))
       
        if( difference == None):
             for i in range(0, len(olDname)):
                 constant = os.stat(olDname[i]).st_size-os.stat(neWname[i]).st_size
                 if(constant !=0):
                      log.describe(unicode_conversion("실패한 파일:\t") + unicode_conversion((originalDirectory[i]))+unicode_conversion("\n 잃어버린 바이트 :\t") +loss_byte(constant,log))
        else: 
             for i in range(0,len(difference)):
                  constant = os.stat(originalDirectory+"\\"+str(difference[i])).st_size
                  log.describe(unicode_conversion("\n\n실패한폴더:\t")+(unicode_conversion(difference[i]))+"\n") #cannot calculate when there is a permission lock on the file. .
                  if(constant !=0):
        #            draw the line.
                     log.describe(unicode_conversion("잃어버린자료 용량 :\t") +loss_byte(constant,log))
        #            draw the line        
        #======================================================================= Termination
    def _get_size(startPath):
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
            log.describe(str(Constant2 +unicode_conversion("\t바이트\n")),text)
        elif (1e3<Constant2< 1e6):
            log.describe(str(Constant2*1e-3) +unicode_conversion("\t킬로바이트\n"),text)
        elif (1e6<Constant2<1e9):
            log.describe(str(Constant2*1e-6) +unicode_conversion("\t메가바이트\n"),text)
        elif (1e9<Constant2<1e12):
            log.describe(str(Constant2*1e-9) +unicode_conversion("\t기가바이트\n"),text)

            
def unicode_conversion(text):
    # May need to fix it before the submission.
    return str(unicode(text, 'utf-8').decode('cp949'))
=======
        log.write("전체 파일 " +str(totaLfileCounter)+"중"+str(fileCounter)+"파일 복사 완료")
        difference = list(set(olDfiles)-set(neWfiles))
        #폴더가 복사가 안된 경우 에만 가능
        if( difference == None):# 폴더갯수가 같을때
            for i in range(0, len(olDname)):
                constant = os.stat(olDname[i]).st_size-os.stat(neWname[i]).st_size
                if(constant !=0):
                    suggestion.append(originalDirectory+"\\"+str(olDname[i]).decode('cp949').encode('cp949'))
                    suggestion.append("\t 다시 백업을 요청합니다")
                    star(log)
                    log.write("실패한 파일:\t" + str(originalDirectory[i]).decode('cp949').encode('cp949')+"\n 잃어버린 바이트 :\t" +loss_byte(onstant,log))
                    log.write("\n\n이유: \t" + str(e).decode('cp949').encode('cp949')+"\n");
                    error_writing(str(e).decode('cp949').encode('cp949'),log);
                    internalError.append(str(olDname[i]).decode('cp949').encode('cp949'))
                    error_reports(str(e).decode('cp949').encode('cp949'))
                    star(log)
        else: # 폴더 갯수가 다를때
            for i in range(0,len(difference)):
                internalError.append(originalDirectory+"\\"+difference[i].decode('cp949').encode('cp949'))
                suggestion.append(originalDirectory+"\\"+difference[i].decode('cp949').encode('cp949'))
                constant = os.stat(originalDirectory+"\\"+str(difference[i])).st_size
                log.write("\n\n실패한 폴더:\t"+(str(difference[i]).decode('cp949').encode('cp949'))+"\n") #접근 권한이 없으면 그 내용물의 용량도 볼수가 없다.
                log.write("\n\n이유: \t" + str(e).decode('cp949').encode('cp949')+"\n");
                error_writing(str(e).decode('cp949').encode('cp949'),log);
                log.write("\n\n")
                error_reports(str(e).decode('cp949').encode('cp949'))
                if(constant !=0):
                    star(log)
                    log.write("잃어버린 자료 용량 :\t" +loss_byte(constant,log))
                    star(log)        


    @staticmethod
    def loss_byte(Constant2,log): #바이트 유닛 변환기
        if (Constant2 <1e3):
            log.write(str(Constant2 +"\t바이트"))
        elif (1e3<Constant2< 1e6):
            log.write(str(Constant2*1e-3) +"\t킬로바이트")
        elif (1e6<Constant2<1e9):
            log.write(str(Constant2*1e-6) +"\t메가바이트")
        elif (1e9<Constant2<1e12):
            log.write(str(Constant2*1e-9) +"\t메가바이트")
>>>>>>> refs/remotes/origin/master
