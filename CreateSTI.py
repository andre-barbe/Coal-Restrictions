__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-5"
__altered__ = "2017-10-6"  

class CreateSTI(object):
    """Creates an STI File for controlling SLTOTH"""
    
    __slots__ = ["file"]

    def __init__(self, file: str) -> None:
        self.file = file

    def create(self) -> None:

        #Create important lines that you need to worry about
        sl4_location_line="GTAP_Files\SaveSims\{0}.sl4\n".format(self.file)
        csv_location_line="Results\{0}.csv".format(self.file)

        #Create unimportant lines and combine them with important lines
        line_list = ["bat         		! Run in batch.\n",
                     "log		        ! Start a log file\n",
                     "b		        	! Output to both terminal and log file\n",
                     "Control_Files\sltoth_sti.log	    	! Name of log file\n",
                     "ses\n",
                     ",\n",
                     "shl\n",
                     "\n",
                     sl4_location_line,
                     "c\n",
                     #"n\n",
                     "y\n",
                     #"Control_Files\{0}.map\n".format(self.file), #Can't use {0} because filename is "coal01", not "coal"
                     "Control_Files\coal.map\n",
                     csv_location_line]

        #Create final file
        with open("Control_Files\{0}.sti".format(self.file),"w+") as writer: #Create the empty file
            writer.writelines(line_list) #write the line list to the file

