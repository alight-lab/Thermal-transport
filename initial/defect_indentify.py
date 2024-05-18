import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from initial.read_data import ReadLmpData
import copy
import numpy as np


class defect_indentify:
    def __init__(self, initial, final):
        self.Initial = initial
        self.Initial_x = self.Initial.main_data['x']
        self.Initial_y = self.Initial.main_data['y']
        self.Initial_z = self.Initial.main_data['z']
        self.Masses = self.Initial.main_data['mass']

        self.Final = final
        self.Final_x = self.Final.main_data['x']
        self.Final_y = self.Final.main_data['y']
        self.Final_z = self.Final.main_data['z']
        self.defect()

    def defect(self):
        X_series_initial = copy.deepcopy(list(self.Initial_x))
        Y_series_initial = copy.deepcopy(list(self.Initial_y))
        Z_series_initial = copy.deepcopy(list(self.Initial_z))
        X_series_final = copy.deepcopy(list(self.Final_x))
        Y_series_final = copy.deepcopy(list(self.Final_y))
        Z_series_final = copy.deepcopy(list(self.Final_z))
        point_position_final = list(map(list, zip(X_series_final, Y_series_final,
                                                  Z_series_final)))
        point_position_initial = list(map(list, zip(X_series_initial, Y_series_initial,
                                                    Z_series_initial)))
        for i in range(len(point_position_initial)):
            for j in range(len(point_position_initial[i])):
                point_position_initial[i][j] = float(point_position_initial[i][j])
        for i in range(len(point_position_final)):
            for j in range(len(point_position_final[i])):
                point_position_final[i][j] = float(point_position_final[i][j])
        self.num_vacancies = 0
        self.num_interstitials = 0
        some = np.zeros((len(point_position_initial)))
        self.vacancies_position = []
        self.interstitials_position = []
        for i in range(len(point_position_final)):
            point = np.array(point_position_final[i])
            distances = np.linalg.norm(point_position_initial - point, axis=1)
            min_index = np.argmin(distances)
            some[min_index] = some[min_index] + 1
            if some[min_index] > 1:
                self.interstitials_position.append(point_position_initial[i])
                self.num_interstitials = self.num_interstitials + 1
        for i in range(len(point_position_final)):
            if int(some[i]) == 0:
                self.num_vacancies = self.num_vacancies + 1
                self.vacancies_position.append(point_position_initial[i])

if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # defect = defect_indentify('data\small 1.data', 'data\small 2.data')
    # print('Cu间隙原子数目为:', defect.num_interstitials)
    # print('Cu空位原子数目为:', defect.num_vacancies)
