#-*- coding: utf-8 -*-
import zipfile
    ##
    ##myzip = zipfile.ZipFile('D:\\2016-01-19\Zipfile.zip','w')
    ##myzip.write('C:\Users\Hojin\Desktop\\backup') #REQUIRE ISDIR
    ##    
    ##myzip.close()

import os

## Need debugging!!

class zip():

    def zip_directory(self,path, drive, name, flag = 0):
	# path is the address[counter]
	#drive is different drive, need to be given.
	#name is also a different value.It requires input 
            
        propeRdrive = self._drive_correction(drive)
        if flag ==0:
            new_directory = propeRdrive+str(date.today()) + "\\" + name
        else:
            new_directory = propeRdrive+str(datetime.now().strftime('%Y-%m-%d_%H')) + "\\" + name	
            if not os.path.exists(new_directory +".zip"):
                zipname = zipfile.ZipFile(new_directory+".zip",'w')
            else:
                zipname = zipfile.ZipFile(new_directory+".zip",'a')
            paths = self.get_directory_address(path, drive, flag)
        for root, dirs, files in os.walk(paths):
            ## do something here    
            if (files == []):
                zipname.write(root)
            else:
                for file in files:
                    zipname.write(os.path.join(root,file))





    def get_directory_address(self, path, drive, flag =0):
            
            #3) get_directory_address 등의 파라메터로 넘어오는 드라이브가 "D"  혹은 "D:" 와 같을때 어찌 되는지 테스트를 추가하고,  해당 함수를 처리하세요 ()
            #> 공통점 : 첫글자는 드라이브.
             
            ''' 저장되는 디렉토리는 LOG 의 주소를 따름.
            '''
            
            name = path[path.rfind("\\") +1:len(path)].replace(":","")
               #new_directory to toDirectory      
            propeRdrive = self._drive_correction(drive)
            if flag ==0:
                new_directory = propeRdrive+str(date.today()) + "\\" + name
            else:
                new_directory = propeRdrive+str(datetime.now().strftime('%Y-%m-%d_%H')) + "\\" + name
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
