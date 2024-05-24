from lammps import PyLammps
from simulator import *

class MyPyLammps(PyLammps):
    variable: Variable
    def __init__(self, name="", var = Variable, cmdargs=None, ptr=None, comm=None, verbose=False):
        super().__init__(name, cmdargs, ptr, comm, verbose)
        self.load_commands()
        self.load_in(name)


    def load_commands(self):
        for cmd in self.variable.commands:
            self.command(cmd)

    
    def load_in(self, name:str):
        lines = open(name, 'r').readlines
        for line in lines:
            self.command(line)


if __name__ == '__main__':
    from mpi4py import MPI
    var = Variable(
        [AtomTypeContainer(
            AtomType.Ag,
            5,5,5
        ),
        AtomTypeContainer(
            AtomType.Cu,
            5,5,5
        )
        ],
        SystemVarContainer(
            200,300,Ensemble.nve,1,10,Ensemble.nvt,1,100
        )
    )

    in_file = 'in/in.lattice'

    my_lammps = MyPyLammps(in_file, var)

    MPI.Finalize()

