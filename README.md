#BACK-UP(V.2.0) 

* This program is a basic light-weighted program which copies a whole given directory in to a specific directory from the input

* main input :
  1. The text file which have desired paths to copy the directories or files
  2. The path that the user wants to store

## 1. main ##

* This function is to operate all available functions, and write raised errors to an error log, formatted to a txt file.
* This function requires three inputs:an error report path,a directory path, and a drive which directory will be stored. The error report paths must be saved as a text file. 

##2. remove function ##

* This function is to delete the old back-up files, up to 3 weeks from the current date. If files or directories are protected by admin, it raises associated errors which is passed to the main.
	

## 3. log function ##

* This function has required methods for writing a finalized error report in text format style.
	
## 4. address function ##

* This function formats and delivers directory paths to required functions.
 
## 5. copy function ##

* This function is to copy all files in a given directory. 
* If they are protected or not found in the path, then the function will raise correspond errors.

## 6. automation function ##

* This function is to run main at the given specific times. 

## Problems ##

* incompleted version of log-writing format :  will be patched and added with numerous features on the next version. 
* the copy process stops when exception is raised: This can be fixed,only if I have permission to create personal copy_tree method by overriding the exceptions. > Don't. 
* Need to back up 2 different sites.. perhaps can it be improved by having a definite directory? > leave it as an option
* SMT? >through python or os system?
* Another log style such as HTML? Tkinter for visualization? > Don't. It is not necessary.
* Optimization
* Solved:
    - whenever the drive does not exists, it gives bug > Putting the copied folders in to original folders and the error report.
    - it cannot perform over the same folders again. > By using hour unit, it can be repeated after one hour ( or perhaps, two 		      hours?).
    - Sending email option is attached to alert users whenever the program starts 
    - Need to estimate the amount of copied contents for security and completion matter. > implemented as L1(level 1) security check.
    - Add another parameter to run the script at the specific required time. >>automation file. It is "parameterized"
