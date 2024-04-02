
import pandas as pd
import numpy as np
class ReadLmpData:
    """
    ��ȡ�ļ��������ļ���Ҫ���ݷ���һ��DataFrame��
    ����������Ϊԭ����ţ�ԭ�����࣬ԭ�����꣬ԭ������
    """

    def __init__(self, filename):
        self.BoxSize = []  # ���Ӵ�С
        self.Length = []
        self.Masses = []  # ������ԭ������
        self.main_data = 0  # DataFrame
        self.atom_num = 0  # ԭ������
        self.types = []
        self.filename = filename
    def box_size(self):
        """
        ������Ӵ�С
        :return:
        """
        with open(self.filename, 'r') as f:
            line = f.readline()
            while line.find('xlo') == -1:  # ���ļ�ָ���Ƶ�xlo��һ��
                line = f.readline()
            temp1 = line.split()  # ��line�и��ݿհ׷��ֿ�
            temp_1 = float(temp1[0])  # temp_1���������������
            temp1 = float(temp1[1])  # temp1�������������ұ�
            m1 = [temp_1, temp1]  # m1��x����ĳߴ�

            f.seek(0)
            line = f.readline()
            while line.find('ylo') == -1:  # ���ļ�ָ���Ƶ�ylo��һ��
                line = f.readline()
            temp2 = line.split()  # ��line�и��ݿհ׷��ֿ�
            temp_2 = float(temp2[0])  # temp_2���������������
            temp2 = float(temp2[1])  # temp2�������������ұ�
            m2 = [temp_2, temp2]

            f.seek(0)
            line = f.readline()
            while line.find('zlo') == -1:  # ���ļ�ָ���Ƶ�zlo��һ��
                line = f.readline()
            temp3 = line.split()  # ��line�и��ݿհ׷��ֿ�
            temp_3 = float(temp3[0])  # temp_3���������������
            temp3 = float(temp3[1])  # temp3�������������ұ�
            m3 = [temp_3, temp3]

        self.BoxSize = [m1, m2, m3]
        self.Length = [temp1 - temp_1, temp2 - temp_2, temp3 - temp_3]  # �����������ĳ���
        # BoxSize����������ĳߴ�
        # Length����������ĳ���
        f.close()

    def atom_position(self):
        """
        �����Ҫ��Ϣ��
        ԭ��λ�ã���ţ����࣬��ԭ��������
        :return:
        """
        with open(self.filename) as f:
            lines = f.readlines()
            for i, line in enumerate(lines): # for ѭ���õ��ļ���Ҫ����
                if 'Atoms' in line:
                    self.main_data = lines[i + 1:]
                    data_type_line = line.split()  #������У���������ж�data�ļ���ʽ
            for i, line in enumerate(self.main_data):
                self.main_data[i] = self.main_data[i].split()
        f.close()
        self.main_data = pd.DataFrame(self.main_data) # ת��ΪDataFrame��ʽ�������������
        self.main_data = self.main_data.replace(to_replace='None', value=np.nan).dropna(axis=0, how='all') # ��ȥ����
        self.atom_num = len(self.main_data) # �õ�ԭ������
        if 'atomic' in data_type_line:
            self.main_data.columns = ["serial number", "type", "x", "y", "z"] # Ϊ������ϱ���
            self.main_data['mass'] = None
            for i in range(self.atom_num): # forѭ�������õ�ÿ��ԭ�ӵ����������뵽DataFrame��
                pos = self.types.index(int(self.main_data['type'][i+1]))
                self.main_data['mass'][i+1] = self.Masses[pos]
            self.atom_num = len(self.main_data) # �õ�ԭ������
        elif 'charge' in data_type_line:
            self.main_data.columns = ["serial number", "type", "charge_number", "x", "y", "z"] # Ϊ������ϱ���
            self.main_data['mass'] = None
            for i in range(self.atom_num): # forѭ�������õ�ÿ��ԭ�ӵ����������뵽DataFrame��
                pos = self.types.index(int(self.main_data['type'][i+1]))
                self.main_data['mass'][i+1] = self.Masses[pos]


    def atom_type(self):
        """
        ͳ��ԭ������
        :return:
        """
        with open(self.filename, 'r') as f:
            line = f.readline()
            while line.find('Masses') == -1:
                line = f.readline()
            line = f.readline()
            while line.find('Atoms') == -1:
                line = line.strip() # ȥ������
                if line:
                    data = line.split()
                    self.types.append(int(data[0]))
                    self.Masses.append(float(data[1]))
                line = f.readline()
        f.close()

    def run_read(self):
        """
        ���к���
        :return:
        """
        self.box_size()
        self.atom_type()
        self.atom_position()


if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    path = sys.path[0].replace('initial', 'data')
    TotData = ReadLmpData(path + "\\file.data")
    TotData.run_read()
    # print(TotData.main_data)
    position = TotData.main_data[['x', 'y', 'z']]
    position = position.to_numpy(dtype=float)
    print("ԭ������Ϊ��\n", TotData.types)
    # print("������ԭ��������\n", TotData.Masses)
    # print("���Ӵ�С:\n", TotData.BoxSize[:])
    # print("ԭ������:\n", TotData.atom_num)
    print(position*10**(-9))