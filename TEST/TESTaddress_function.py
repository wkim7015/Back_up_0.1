#-*- coding: utf-8 -*-


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
sys.path.append("C:\\Users\\Hojin\\Desktop\\TEST\\Back_up_0.1-master")
import calendar
import string
#import markdown
from distutils.dir_util import mkpath
from distutils.errors import DistutilsFileError
from distutils.file_util import copy_file

from address_function import extract_address

import unittest

#########################===========================================================================================
#TEST INPUTS

AddressDirectory ="C:\Users\Hojin\Desktop"
AddressName = "exp02\n"
# if you use AddressName to regarding as inappropriate format, please write the correct format of the name as below.
AddressCorrectName = "exp02"

#########################===========================================================================================

Address= AddressDirectory + AddressName

class TESTcopy_address(unittest.TestCase):

    # test begins!

    def test_copy_address_address(self):  #주소 복사 검사

        global Address

        test_copy = extract_address().copy_address( Address )
        correctString = AddressDirectory+AddressCorrectName
        self.assertEqual(test_copy,correctString)
        #test_copy = extract_address().copy_address( "C:\\Users\\Hojin\\Desktop\\exp01\n" )
        #correctString = "C:\Users\Hojin\Desktop\exp01"
        #self.assertEqual(test_copy,correctString)
        
    def test_copy_address_isNone(self): #None 일경우 복사 가 되는지 검사 
        test_copy = extract_address().copy_address( None )
        correctString =''
        self.assertEqual(test_copy,correctString)
        
    def test_copy_address_is_space(self): # 빈 공간이 있을시 복사가 되는지 검사
        test_copy = extract_address().copy_address( ' ' )
        correctString =''
        self.assertEqual(test_copy,correctString)
        
    def test_copy_address_line_space(self): # 엔터 키가 눌려진 경우 복사가 되는 지 검사
        test_copy = extract_address().copy_address( '\n' )
        correctString =''
        self.assertEqual(test_copy,correctString)

##################################################################==================================================================

'''
Below test requires a text file which contains a set of addresses as an array. Prior running the below function, it is neccessary to
create the text file which contains the the addresses.When the textfiles are downloaded,below parameters do not require to change.
'''
textFile = r"C:\Users\Hojin\Desktop\test_address.txt"

"Then, please write the paths of the addresses below the array."

trueArray = [ "C:\Users\Hojin\Desktop\exp02","C:\Users\Hojin\Desktop\exp1",
                     "C:\Users\Hojin\Desktop\ 새 폴더","C:\Users\Hojin\Desktop\\remove_expire.pyc", "D:\Fakefiles.txt" ]

###################################################################==================================================================

class TESTget_address(unittest.TestCase):

    def test_get_address(self): #주소를 가져오는지 검사

        global textFile
        global trueArray
        test_link = open ( textFile, 'r' )
        testArray = extract_address().get_address( test_link )
        #trueArray = [ "C:\Users\Hojin\Desktop\exp02","C:\Users\Hojin\Desktop\exp1",
        #             "C:\Users\Hojin\Desktop\ 새 폴더","C:\Users\Hojin\Desktop\\remove_expire.pyc", "D:\Fakefiles.txt" ]
        self.assertEqual(testArray,trueArray)
        
    def test_null_address(self): #주소가 None 이나 빈공간 그리고 엔터키가 눌려진 공간과 섞여있을경우 주소를 가져오는지 검사
        
        test_link2 = open (r"C:\Users\Hojin\Desktop\test_null_address.txt",'r')
       
        testArray = extract_address().get_address( test_link2 )
        
        trueArray = ["C:\Users\Hojin\Desktop\exp02","C:\Users\Hojin\Desktop\exp1",
                     "C:\Users\Hojin\Desktop\ 새 폴더","C:\Users\Hojin\Desktop\\remove_expire.pyc", "D:\Fakefiles.txt" ]
       
        self.assertEqual( testArray, trueArray )


class TESTmain(unittest.TestCase):

    def test_main_01(self): #given
        
        test_link2 = open ( r"C:\Users\Hojin\Desktop\test_null_address.txt",'r' )
        #print test_link2
        testArray = extract_address().main( test_link2 )
        #print testArray
        trueArray = [ "C:\Users\Hojin\Desktop\exp02","C:\Users\Hojin\Desktop\exp1",
                      "C:\Users\Hojin\Desktop\ 새 폴더","C:\Users\Hojin\Desktop\\remove_expire.pyc", "D:\Fakefiles.txt" ]
        #print trueArray
        self.assertEqual( testArray, trueArray )

if __name__ == '__main__': 

    unittest.main()
