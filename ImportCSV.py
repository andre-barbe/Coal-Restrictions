from typing import List

__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-14"
__altered__ = "2017-10-14"

class ImportCSV(object):
    """Imports the CSV Files outputed by SLTOHT"""

    __slots__ = ["file","simulation_list"]

    def __init__(self, file: str, simulation_list: List[str]) -> None:
        self.file = file
        self.simulation_list = simulation_list

    def filecontents(self, simulation_number) -> List[str]:
        """
        Reads the CSV file into memory
        :return:
        """
        with open("Results\{0}{1}.csv".format(self.file,simulation_number),"r") as reader: #Read the csv file
            return [line for line in reader.readlines() if line!=" \n"]  #deletes lines that are nothing but line breaks

    def create(self) -> dict:
        """
        Takes the CSV file of lines and returns a dictionary of uncleaned values
        :return:
        """
        variable_values = {}
        for simulation in self.simulation_list:
            name_array=[]
            name_matrix=[]
            list_name_col=[]
            name_col=[]
            name_row=[]

            for line in self.filecontents(simulation):
                if line[0:12] == " ! Variable " and line[-2:] == "#\n": #checks if line contains name of subsequent array
                    name_array=(line[12:].split(" "))[0]

                if line[0:14] == " ! The matrix ": #checks if line contains name of subsequent matrix
                    name_matrix = (line.split(":\"")[1]).split("\"")[0]

                if name_array!=[]: #checks if line contains name of columns
                    if line.split("(")[0] == " "+name_array:
                        list_name_col=line.split(",")

                name_row = line.split(",")[0] #row name is just first entry of a line

                #foreach cell in a line, assigns its value to a dictionary with keys for the array, matrix, col, and row names
                for i, cell in enumerate(line.split(",")):
                    if name_array != [] and name_matrix != [] and name_row !=[] and list_name_col!=[]:
                        name_col = list_name_col[i]
                        variable_values[simulation,name_array,name_matrix,name_row,name_col]=cell

        return variable_values

