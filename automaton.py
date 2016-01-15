import sys
import os
sys.path.append(os.path.realpath('..'))
from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour=11, minute=18, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    import main
    os.system("main.py")# execute. 

t = Timer(secs, hello_world)
t.start()
