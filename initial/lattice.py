import os
import sys
import numpy as np
class Lattice:
    def __init__(self, element):
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.path = sys.path[len(sys.path) - 1]
        self.element = element
        # Ԫ�ص���������ӳ���ֵ�
        self.element_lattice_constants = {
            "Cu": 3.61,
            "Ag": 4.09,
            "Au": 4.08,
            "Ni": 3.52,
            "Pd": 3.89,
            "Pt": 3.92,
            "Al": 4.05,
            "Pb": 4.95,
            "Fe": 2.87,
            "Mo": 3.15,
            "Ta": 3.30,
            "W": 3.16,
            "Mg": 3.21,
            "Co": 3.54,
            "Ti": 3.32,
            "Cr": 2.88,
            "Zr": 3.23
        }
        # Ԫ�ص�����ṹ���͵�ӳ���ֵ�
        self.element_structures = {
            "Cu": "fcc",
            "Ag": "fcc",
            "Au": "fcc",
            "Ni": "fcc",
            "Pd": "fcc",
            "Pt": "fcc",
            "Al": "fcc",
            "Pb": "fcc",
            "Fe": "bcc",
            "Mo": "bcc",
            "Ta": "bcc",
            "W": "bcc",
            "Mg": "fcc",
            "Co": "fcc",
            "Ti": "fcc",
            "Cr": "bcc",
            "Zr": "bcc"
        }
        # Ԫ�ص����ԭ��������ӳ���ֵ�
        self.element_atomic_masses = {
            "Cu": 63.55,
            "Ag": 107.87,
            "Au": 196.97,
            "Ni": 58.69,
            "Pd": 106.42,
            "Pt": 195.08,
            "Al": 26.98,
            "Pb": 207.2,
            "Fe": 55.85,
            "Mo": 95.95,
            "Ta": 180.95,
            "W": 183.84,
            "Mg": 24.31,
            "Co": 58.93,
            "Ti": 47.87,
            "Cr": 51.99,
            "Zr": 91.22
        }

    def determine_lattice_constant(self):
        # ����Ԫ�������Ҿ�����
        if self.element in self.element_lattice_constants:
            return self.element_lattice_constants[self.element]
        else:
            raise ValueError("Unsupported element")

    def determine_lattice_type(self):
        # ����Ԫ�������Ҿ���ṹ����
        if self.element in self.element_structures:
            return self.element_structures[self.element]
        else:
            raise ValueError("Unsupported element")

    def determine_atomic_mass(self):
        # ����Ԫ�����������ԭ������
        if self.element in self.element_atomic_masses:
            return self.element_atomic_masses[self.element]
        else:
            raise ValueError("Unsupported element")

    def generate_lattice(self, x, y, z):
        lattice_constant = self.determine_lattice_constant()
        lattice_type = self.determine_lattice_type()
        if lattice_type == "fcc":
            return self.generate_fcc_lattice(lattice_constant, x, y, z)
        elif lattice_type == "bcc":
            return self.generate_bcc_lattice(lattice_constant, x, y, z)
        elif lattice_type == "sc":
            return self.generate_sc_lattice(lattice_constant, x, y, z)
        else:
            raise ValueError("Unsupported lattice type")

    def generate_fcc_lattice(self, lattice_constant, x, y, z):

        lattice = []
        for i in range(x):
            for j in range(y):
                for k in range(z):
                    lattice.append([i, j, k])
                    lattice.append([i + 0.5, j + 0.5, k])
                    lattice.append([i, j + 0.5, k + 0.5])
                    lattice.append([i + 0.5, j, k + 0.5])
        return np.array(lattice) * lattice_constant

    def generate_bcc_lattice(self, lattice_constant, x, y, z):

        lattice = []
        for i in range(x):
            for j in range(y):
                for k in range(z):
                    lattice.append([i, j, k])
                    lattice.append([i + 0.5, j + 0.5, k + 0.5])
        return np.array(lattice) * lattice_constant

    def generate_sc_lattice(self, lattice_constant, x, y, z):
        lattice = []
        for i in range(x):
            for j in range(y):
                for k in range(z):
                    lattice.append([i, j, k])
        return np.array(lattice) * lattice_constant

    def write_lmp_file(self, filename, x, y, z):
        lattice = self.generate_lattice(x, y, z)
        x_length = self.determine_lattice_constant() * x
        y_length = self.determine_lattice_constant() * y
        z_length = self.determine_lattice_constant() * z
        with open(filename, 'w') as f:
            # д��ͷ����Ϣ
            f.write("LAMMPS Description\n\n")
            f.write("{} atoms\n".format(len(lattice)))
            f.write("1 atom types\n")
            f.write("\n")
            f.write("0.0 {} xlo xhi\n".format(x_length))
            f.write("0.0 {} ylo yhi\n".format(y_length))
            f.write("0.0 {} zlo zhi\n".format(z_length))
            f.write("\n")
            f.write("Masses\n\n")
            f.write("{} {}\n".format(1, self.determine_atomic_mass()))
            f.write("\n")
            f.write("Atoms # atomic\n\n")

            # д��ԭ��������Ϣ
            for i, atom in enumerate(lattice):
                f.write("{} {} {} {} {}\n".format(i + 1, 1, *atom))

if __name__ == "__main__":
    # ʹ���µ�Lattice�������ɾ���ģ�Ͳ�����д��.lmp�ļ���
    import numpy as np
    copper_lattice = Lattice(element="Cu")
    copper_lattice.write_lmp_file("copper.lmp", x=3, y=4, z=5)

    # ʹ���������ɾ���ģ��
    iron_lattice = Lattice(element="Fe")
    iron_lattice.write_lmp_file("iron.lmp", x=3, y=4, z=5)










