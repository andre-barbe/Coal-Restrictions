__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-5"
__altered__ = "2017-10-19"

from CreateSTIs import *
from CreateBAT import *
from CreateCMF import *
from CreateMAP import *
from ImportCSV import *
from PostEstimation import *
from Tables import *
from Cleanup import *
import subprocess

#Program Control Variables
simulation_list_normal   = ['10', '20', '30', '40']
simulation_list_marginal = ['11', '21', '31', '41']
project_name="coal"
run_GEMSIM=True
solution_method="default_g"

#Call methods
simulation_list = simulation_list_normal+simulation_list_marginal
Cleanup(project_name, simulation_list).main()
CreateBAT(project_name, simulation_list).create()
CreateSTIs(project_name,simulation_list).create()
CreateCMF(project_name,solution_method).create()
CreateMAP(project_name).create()
if run_GEMSIM: subprocess.call("Control_Files\{0}.bat".format(project_name))
    # note: this will fail to run if the file is on a networked drive
    # for example, if the drive begins with "\\hq-fs-1\", it is networked
    # if it begins with something like "P:" then it is not networked
    # Also note that some drives may be access through either method
database = ImportCSV(project_name, simulation_list).create()
PostEstimation(database).create()
ExportTables(project_name, database,simulation_list_normal,simulation_list_marginal).create()
