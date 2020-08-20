from abaqus import *
from abaqusConstants import *

import csv
import os
import numpy as np
import time

from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup

os.chdir(r"D:\temp_abaqus")

num =587
a = range(96)
c = range(35) # 17*232+16
for x in a:
    for  z in c:   
     mdb.jobs['model'+ str(num)].submit(consistencyChecking=OFF) 
     num = num +1
    mdb.jobs['model'+ str(num-34)].waitForCompletion()
    mdb.jobs['model'+ str(num-33)].waitForCompletion()
    mdb.jobs['model'+ str(num-32)].waitForCompletion()
    mdb.jobs['model'+ str(num-31)].waitForCompletion()
    mdb.jobs['model'+ str(num-30)].waitForCompletion()
    mdb.jobs['model'+ str(num-29)].waitForCompletion()
    mdb.jobs['model'+ str(num-28)].waitForCompletion()
    mdb.jobs['model'+ str(num-27)].waitForCompletion()
    mdb.jobs['model'+ str(num-26)].waitForCompletion()
    mdb.jobs['model'+ str(num-25)].waitForCompletion()
    mdb.jobs['model'+ str(num-24)].waitForCompletion()      
    mdb.jobs['model'+ str(num-23)].waitForCompletion()
    mdb.jobs['model'+ str(num-22)].waitForCompletion()
    mdb.jobs['model'+ str(num-21)].waitForCompletion()
    mdb.jobs['model'+ str(num-20)].waitForCompletion()
    mdb.jobs['model'+ str(num-19)].waitForCompletion()
    mdb.jobs['model'+ str(num-18)].waitForCompletion()
    mdb.jobs['model'+ str(num-17)].waitForCompletion()
    mdb.jobs['model'+ str(num-16)].waitForCompletion()
    mdb.jobs['model'+ str(num-15)].waitForCompletion()
    mdb.jobs['model'+ str(num-14)].waitForCompletion()
    mdb.jobs['model'+ str(num-13)].waitForCompletion()
    mdb.jobs['model'+ str(num-12)].waitForCompletion()
    mdb.jobs['model'+ str(num-11)].waitForCompletion()
    mdb.jobs['model'+ str(num-10)].waitForCompletion()
    mdb.jobs['model'+ str(num-9)].waitForCompletion()
    mdb.jobs['model'+ str(num-8)].waitForCompletion()
    mdb.jobs['model'+ str(num-7)].waitForCompletion()
    mdb.jobs['model'+ str(num-6)].waitForCompletion()
    mdb.jobs['model'+ str(num-5)].waitForCompletion()
    mdb.jobs['model'+ str(num-4)].waitForCompletion()
    mdb.jobs['model'+ str(num-3)].waitForCompletion()
    mdb.jobs['model'+ str(num-2)].waitForCompletion()
    mdb.jobs['model'+ str(num-1)].waitForCompletion()
    mdb.jobs['model'+ str(num-0)].waitForCompletion()

# remaining
d = range(14) #900
for  y in d:   
 mdb.jobs['model'+ str(num)].submit(consistencyChecking=OFF) 
 num = num +1
mdb.jobs['model'+ str(num-13)].waitForCompletion()
mdb.jobs['model'+ str(num-12)].waitForCompletion()
mdb.jobs['model'+ str(num-11)].waitForCompletion()
mdb.jobs['model'+ str(num-10)].waitForCompletion()
mdb.jobs['model'+ str(num-9)].waitForCompletion()
mdb.jobs['model'+ str(num-8)].waitForCompletion()
mdb.jobs['model'+ str(num-7)].waitForCompletion()
mdb.jobs['model'+ str(num-6)].waitForCompletion()
mdb.jobs['model'+ str(num-5)].waitForCompletion()
mdb.jobs['model'+ str(num-4)].waitForCompletion()
mdb.jobs['model'+ str(num-3)].waitForCompletion()
mdb.jobs['model'+ str(num-2)].waitForCompletion()
mdb.jobs['model'+ str(num-1)].waitForCompletion()
mdb.jobs['model'+ str(num-0)].waitForCompletion()




 
 



