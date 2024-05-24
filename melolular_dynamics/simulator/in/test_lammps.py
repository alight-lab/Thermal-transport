# from mpi4py import MPI
# from lammps import lammps
# lmp = lammps()
# lmp.command('variable x equal {}'.format(10))
# lines = open('in.melt.lmp', 'r').readlines()
# for line in lines:
#     lmp.command(line)

from lammps import lammps
lmp = lammps()
lmp.file("in.lattice")