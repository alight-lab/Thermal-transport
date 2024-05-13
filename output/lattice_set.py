def lattice_set(element1, element2, element3, size1, size2, size3):
    from initial.lattice import Lattice
    from initial.mix import mixture
    import numpy as np
    import os
    if element1 != '':
        lattice = Lattice(element=element1)
        lattice.write_lmp_file('data\lattice.lmp', x=size1[0], y=size1[1], z=size1[2])
        x = 0.0
    if element2 != '' and element3 != '':
        lattice_1 = Lattice(element=element2)
        lattice_1.write_lmp_file('data\lattice_1.lmp', x=size2[0], y=size2[1], z=size2[2])
        lattice_2 = Lattice(element=element3)
        lattice_2.write_lmp_file('data\lattice_2.lmp', x=size3[0], y=size3[1], z=size3[2])
        x = mixture('data\lattice_1.lmp', 'data\lattice_2.lmp')
    return x