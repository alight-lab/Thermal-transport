# coding=gbk
# ��ʼ����ϵ������

class System:
    """
    ��ʼ��ϵͳ��
    temperature0: ϵͳ���¶�Ĭ��Ϊ1000
    run_num: �����в����� Ĭ��ֵΪ10000
    kB: ������������ ��J/K��
    NA: ����٤���޳��� (mol^-1)
    timestep: ����
    epsilon, sigma: lj�ƺ������� ��λ��{(J), (m)}
    cutoff: �ضϰ뾶
    velocity: �ٶȾ������зֱ�Ϊvx, vy, vz
    """

    kB = 1.380649e-23
    NA = 6.023e23
    def __init__(self, total_data, time_step=1e-15, temperature0 = 300):
        self.temperature0 = temperature0
        self.total_data = total_data
        self.time_step = time_step

    def initialize(self):
        import numpy as np
        velocity = np.zeros((self.total_data.atom_num, 3))
        type_list = self.total_data.main_data['type'].to_numpy(np.int32)
        for i in self.total_data.types:
            for j, x in enumerate(type_list):
                if x == i:
                    velocity[j, :] = np.random.normal(pow(3*1000*self.kB*self.temperature0*self.NA/self.total_data.Masses[i-1], 0.5), np.random.uniform(10,25))
        theta = np.multiply(np.random.uniform(0,1, (self.total_data.atom_num, 1)), 2*np.pi)
        phi = np.multiply(np.random.uniform(0,1, (self.total_data.atom_num, 1)), np.pi)
        Transformation_matrix = np.concatenate((np.multiply(np.sin(phi), np.cos(theta)), np.multiply(np.sin(phi), np.sin(theta)), np.cos(phi)), axis=1)
        velocity = np.multiply(velocity, Transformation_matrix)
        velocity = velocity
        return velocity