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
#from . import address_function
#from . import copy_function
#from . import log_function
#from . import remove_function




#import TESTS
import sys
import gc
# Input parameters

###########################################################################==================================================


reportName = "Errorreports.txt" #name of the file and the extension for a log

directoryPath = "C:\Users\Hojin\Desktop\\address.txt"

# additional parameters

drive = "D:\\"  #where do you want to save( directory path)



############################################################################==================================================



if not os.path.exists(drive[0]+":\\"):
    drive = ".\\"

folderNameDate = drive+str(date.today())
folderNameTime = drive +str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

'''Garbage checking
'''
def dump_garbage():
    print "GARBAGE"
    gc.collect()
    print "\nGARBAGE OBJECTS:"
    for x in gc.garbage:
        s = str(x)
        print type(x),"\n",s



if __name__ == "__main__":

    #gc.enable()
    #gc.set_debug(gc.DEBUG_LEAK)
    


    flag = 0
    global directoryPath
    global drive
    global folderNameDate
    global folderNameTime
    reportPath = ''
    folderName = ''
    try:
        #need to make the directory before make the text.
        #global reportPath
        folderName = folderNameDate
        if not os.path.exists(folderName):
            os.makedirs (folderName)
        else:
            folderName = folderNameTime
            flag = 1
            os.makedirs (folderName)
        reportPath = folderName +"\\"+reportName
        text = text_log()
        text.make_report(reportPath)
        text.initial(reportPath)
        function_address = extract_address()
        
        address = function_address.main(open(directoryPath))
        
        ''' Copy the given directory
        '''
        counter = 0
        while counter < len(address) and address[counter] is not None:

            copy_folder(address[counter], reportPath, drive,flag)
            counter +=1

        #dump_garbage()
    except Exception as e:
        
        print str(e)
        text.failed(reportPath)
        
        text.error(reportPath,str(e))

        #text.final(reportPath)
        #dump_garbage()

    finally:
       
  
        ''' Remove the expired folders
        '''
        remove_expire(drive)
        reportPath = folderName +"\\"+reportName
        #dump_garbage()
        if(text.isContain(reportPath) is False):
            text.success(reportPath)
        text.final(reportPath)
    
        
        # may need to check whether below lines are going to 
        #executed, no matter of the errors.
        

