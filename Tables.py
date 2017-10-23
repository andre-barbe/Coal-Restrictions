__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-16"
__altered__ = "2017-10-18"


class ExportTables(object):
    """Creates Tables and Graphs from cleaned data"""

    __slots__ = ["file", "database","simulations_normal","simulations_marginal"]

    def __init__(self, file: str, database: dict,simulations_normal: list, simulations_marginal: list) -> None:
        self.file = file
        self.database = database
        self.simulations_normal= simulations_normal
        self.simulations_marginal = simulations_marginal

    def create_variable_line(self, row_label, array, matrix, row, column, simulation_list) -> str:
        # Create a line with a variable and its information
        variable_line = row_label  # line starts with the row label
        for i in simulation_list:  # add an entry to the line for each simulation in list
            key = (i, array, matrix, row, column)
            variable_line += "\t" + "{:,}".format(round(self.database[key]))
            # Adds database entries to the line, seperatored by tabs
            # "{:,}".format(value) adds a thousands seperator
        variable_line += "\n"  # end line with newline character
        return variable_line

    def create_variable_line_ratio(self, row_label, numerator, denominator, simulation_list) -> str:
        # save the function entries in a more manageable form

        # numerator
        num_array = numerator[0]
        num_matrix = numerator[1]
        num_row = numerator[2]
        num_column = numerator[3]

        # denominator
        den_array = denominator[0]
        den_matrix = denominator[1]
        den_row = denominator[2]
        den_column = denominator[3]

        # Create a line with a variable and its information
        variable_line = row_label  # line starts with the row lable
        for simulation in simulation_list:  # add an entry to the line for each simulation in list
            numerator_key = (simulation, num_array, num_matrix, num_row, num_column)
            denominator_key = (simulation, den_array, den_matrix, den_row, den_column)
            ratio_value = round(self.database[numerator_key] / self.database[denominator_key], 2)
            variable_line += "\t" + "{:,}".format(ratio_value)
            # Adds database entries to the line, seperatored by tabs
            # "{:,}".format(value) adds a thousands seperator
        variable_line += "\n"  # end line with newline character
        return variable_line

    def create_variable_line_marginal(self, row_label, numerator1, numerator2, denominator1, denominator2) -> str:
        # save the function entries in a more manageable form

        # Create a line with a variable and its information
        variable_line = row_label  # line starts with the row lable
        for i, simulation in enumerate(numerator1[0]):  # add an entry to the line for each simulation in list

            # (,) is used to convert element to tuple and then add with the other tuple
            numerator1_key = (numerator1[0][i],) + numerator1[1:]
            numerator2_key = (numerator2[0][i],) + numerator2[1:]
            denominator1_key = (denominator1[0][i],) + denominator1[1:]
            denominator2_key = (denominator2[0][i],) + denominator2[1:]

            value = round((self.database[numerator2_key] - self.database[numerator1_key]) /
                          (self.database[denominator2_key] - self.database[denominator1_key]))
            variable_line += "\t" + "{:,}".format(value)
            # Adds database entries to the line, seperatored by tabs
            # "{:,}".format(value) adds a thousands seperator
        variable_line += "\n"  # end line with newline character
        return variable_line

    def create(self) -> None:
        # Writes output to a text file

        numer = ["EV", "Lin+Lev", "NonUS", "Linear"]
        denom = ["EV", "Lin+Lev", "USA", "Linear"]
        line_ratio_change_welfare_nonus_us = self.create_variable_line_ratio(
            "Ratio of Change in Welfare, Non-U.S. / U.S.", numer, denom, self.simulations_normal)

        numer1 = (self.simulations_normal, "EV", "Lin+Lev", "USA", "Linear")
        numer2 = (self.simulations_marginal, "EV", "Lin+Lev", "USA", "Linear")
        denom1 = (self.simulations_normal, "gco2", "PostLevel", "Total", "Total")
        denom2 = (self.simulations_marginal, "gco2", "PostLevel", "Total", "Total")
        line_marginal_us_welfare_cost = self.create_variable_line_marginal("Marginal U.S. Welfare Cost (USD per MT)",
                                                                           numer1, numer2, denom1, denom2)

        # Create lines to write to text file
        line_list = ["Table 1: Changes in U.S. Electricity Generation (Percent) from Restricting Coal Consumption\n",
                     "\tCoal Intensity Reduction Policy (percent)\n",
                     "\t" + "\t".join(self.simulations_normal) + "\n",
                     self.create_variable_line("Unit Demand for Coal", "intf", "Linear", "coal", "Electricity", self.simulations_normal),
                     self.create_variable_line("Unit Demand for Noncoal", "intf", "Linear", "ncoal", "Electricity", self.simulations_normal),
                     self.create_variable_line("Unit Demand for Non-elec energy", "intf", "Linear", "nely", "Electricity",
                                               self.simulations_normal),
                     self.create_variable_line("Unit Demand for Energy Subproduct", "intf", "Linear", "eny", "Electricity",
                                               self.simulations_normal),
                     self.create_variable_line("Unit Demand for K-Energy Subproduct", "intf", "Linear", "ken",
                                               "Electricity", self.simulations_normal),
                     self.create_variable_line("Unit Demand for Gas in noncoal", "intf", "Linear", "gas", "Electricity",
                                               self.simulations_normal),
                     self.create_variable_line("Electricity Generation", "qo", "Linear", "Electricity", "USA", self.simulations_normal),
                     self.create_variable_line("Demand for Gas for Generation", "qf", "Linear", "Gas", "Electricity",
                                               self.simulations_normal),
                     self.create_variable_line("Demand for Gas for Generation", "qf", "Linear", "Coal", "Electricity",
                                               self.simulations_normal),
                     "\n",
                     "\n",
                     "\n",


                    "Table 2: Changes in U.S. Coal Trade (Percent)\n",
                     "\tCoal Intensity Reduction Policy (percent)\n",
                     "\t" + "\t".join(self.simulations_normal) + "\n",
                     self.create_variable_line("U.S. Production", "qo", "Linear", "Coal", "USA", self.simulations_normal),
                     self.create_variable_line("U.S. Imports", "qiw", "Linear", "Coal", "USA", self.simulations_normal),
                     self.create_variable_line("U.S. Exports", "qxw", "Linear", "Coal", "USA", self.simulations_normal),
                     self.create_variable_line("World Production", "qo", "Linear", "Coal", "Total", self.simulations_normal),
                     "\n",
                     "\n",
                     "\n",


                     "Table 3: Change in Carbon Emissions and Coal Exports from Restricting Coal Consumption\n",
                     "\tCoal Intensity Reduction Policy (percent)\n",
                     "\t" + "\t".join(self.simulations_normal) + "\n",
                     "Cumulative Change in Emissions by Source (million MT)\n",
                     "\t" + self.create_variable_line("U.S. Total", "gco2", "Changes", "USA", "Total", self.simulations_normal),
                     "\t" + self.create_variable_line("U.S. Coal", "gco2", "Changes", "USA", "coal", self.simulations_normal),
                     "\t" + self.create_variable_line("U.S. Oil", "gco2", "Changes", "USA", "oil", self.simulations_normal),
                     "\t" + self.create_variable_line("U.S. Gas", "gco2", "Changes", "USA", "gas", self.simulations_normal),
                     "\t" + self.create_variable_line("Non-U.S.", "gco2", "Changes", "NonUS", "Total",
                                                      self.simulations_normal),
                     "\t" + self.create_variable_line("Total World", "gco2", "Changes", "Total", "Total",
                                                      self.simulations_normal),
                     "\n",
                     self.create_variable_line("Change in Total U.S. Emissions (percent)", "gco2", "Linear", "USA",
                                               "Total", self.simulations_normal),
                     "\n",
                     "\n",
                     "\n",

                     "Table 4: Change in Welfare from Restricting Coal Consumption\n",
                     "\tCoal Intensity Reduction Policy (percent)\n",
                     "\t" + "\t".join(self.simulations_normal) + "\n",
                     "Change in Welfare (million USD)\n",
                     self.create_variable_line("U.S.", "EV", "Lin+Lev", "USA", "Linear", self.simulations_normal),
                     self.create_variable_line("Non_U.S.", "EV", "Lin+Lev", "NonUS", "Linear", self.simulations_normal),
                     self.create_variable_line("Total World", "EV", "Lin+Lev", "Total", "Linear", self.simulations_normal),
                     "\n",
                     line_ratio_change_welfare_nonus_us,
                     "\n",
                     line_marginal_us_welfare_cost
                     ]

        # Create final file
        with open("Final\{0}.txt".format(self.file), "w+") as writer:  # Create the empty file
            writer.writelines(line_list)  # write the line list to the file
