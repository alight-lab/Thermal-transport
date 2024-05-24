from lammps import PyLammps

class simulator():
    def __init__(self) -> None:
        self.pylammps = PyLammps()
        self.pylammps.write_script('data/history.lmp')

    


    def __import_parameter(self):
        