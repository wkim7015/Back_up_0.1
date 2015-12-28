BACK-UP(V.1.0) 

This program is a basic light-weighted program which copies

a whole given directory in to a specific directory from the input 
 
 
1. main

This function is to operate all available functions, and write raised errors to an error log, formatted to a txt file.

This functions requires three inputs:an error report path,a directory path, and a drive which directory will be stored. The error report paths must be saved as a text file. 

2. remove function

This function is to delete the old back-up files, up to 3 weeks from the current date. If files or directories are protected by 
admin, it will raise associated error which will be passed to the main.
	

3. log function

 This function has required methods for writing a finalized error report in text format style.
	
4. address function

 This function formats and delivers directory paths to required functions.
 
5. copy function

 This function is to copy all files in a given directory. 
If they are protected or not found in the path, then the function will raise correspond errors.

Problems:

it cannot perform over the same folders again. > By using hour units, it can be repeated with a delay of second.

incompleted version of log-writing format : will be patched next version. 


