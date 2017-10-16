from CreateSTI import *
from CreateBAT import *
from CreateCMF import *
from CreateMAP import *
from ImportCSV import *
from TablesAndGraphs import *
import subprocess

__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-5"
__altered__ = "2017-10-14"

#simulation_list=('01','02','03')
simulation_list=('01','01')

CreateBAT("coal",simulation_list).create()

for x in simulation_list:
    CreateSTI("coal{0}".format(x)).create()

CreateCMF("coal").create()

CreateMAP("coal").create()

subprocess.call("Control_Files\coal.bat")
    #note: this will fail to run if the file is on a networked drive
    #for example, if the drive begins with "\\hq-fs-1\", it is networked
    #if it begins with something like "P:" then it is not networked
    #Also note that some drives may be access through either method

c=ImportCSV("coal",simulation_list).create()
TablesAndGraphs("coal",c).create()
#The problem was that the final variable only has 1 matrix, so it is a little different from the previous ones