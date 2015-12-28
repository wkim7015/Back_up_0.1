#-*- coding: cp949 -*-


#import libraries
import shutil
import os
import time
from datetime import timedelta
from datetime import date
from datetime import datetime
import stat
from distutils.dir_util import copy_tree
import sys
import traceback
import calendar
import string
#import markdown
from distutils.dir_util import mkpath
from distutils.errors import DistutilsFileError
from distutils.file_util import copy_file

from address_function import extract_address

import unittest

class TESTcopy_address(unittest.TestCase):

    # test begins!

    def test_copy_address_address(self):  #주소 복사 검사

        test_copy = extract_address( "C:\Users\Hojin\Desktop\test_null_address.txt", "D:\\",
                                     '2015-12-14', None, "txt" ).copy_address( "C:\Users\Hojin\Desktop\exp02\n" )
        correctString = "C:\Users\Hojin\Desktop\exp02"
        self.assertEqual(test_copy,correctString)
        test_copy = extract_address( "C:\Users\Hojin\Desktop\test_null_address.txt",
                                     "D:\\", '2015-12-14', None, "txt" ).copy_address( "C:\\Users\\Hojin\\Desktop\\exp01\n" )
        correctString = "C:\Users\Hojin\Desktop\exp01"
        self.assertEqual(test_copy,correctString)
        
    def test_copy_address_isNone(self): #None 일경우 복사 가 되는지 검사 
        test_copy = extract_address("C:\Users\Hojin\Desktop\test_null_address.txt","D:\\", '2015-12-14', None, "txt" ).copy_address( None )
        correctString =''
        self.assertEqual(test_copy,correctString)
        
    def test_copy_address_is_space(self): # 빈 공간이 있을시 복사가 되는지 검사
        test_copy = extract_address("C:\Users\Hojin\Desktop\test_null_address.txt", "D:\\", '2015-12-14', None, "txt" ).copy_address( ' ' )
        correctString =''
        self.assertEqual(test_copy,correctString)
        
    def test_copy_address_line_space(self): # 엔터 키가 눌려진 경우 복사가 되는 지 검사
        test_copy = extract_address("C:\Users\Hojin\Desktop\test_null_address.txt", "D:\\", '2015-12-14', None, "txt" ).copy_address( '\n' )
        correctString =''
        self.assertEqual(test_copy,correctString)


class TESTget_address(unittest.TestCase):

    def test_get_address(self): #주소를 가져오는지 검사
        test_link = open ( r"C:\Users\Hojin\Desktop\test_address.txt", 'r' )
        testArray = extract_address( "C:\Users\Hojin\Desktop\test_null_address.txt",
                                     "D:\\", '2015-12-14', None, "txt" ).get_address( test_link )
        trueArray = [ "C:\Users\Hojin\Desktop\exp02","C:\Users\Hojin\Desktop\exp1",
                     "C:\Users\Hojin\Desktop\ 새 폴더","C:\Users\Hojin\Desktop\\remove_expire.pyc", "D:\Fakefiles.txt" ]
        self.assertEqual(testArray,trueArray)
        
    def test_null_address(self): #주소가 None 이나 빈공간 그리고 엔터키가 눌려진 공간과 섞여있을경우 주소를 가져오는지 검사
        
        test_link2 = open (r"C:\Users\Hojin\Desktop\test_null_address.txt",'r')
       
        testArray = extract_address("C:\Users\Hojin\Desktop\test_null_address.txt",
                                    "D:\\", '2015-12-14', None, "txt" ).get_address( test_link2 )
        
        trueArray = ["C:\Users\Hojin\Desktop\exp02","C:\Users\Hojin\Desktop\exp1",
                     "C:\Users\Hojin\Desktop\ 새 폴더","C:\Users\Hojin\Desktop\\remove_expire.pyc", "D:\Fakefiles.txt" ]
       
        self.assertEqual( testArray, trueArray )


class TESTmain(unittest.TestCase):

    def test_main_01(self):
        
        test_link2 = open ( r"C:\Users\Hojin\Desktop\test_null_address.txt",'r' )
        #print test_link2
        testArray = extract_address( "C:\Users\Hojin\Desktop\test_null_address.txt",
                                     "D:\\", '2015-12-14', None, "txt" ).main( test_link2 )
        #print testArray
        trueArray = [ "C:\Users\Hojin\Desktop\exp02","C:\Users\Hojin\Desktop\exp1",
                      "C:\Users\Hojin\Desktop\ 새 폴더","C:\Users\Hojin\Desktop\\remove_expire.pyc", "D:\Fakefiles.txt" ]
        #print trueArray
        self.assertEqual( testArray, trueArray )

if __name__ == '__main__': 

    unittest.main()
