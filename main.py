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
import calendar
import string
#import markdown
from distutils.dir_util import mkpath
from distutils.errors import DistutilsFileError
from distutils.file_util import copy_file
####### importing files
from address_function import extract_address
from copy_function import copy_folder
from log_function import text_log
from remove_function import remove_expire

# Input parameters

reportPath = ""

directoryPath = "" 

# additional parameters

drive = ""

if __name__ == "__main__":
    
    global reportPath
    global directoryPath
    global drive
    
    try:
        
        text = text_log()
        text.make_report(reportPath)
        
        function_address = extract_address()
        
        text.initial(reportPath)
        
        address = function_address(directoryPath)
        
        ''' Copy the given directory
        '''
        counter = 0
        while address[counter] is not None:
            copy_folder(address, log_path, drive)
            counter +=1
            
        ''' Remove the expired folders
        '''
        remove_expire()
        
        
        # may need to check whether below lines are going to 
        #executed, no matter of the errors.
        text.final(reportPath)
        text.success(reportPath)

    except Exception as e:
        
        print str(e)
        text.final(reportPath)
        
        text.failed(reportPath)
        
        text.error(reportPath,str(e))
        
