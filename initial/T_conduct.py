
def NEMD( TotData, velocity, EAM, time_step, Temperature0, ensemble_name, heat = 6, steps = 500, x_parti = 0.0):
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from initial.read_data import ReadLmpData
    from initial.integrate import integrate
    import numpy as np
    from initial.initialize_system import System
    from initial.eam_force import eam_force
    """
    NEMD���������¶��ݶ�
    :param TotData:
    :param velocity:
    :param EAM:
    :param time_step:
    :param Temperature0:
    :param heat:
    :param steps:
    :return:
    """
    #��ʼ��
    ensemble_name = ensemble_name
    types = len(TotData.types)
    mass = TotData.main_data['mass']
    mass = mass.to_numpy(dtype=float)                           # ����ԭ������
    x_size = TotData.BoxSize[0][1] - TotData.BoxSize[0][0]      # x�᷽�򳤶�
    if types == 1:
        num_chunk = 10                              # ����������
        dx = x_size/10
        Heat_source = 1                                             # ��Դ����
        Heat_sink = 8                                   # �Ȼ�����
        # ������
        for i in range(steps):
            position = TotData.main_data[['x', 'y', 'z']]
            position = position.to_numpy(dtype=float)
            all_chunk_pos = []  # ��Ÿ�����ԭ��λ��
            all_chunk_velocity = []  # ��Ÿ�����ԭ���ٶ�
            all_chunk_mass = []  # ��Ÿ�����ԭ������
            mark_source = []  # ��¼����Դ���Ȼ�ԭ�ӱ�ǩ
            mark_sink = []

            # ��¼����
            for j in range(num_chunk):
                chunk_pos = np.array([0, 0, 0])
                chunk_velocity = np.array([0, 0, 0])
                chunk_mass = np.array([])
                for k in range(TotData.atom_num):
                    if position[k, 0] >= j * dx and position[k, 0] < (j + 1) * dx:
                        if j == Heat_source:
                            chunk_pos = np.vstack((chunk_pos, position[k]))
                            chunk_velocity = np.vstack((chunk_velocity, velocity[k]))
                            chunk_mass = np.append(chunk_mass, mass[k])
                            mark_source.append(k)
                        elif j == Heat_sink:
                            chunk_pos = np.vstack((chunk_pos, position[k]))
                            chunk_velocity = np.vstack((chunk_velocity, velocity[k]))
                            chunk_mass = np.append(chunk_mass, mass[k])
                            mark_sink.append(k)
                        else:
                            chunk_pos = np.vstack((chunk_pos, position[k]))
                            chunk_velocity = np.vstack((chunk_velocity, velocity[k]))
                            chunk_mass = np.append(chunk_mass, mass[k])

                chunk_pos = chunk_pos[1:]
                chunk_velocity = chunk_velocity[1:]
                all_chunk_pos.append(chunk_pos)
                all_chunk_velocity.append(chunk_velocity)
                all_chunk_mass.append(chunk_mass)

            # ��ʼ���� (���¼��㿪ʼ���ù��ʵ�λ��)
            heat_energy = heat * time_step * (1.6022 * 1e-7)  # ÿ����λʱ�䴫�ݵ�����
            ke_source = 0.5 * (all_chunk_mass[Heat_source] / (1000 * 6.023e23)) * np.sum(
                np.power(all_chunk_velocity[Heat_source], 2), axis=1)
            ke_sink = 0.5 * (all_chunk_mass[Heat_sink] / (1000 * 6.023e23)) * np.sum(
                np.power(all_chunk_velocity[Heat_sink], 2), axis=1)
            ke_source = np.sum(ke_source)
            ke_sink = np.sum(ke_sink)
            gama1 = 1 + heat_energy / ke_source  # heat_energy ��ռ��Դ�ܶ��ܵı���ϵ��
            gama2 = 1 - heat_energy / ke_sink  # heat_energy ��ռ�Ȼ��ܶ��ܵı���ϵ��
            v_source = all_chunk_velocity[Heat_source]
            v_sink = all_chunk_velocity[Heat_sink]
            v_source = v_source * np.power(gama1, 1 / 2)
            v_sink = v_sink * np.power(gama2, 1 / 2)
            all_chunk_velocity[Heat_source] = v_source
            all_chunk_velocity[Heat_sink] = v_sink
            num_source = len(all_chunk_mass[Heat_source])
            num_sink = len(all_chunk_mass[Heat_sink])
            # ��ʼ������ϸ������¶�
            T_chunk = []  # ������Ų��ϸ������¶�
            for j in range(num_chunk):
                atom_num = len(all_chunk_mass[j])
                mass_chunk = all_chunk_mass[j]
                v_chunk = all_chunk_velocity[j]
                ke_chunk = 0.5 * (mass_chunk / (1000 * 6.023e23)) * np.sum(np.power(v_chunk, 2), axis=1)
                ke_chunk = np.sum(ke_chunk)
                T = (2 / 3) * ke_chunk / (atom_num * 1.380649e-23)
                T_chunk.append(T)
            # ����Դ�Ȼ��ٶ�����ٶȾ����Ա����
            for p in range(num_source):
                velocity[mark_source[p]] = v_source[p]
            for p in range(num_sink):
                velocity[mark_sink[p]] = v_sink[p]

            # nve ��ԥ
            if i == 0:
                [Temperature, TotData, velocity, EAM] = integrate(TotData, EAM, velocity, ensemble_name, Temperature0, Temperature0, 1,
                                                                  time_step)
            else:
                temp = Temperature
                [Temperature, TotData, velocity, EAM] = integrate(TotData, EAM, velocity, ensemble_name, temp,Temperature0, 1,time_step)
            x_chunk = [q * dx for q in range(1, 9)]
            x_chunk = np.array(x_chunk) * 1e-10
            T_chunk_real = T_chunk[Heat_source:Heat_sink + 1]
            dT_dx = np.gradient(T_chunk_real, x_chunk)
            dT_dx = np.mean(dT_dx)

        return [T_chunk_real, Temperature, dT_dx, heat, x_chunk]
    if types == 2:
        num_chunk = 10
        dx1 = x_parti/5
        dx2 = (x_size-x_parti)/5
        Heat_source = 1
        Heat_sink = 8
        # ������
        for i in range(steps):
            position = TotData.main_data[['x', 'y', 'z']]
            position = position.to_numpy(dtype=float)
            all_chunk_pos = []                                      # ��Ÿ�����ԭ��λ��
            all_chunk_velocity = []                                 # ��Ÿ�����ԭ���ٶ�
            all_chunk_mass = []                                     # ��Ÿ�����ԭ������
            mark_source = []                                        #��¼����Դ���Ȼ�ԭ�ӱ�ǩ
            mark_sink = []

            # ��¼����
            for j in range(num_chunk):
                chunk_pos = np.array([0,0,0])
                chunk_velocity = np.array([0,0,0])
                chunk_mass = np.array([])
                if j <= 4:
                    for k in range(TotData.atom_num):
                        if position[k, 0] >= j*dx1 and position[k, 0] < (j+1)*dx1:
                            if j == Heat_source:
                                chunk_pos = np.vstack((chunk_pos, position[k]))
                                chunk_velocity = np.vstack((chunk_velocity, velocity[k]))
                                chunk_mass = np.append(chunk_mass, mass[k])
                                mark_source.append(k)
                            elif j == Heat_sink:
                                chunk_pos = np.vstack((chunk_pos, position[k]))
                                chunk_velocity = np.vstack((chunk_velocity, velocity[k]))
                                chunk_mass = np.append(chunk_mass, mass[k])
                                mark_sink.append(k)
                            else:
                                chunk_pos = np.vstack((chunk_pos, position[k]))
                                chunk_velocity = np.vstack((chunk_velocity, velocity[k]))
                                chunk_mass = np.append(chunk_mass, mass[k])

                    chunk_pos = chunk_pos[1:]
                    chunk_velocity = chunk_velocity[1:]
                    all_chunk_pos.append(chunk_pos)
                    all_chunk_velocity.append(chunk_velocity)
                    all_chunk_mass.append(chunk_mass)
                if j > 4 and j <= 9:
                    for k in range(TotData.atom_num):
                        if position[k, 0] >= x_parti+(j-5) * dx2 and position[k, 0] < x_parti+(j - 4) * dx2:
                            if j == Heat_source:
                                chunk_pos = np.vstack((chunk_pos, position[k]))
                                chunk_velocity = np.vstack((chunk_velocity, velocity[k]))
                                chunk_mass = np.append(chunk_mass, mass[k])
                                mark_source.append(k)
                            elif j == Heat_sink:
                                chunk_pos = np.vstack((chunk_pos, position[k]))
                                chunk_velocity = np.vstack((chunk_velocity, velocity[k]))
                                chunk_mass = np.append(chunk_mass, mass[k])
                                mark_sink.append(k)
                            else:
                                chunk_pos = np.vstack((chunk_pos, position[k]))
                                chunk_velocity = np.vstack((chunk_velocity, velocity[k]))
                                chunk_mass = np.append(chunk_mass, mass[k])

                    chunk_pos = chunk_pos[1:]
                    chunk_velocity = chunk_velocity[1:]
                    all_chunk_pos.append(chunk_pos)
                    all_chunk_velocity.append(chunk_velocity)
                    all_chunk_mass.append(chunk_mass)


            # ��ʼ���� (���¼��㿪ʼ���ù��ʵ�λ��)
            heat_energy = heat*time_step*(1.6022*1e-7)                                                   # ÿ����λʱ�䴫�ݵ�����
            ke_source = 0.5 * (all_chunk_mass[Heat_source]/(1000 * 6.023e23)) * np.sum(np.power(all_chunk_velocity[Heat_source], 2), axis=1)
            ke_sink = 0.5 * (all_chunk_mass[Heat_sink]/(1000 * 6.023e23)) * np.sum(np.power(all_chunk_velocity[Heat_sink], 2), axis=1)
            ke_source = np.sum(ke_source)
            ke_sink = np.sum(ke_sink)
            gama1 = 1 + heat_energy/ke_source                                                       # heat_energy ��ռ��Դ�ܶ��ܵı���ϵ��
            gama2 = 1 - heat_energy/ke_sink                                                         # heat_energy ��ռ�Ȼ��ܶ��ܵı���ϵ��
            v_source = all_chunk_velocity[Heat_source]
            v_sink = all_chunk_velocity[Heat_sink]
            v_source = v_source * np.power(gama1, 1/2)
            v_sink = v_sink * np.power(gama2, 1/2)
            all_chunk_velocity[Heat_source] = v_source
            all_chunk_velocity[Heat_sink] = v_sink
            num_source = len(all_chunk_mass[Heat_source])
            num_sink = len(all_chunk_mass[Heat_sink])
            #��ʼ������ϸ������¶�
            T_chunk = []                                                                            # ������Ų��ϸ������¶�
            for j in range(num_chunk):
                atom_num = len(all_chunk_mass[j])
                mass_chunk = all_chunk_mass[j]
                v_chunk = all_chunk_velocity[j]
                ke_chunk = 0.5 * (mass_chunk/(1000 * 6.023e23)) * np.sum(np.power(v_chunk, 2), axis=1)
                ke_chunk = np.sum(ke_chunk)
                T = (2/3) * ke_chunk / (atom_num * 1.380649e-23)
                T_chunk.append(T)
            # ����Դ�Ȼ��ٶ�����ٶȾ����Ա����
            for p in range(num_source):
                velocity[mark_source[p]] = v_source[p]
            for p in range(num_sink):
                velocity[mark_sink[p]] = v_sink[p]

            # nve ��ԥ
            if i == 0:
                [Temperature, TotData, velocity, EAM] = integrate(TotData, EAM, velocity, ensemble_name, Temperature0, Temperature0, 1,
                                                                  time_step)
            else:
                temp = Temperature
                [Temperature, TotData, velocity, EAM] = integrate(TotData, EAM, velocity, ensemble_name, temp, Temperature0, 1,
                                                                  time_step)
            x_chunk1 = [q*dx1 for q in range(1, 5)]
            x_chunk2 = [(x_parti)+q*dx2 for q in range(4)]
            x_chunk = x_chunk1+x_chunk2
            x_chunk = np.array(x_chunk) * 1e-10
            T_chunk_real = T_chunk[Heat_source:Heat_sink+1]
            dT_dx = np.gradient(T_chunk_real[3:5], x_chunk[3:5])
            dT_dx = np.mean(dT_dx)

        return [T_chunk_real, Temperature, dT_dx, heat, x_chunk]

