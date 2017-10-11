__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-5"
__altered__ = "2017-10-5"

__all__ = ["CreateBAT"]

class CreateBAT(object):
    """Creates the BAT File"""

    __slots__ = ["file","simulation_list"]

    def __init__(self, file: str,simulation_list: list) -> None:
        self.file = file
        self.simulation_list = simulation_list

    def create(self) -> None:

        #Create important lines that you need to worry about
        sltoht_line="	sltoht -sti Control_Files\coal%%a.sti\n"
        simulation_list_formatted=",".join(self.simulation_list)

        #Create unimportant lines and combine them with important lines
        line_list = [#"cd..\n",     
                     "for %%a in ({0}) do (\n".format(simulation_list_formatted),     
                     "	gemsim -cmf Control_Files\coal.cmf -p1=%%a\n",     
                     "pause\n",     
                     sltoht_line,    
                     "pause",
                     ")"]

        #Create final file
        with open("Control_Files\{0}.bat".format(self.file),"w+") as writer: #Create the empty file
            writer.writelines(line_list) #write the line list to the file