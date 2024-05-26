from initial.read_data import ReadLmpData

def renew(Tot_data):
    import numpy as np
    with open ('data\lattice.lmp', 'w') as f:
        f.write("LAMMPS Description\n\n")
        f.write("{} atoms\n".format(Tot_data.atom_num))
        f.write("{} atom types\n".format(len(Tot_data.types)))
        f.write("\n")
        f.write("0.0 {} xlo xhi\n".format(Tot_data.BoxSize[0][1]))
        f.write("0.0 {} ylo yhi\n".format(Tot_data.BoxSize[1][1]))
        f.write("0.0 {} zlo zhi\n".format(Tot_data.BoxSize[2][1]))
        f.write("\n")
        f.write("Masses\n\n")
        if len(Tot_data.Masses) == 1:
            f.write("{} {}\n".format(1, Tot_data.Masses[0]))
        else:
            f.write("{} {}\n".format(1, Tot_data.Masses[0]))
            f.write("{} {}\n".format(2, Tot_data.Masses[1]))
        f.write("\n")
        f.write("Atoms # atomic\n\n")

        # д��ԭ��������Ϣ
        for i in range(Tot_data.atom_num):
            f.write("{} {} {} {} {}\n".format(i + 1, int(Tot_data.main_data.iloc[i, 1]), 
                                              Tot_data.main_data.iloc[i, 2],
                                              Tot_data.main_data.iloc[i, 3],
                                              Tot_data.main_data.iloc[i, 4]))

if __name__ == '__main__':
    ReadLmpData = ReadLmpData('data\Cu1.lmp')
    ReadLmpData.run_read()
    renew(ReadLmpData)