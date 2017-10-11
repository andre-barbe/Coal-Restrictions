__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-6"
__altered__ = "2017-10-6"  

class ReadCSV(object):
    """Reads the CSV Files outputed by SLTOHT"""
    
    __slots__ = ["file","simulation_list"]

    def __init__(self, file: str,simulation_list: list) -> None:
        self.file = file
        self.simulation_list = simulation_list

    def create(self) -> None:
        with open("Results\{0}.csv".format(self.file),"r") as reader: #Read the csv file
            print(reader.readlines()) #read the contents of the CSV file