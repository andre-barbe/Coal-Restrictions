from CreateSTI import *
from CreateBAT import *
from CreateCMF import *
from CreateMAP import *
from ReadCSV import *
import subprocess

__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-5"
__altered__ = "2017-10-6"

#simulation_list=('01','02','03')
simulation_list=('10','20')

CreateBAT("coal",simulation_list).create()

for x in simulation_list:
    CreateSTI("coal{0}".format(x)).create()

CreateCMF("coal").create()

CreateMAP("coal").create()

#subprocess.call("Control_Files\coal.bat")
subprocess.call("Control_Files\coal.bat")
    #note: this will fail to run if the file is on a networked drive
    #for example, if the drive begins with "\\hq-fs-1\", it is networked
    #if it begins with something like "P:" then it is not networked
    #Also note that some drives may be access through either method

ReadCSV("coal",simulation_list).create()