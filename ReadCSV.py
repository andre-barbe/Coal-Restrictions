from typing import List

__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-6"
__altered__ = "2017-10-13"

class ReadCSV(object):
    """Reads the CSV Files outputed by SLTOHT"""

    __slots__ = ["file","simulation_list"]

    def __init__(self, file: str, simulation_list: List[str]) -> None:
        self.file = file
        self.simulation_list = simulation_list

    def create(self) -> List[str]:
        """
        Runs all the subprocesses to create the final variables
        :return: The list of arrays
        """
        x = self.filecontents()
        y = self.break_into_arrays(x)
        z =[]
        for array in y:
            z.append(self.break_into_matrices(array))
        newz=[]
        for array in z:
            newarray=[]
            for matrix in array:
                newarray.append(self.break_into_values(matrix))
            newz.append(newarray)
        #a = self.break_into_values(z[1][1])
        return newz


    def create2(self) -> dict:
        """
        Runs all the subprocesses to create the final variables
        :return: The list of arrays
        """
        x = self.create()
        variablevalue={}
        variablevaluewithnames={}
        for c1, array in enumerate(x):
            array_num=c1
            for c2, matrix in enumerate(array):
                matrix_num=c2
                for c3, row in enumerate(matrix):
                    row_num=c3
                    for c4, column in enumerate(row):
                        col_num=c4
                        variablevalue[array_num,matrix_num,row_num,col_num]=column
                        # print("test1")
                        # print(column)
                        # print(variablevalue[array_num,1,0,0])
                        # array_name=variablevalue[array_num,1,0,0]
                        # matrix_name = variablevalue[array_num, matrix_num, 0, 0]
                        # row_name = variablevalue[array_num, matrix_num, row_num, 0]
                        # col_name = variablevalue[array_num, matrix_num, 0, col_num]
                        # print("test4")
                        # print([array_name, matrix_name, row_name, col_name])
                        # variablevaluewithnames[array_name, matrix_name, row_name, col_name] = column
        #return variablevaluewithnames
        return variablevalue

    def create3(self) -> dict:
        """
        Runs all the subprocesses to create the final variables
        :return: The list of arrays
        """
        x = self.create()
        variablevalue={}
        variablevaluewithnames={}
        for c1, array in enumerate(x):
            array_num=c1
            for c2, matrix in enumerate(array):
                matrix_num=c2
                for c3, row in enumerate(matrix):
                    row_num=c3
                    for c4, column in enumerate(row):
                        col_num=c4
                        variablevalue[array_num,matrix_num,row_num,col_num]=column
                        print("test1")
                        print(column)
                        print(variablevalue[array_num,1,0,0])
                        array_name=variablevalue[array_num,1,0,0]
                        matrix_name = variablevalue[array_num, matrix_num, 0, 0]
                        row_name = variablevalue[array_num, matrix_num, row_num, 0]
                        col_name = variablevalue[array_num, matrix_num, 0, col_num]
                        print("test4")
                        print([array_name, matrix_name, row_name, col_name])
                        variablevaluewithnames[array_name, matrix_name, row_name, col_name] = column
        return variablevaluewithnames
        #return variablevalue



    def filecontents(self) -> List[str]:
        """
        Reads the CSV file into memory
        :return:
        """
        with open("Results\{0}01.csv".format(self.file),"r") as reader: #Read the csv file
            return [line for line in reader.readlines() if line!=" \n"]  #read the contents of the csv file
            #return reader.readlines()



    def break_into_arrays(self, csvlines: List[str]) -> List[str]:
        """
        Groups the list of lines by array
        :param csvlines:
        :return:
        """
        listofarrays = []
        currentarray = []
        for i, line in enumerate(csvlines):
            if line[0:11] == " ! Variable" and line[-2:] == "#\n":
                listofarrays.append(currentarray)
                currentarray = []
            if (line[0:11] != " ! Variable" and line[0:25] != " ! (This array is shown as"):
                currentarray.append(line)
            if i == len(csvlines) - 1:
                listofarrays.append(currentarray)
        return listofarrays



    def break_into_matrices(self, arraylines: List[str]) -> List[str]:
        """
        Groups the lines of an array by matrix
        :param arraylines: lines of a single array
        :return:
        """
        listofmatrices = []
        currentmatrix = []
        for i, line in enumerate(arraylines):
            if line[0:14] == " ! The matrix ":
                listofmatrices.append(currentmatrix)
                currentmatrix = []
            currentmatrix.append(line)
            if i == len(arraylines) - 1:
                listofmatrices.append(currentmatrix)
        return listofmatrices



    def break_into_values(self, matrixlines: List[str]) -> List[str]:
        """
        Convert the lines of a matrix into a matrix object
        :param arraylines: lines of a single array
        :return:
        """
        valuematrix=[]
        lineswithvalues = [line for line in matrixlines if line[0:2]!=" !"] #skip the lines which just describe the matrix (or array)
        for line in lineswithvalues:
            valuematrix.append(line.split(","))
        return valuematrix

