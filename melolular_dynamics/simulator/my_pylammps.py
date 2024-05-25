from lammps import PyLammps
from parameter import *
import sys

class MyPyLammps():
    variable: Variable
    py_lammps: PyLammps
    def __init__(self, in_name: str, var: Variable) -> None:
        self.variable = var
        self.py_lammps = PyLammps()
        self.load_commands()
        self.load_in(in_name)


    def load_commands(self):
        for cmd in self.variable.commands:
            self.py_lammps.command(cmd)

    
    def load_in(self, name:str):
        with open(name, 'r',encoding='UTF-8') as file:
            for line in file.readlines():
                self.py_lammps.command(line)


if __name__ == '__main__':
    from mpi4py import MPI
    var = Variable(
        [AtomTypeContainer(
            AtomType.Cu,
            5,5,5
        ),
        # AtomTypeContainer(
        #     AtomType.Ag,
        #     5,5,5
        # )
        ],
        SystemVarContainer(
            200,300,Ensemble.nve,1,10,Ensemble.nvt,1,100
        )
    )

    # in_file = 'melolular_dynamics\simulator\in\in.lattice_2'
    in_file = 'melolular_dynamics\simulator\in\in.lattice'

    my_lammps = MyPyLammps(in_file, var)

    me = MPI.COMM_WORLD.Get_rank()
    nprocs = MPI.COMM_WORLD.Get_size()
    print("Proc %d out of %d procs has" % (me,nprocs), my_lammps.py_lammps)

    MPI.Finalize()