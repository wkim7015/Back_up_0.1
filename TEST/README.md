#(TEST)BACKUP V0.1 [README]

All of the test files are uploaded here. TESTmain, the test file for merged functions, has not been completed. However, in the future, if the scope is broaden, it will be functional.

The inputs can be found in the front of the functions;All of the inputs is at the very front-lines after declaration of global variables.
Circumferenced by "#================",They can be easily found and modified as below.


Furthermore, before running the files, it is essential to put the test files in the directory where the functions are stored. 
_1. TESTcopyfunction_

It has two kind of inputs: path1~6 and drive

Each of paths denotes the full paths from the drive to the directory. 
drive is the full location which user wants to store copied files and directory.

_2. TESTlogfunction_

the "inputs" parameters serve same purposes to above "paths" parameters
textPath is the path of the text for storing a log signature.
directoryPath is optional. However, its usage is for creating multiple logs to check robustness of the function.

_3. TESTaddressfunction_

First of all, download uploaded address files.If a user wants to customize the tests, it does not require to do so. 
Address has 3 components: AddressDirectory,AddressName, and AddressCorrectName.
The first one requires to write the full path of the directory.
The second is to store the name of the directory
The last is optional, to store the appropriate-correct name of the directory for assert test.

textFile is the text file which needs to be created prior to start. It requires full paths of files.
trueArray is used as a reference, stored the correct paths of the files.

_4. Merged_

This runs all of above functions in one go. It does not need neither inputs nor parameters.

*For convenience, the inputs are recorded in the file as examples.* 
