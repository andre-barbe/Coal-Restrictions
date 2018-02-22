__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-19"
__altered__ = "2017-10-19"

import os


class Cleanup(object):
    """Deletes intermediate work files"""

    __slots__ = ["project", "simulation_list"]

    def __init__(self, project: str, simulation_list: list) -> None:
        self.project = project
        self.simulation_list = simulation_list

    def main(self) -> None:
        # Deletes intermediate work files
        [os.remove(os.path.join("Results", f)) for f in os.listdir("Results") if f.endswith(".csv")]
        [os.remove(os.path.join("GTAP_Files\SaveSims", f)) for f in os.listdir("GTAP_Files\SaveSims")]
        [os.remove(os.path.join("Final", f)) for f in os.listdir("Final")]