def compute_result(TotData, dT_dx, heat):
    """
    �����ȵ��ʣ����ݸ���Ҷ�ȴ�������
    """
    if len(TotData.types) == 1:
        S = (TotData.BoxSize[1][1]-TotData.BoxSize[1][0])*(TotData.BoxSize[2][1]-TotData.BoxSize[2][0])*1e-20
        heat1 = (heat*1.60217653*1e-7)/S
        t_conductivity = abs(heat1/dT_dx)
        return t_conductivity
    if len(TotData.types) == 2:
        S = (TotData.BoxSize[1][1] - TotData.BoxSize[1][0]) * (TotData.BoxSize[2][1] - TotData.BoxSize[2][0]) * 1e-20
        heat1 = (heat * 1.60217653 * 1e-7) / S
        t_conductivity = abs(heat1 / dT_dx)
        return t_conductivity



if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from initial.read_data import ReadLmpData
    from compute.integrate import integrate
    import numpy as np
    from initial.initialize_system import System
    from compute.eam_force import eam_force
    from initial.lattice import Lattice
    from mix import mixture

    copper_lattice = Lattice(element="Cu")
    copper_lattice.write_lmp_file("copper.lmp", x=10, y=3, z=3)
    iron_lattice = Lattice(element="Fe")
    iron_lattice.write_lmp_file("iron.lmp", x=10, y=3, z=3)
    # x_parti = mixture("D:\\all_code\PyCode\\app_v1\compute\\copper.lmp", "D:\\all_code\PyCode\\app_v1\compute\\iron.lmp")
    TotData = ReadLmpData('file.data')
    TotData.run_read()
    position = TotData.main_data[['x', 'y', 'z']]
    position = position.to_numpy(dtype=float)
    system = System(TotData, 1e-15)
    velocity =  system.initialize()
    EAM = eam_force('CuFe.eam.alloy', TotData)
    EAM.read_eam()
    EAM.compute_eam()

    [T_chunk_real, Temperature, dT_dx, heat, x_chunk] = NEMD(TotData, velocity, EAM, system.time_step, system.temperature0,x_parti=35.1975)
    s = compute_result(TotData, dT_dx, heat)
    print(s)
    print(T_chunk_real)
    print(dT_dx)