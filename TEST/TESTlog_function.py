#-*- coding: utf-8 -*-

import unittest
import sys
import os.path
sys.path.append(os.path.realpath('..'))
from log_function import *
from datetime import *

import string
import random

###########################======================================
# textfile paths. Any name can be used.However, the paths must be precised.

directoryName = os.path.dirname(__file__)
input1 = directoryName+"\\testfile.txt"
input3 = directoryName+"\\될까!!@!!!@!%^$#@%#^%#&.txt"
input4 = directoryName+"\\testfiletxt"
input5 = directoryName+"\\tEstFile2.tXT"
input6 = directoryName+"\\tEstFile3.tXT"
input2 = directoryName+"\\될까.txt"

###########################======================================
# text and directory paths to keep logs. Be aware of the directoryPath which needs to be emptied, for simplicity's sake.

textPath = "C:\\Users\\Hojin\\Desktop\\테스트파일.txt"
directoryPath = "C:\Users\Hojin\Desktop\새 폴더 (2)"

###########################======================================


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
      return ''.join(random.choice(chars) for _ in range(size))

class TESTget_current_time(unittest.TestCase):
    
    def test_time(self):
        time = datetime.now().replace(second=0, microsecond=0)
        time_2 = text_log.get_current_time()
        self.assertEqual(time,time_2)
        
def check_file(string):
    
    return os.path.isfile(string)

def create_text_log(string):

    text_log().make_report(string)

def test_log(string):

    create_text_log(string)

    return check_file(string)
    
class TESTmake_report_open_report(unittest.TestCase):

    global input1
    global input3
    global input4
    global input5
    global input6
    global input2
      
    path =  (input1).decode('cp949').encode('cp949')
    #path2 =  ("D:\\Users\\Hojin\\Desktop\\testfile.txt").decode('cp949').encode('cp949') #> 디렉토리가 없을시, 변환 불가능. open 에서 에러
    path3 =  (input3).decode('cp949').encode('cp949') # 만약 \\ 가 안될시? : eclipse 폴더 안에 저장됨
    #path4 =  (input4).decode('cp949').encode('cp949') #민약 파일이름이 기호 일시 실험 >기호사용한 이름 파일 지원 불가능
    path5 =  (input4) #만약 파일이름이 한국어 일때 실험 > 가능
    String = (input5) #Result: create the file without extension
    capitalString = (input2) # worked
    backString = (input6) #검사 완료
    #no way for escape strings
    def test_existence(self):# worked.
        file2 = text_log().make_report(self.path3)
        file_check1  = os.path.isfile(self.path3)
        self.assertTrue(file_check1,msg = 'True')


    def test_koreanfilename(self): #worked
        file5 = text_log().make_report(self.path5)
        file_check2 = os.path.isfile(self.path5)
        self.assertTrue(file_check2,msg = 'True')


    def test_existence2(self): #worked   

        file1 = text_log().make_report(self.path)

        file_check0 = os.path.isfile(self.path)
        self.assertTrue(file_check0, msg='True')

        
    def test_extension_difference(self): 
        T_file = text_log().make_report(self.String)
        s = check_file(self.String)
        self.assertTrue(s, msg = "True") 


    def test_Capital_letter(self):
        create_text_log(self.capitalString)
        s = check_file(self.capitalString)
        self.assertTrue(s,msg = "True")


    def test_escapeString(self):
        s = test_log(self.backString)
        self.assertTrue(os.path.isfile(self.backString),msg = "True")
          

class TESTlog(unittest.TestCase):
      
      global textPath
      path =textPath
      text = text_log()
      textfile = text.make_report(path)

    
      def test_initial(self):
          textfile = self.text.make_report(self.path)
          os.remove(self.path)
          self.text.initial(self.path) #manually checked
          lines = [line.rstrip('').decode('cp949').encode('cp949') for line in open(self.path)]
          check_lines = [str(date.today())+"\t\t\t에러 리포트\n","\n","\t\n",
                       "사용한 텍스트 파일 주소:\t"+self.path+"\n","\n","로그 시작한 시간:\t\t "+str(datetime.now().replace(second=0, microsecond=0))+"\n","\n","\n",
                       "\t\t" +"\t백업 과정 보고서\n","\n","\n"]
          print set(lines)-set(check_lines)
          self.assertEqual(lines,check_lines)

    
      def test_success(self):

              text = text_log()
              os.remove(self.path)
              text.success(self.path)
        
              lines = [line.rstrip('\n').decode('cp949').encode('cp949') for line in open(self.path)]
              check_lines = ["성공여부\t\t**\t #!!복사 성공!!#\t:)\n".rstrip('\n'),"코멘트\t\t\t\t"]
            
              self.assertEqual(lines,check_lines)

    
      def test_failed(self):
           
              text = text_log()
              os.remove(self.path)
              text.failed(self.path)
              lines = [line.rstrip('\n').decode('cp949').encode('cp949') for line in open(self.path)]
              check_lines = ["성공여부\t\t**\t #!!복사 실패!!#".rstrip('\n')+ "\tX(\n".rstrip('\n'),"코멘트\t\t\t\t"]
              self.assertEqual(lines,check_lines)
                                                        
      def test_writeError(self):
               text = text_log()
               os.remove(self.path)
               text.error(self.path, "에러입니다?#@!(*&^$@!#%^&")
               lines = [line for line in open(self.path)]
               check_lines=["에러입니다?#@!(*&^$@!#%^&\n"]
               self.assertEqual(lines,check_lines)
        
class TESTfinal(unittest.TestCase):
    
    #가장 중요한 메인 함수 두개 검사. 

    pathDirectory = directoryPath
    
    if not os.path.isdir(pathDirectory):
          os.mkdir(pathDirectory)
    N = 3000
    F = 7000
    text_log().make_report(pathDirectory+"\error.txt")
    path = pathDirectory+"\error.txt"


    def test_make_reportfile(self):
        
        for i in range(0, self.N):
             x = id_generator()
             file2 = text_log().make_report(self.pathDirectory+"\\"+x+".txt")
             file_check1  = os.path.isfile(self.pathDirectory+"\\"+x+".txt")
             self.assertTrue(file_check1,msg = "True")

    
    def test_writeError(self):
        
        for i in range(0, self.F):
            x = id_generator()
           # os.remove("C:\Users\Hojin\Desktop\새 폴더 (2)\error.txt")
            text_log().make_report(self.pathDirectory+"\error.txt")
            text = text_log()
            text.error(self.path, x)
            lines = [line.rstrip("\n") for line in open(self.path)]
            check_lines=[x]
            self.assertEqual(lines,check_lines)  

             
if __name__ == '__main__': 

    unittest.main()
        
