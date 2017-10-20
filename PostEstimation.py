__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-17"
__altered__ = "2017-10-18"

import numpy

class PostEstimation(object):
    """Creates new variables and regions after estimation completes"""

    __slots__ = ["database"]

    def __init__(self, database: dict) -> None:
        self.database = database

    def create(self) -> None:
        """
        Adds additional entries to the database
        """

        # this code is very slow and inefficient
        for simulation in list(sorted(set([key[0] for key in self.database.keys()]))):

            # creating a sub database to work with greatly speeds up the program
            simulation_database = {key: value for key, value in self.database.items() if key[0] == simulation}

            for array in list(sorted(set([key[1] for key in simulation_database.keys()]))):

                # creating a sub database to work with greatly speeds up the program
                array_database = {key: value for key, value in simulation_database.items() if key[1] == array}
                database_of_added = {}

                for matrix in list(sorted(set([key[2] for key in array_database.keys()]))):
                    if matrix in ["PreLevel", "PostLevel", "Changes"] or array == "EV":
                        # Levels are percentages so you can't just add levels together to get aggregate levels
                        # But for EV, the levels actually are absolute values

                        # creating a sub database to work with greatly speeds up the program
                        matrix_database = {key: value for key, value in array_database.items() if key[2] == matrix}
                        row_list = list(sorted(set([key[3] for key in matrix_database.keys()])))

                        # Create total sums
                        for row in row_list:
                            # Creates sum of columns in a row
                            key_to_match = (simulation, array, matrix, row)
                            sum_of_cols_in_row = sum(
                                self.database[key] for key in matrix_database.keys() if key[0:4] == key_to_match)
                            key_total = key_to_match + ("Total",)

                            self.database[key_total] = sum_of_cols_in_row
                            database_of_added[key_total] = sum_of_cols_in_row  # for creating levels
                            matrix_database[key_total] = sum_of_cols_in_row
                            # update matrix database with new entries so they can be summed over in col sum creation

                        col_list = list(sorted(set(
                            [key[-1] for key in matrix_database.keys() if key[0:3] == (simulation, array, matrix)])))
                        for col in col_list:
                            # Creates sum of rows in a column
                            key_to_match = (col, simulation, array, matrix)
                            sum_of_rows_in_col = sum(self.database[key] for key in matrix_database.keys() if
                                                     (key[-1:] + key[:3]) == key_to_match)
                            key_total = key_to_match + ("Total",)
                            key_total = key_total[1:] + key_total[:1]

                            self.database[key_total] = sum_of_rows_in_col
                            database_of_added[key_total] = sum_of_cols_in_row  # for creating levels
                            matrix_database[key_total] = sum_of_cols_in_row
                            # update matrix database with new entries so they can be summed over in non-US sum creation

                        # Create non-US sums
                        row_list = list(sorted(set([key[3] for key in matrix_database.keys()])))
                        for row in row_list:
                            # Creates sum of non-US columns in a row
                            key_us = (simulation, array, matrix, row, "USA")
                            if key_us in matrix_database:
                                key_total = (simulation, array, matrix, row, "Total")
                                key_non_us = (simulation, array, matrix, row, "NonUS")

                                self.database[key_non_us] = self.database[key_total] - self.database[key_us]
                                database_of_added[key_non_us] = self.database[key_total] - self.database[key_us]  # for creating levels
                                matrix_database[key_non_us] = self.database[key_total] - self.database[key_us]

                        col_list = list(sorted(set([key[-1] for key in matrix_database.keys()])))
                        for col in col_list:
                            # Creates sum of rows in a column
                            key_us = (simulation, array, matrix, "USA", col)
                            if key_us in matrix_database:
                                key_total = (simulation, array, matrix, "Total", col)
                                key_non_us = (simulation, array, matrix, "NonUS", col)

                                self.database[key_non_us] = self.database[key_total] - self.database[key_us]
                                database_of_added[key_non_us] = self.database[key_total] - self.database[key_us]  # for creating levels
                                matrix_database[key_non_us] = self.database[key_total] - self.database[key_us]

                if (array != "EV"):  # Now Create Levels variables. Note that this is at the array nest, not matrix
                    row_list = list(sorted(set([key[3] for key in database_of_added.keys()])))
                    for row in row_list:
                        col_list = list(sorted(set([key[-1] for key in database_of_added.keys()])))
                        for col in col_list:
                            #value = numpy.float64(100 * self.database[simulation, array, "Changes", row, col] /self.database[simulation, array, "PreLevel", row, col])
                            changes=self.database[simulation, array, "Changes", row, col]
                            prelevel=self.database[simulation, array, "PreLevel", row, col]
                            linear_key=(simulation, array, "Linear", row, col)
                            if linear_key in self.database:
                               1==1
                            elif changes == 1.00E+10 or prelevel==1.00E+10:
                                self.database[linear_key] = 1.00E+10
                            else:
                                self.database[simulation, array, "Linear", row, col] = 100 * changes / prelevel
                            # Need to be careful here since it could overwrite eexisting levels