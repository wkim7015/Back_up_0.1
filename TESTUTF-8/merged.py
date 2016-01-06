import unittest
import sys
import os
print sys.stdin.encoding
print os.path.dirname(__file__)
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
#sys.path.append('..')
#sys.path.append(".")
from TESTcopy_function import*
from TESTaddress_function import *
from TESTlog_function import *
#######################

if __name__ == "__main__":
    unittest.main()
