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
sys.path.append(os.path.realpath('..'))
import traceback
import calendar
import string
#import markdown
from distutils.dir_util import mkpath
from distutils.errors import DistutilsFileError
from distutils.file_util import copy_file
####### importing files
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
sys.path.append(os.path.realpath('..'))
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
from security_function_L1 import security_byte
# import admin
#if not admin.isUserAdmin():
#       admin.runAsAdmin()

#import TESTS
import sys
import gc
# Input parameters

###########################################################################==================================================


reportName = "Errorreports.txt" #name of the file and the extension for a log

directoryPath = "C:\Users\Hojin\Desktop\\address.txt"

# additional parameters

drive = "D:\\"  #where do you want to save( directory path)



#The below is optional.


##email =

##password =

##addresses =


############################################################################==================================================



if not os.path.exists(drive[0]+":\\"):
    drive = ".\\"

folderNameDate = drive+str(date.today())
folderNameTime = drive +str(datetime.now().strftime('%Y-%m-%d_%H'))
#print folderNameTime
#print folderNameDate
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
    

    errorFlag = 0
    flag = 0
    global directoryPath
    global drive
    global folderNameDate
    global folderNameTime
    ##  global email
    ##  global password
    ##  global addresses
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
        ##text.send_email(email,password,addresses)
        text.make_report(reportPath)
        text.initial(reportPath)
        function_address = extract_address()
        
        address = function_address.main(open(directoryPath))
        
        ''' Copy the given directory
        '''
        counter = 0
        while counter < len(address) and address[counter] is not None:

            copy_folder(address[counter], reportPath, drive,flag)
            newAddress = copy_folder(address[counter], reportPath, drive,flag).get_directory_address(address[counter],drive,flag)
            ### do it here.=====================================
            '''address[counter] : the originalDirectory address
               newDirectory = : get directory address  from the copy folder
                (path, drive parameters are required) :address[counter],drive)               
               securityL1 = security_byte()
               securityL1.file_check(address[counter, newDirectory, reportPath)
            '''
            securityL1 = security_byte()
            #print newAddress
            #print address[counter]
            securityL1.file_check(address[counter], newAddress, reportPath)
            
            
            ###=================================================
            counter +=1

        #dump_garbage()
    except Exception as e:
            #print str(e)
            text = text_log()
            if not text.finalContain(reportPath):
                text.failed(reportPath)
            text.error(reportPath,str(e))
            text.final(reportPath)
        #dump_garbage()

    finally:
       
  
        ''' Remove the expired folders
        '''
        remove_expire(drive)
        reportPath = folderName +"\\"+reportName
        #dump_garbage()
        if(text.isContain(reportPath) is False and text.byteContain(reportPath) is False):
                text.success(reportPath)
        if( text.byteContain(reportPath) is True):
            if(text.finalContain(reportPath) is False):
                text.failed(reportPath)
                
        text.final(reportPath)
        ##text.send_email(email,password,addresses,1) >> need to check the emails.
        
        # may need to check whether below lines are going to 
        #executed, no matter of the errors.
        

