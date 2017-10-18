__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-16"
__altered__ = "2017-10-17"


class TablesAndGraphs(object):
    """Creates Tables and Graphs from cleaned data"""

    __slots__ = ["file","database"]

    def __init__(self, file: str, database: dict) -> None:
        self.file = file
        self.database = database


    def create_variable_line(self,row_label,array,matrix,row,column,simulation_list) -> str:
        # Create a line with a variable and its information
        variable_line = row_label #line starts with the row lable
        for i in simulation_list: #add an entry to the line for each simulation in list
            key = (i, array, matrix, row, column)
            variable_line += "\t" + "{:,}".format(round(self.database[key]))
                #Adds database entries to the line, seperatored by tabs
                #"{:,}".format(value) adds a thousands seperator
        variable_line += "\n" #end line with newline character
        return variable_line
    
    def create_variable_line_ratio(self,row_label,numerator,denominator, simulation_list) -> str:
        #save the function entries in a more manageable form
        
        #numerator
        num_array=numerator[0]
        num_matrix=numerator[1]
        num_row=numerator[2]
        num_column=numerator[3]

        #denominator
        den_array=denominator[0]
        den_matrix=denominator[1]
        den_row=denominator[2]
        den_column=denominator[3]

        # Create a line with a variable and its information
        variable_line = row_label #line starts with the row lable
        for simulation in simulation_list: #add an entry to the line for each simulation in list
            numerator_key = (simulation, num_array, num_matrix, num_row, num_column)
            denominator_key = (simulation, den_array, den_matrix, den_row, den_column)
            ratio_value=round(self.database[numerator_key]/self.database[denominator_key],2)
            variable_line += "\t" + "{:,}".format(ratio_value)
                #Adds database entries to the line, seperatored by tabs
                #"{:,}".format(value) adds a thousands seperator
        variable_line += "\n" #end line with newline character
        return variable_line

    def create_variable_line_marginal(self, row_label, numerator1, numerator2,denominator1, denominator2) -> str:
        # save the function entries in a more manageable form

        # Create a line with a variable and its information
        variable_line = row_label  # line starts with the row lable
        for i, simulation in enumerate(numerator1[0]):  # add an entry to the line for each simulation in list

            # (,) is used to convert element to tuple and then add with the other tuple
            numerator1_key = (numerator1[0][i],)+numerator1[1:]
            numerator2_key = (numerator2[0][i],)+numerator2[1:]
            denominator1_key = (denominator1[0][i],)+denominator1[1:]
            denominator2_key = (denominator2[0][i],)+denominator2[1:]

            value = round((self.database[numerator2_key]-self.database[numerator1_key]) /
                          (self.database[denominator2_key]-self.database[denominator1_key]))
            variable_line += "\t" + "{:,}".format(value)
            # Adds database entries to the line, seperatored by tabs
            # "{:,}".format(value) adds a thousands seperator
        variable_line += "\n"  # end line with newline character
        return variable_line

    def create(self) -> None:
        # Writes output to a text file
        simulation_list_1 = ['10', '20', '30', '40', '50'] #hardcode simulation list for now


        test=self.create_variable_line("Production", "qo", "Linear", "Coal", "USA", simulation_list_1)

        numer=["EV", "Lin+Lev", "NonUS", "Linear"]
        denom=["EV", "Lin+Lev", "USA", "Linear"]
        line_ratio_change_welfare_nonus_us = self.create_variable_line_ratio(
            "Ratio of Change in Welfare, Non-U.S. / U.S.",numer,denom, simulation_list_1)

        simulation_list_2 = ['11', '21', '31', '41', '51'] #hardcode simulation list for now
        numer1=(simulation_list_1,"EV", "Lin+Lev", "USA", "Linear")
        numer2 = (simulation_list_2,"EV", "Lin+Lev", "USA", "Linear")
        denom1=(simulation_list_1,"gco2", "PostLevel", "Total", "Total")
        denom2 = (simulation_list_2,"gco2", "PostLevel", "Total", "Total")
        line_marginal_us_welfare_cost = self.create_variable_line_marginal("Marginal U.S. Welfare Cost (USD per MT)",numer1,numer2,denom1,denom2)

        #Create lines to write to text file
        line_list = ["Table 1: Changes in U.S. Coal Trade (Percent)\n",
                     "\tCoal Intensity Reduction Policy (percent)\n",
                     "\t"+"\t".join(simulation_list_1)+"\n",
                     self.create_variable_line("Production", "qo", "Linear", "Coal", "USA", simulation_list_1),
                     self.create_variable_line("Imports", "qiw", "Linear", "Coal", "USA", simulation_list_1),
                     self.create_variable_line("Exports", "qxw", "Linear", "Coal", "USA", simulation_list_1),
                     "\n",
                     "\n",
                     "\n",

                     "Table 2: Changes in Non-U.S. Coal Trade (Percent)\n",
                     "\tCoal Intensity Reduction Policy (percent)\n",
                     "\t"+"\t".join(simulation_list_1)+"\n",
                     self.create_variable_line("Production", "qo", "Linear", "Coal", "NonUS", simulation_list_1),
                     self.create_variable_line("Imports", "qiw", "Linear", "Coal", "NonUS", simulation_list_1),
                     self.create_variable_line("Exports", "qxw", "Linear", "Coal", "NonUS", simulation_list_1),
                     "\n",
                     "\n",
                     "\n",

                     "Table 3: Change in Carbon Emissions and Coal Exports from Restricting Coal Consumption\n",
                     "\tCoal Intensity Reduction Policy (percent)\n",
                     "\t"+"\t".join(simulation_list_1)+"\n",
                     "Cumulative Change in Emissions by Source (million MT)\n",
                     "\t" + self.create_variable_line("U.S.", "gco2", "Changes", "USA", "Total", simulation_list_1),
                     "\t" + self.create_variable_line("U.S. Coal", "gco2", "Changes", "USA", "coal", simulation_list_1),
                     "\t" + self.create_variable_line("U.S. Oil", "gco2", "Changes", "USA", "oil", simulation_list_1),
                     "\t" + self.create_variable_line("U.S. Gas", "gco2", "Changes", "USA", "gas", simulation_list_1),
                     "\t" + self.create_variable_line("Non-U.S.", "gco2", "Changes", "NonUS", "Total", simulation_list_1),
                     "\t" + self.create_variable_line("Total World", "gco2", "Changes", "Total", "Total", simulation_list_1),
                     "\n",
                     self.create_variable_line("Change in Total U.S. Emissions (percent)", "gco2", "Levels", "USA", "Total", simulation_list_1),
                     "\n",
                     "\n",
                     "\n",

                     "Table 4: Change in Welfare from Restricting Coal Consumption\n",
                     "\tCoal Intensity Reduction Policy (percent)\n",
                     "\t"+"\t".join(simulation_list_1)+"\n",
                     "Change in Welfare (million USD)\n",
                     self.create_variable_line("U.S.", "EV", "Lin+Lev", "USA", "Linear", simulation_list_1),
                     self.create_variable_line("Non_U.S.", "EV", "Lin+Lev", "NonUS", "Linear",simulation_list_1),
                     self.create_variable_line("Total World", "EV", "Lin+Lev", "Total", "Linear", simulation_list_1),
                     "\n",
                     line_ratio_change_welfare_nonus_us,
                     "\n",
                     line_marginal_us_welfare_cost
                      ]

        # Create final file
        with open("Final\{0}.txt".format(self.file), "w+") as writer:  # Create the empty file
            writer.writelines(line_list)  # write the line list to the file

