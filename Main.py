from CreateSTI import *
from CreateBAT import *
from CreateCMF import *
from CreateMAP import *
from ImportCSV import *
from PostEstimation import *
from PostEstimationZZZZ import *
from Tables import *
import subprocess

__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-5"
__altered__ = "2017-10-14"

#simulation_list=('01','02','03')
simulation_list=('00','01','10','11','20','21','30','31','40','41','50','51')

CreateBAT("coal",simulation_list).create()

for x in simulation_list:
    CreateSTI("coal{0}".format(x)).create()

CreateCMF("coal").create()

CreateMAP("coal").create()

#subprocess.call("Control_Files\coal.bat")
    #note: this will fail to run if the file is on a networked drive
    #for example, if the drive begins with "\\hq-fs-1\", it is networked
    #if it begins with something like "P:" then it is not networked
    #Also note that some drives may be access through either method

c=ImportCSV("coal",simulation_list).create()
c2=ImportCSV("coal",simulation_list).create()
d=PostEstimationZZZZ(c).create()
d2=PostEstimation(c2).create()
d1_only=sorted(set(d.items())-set(d2.items()))
d2_only=sorted(set(d2.items())-set(d.items()))
print(d1_only)
print(d2_only)
TablesAndGraphs("coal",d).create()
#The problem was that the final variable only has 1 matrix, so it is a little different from the previous ones