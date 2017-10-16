__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-16"
__altered__ = "2017-10-16"


class TablesAndGraphs(object):
    """Creates Tables and Graphs from cleaned data"""

    __slots__ = ["file","database"]

    def __init__(self, file: str, database: dict) -> None:
        self.file = file
        self.database = database

    def create(self) -> None:
        # Create the contents to be written to the file
        us_exports=[]
        simulation_list_1=["01"]
        for i in simulation_list_1:
            key=(i,"qxw","Linear","Coal","USA")
            us_exports.append(self.database[key])

        line_list = ["Table 1: Changes in U.S. Coal Trade (Percent)\n",
                     "\tCoal Intensity Reduction Policy (percent)\n",
                     "\t10\t20\t30\t40\t50\n",
                     "Production\n",
                     "Consumption\n",
                     "Imports\n",
                      "Exports\t{0}\n".format(us_exports[0]),
                     #"Exports\t{0}\t{1}\t{2}\t{3}\t{4}\n".format(us_exports),
                     "\n",
                     "\n",
                     "\n",

                     "Table 2: Changes in Non-U.S. Coal Trade (Percent)\n",
                     "\tCoal Intensity Reduction Policy (percent)\n",
                     "\t10\t20\t30\t40\t50\n",
                     "Production\n",
                     "Consumption\n",
                     "Imports\n",
                     "Exports\n",
                     "\n",
                     "\n",
                     "\n",

                     "Table 3: Change in Carbon Emissions and Coal Exports from Restricting Coal Consumption\n",
                     "\tCoal Intensity Reduction Policy (percent)\n",
                     "\t10\t20\t30\t40\t50\n",
                     "Cumulative Change in Emissions by Source (million MT)\n",
                     "\tU.S. Coal\t-204\t-427\t-676\t-958\t-1,294\n",
                     "\tU.S. Oil and Gas\t31\t72\t127\t212\t368\n",
                     "\tNon-U.S.\t-1\t-2\t-2\t-3\t-4\n",
                     "\tTotal World\t-173\t-357\t-551\t-750\t-930\n",
                     "\n",
                     "Change in Total U.S. Emissions (percent)\t-3\t-6\t-10\t-13\t-17\n",
                     "\n",
                     "\n",
                     "\n",

                     "Table 4: Change in Welfare from Restricting Coal Consumption\n",
                     "\tCoal Intensity Reduction Policy (percent)\n",
                     "\t10\t20\t30\t40\t50\n",
                     "Change in Welfare (billion USD)\n",
                     "\tU.S.\t-1.3\t-5.6\t-15.3\t-36.6\t-89.9\n",
                     "\tNon-U.S.\t0.2\t0.9\t2.4\t5.7\t13.8\n",
                     "\tTotal World\t-1.1\t-4.7\t-12.9\t-30.9\t-76.1\n",
                     "\n",
                     "Ratio of Change in Welfare, Non-U.S. / U.S.\t-0.19\t-0.17\t-0.16\t-0.16\t-0.15\n",
                     "\n",
                     "Marginal U.S. Welfare Cost (USD per MT CO2)\t15\t35\t73\t166\t678\n",
                      ]

        # Create final file
        with open("Final\{0}.txt".format(self.file), "w+") as writer:  # Create the empty file
            writer.writelines(line_list)  # write the line list to the file

