def renew(Tot_data):
    import numpy as np
    with open ('data\lattice_final.lmp', 'w') as f:
        f.write("LAMMPS Description\n\n")
        f.write("{} atoms\n".format(Tot_data.atom_num))
        f.write("1 atom types\n")
        f.write("\n")
        # f.write("0.0 {} xlo xhi\n".format(x_length))
        # f.write("0.0 {} ylo yhi\n".format(y_length))
        # f.write("0.0 {} zlo zhi\n".format(z_length))
        # f.write("\n")
        # f.write("Masses\n\n")
        # f.write("{} {}\n".format(1, self.determine_atomic_mass()))
        # f.write("\n")
        # f.write("Atoms # atomic\n\n")

        # # д��ԭ��������Ϣ
        # for i, atom in enumerate(lattice):
        #     f.write("{} {} {} {} {}\n".format(i + 1, 1, *atom))