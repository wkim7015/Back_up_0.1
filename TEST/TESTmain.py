from main import *
import unittest




class copytest (unittest.TestCase):
    
    def test_main(self):
        
        ''' This test is to examine whether the supposed main procedures work or not. 
        
        This test should copy 
        
        1. the name of the folders in to the drive from the given parameters
        
        2. the directories, up to 3 weeks, should be removed.
        
        3. Whenever the log drive is not given, the log should be stored in the the copied directory.
        
        4. The report should be produced in txt format. 
        
        
        the paths needs to be given.
        
        GUI may be implemented in the future for the user's convenience. 
        
        Furthemore, once the address is given, the data will be stored in the future, starting the procedures automatically unless user wants to modify it.
       
       '''
        
        
        # 1. Create the path
        
        directoryPath = ""
        logPath = ""
        drive = ""
        
        #2. Start the function
        main(reportPath, directoryPath,drive)
        
        #3. check the functions
        
        '''
        1. folder check: os.path.exists("PATH)
        
        
        2. file check : length of the files should be examine
        d
        
        3. The text check: whether the text is written without any
        errors
        
        # The above formats are copied from the other unit_test files
        
        '''
        
        
        
        
        
        return
    
 
