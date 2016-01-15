import sys
import os
sys.path.append(os.path.realpath('..'))
from datetime import datetime
from threading import Timer
####-----------------------------------------
''' This file is to automatically run the main function at the given time. The below parameters are required to be filled in
'''
Hour = 11
Minute = 18
Second = 0
# Then the above will be excuted 11:18 am everyday.
####------------------------------------------
x=datetime.today()
y=x.replace(day=x.day+1, hour=Hour, minute=Minute, second=Second, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    import main
    os.system("main.py")# execute. 

t = Timer(secs, hello_world)
t.start()
