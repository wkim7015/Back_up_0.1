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

reportName = "Errorreports.txt"

directoryPath = "C:\Users\Hojin\Desktop\\address.txt"

# additional parameters

drive = "D:\\"


folderName = drive+str(date.today())
reportPath = folderName +"\\"+reportName
if __name__ == "__main__":
    
    global reportPath
    global directoryPath
    global drive6
    global folderName
    
    try:
        #need to make the directory before make the text.
        if not os.path.exists(folderName):
            os.makedirs (folderName)

        print reportPath
        text = text_log()
        text.make_report(reportPath)
      
        text.initial(reportPath)

        text.final(reportPath)
        text.success(reportPath)
        
    except Exception as e:
        
        text.final(reportPath)
        
        text.failed(reportPath)
        
        text.error(reportPath,str(e))    

    finally:
        
        function_address = extract_address()
        
        address = function_address.main(open(directoryPath))
        
        ''' Copy the given directory
        '''
        counter = 0
        print address
        while counter < len(address) and address[counter] is not None:
                
            print counter
            copy_folder(address[counter], reportPath, drive)
            counter +=1
            print counter 
        ''' Remove the expired folders
        '''
        remove_expire(drive)
        
        
        # may need to check whether below lines are going to 
        #executed, no matter of the errors. >used "finally"
        
