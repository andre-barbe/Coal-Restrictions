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

    def create(self) -> None:
        # Writes output to a text file
        simulation_list_1 = ['10', '20', '30', '40', '50'] #hardcode simulation list for now

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
                     "\t" + self.create_variable_line("U.S.", "gco2", "Changes", "USA", "ZZZZTotal", simulation_list_1),
                     "\t" + self.create_variable_line("U.S. Coal", "gco2", "Changes", "USA", "coal", simulation_list_1),
                     "\t" + self.create_variable_line("U.S. Oil", "gco2", "Changes", "USA", "oil", simulation_list_1),
                     "\t" + self.create_variable_line("U.S. Gas", "gco2", "Changes", "USA", "gas", simulation_list_1),
                     "\t" + self.create_variable_line("Non-U.S.", "gco2", "Changes", "NonUS", "ZZZZTotal", simulation_list_1),
                     "\t" + self.create_variable_line("Total World", "gco2", "Changes", "ZZZZTotal", "ZZZZTotal", simulation_list_1),
                     "\tTotal World\t-173\t-357\t-551\t-750\t-930\n",

                     "\n",
                     "Change in Total U.S. Emissions (percent)\t-3\t-6\t-10\t-13\t-17\n",
                     "\n",
                     "\n",
                     "\n",

                     "Table 4: Change in Welfare from Restricting Coal Consumption\n",
                     "\tCoal Intensity Reduction Policy (percent)\n",
                     "\t"+"\t".join(simulation_list_1)+"\n",
                     "Change in Welfare (billion USD)\n",
                     "Millions\t" + self.create_variable_line("U.S.", "EV", "Lin+Lev", "USA", "Linear", simulation_list_1),
                     self.create_variable_line("Non_U.S.", "EV", "Lin+Lev", "NonUS", "Linear",simulation_list_1),

                     "\tNon-U.S.\t0.2\t0.9\t2.4\t5.7\t13.8\n",
                     "\tTotal World\t-1.1\t-4.7\t-12.9\t-30.9\t-76.1\n",
                     self.create_variable_line("Total World", "EV", "Lin+Lev", "ZZZZTotal", "Linear", simulation_list_1),
                     "\n",
                     "Ratio of Change in Welfare, Non-U.S. / U.S.\t-0.19\t-0.17\t-0.16\t-0.16\t-0.15\n",
                     "\n",
                     "Marginal U.S. Welfare Cost (USD per MT CO2)\t15\t35\t73\t166\t678\n",
                      ]

        # Create final file
        with open("Final\{0}.txt".format(self.file), "w+") as writer:  # Create the empty file
            writer.writelines(line_list)  # write the line list to the file

