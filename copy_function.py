#-*- coding: cp949 -*-
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
from mhlib import PATH

#copy_folder(TEXTlog=None).folder_copy(TEXTdirectory)?
# TEXTlog is only activated when TEXTlog parameter is given

'''
quota:
1) copy_function 에서 하드코딩된 "D:\\"  를 제거하고 변수(지역 혹은 멤버,  파라메터 등등)로 대치하세요 ()

2) ", " 다음 항상 공백(space)를 넣으세요 ()

3) get_directory_address 등의 파라메터로 넘어오는 드라이브가 "D"  혹은 "D:" 와 같을때 어찌 되는지 테스트를 추가하고,  해당 함수를 처리하세요 ()

4)TESTcopy_function와 TESTmain 의 copytest 에서 사용된 변수 x,  y,  z 의 명칭을 의미를 알 수 있도록 naming 을 다시 해주세요

5) string,  string1,  string2,  test 의 변수명도 의미를 알 수 있도록 naming 을 다시 해주세요. 통상 assert... 함수에서는 assertEqual(expected,  actual) 처럼 변수명을 지정합니다.

6) 폴더이름과 파일이름이 한글이 섞여있거나 한글로된 것,  특수문자가 섞인것의 테스트도 해주세요.

7) TESTmain ,  test_main 등등에서,  명칭때문에 나중에 문제가 되어 이름을 바꾸어야 할 수도 있을것 같습니다. main ,  최종,  final 등의 단어는 사용에 유의해 주세요.

8) copytest 함수가 2개의 class에서 중복으로 사용됩니다. 하나로 합쳐보세요.

9) 공백의 사용이 일정하지 않습니다. = ( ) 등의 부호에 앞뒤로 사용되는 공백(space)를 규칙있게 통일해주세요. 공백이 2개인곳은 1개로 변경해주세요.
'''

'''
2.5 ": copy_tree version
"""Copy an entire directory tree 'src' to a new location 'dst'.
    Both 'src' and 'dst' must be directory names.  If 'src' is not a
    directory,  raise DistutilsFileError.  If 'dst' does not exist,  it is
    created with 'mkpath()'.  The end result of the copy is that every
    file in 'src' is copied to 'dst',  and directories under 'src' are
    recursively copied to 'dst'.  Return the list of files that were
    copied or might have been copied,  using their output name.  The
    return value is unaffected by 'update' or 'dry_run': it is simply
    the list of all files under 'src',  with the names changed to be
    under 'dst'.
    'preserve_mode' and 'preserve_times' are the same as for
    'copy_file'; note that they only apply to regular files,  not to
    directories.  If 'preserve_symlinks' is true,  symlinks will be
    copied as symlinks (on platforms that support them!); otherwise
    (the default),  the destination of the symlink will be copied.
    'update' and 'verbose' are the same as for 'copy_file'.
'''

class copy_folder():
    
    #2) ", " 다음 항상 공백(space)를 넣으세요 ()
    
    #log = text_log ()
    
    def __init__(self, directory_path, log_path, drive):
        
        #try: 
            self.path = directory_path
            self.log_path = log_path
             #Use the txt log. May other classes will be implemented to ask
            #an opinion of the extensions.
            #log.make_report(log_path)>> do that in the main
            self.copy_function(directory_path,  log_path, drive)
        #except Exception as e:
            #log.error(self.log_path, str(e))

    def copy_function(self ,  path,  log_path, drive):
        
        #copy_function to copy_folder_function

        #1) copy_function 에서 하드코딩된 "D:\\"  를 제거하고 변수(지역 혹은 멤버,  파라메터 등등)로 대치하세요 () >>완료
        if(path != None) or (not path.isspace()):
            
            #drive = log_path[0]
            #print drive
            # the above implementation is only when log_path is null.
            # where it cannot be NULL. fix the "find" quote.
            to_path = self.get_directory_address(path,  drive)
            from_path = str(path)
            copy_tree(from_path, to_path)
            
        else:
            
            print ""
            
    def get_directory_address(self, path, drive):
        
        #3) get_directory_address 등의 파라메터로 넘어오는 드라이브가 "D"  혹은 "D:" 와 같을때 어찌 되는지 테스트를 추가하고,  해당 함수를 처리하세요 ()
        #> 공통점 : 첫글자는 드라이브.
         
        ''' 저장되는 디렉토리는 LOG 의 주소를 따름.
        '''
        
        name = path[path.rfind("\\") +1:len(path)].replace(":","")
           #new_directory to toDirectory      
        propeRdrive = self._drive_correction(drive)
        new_directory = propeRdrive+str(date.today()) + "\\" + name
        if not os.path.exists(new_directory):
            os.makedirs (new_directory)
        else: pass
        return new_directory
    
    def _drive_correction(self, drive):
        
        ''' drive:
           if drive is null : pass .\\ by copy_function >> Hence,  do nothing
           if drive is .\\  : pass
           if drive is given by D (the first letter) : append :\\ at the end of the string
           if drive is given by D:    :     append \\ at the end of the string.
        '''
        
        if drive == ".\\"   :   return ".\\"
        elif len(drive) == 1 :  return drive +":\\" 
        elif drive.find(":") != -1 : 
            if os.path.exists(drive+".\\") : return drive
            else : return ".\\"
        else : return ".\\"
 
        
        
        
        
            
            
        
    
