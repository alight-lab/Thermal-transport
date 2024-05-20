"""
生成点缺陷，模拟材料辐照后的状态
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def defect(filename, defect_num):
    """
    先读取文件内容
    改变Tot_data生成缺陷
    生成缺陷后返回Tot_data
    :param filename:
    :return: Tot_data
    """
    from initial.read_data import ReadLmpData
    import numpy as np

    Tot_data = ReadLmpData(filename)
    Tot_data.run_read()
    position = Tot_data.main_data[['x', 'y', 'z']]
    position = position.to_numpy(dtype=float)
    atom_id = np.random.choice(Tot_data.atom_num, defect_num, replace=False)
    for i in range(defect_num):
        position[atom_id[i]][0] = np.random.uniform(Tot_data.BoxSize[0][0], Tot_data.BoxSize[0][1])
        position[atom_id[i]][1] = np.random.uniform(Tot_data.BoxSize[1][0], Tot_data.BoxSize[1][1])
        position[atom_id[i]][2] = np.random.uniform(Tot_data.BoxSize[2][0], Tot_data.BoxSize[2][1])
    Tot_data.main_data[['x', 'y', 'z']] = position
    return Tot_data



if __name__ == "__main__":
    Total_data = defect("data/Cu1.lmp", 100)
    print(Total_data.main_data)