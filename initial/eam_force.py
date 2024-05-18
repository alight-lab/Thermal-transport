
"""
����eam�Ƽ�����������
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from initial.read_data import ReadLmpData
class eam_force:

    def __init__(self, filename, TotData):
        self.filename = filename
        self.TotData = TotData
        self.drho = 0
        self.dr = 0
        self.cutoff = 0
        self.Fp_li = None
        self.rhor_li = None
        self.phi_li = None
        self.atom_types = 0
        self.pe = 0
        self.force = None
    def read_eam(self):
        """
        ��ȡ�ƺ����ļ�����
        :return:
        """
        import numpy as np
        with open(self.filename) as fp:
            for i in range(4):
                line = fp.readline()
            temp0 = line.split()
            self.atom_types = int(temp0[0])
            line = fp.readline()
            temp1 = line.split()
            line = fp.readline()
            temp2 = line.split()
            self.drho = float(temp1[1])
            self.dr = float(temp1[3])
            self.cutoff = float(temp1[4])
            mass = []
            lattice = []
            mass.append(float(temp2[1]))
            lattice.append(float(temp2[2]))
            if self.atom_types == 1:
                self.Fp_li = np.zeros((400, 5))
                self.rhor_li = np.zeros((400, 5))
                self.phi_li = np.zeros((400, 5))
                for i in range(400):
                    self.Fp_li[i, :] = fp.readline().split()
                for i in range(400):
                    self.rhor_li[i, :] = fp.readline().split()
                for i in range(400):
                    self.phi_li[i, :] = fp.readline().split()
                self.Fp_li = self.Fp_li.flatten().astype(float)
                self.phi_li = self.phi_li.flatten().astype(float)
                self.rhor_li = self.rhor_li.flatten().astype(float)
            elif self.atom_types == 2:
                self.Fp_li = np.zeros((800, 5))
                self.rhor_li = np.zeros((800, 5))
                self.phi_li = np.zeros((1200, 5))
                for i in range(400):
                    self.Fp_li[i, :] = fp.readline().split()
                for i in range(400):
                    self.rhor_li[i, :] = fp.readline().split()
                line = fp.readline()
                temp2 = line.split()
                mass.append(float(temp2[1]))
                lattice.append(float(temp2[2]))
                for i in range(400, 800):
                    self.Fp_li[i, :] = fp.readline().split()
                for i in range(400, 800):
                    self.rhor_li[i, :] = fp.readline().split()
                for i in range(1200):
                    self.phi_li[i, :] = fp.readline().split()
                self.Fp_li = self.Fp_li.flatten().astype(float)
                self.phi_li = self.phi_li.flatten().astype(float)
                self.rhor_li = self.rhor_li.flatten().astype(float)
        fp.close()
    def compute_eam(self):
    #����������
        import numpy as np
        position = self.TotData.main_data[['x', 'y', 'z']]
        position = position.to_numpy(dtype=float)
        n, m = position.shape
        # ����Gram ����
        G = np.dot(position, position.T)
        H = np.tile(np.diag(G), (n, 1))
        # ��ʼ�����������Ϊ��n�����������������n x n
        dist = np.sqrt(H + H.T - 2*G)
    #��������
        if self.atom_types == 1:
            Tot_pe = 0
            atom_force = np.zeros((self.TotData.atom_num, 3))
            for i in range(self.TotData.atom_num-1):
                rhor_i = 0
                phi_i = 0
                for j in range(i+1, self.TotData.atom_num):
                    if dist[i][j] < self.cutoff:
                        distij = (position[i] - position[j])/dist[i][j]
                        n = int(dist[i][j]//self.dr)
                        rhor = self.rhor_li[n]
                        rhor_i += rhor
                        phi = self.phi_li[n]/(n*self.dr)
                        phi_i += (1/2)*phi
                        atom_pe2 = (1 / 2) * phi
                        atom_force[i] = (atom_pe2/dist[i][j])*distij + atom_force[i]
                        atom_force[j] = atom_force[j] - (atom_pe2/dist[i][j])*distij
                if rhor_i > self.Fp_li[-1]:
                    Fp_i = self.Fp_li[-1]
                else:
                    Fp_i = self.Fp_li[int(rhor_i//self.drho)]
                Tot_pe += Fp_i+phi_i
            Tot_pe = Tot_pe*1.60217e-19
            where_are_inf = np.isinf(atom_force)
            atom_force[where_are_inf] = 0
            self.pe = Tot_pe
            self.force = atom_force
        elif self.atom_types == 2:
            Tot_pe = 0
            atom_force = np.zeros((self.TotData.atom_num, 3))
            for i in range(self.TotData.atom_num-1):
                rhor_i = 0
                phi_i = 0
                for j in range(i+1, self.TotData.atom_num):
                    if dist[i][j] < self.cutoff:
                        distij = (position[i] - position[j]) / dist[i][j]
                        n = int(dist[i][j] // self.dr)
                        rhor = self.rhor_li[n]
                        rhor_i += rhor
                        sum_type = int(self.TotData.main_data.loc[i + 1, 'type']) + int(self.TotData.main_data.loc[j + 1, 'type']) - 2
                        phi = self.phi_li[sum_type*400 + n]/(n*self.dr)
                        phi_i += (1/2)*phi
                        atom_pe2 =(1 / 2) * phi
                        atom_force[i] = (atom_pe2 / dist[i][j]) * distij + atom_force[i]
                        atom_force[j] = atom_force[j] - (atom_pe2 / dist[i][j]) * distij
                if rhor_i > self.Fp_li[-1]:
                    Fp_i = self.Fp_li[-1]
                else:
                    Fp_i = self.Fp_li[int(rhor_i // self.drho)]
                Tot_pe += Fp_i+phi_i
            Tot_pe = Tot_pe * 1.60217e-19
            where_are_inf = np.isinf(atom_force)
            atom_force[where_are_inf] = 0
            self.pe = Tot_pe
            self.force = atom_force












if __name__ == "__main__":
    import time
    import numpy as np
    start = time.perf_counter()
    TotData = ReadLmpData("Cu1.lmp")
    TotData.run_read()
    EAM = eam_force('Cu.eam.alloy', TotData)
    EAM.read_eam()
    EAM.compute_eam()
    print(EAM.force)
    print(EAM.pe)
    np.savetxt("dets.txt", EAM.force, fmt='%f', delimiter=',')
    end = time.perf_counter()