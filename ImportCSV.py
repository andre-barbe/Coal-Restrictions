from typing import List

__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-14"
__altered__ = "2017-10-18"


class ImportCSV(object):
    """Imports the CSV Files created by SLTOHT"""

    __slots__ = ["project", "simulation_list"]

    def __init__(self, project: str, simulation_list: List[str]) -> None:
        self.project = project
        self.simulation_list = simulation_list

    def filecontents(self, simulation_number) -> List[str]:
        """
        Reads the CSV file into memory
        :return:
        """
        with open("Results\{0}{1}.csv".format(self.project, simulation_number), "r") as reader:  # Read the csv file
            return [line for line in reader.readlines() if
                    line != " \n"]  # deletes lines that are nothing but line breaks

    def create(self) -> dict:
        """
        Takes the CSV file of lines and returns a dictionary of cleaned values
        :return:
        """
        variable_values = {}
        for simulation in self.simulation_list:
            name_array = []
            name_matrix = []
            list_name_col = []
            name_col = []
            name_row = []

            for line in self.filecontents(simulation):
                do_not_store_this_line = 0

                # checks if line contains name of subsequent array
                if line[0:12] == " ! Variable " and line[-2:] == "#\n":
                    name_array = (line[12:].split(" "))[0]
                    name_matrix = []
                    list_name_col = []
                    name_col = []
                    do_not_store_this_line = 1

                # checks if line contains name of columns (and also matrix)
                if name_array != []:
                    if line.split("(")[0] == " " + name_array:
                        list_name_col = line.split(",")  # defines name of matrix
                        name_matrix = line.split(")")[0].split(":")[-1].strip("\"")  # defines name of matrix
                        do_not_store_this_line = 1

                # row name is just first entry of a line
                name_row = line.split(",")[0].strip()

                # foreach cell in a line, assigns its value to a dictionary with keys for the
                # array, matrix, col, and row names
                for i, cell in enumerate(line.split(",")):
                    if name_array != [] and name_matrix != [] and name_row != [] and list_name_col != []:
                        name_col = list_name_col[i].strip()
                        if (do_not_store_this_line == 0 and i != 0 and name_col != ""):
                            key = (simulation, name_array, name_matrix, name_row, name_col)
                            variable_values[key] = float(cell.strip())

        return variable_values
