##-*- coding: cp949 -*-
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
from distutils.dir_util import mkpath
from distutils.errors import DistutilsFileError
from distutils.file_util import copy_file



class extract_address():

 
    result = []
  
    address = ""



    def main(self,address):
        # 메인 함수; 로그 작성과 폴더 주소를 상위함수 로 전달

        
        flag = 0
        counter = 0
            
        self.get_address(address)
        return result
    
    def get_address(self,address):		#  폴더의 주소를 복사 를 ARRAY 에 복사하는 함수. 

       
        global result
        del result[:]
        path = address
        while not path is '' and not path is ' ':
            path = ((address.readline()))
            addressResult = self.copy_address(path)
            if( addressResult != '' and addressResult != 'None'):
                result.append(addressResult)
        return result    
            

    def copy_address(self,path):		# None 과 빈 공간이 있을시에 주소만 받는 함수.

        if  not path == '' and not path is None and not path.isspace():
            return path[0:len(path)-1] # 바뀜
        else: return ''
