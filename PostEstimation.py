__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-17"
__altered__ = "2017-10-17"

class PostEstimation(object):
    """Creates new variables and regions after estimation completes"""

    __slots__ = ["database"]

    def __init__(self, database: dict) -> None:
        self.database = database

    def create(self) -> dict:
            """
            Adds additional entries to the database
            :return: newdatabase
            """

            #this code is very slow and inefficient
            for simulation in list(sorted(set([key[0] for key in self.database.keys()]))):
                simulation_database = {key: value for key, value in self.database.items() if key[0] == simulation} #creating a sub database to work with greatly speeds up the program
                for array in list(sorted(set([key[1] for key in simulation_database.keys()]))):
                    array_database = {key: value for key, value in simulation_database.items() if key[1] == array} #creating a sub database to work with greatly speeds up the program
                    for matrix in list(sorted(set([key[2] for key in array_database.keys()]))):
                        if (matrix != "Levels" or array == "EV"):
                            """
                            Levels are percentages so you can't just add levels together to get aggregate levels. But for EV, the levels actually are absolute values
                            """
                            matrix_database = {key: value for key, value in array_database.items() if key[2] == matrix} #creating a sub database to work with greatly speeds up the program
                            row_list=list(sorted(set([key[3] for key in matrix_database.keys()])))

                            #Create total sums
                            for row in row_list:
                                # Creates sum of columns in a row
                                key_to_match=(simulation,array,matrix,row)
                                #print(self.database)
                                sum_of_cols_in_row=sum(self.database[key] for key in matrix_database.keys() if key[0:4]==key_to_match)
                                key_total = key_to_match + ("ZZZZTotal",)
                                    #the name makes sure this col will be sorted to the last so the col sums are correct)
                                self.database[key_total]=sum_of_cols_in_row
                                matrix_database[key_total]=sum_of_cols_in_row
                                    #update matrix database with new entries so they can be summed over in col sum creation
                            col_list=list(sorted(set([key[-1] for key in matrix_database.keys() if key[0:3]==(simulation,array,matrix)])))
                            for col in col_list:
                                #Creates sum of rows in a column
                                key_to_match=(col,simulation,array,matrix)
                                sum_of_rows_in_col=sum(self.database[key] for key in matrix_database.keys() if (key[-1:]+key[:3])==key_to_match)
                                key_total = key_to_match + ("ZZZZTotal",)
                                key_total = key_total[1:] +key_total[:1]
                                self.database[key_total]=sum_of_rows_in_col
                                matrix_database[key_total]=sum_of_cols_in_row
                                    #update matrix database with new entries so they can be summed over in non-US sum creation

                            #Create non-US sums
                            row_list=list(sorted(set([key[3] for key in matrix_database.keys()])))
                            for row in row_list:
                                # Creates sum of non-US columns in a row
                                key_us = (simulation, array, matrix, row, "USA")
                                if key_us in matrix_database:
                                    key_total= (simulation, array, matrix, row, "ZZZZTotal")
                                    key_non_us= (simulation, array, matrix, row, "NonUS")
                                    self.database[key_non_us] = self.database[key_total] - self.database[key_us]
                                    matrix_database[key_non_us]=self.database[key_non_us]

                            col_list = list(sorted(set([key[-1] for key in matrix_database.keys()])))
                            for col in col_list:
                                # Creates sum of rows in a column
                                key_us = (simulation, array, matrix, "USA", col)
                                if key_us in matrix_database:
                                    key_total= (simulation, array, matrix, "ZZZZTotal", col)
                                    key_non_us= (simulation, array, matrix, "NonUS", col)
                                    self.database[key_non_us] = self.database[key_total] - self.database[key_us]
                                    matrix_database[key_non_us]=self.database[key_non_us]

            return self.database