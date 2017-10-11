__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-6"
__altered__ = "2017-10-6"  

class CreateMAP(object):
    """Creates the MAP File for use in SLTOTH"""
    
    __slots__ = ["file"]

    def __init__(self, file: str) -> None:
        self.file = file

    def create(self) -> None:

        #Create the contents to be written to the file
        line_list = ["qxw\n",
                     "qiw\n",
                     "qo\n",
                     "pm\n",
                     "gco2\n"
                     "ev"]

        #Create final file
        with open("Control_Files\{0}.map".format(self.file),"w+") as writer: #Create the empty file
            writer.writelines(line_list) #write the line list to the file

