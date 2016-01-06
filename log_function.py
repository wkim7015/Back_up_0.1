#-*- coding: utf-8 -*-
from datetime import *
class text_log():
    

    #drive = ''
    #name = ''
    #fileExtension = ''
    #directory = ''
    #TEXT = ''
    
    @staticmethod
    def get_current_time():
        
        ''' Find the date in which operation performs
        '''
        return datetime.now().replace(second=0,microsecond=0)
    
    
    
    def make_report(self,text):
        

        
        s = unicode_conversion(text)
        open(s,'w')
   

    def _open_report(self,text):
        s = unicode_conversion(text)
        
        return open(s,'a')
    
  
    def initial(self,text):
        '''all of initial writing:  1. the name of the address used
                                    2. today's date
                                    3.  error report name
                                    4. address of the report
                                    
        ''' 
        report = self._open_report(text)
        startTime =self.get_current_time()
        report.write(str(date.today())+unicode_conversion("\t\t\t에러 리포트\n\n"))
        report.write(unicode_conversion("\t\n사용한 텍스트 파일 주소:\t")+text) 
        report.write(unicode_conversion("\n\n로그 시작한 시간:\t\t ")+str(startTime)+"\n")
        report.write(unicode_conversion("\n\n\t\t" +"\t백업 과정 보고서\n\n\n")) 
        
        #return startTime
    def final(self,text):
        
        ''' all of final writing:   1. whether it is succeeded or not
                                    2. completed time difference
                                    3. completed time
        # do we want to implement saving of the data,where the last addressses are saved
        or not?
        > completion time:  bring the datetime.now()
        > completed time difference: can we bring the data from the main function?
        >> no: Do that on the main function
        > succeded or not: may be implmented when divisions of the functions are failed.
        
        '''
        report = self._open_report(text)
        endTime = self.get_current_time()
        report.write(unicode_conversion("\n최종시간:"+"\t"*2 +str(endTime))+"\n"*2)
            
    
   
    def success(self,text):
        
        ''' all of success case     1. success indication
                                    2. report time difference
                                    3. final time
                                    
        '''
        report = self._open_report(text)
        report.write(unicode_conversion("성공여부\t\t**"))
        report.write(unicode_conversion('\t #!!복사 성공!!#'+ "\t:)\n"))
        report.write(unicode_conversion("코멘트\t\t\t\t"))
        report.write("\n")
        
        
        
  
    def failed(self,text):
        
        '''all of failed case     1.  failure indication
                                    2. report time difference
                                    3. final time
        
        '''
        report = self._open_report(text)
        report.write(unicode_conversion("성공여부\t\t**"))
        report.write(unicode_conversion('\t #!!복사 실패!!#'+ "\tX(\n"))
        report.write(unicode_conversion("코멘트\t\t\t\t"))
        report.write("\n")
        
        
        

    def error(self,text,msg):
        ''' write all of the errors into the log
        send the file to bug_database >>not implemented yet. > do we though?
        '''
        report = self._open_report(text)
        #write the errors to the report.
        report.write(unicode_conversion(msg) +"\n")
        
    
    
    @classmethod  
    def get_drive(cls): # left for just in case.
        return cls.drive
    @staticmethod
    def isContain(text):

        if unicode_conversion('실패') in open(text).read():
            return True
        else:
            return False

        
 
    
def unicode_conversion(string):
    return str(unicode(string,"utf-8").encode('cp949'))

