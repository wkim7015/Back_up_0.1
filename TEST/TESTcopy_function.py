#-*- coding: utf-8 -*-
import unittest
import sys
sys.path.append("C:\\Users\\Hojin\\Desktop\\TEST\\Back_up_0.1-master")
#from text_log import *
from copy_function import *
from datetime import date

def code(s):
    return str(s).decode('cp949').encode('cp949')

'''
test the robustness of copy_folder function

To satisfy the conditions,

1. folder must not be copied twice. >> addressed.

2. any name, including non ASCII code, needs to be copied without
 any association
with the interpreter        >fxed

3. any name, including non ASCII code, needs to be addressed 
without any association
with the interpreter    >> fixed

4. escape copied_address validation >> may be implemented as an option  e.g \\a > \a : don't need to: approximated to be a copy_tree error.
5.  can we test copy_tree function as the individual implemented f?
6. ... 
'''

#5) copied_address, from_address, copied_address, test 의 변수명도 의미를 알 수 있도록 naming 을 다시 해주세요. 통상 assert... 함수에서는 assertEqual(expected, actual) 처럼 변수명을 지정합니다.
#> 완료

#9) 공백의 사용이 일정하지 않습니다. = () 등의 부호에 앞뒤로 사용되는 공백(space)를 규칙있게 통일해주세요. 공백이 2개인곳은 1개로 변경해주세요. >완료 그리고 3번 검사. 

####################=====================================================
"INPUTS"

path = "C:\Users\Hojin\Desktop\\backup"
pathKorean = "C:\Users\Hojin\Desktop\\테스트1"
pathSpecial = "C:\Users\Hojin\Desktop\\테스트1%^&&&^%%$##!#$&&^$#()_+=" 
pathProtected ="C:\Users\Hojin\Desktop\\protectedtest"
driveName = "D"

####################=====================================================

drive = driveName +":\\"


def get_name(path):

    return path[path.rfind("\\") +1:len(path)]

class TESTget_directory_address(unittest.TestCase): #Create a method to extract the name of the folder.
    
    '''
    get_directory_address requires 2 parameters, in which path and drive
    of the copied address are required. 
    '''

    def test_get_directory_address(self):
        
        '''
        use drive as D drive and print whether the path exists
        and return its appropriate format where the date and teh copied_address of
        the new directory must be returned
        '''
        global path
        global drive
        copied_address = drive+str(date.today()) +"\\"+get_name(path)
        test = copy_folder(path, None, drive).get_directory_address(path, drive)
        actual = copied_address
        expected = test
        self.assertEqual(expected, actual)

    def test_get_directory_address_korean(self):
        
        global pathKorean
        path = pathKorean
        global drive
        copied_address  = drive+str(date.today())+"\\"+get_name(pathKorean)
        test = copy_folder(path, None, drive).get_directory_address(path, drive)
        expected = test
        actual = copied_address
        self.assertEqual(expected, actual)

    def test_get_directory_address_drive(self):
        
        ''' the case of the drive is not with back-slash but itself.
        #3) get_directory_address 등의 파라메터로 넘어오는 드라이브가 "D"  혹은 "D:" 와 같을때 어찌 되는지 테스트를 추가하고, 해당 함수를 처리하세요 () 
        '''
        global pathKorean
        path = pathKorean
        global drive
        copied_address  = drive+str(date.today())+"\\"+get_name(pathKorean)
        test = copy_folder(path, None, drive).get_directory_address(path, drive)
        expected = test
        actual = copied_address
        self.assertEqual(expected, actual)

#8) copytest 함수가 2개의 class에서 중복으로 사용됩니다. 하나로 합쳐보세요. >완료

#4)TESTcopy_function와 TESTmain 의 copytest 에서 사용된 변수 x, y, z 의 명칭을 의미를 알 수 있도록 naming 을 다시 해주세요 >완료

def copytest(test):
    
    # 파일 갯수  검사하는 함수  
    
    directoryName = []
    fileName = []
        
    for root, directories, filenames in os.walk(test):
        for directory in directories:
                directoryName.append(os.path.join(root, directory))
        for filename in filenames: 
                fileName.append(os.path.join(root,filename))
    name=directoryName+fileName
    return name

class TESTcopy_function(unittest.TestCase):
    
    def test_copy_function(self):

        global path
        from_address =  copytest(path)
        global drive
        global driveName
        test = copy_folder(path, None , driveName).copy_function(path, drive+str(date.today())+"\\"+get_name(path), "D")
        copied_address = copytest(drive+str(date.today())+"\\"+get_name(path))
        expected = len(from_address)
        actual = len(copied_address)
        self.assertEqual(expected, actual)

    #없는 파일 복사 시도 >> copy_tree 디렉토리 에러 발견
    def test_copy_function_not_exists(self):
        
        global drive
        global driveName
        path = "C:\Users\Hojin\Desktop\\backup\\notexists"
        from_address =  copytest(path)
        test = copy_folder(path, None , driveName).copy_function(path, drive+str(date.today())+"\\"+get_name(path), "d")
        copied_address = copytest(drive+str(date.today())+"\\"+get_name(path))
        expected = len(from_address)
        actual = len(copied_address)
        self.assertEqual(expected, actual) # 없기때문에 복사 불가능
        
            

#7) TESTmain , test_main 등등에서, 명칭때문에 나중에 문제가 되어 이름을 바꾸어야 할 수도 있을것 같습니다. main , 최종, final 등의 단어는 사용에 유의해 주세요. >main 을 all 로 번경 완료

class TESTMain(unittest.TestCase):
    
    #6) 폴더이름과 파일이름이 한글이 섞여있거나 한글로된 것, 특수문자가 섞인것의 테스트도 해주세요. >완료
    
    def test_special_characters(self):
        
        ''' 
                폴더 이름 : 테스트1%^&&&^%%$##!#$&&^$#()_+=
    
                그 안에 있는 파일 이름: 테스트파일 %^&&&^%%$##!!#$&&^$#()_+= 
        '''
             
        global pathSpecial
        path = pathSpecial
        global drive
        global driveName
        from_address = copytest(path)
        test = copy_folder(path, None, driveName)
        copied_address = copytest(drive+str(date.today())+"\\"+get_name(pathSpecial))
        expected = len(from_address)
        actual = len(copied_address)
        self.assertEqual(expected, actual)
        
        
    def test_all(self):
        
        global path
        global drive
        global driveName
        from_address =  copytest(path)
        test = copy_folder(path, "anylog:not_going_to_test_here", driveName)
        copied_address = copytest(drive+str(date.today())+"\\"+get_name(path))
        expected = len(from_address)
        actual = len(copied_address)
        self.assertEqual(expected, actual)

    def test_protected_file(self): # 에러:  ERRNO 13 : 권한 에러 > copy_tree 에러.
        
        path = "C:\Users\Hojin\Desktop\\protectedtest"
        global pathProtected
        global drive
        global driveName
        path = pathProtected
        from_address =  copytest(path)
        test = copy_folder(path, "log:not_going_to_test_here", driveName)
        copied_address = copytest(drive+str(date.today())+"\\"+get_name(pathProtected))
        expected = len(from_address)
        actual = len(copied_address)
        self.assertEqual(expected, actual)

if __name__ == '__main__':

    # 총 에러 가 나오는 숫자 :3.
    
    #에러 가 나오더라도 폴더 복사 완료 > Q2

    unittest.main()
        
