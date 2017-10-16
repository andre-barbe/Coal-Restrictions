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
        line_list1 = ["qxw\thello\n",
                     "qiw\n",
                     "qo\n",
                     "pm\n",
                     "gco2\n"
                     "ev"  # this only has one matrix and so can sometime cause problems
                     ]

        # Create final file
        with open("Final\{0}.txt".format(self.file), "w+") as writer:  # Create the empty file
            writer.writelines(line_list1)  # write the line list to the file

