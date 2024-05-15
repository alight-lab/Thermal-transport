import os
import sys
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
def integrate(Tot_data, EAM, velocity, choose, Temperature0, Temperature_set, num, time_step):
    NA = 6.02 * 10 ** 23
    KB = 1.380649 * 10 ** (-23)
    force = EAM.force * 1.6022 * 10 ** (-9)       #转化成J/m
    position = Tot_data.main_data[['x', 'y', 'z']]
    position = position.to_numpy(dtype=float)
    position = position * 10 ** (-10)
    mass = Tot_data.main_data.iloc[:, 5]
    mass = mass.to_numpy(dtype=float)
    mass = (mass / NA) * 10 ** (-3)  # 单位为kg
    length = Tot_data.BoxSize[:]
    length = np.array(length)
    length = length * 10 ** (-10)  # 单位为m
    for i_num in range(num):
        for i in range(Tot_data.atom_num):
            for j in range(3):
                position[i][j] = (position[i][j] + velocity[i][j] * time_step + 0.5 *
                                       (force[i][j] / mass[i]) * time_step ** 2)
                if j != 0 :
                    if position[i][j] > length[j][1]:
                        n1 = int(position[i][j] / length[j][1])
                        position[i][j] = position[i][j] - n1 * length[j][1]
                    if position[i][j] < length[j][0]:
                        n1 = math.ceil(position[i][j] / length[j][1])
                        position[i][j] = position[i][j] - n1 * length[j][1] + length[j][1]
                if j == 0 :
                    if position[i][j] > length[j][1]:
                        n1 = int(position[i][j] / length[j][1])
                        position[i][j] = length[j][1] - (position[i][j] - n1 * length[j][1])
                        velocity[i][j] = velocity[i][j] * (-1)
                    if position[i][j] < length[j][0]:
                        n1 = math.ceil(position[i][j] / length[j][1])
                        position[i][j] = length[j][1] - (position[i][j] - n1 * length[j][1] + length[j][1])
                        velocity[i][j] = velocity[i][j] * (-1)
        some0 = []
        some1 = []
        some2 = []
        for h in range(Tot_data.atom_num):
            some0.append(position[h][0]* 10 ** 10)
            some1.append(position[h][1]* 10 ** 10)
            some2.append(position[h][2]* 10 ** 10)
        Tot_data.main_data.loc[:, 'x'] = some0
        Tot_data.main_data.loc[:, 'y'] = some1
        Tot_data.main_data.loc[:, 'z'] = some2
        if choose == 'nvt':
            if i_num == 0:
                time = 0
            time_coupling = time_step*2
            Temperature = Temperature_set + (Temperature0 - Temperature_set) * math.e ** (-1 * time / time_coupling)
            time = time + time_step
            velocity = velocity * (1 + time_step * (Temperature_set / Temperature - 1) / time_coupling) ** 0.5
        if choose == 'nve':
            for i in range(Tot_data.atom_num):
                for j in range(3):
                    velocity[i][j] = (velocity[i][j] + force[i][j]
                                           * time_step / (mass[i]))
            ke = 0
            for i in range(len(velocity)):
                for j in range(3):
                    ke = ke + 0.5 * mass[i] * velocity[i][j] ** 2
            Temperature = 2 * ke / (3 * Tot_data.atom_num * KB)
            EAM.compute_eam()
            force = EAM.force * 1.6022 * 10 ** (-9)
    return [Temperature, Tot_data, velocity, EAM]

if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from initial.read_data import ReadLmpData
    from initial.integrate import integrate
    import numpy as np
    from initial.initialize_system import System
    from initial.eam_force import eam_force
    TotData = ReadLmpData('data\Cu1.lmp')
    TotData.run_read()
    position = TotData.main_data[['x', 'y', 'z']]
    position = position.to_numpy(dtype=float)
    system = System(TotData, time_step=1e-15, temperature0=300)
    velocity =  system.initialize()
    EAM = eam_force('data\\Cu.eam.alloy', TotData)
    EAM.read_eam()
    EAM.compute_eam()

    for i in range(10):
        if i == 0:
            Temperature = 300
        [Temperature, TotData, velocity, EAM] = integrate(TotData, EAM, velocity, 'nve', Temperature, 400, 1,
                                                              system.time_step)
        print(Temperature)