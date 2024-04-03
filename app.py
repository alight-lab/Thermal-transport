import time
import os
import sys
import numpy as np
import copy
from main import Ui_Form
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
# from PyQt5.QtDataVisualization import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
from initial.create_eam import create_eam
from initial.read_data import ReadLmpData
from initial.initialize_system import System
from initial.lattice import Lattice
from compute.mix import mixture
from compute.T_conduct import NEMD, compute_result
from compute.eam_force import eam_force
from compute.integrate import integrate
from compute.vacf_pdos import find_pdos
from compute.defect_indentify import defect_indentify
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.atom_all = ['请选择', "Cu", "Ag", "Au", "Ni", "Pd", "Pt", "Al", "Pb", "Fe", "Mo", "Ta", "W"]
        self.radioButton.setChecked(True)
        self.checkBox.setEnabled(False)
        self.setting()
        self.comboBox.currentIndexChanged.connect(self.create_lattice)
        self.comboBox_2.currentIndexChanged.connect(self.create_lattice)
        self.comboBox_4.currentIndexChanged.connect(self.create_lattice)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.spinBox.valueChanged.connect(self.create_lattice)
        self.spinBox_2.valueChanged.connect(self.create_lattice)
        self.spinBox_3.valueChanged.connect(self.create_lattice)
        self.spinBox_6.valueChanged.connect(self.create_lattice)
        self.spinBox_7.valueChanged.connect(self.create_lattice)
        self.spinBox_8.valueChanged.connect(self.create_lattice)
        self.spinBox_9.valueChanged.connect(self.create_lattice)
        self.spinBox_10.valueChanged.connect(self.create_lattice)
        self.spinBox_13.valueChanged.connect(self.create_lattice)
        self.checkBox.clicked.connect(self.plot_atom_final)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.radioButton.clicked.connect(self.choose_page_0)
        self.radioButton_2.clicked.connect(self.choose_page_1)
        self.pushButton.clicked.connect(self.main_compute)

    def setting(self):
        self.lineEdit.setText('300')
        self.lineEdit_2.setText('1')
        self.lineEdit_5.setText('1')
        self.comboBox.addItems(self.atom_all)
        self.comboBox_2.addItems(self.atom_all)
        self.comboBox_4.addItems(self.atom_all)
        self.comboBox_3.addItem('nvt')
        self.comboBox_3.addItem('nve')
        self.comboBox_7.addItem('nvt')
        self.comboBox_7.addItem('nve')
        self.spinBox_6.setValue(1)
        self.spinBox_7.setValue(1)
        self.spinBox_8.setValue(1)
        self.spinBox.setValue(1)
        self.spinBox_2.setValue(1)
        self.spinBox_3.setValue(1)
        self.spinBox_9.setValue(1)
        self.spinBox_10.setValue(1)
        self.spinBox_13.setValue(1)
        self.spinBox_6.setMinimum(1)
        self.spinBox_7.setMinimum(1)
        self.spinBox_8.setMinimum(1)
        self.spinBox.setMinimum(1)
        self.spinBox_2.setMinimum(1)
        self.spinBox_3.setMinimum(1)
        self.spinBox_9.setMinimum(1)
        self.spinBox_10.setMinimum(1)
        self.spinBox_13.setMinimum(1)
        self.spinBox_4.setMinimum(1)
        self.spinBox_11.setMinimum(1)

        self.spinBox_4.setValue(10) # 弛豫迭代步数
        self.spinBox_4.setMaximum(1000)
        self.spinBox_5.setValue(0)  # 点缺陷
        self.spinBox_11.setValue(10)    # 热导率迭代步数
        self.spinBox_12.setValue(10)    # 热流
        self.atom_background()
        self.T_time_background()
        self.T_X_background()
        self.pdos_omega_background()
        self.create_lattice()

    def choose_page_0(self):
        self.checkBox.setChecked(False)
        self.checkBox.setEnabled(False)
        self.radioButton.setChecked(True)
        self.radioButton_2.setChecked(False)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_7.setText('')
        self.lineEdit_6.setText('')
        self.create_lattice()

    def choose_page_1(self):
        self.checkBox.setChecked(False)
        self.checkBox.setEnabled(False)
        self.radioButton.setChecked(False)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_7.setText('')
        self.lineEdit_6.setText('')
        self.ax_T_time.cla()
        self.ax_T_X.cla()
        self.ax_pdos_omega.cla()
        self.create_lattice()

    def create_lattice(self):
        self.element_0 = self.comboBox_4.currentText()
        self.element_1 = self.comboBox.currentText()
        self.element_2 = self.comboBox_2.currentText()
        self.x0 = int(self.spinBox_6.text())
        self.y0 = int(self.spinBox_7.text())
        self.z0 = int(self.spinBox_8.text())
        self.x1 = int(self.spinBox.text())
        self.y1 = int(self.spinBox_2.text())
        self.z1 = int(self.spinBox_3.text())
        self.x2 = int(self.spinBox_9.text())
        self.y2 = int(self.spinBox_10.text())
        self.z2 = int(self.spinBox_13.text())
        if self.radioButton.isChecked() == True:
            if self.radioButton.isChecked() == True and self.element_0 != '请选择':
                LATTICE = Lattice(element=self.element_0)
                LATTICE.write_lmp_file('lattice_0.lmp', x=self.x0, y=self.y0, z=self.z0)
                self.Tot_data = ReadLmpData(sys.path[0] + '\\data\\lattice_0.lmp')
                self.Tot_data.run_read()
                self.Tot_data_initial = copy.deepcopy(self.Tot_data)
                self.filename = sys.path[0] + '\\data\\lattice_0.lmp'
                create_eam([self.element_0])
                self.filename_potential = sys.path[0] + '\\data\\' + self.element_0 + '.eam.alloy'
                self.lineEdit_4.setText(self.element_0)
                self.lineEdit_9.setText(str(self.Tot_data_initial.atom_num))
                self.lineEdit_8.setText(self.lineEdit.text())
                self.lineEdit_7.setText(str(self.Tot_data_initial.Masses[0]))
                self.plot_atom_initial()
            else:
                self.ax_atom.cla()
                self.ax_atom.patch.set_alpha(0)
        if self.radioButton_2.isChecked() == True:
            if self.radioButton_2.isChecked() == True and self.element_1 != '请选择' and self.element_2 != '请选择':
                LATTICE = Lattice(element=self.element_1)
                LATTICE.write_lmp_file('lattice_0.lmp', x=self.x1, y=self.y1, z=self.z1)
                LATTICE = Lattice(element=self.element_2)
                LATTICE.write_lmp_file('lattice_1.lmp', x=self.x2, y=self.y2, z=self.z2)
                self.x = mixture(sys.path[0] + '\\data\\lattice_0.lmp', sys.path[0] + '\\data\\lattice_1.lmp')
                self.Tot_data = ReadLmpData(sys.path[0] + '\\data\\file.data')
                self.Tot_data.run_read()
                self.Tot_data_initial = copy.deepcopy(self.Tot_data)
                self.filename = sys.path[0] + '\\data\\' + 'file.data'
                create_eam([self.element_1, self.element_2])
                self.filename_potential = sys.path[0] + '\\data\\' + self.element_1 + self.element_2 + '.eam.alloy'
                self.lineEdit_4.setText(self.element_1)
                self.lineEdit_3.setText(self.element_2)
                self.lineEdit_9.setText(str(self.Tot_data_initial.atom_num))
                self.lineEdit_8.setText(self.lineEdit.text())
                self.lineEdit_7.setText(str(self.Tot_data_initial.Masses[0]))
                self.lineEdit_6.setText(str(self.Tot_data_initial.Masses[1]))
                self.plot_atom_initial()
            else:
                self.ax_atom.cla()
                self.ax_atom.patch.set_alpha(0)
        
    def atom_background(self):
        fig = plt.figure()
        fig.patch.set_facecolor('#343a40')
        plt.ion()
        self.ax_atom = fig.add_subplot(1, 1, 1, projection='3d')
        canvas = FigureCanvas(fig)
        self.ax_atom.w_xaxis.set_pane_color('#343a40')
        self.ax_atom.w_yaxis.set_pane_color('#343a40')
        self.ax_atom.w_zaxis.set_pane_color('#343a40')
        self.ax_atom.set_title('crystal structure')
        self.ax_atom.patch.set_alpha(0)
        self.verticalLayout_52.addWidget(canvas)
        plt.close()       
    
    def plot_atom_initial(self):
        self.ax_atom.cla()
        self.ax_atom.set_title('crystal structure')
        self.ax_atom.patch.set_facecolor('#4c4c4c')
        if self.radioButton.isChecked() == True:
            position = self.Tot_data_initial.main_data[['x', 'y', 'z']]
            position = position.to_numpy(dtype=float)
            x = position[:, 0]
            y = position[:, 1]
            z = position[:, 2]
            self.ax_atom.scatter(x, y, z,alpha=1, c='#00868B', ec='black', lw=0.2, zorder=2, s=100)
            self.ax_atom.scatter(x-0.02, y+0.015, z+0.02, s=10, c='#b2b9b6',alpha = 0.6, zorder=2)
            self.ax_atom.patch.set_alpha(0)
        if self.radioButton_2.isChecked() == True:
            num = np.flatnonzero(self.Tot_data_initial.main_data['type'] == '2')[0]
            position_0 = self.Tot_data_initial.main_data.iloc[0:num][['x', 'y', 'z']]
            position_1 = self.Tot_data_initial.main_data.iloc[num:][['x', 'y', 'z']]
            position_0 = position_0.to_numpy(dtype=float)
            position_1 = position_1.to_numpy(dtype=float)
            x0 = position_0[:, 0]
            y0 = position_0[:, 1]
            z0 = position_0[:, 2]
            x1 = position_1[:, 0]
            y1 = position_1[:, 1]
            z1 = position_1[:, 2]
            self.ax_atom.scatter(x0, y0, z0,alpha=1, c='#00868B', ec='black', lw=0.2, zorder=2, s=100)
            self.ax_atom.scatter(x0-0.02, y0+0.015, z0+0.02, s=10, c='#b2b9b6',alpha = 0.6, zorder=2)
            self.ax_atom.scatter(x1, y1, z1,alpha=1, c='#5f6260', ec='black', lw=0.2, zorder=2, s=100)
            self.ax_atom.scatter(x1-0.02, y1+0.015, z1+0.02, s=10, c='#b2b9b6',alpha = 0.6, zorder=2)
            self.ax_atom.patch.set_alpha(0)
        self.ax_atom.set_box_aspect([1, 1, 1])
        self.ax_atom.view_init(elev=30, azim=30)
        self.ax_atom.set_xlabel('X/A')
        self.ax_atom.set_ylabel('Y/A')
        self.ax_atom.set_zlabel('Z/A')
        self.ax_atom.autoscale_view()
        if self.element_1 == '':
            position = self.Tot_data_initial.main_data[['x', 'y', 'z']]
            position = position.to_numpy(dtype=float)
            x = position[:, 0]
            y = position[:, 1]
            z = position[:, 2]

    def plot_atom_final(self):
        self.ax_atom.cla()
        self.ax_atom.set_title('crystal structure')
        self.ax_atom.patch.set_facecolor('#4c4c4c')
        if self.radioButton.isChecked() == True:
            position = self.Tot_data_final.main_data[['x', 'y', 'z']]
            position = position.to_numpy(dtype=float)
            x = position[:, 0]
            y = position[:, 1]
            z = position[:, 2]
            self.ax_atom.scatter(x, y, z,alpha=1, c='#00868B', ec='black', lw=0.2, zorder=2, s=100)
            self.ax_atom.scatter(x-0.02, y+0.015, z+0.02, s=10, c='#b2b9b6',alpha = 0.6, zorder=2)
            self.ax_atom.patch.set_alpha(0)
        if self.radioButton_2.isChecked() == True:
            num = np.flatnonzero(self.Tot_data_final.main_data['type'] == '2')[0]
            position_0 = self.Tot_data_final.main_data.iloc[0:num][['x', 'y', 'z']]
            position_1 = self.Tot_data_final.main_data.iloc[num:][['x', 'y', 'z']]
            position_0 = position_0.to_numpy(dtype=float)
            position_1 = position_1.to_numpy(dtype=float)
            x0 = position_0[:, 0]
            y0 = position_0[:, 1]
            z0 = position_0[:, 2]
            x1 = position_1[:, 0]
            y1 = position_1[:, 1]
            z1 = position_1[:, 2]
            self.ax_atom.scatter(x0, y0, z0,alpha=1, c='#00868B', ec='black', lw=0.2, zorder=2, s=100)
            self.ax_atom.scatter(x0-0.02, y0+0.015, z0+0.02, s=10, c='#b2b9b6',alpha = 0.6, zorder=2)
            self.ax_atom.scatter(x1, y1, z1,alpha=1, c='#5f6260', ec='black', lw=0.2, zorder=2, s=100)
            self.ax_atom.scatter(x1-0.02, y1+0.015, z1+0.02, s=10, c='#b2b9b6',alpha = 0.6, zorder=2)
            self.ax_atom.patch.set_alpha(0)
        defect = defect_indentify(self.Tot_data_initial, self.Tot_data_final)
        inter_position = defect.interstitials_position
        vacc_position = defect.vacancies_position
        inter_x = []
        inter_y = []
        inter_z = []
        vacan_x = []
        vacan_y = []
        vacan_z = []
        for i in range(len(inter_position)):
            inter_x.append(inter_position[i][0])
            inter_y.append(inter_position[i][1])
            inter_z.append(inter_position[i][2])
            vacan_x.append(vacc_position[i][0])
            vacan_y.append(vacc_position[i][1])
            vacan_z.append(vacc_position[i][2])
        if self.checkBox.isChecked() == True:
            self.ax_atom.cla()
            self.ax_atom.scatter(inter_x, inter_y, inter_z, c='r')
            self.ax_atom.scatter(vacan_x, vacan_y, vacan_z, c='w')
            self.ax_atom.patch.set_alpha(0)
        if self.checkBox.isChecked() == False:
            self.ax_atom.cla()
            if self.radioButton.isChecked() == True:
                self.ax_atom.scatter(x, y, z,alpha=1, c='#00868B', ec='black', lw=0.2, zorder=2, s=100)
                self.ax_atom.scatter(x-0.02, y+0.015, z+0.02, s=10, c='#b2b9b6',alpha = 0.6, zorder=2)
                self.ax_atom.patch.set_alpha(0)
            if self.radioButton_2.isChecked() == True:
                self.ax_atom.scatter(x0, y0, z0,alpha=1, c='#00868B', ec='black', lw=0.2, zorder=2, s=100)
                self.ax_atom.scatter(x0-0.02, y0+0.015, z0+0.02, s=10, c='#b2b9b6',alpha = 0.6, zorder=2)
                self.ax_atom.scatter(x1, y1, z1,alpha=1, c='#5f6260', ec='black', lw=0.2, zorder=2, s=100)
                self.ax_atom.scatter(x1-0.02, y1+0.015, z1+0.02, s=10, c='#b2b9b6',alpha = 0.6, zorder=2)
                self.ax_atom.patch.set_alpha(0)
            
        self.ax_atom.set_box_aspect([1, 1, 1])
        self.ax_atom.view_init(elev=30, azim=30)
        self.ax_atom.set_xlabel('X/A')
        self.ax_atom.set_ylabel('Y/A')
        self.ax_atom.set_zlabel('Z/A')
        self.ax_atom.autoscale_view()

    def read_GUI(self):
        self.temperature0 = float(self.lineEdit.text())
        self.ensemble_name = self.comboBox_3.currentText()
        self.ensemble_name_1 = self.comboBox_7.currentText()
        self.timestep_0 = float(self.lineEdit_2.text()) * 10 ** -15
        self.timestep_1 = float(self.lineEdit_5.text()) * 10 ** -15
        self.iterate_0 = int(self.spinBox_4.text())
        self.iterate_1 = int(self.spinBox_11.text())
        self.defect_num = int(self.spinBox_5.text())
        self.heat = int(self.spinBox_12.text())

    def initial_velocity(self):
        System_create = System(self.Tot_data, self.temperature0)
        self.velocity = System_create.initialize()
    
    def compute_force(self):
        EAM = eam_force(self.filename_potential, self.Tot_data)
        EAM.read_eam()
        EAM.compute_eam()
        self.force = EAM.force
        self.pe = EAM.pe

    def main_compute(self):
        self.checkBox.setEnabled(True)
        self.pushButton.setEnabled(False)
        self.read_GUI()
        self.initial_velocity()
        self.compute_force()

        EAM = eam_force(self.filename_potential, self.Tot_data)
        EAM.read_eam()
        EAM.compute_eam()

        # self.T_chunk, self.Temperature, self.dT_dx, self.heat, self.x_chunk = NEMD(self.Tot_data, self.velocity, EAM, self.timestep_1, self.temperature0, self.heat, self.iterate_1, self.x)
        self.t = Work(self.filename, self.filename_potential, self.temperature0, 
                 self.iterate_0, self.ensemble_name, self.timestep_0, self.Tot_data, 
                 self.velocity, self.force, self.heat, self.iterate_1, self.timestep_1, self.Tot_data_initial, self.x)
        self.t.start()
        self.t.signal.connect(self.draw_relaxation)
    
    def draw_relaxation(self):
        self.pdos = self.t.pdos
        self.omega = self.t.omega
        self.T_chunk = self.t.T_chunk
        self.x_chunk = self.t.x_chunk
        self.t_conductivity = self.t.t_conductivity
        self.lineEdit_10.setText(str(self.t_conductivity))
        self.Tot_data_final = copy.deepcopy(self.t.Tot_data)
        self.T_axis = self.t.T_axis
        self.Pe_axis = self.t.Pe_axis
        self.Time_axis = self.t.Time_axis
        self.plot_atom_final()
        self.pushButton.setEnabled(True)
        self.time_begin()

    def time_begin(self):
        self.i_T = 0
        self.Time_T_axis_plot = []
        self.T_axis_plot = []
        self.timer_T_time = QTimer(self)

        self.i_X = 0
        self.X_axis_plot = []
        self.T_axis_plot_2 = []
        self.timer_T_X_time = QTimer(self)

        self.i_pdos = 0
        self.omega_axis_plot = []
        self.pdos_axis_plot = []
        self.timer_pdos_omega = QTimer(self)

        self.timer_T_time.timeout.connect(self.plot_T_time)
        self.timer_T_time.setInterval(50)
        self.timer_T_time.start()

        self.timer_T_X_time.timeout.connect(self.plot_T_X)
        self.timer_T_X_time.setInterval(50)
        self.timer_T_X_time.start()

        self.plot_pdos_omega()
        # self.timer_pdos_omega.timeout.connect(self.plot_pdos_omega)
        # self.timer_pdos_omega.setInterval(1)
        # self.timer_pdos_omega.start()

    def plot_T_time(self):
        plt.ion()
        self.ax_T_time.clear()
        self.Time_T_axis_plot.append(self.Time_axis[self.i_T])
        self.T_axis_plot.append(self.T_axis[self.i_T])
        self.ax_T_time.plot(self.Time_T_axis_plot, self.T_axis_plot)
        self.i_T = self.i_T + 1
        if len(self.Time_T_axis_plot) == len(self.Time_axis):
            self.timer_T_time.stop()

    def plot_T_X(self):
        plt.ion()
        self.ax_T_X.clear()
        self.X_axis_plot.append(self.x_chunk[self.i_X])
        self.T_axis_plot_2.append(self.T_chunk[self.i_X])
        self.ax_T_X.plot(self.X_axis_plot, self.T_axis_plot_2)
        self.i_X = self.i_X + 1
        if len(self.X_axis_plot) == len(self.x_chunk):
            self.timer_T_X_time.stop()

    def plot_pdos_omega(self):
        plt.ion()
        self.ax_pdos_omega.clear()
        self.ax_pdos_omega.plot(self.omega, self.pdos)
        # self.omega_axis_plot.append(self.omega[self.i_pdos])
        # self.pdos_axis_plot.append(self.pdos[self.i_pdos])
        # self.ax_pdos_omega.plot(self.omega_axis_plot, self.pdos_axis_plot)
        # self.i_pdos = self.i_pdos + 1
        # if len(self.pdos_axis_plot) == len(self.pdos):
        #     self.timer_pdos_omega.stop()
        #     self.radioButton_2.setCheckable(True)

    def T_time_background(self):
        fig = plt.figure()
        fig.patch.set_facecolor('#343a40')
        cav_T_time = FigureCanvas(fig)  # 创建matplotlib画布
        self.ax_T_time = fig.subplots()
        self.ax_T_time.spines['right'].set_visible(False)
        self.ax_T_time.spines['top'].set_visible(False)
        self.ax_T_time.set_xlabel('time', x=1.08, labelpad=-20)
        self.ax_T_time.set_ylabel('T', y=1.08, rotation=0, labelpad=-20)
        self.ax_T_time.set_facecolor('#343a40')
        self.ax_T_time.grid(alpha=0.1)
        plt.text(0.99, -0.025, '>', fontdict={'size': 12})
        plt.text(-0.02, 0.98, '>', fontdict={'size': 12, 'rotation' : 90})
        self.i_T = 0
        self.verticalLayout_30.addWidget(cav_T_time)
        plt.close()

    def T_X_background(self):
        fig = plt.figure()
        fig.patch.set_facecolor('#343a40')
        cav_T_time = FigureCanvas(fig)  # 创建matplotlib画布
        self.ax_T_X = fig.subplots()
        self.ax_T_X.spines['right'].set_visible(False)
        self.ax_T_X.spines['top'].set_visible(False)
        self.ax_T_X.set_facecolor('#343a40')
        self.ax_T_X.grid(alpha=0.1)
        plt.text(0.99, -0.025, '>', fontdict={'size': 12})
        plt.text(-0.02, 0.98, '>', fontdict={'size': 12, 'rotation' : 90})
        self.i_X = 0
        self.verticalLayout_22.addWidget(cav_T_time)
        plt.close()

    def pdos_omega_background(self):
        fig = plt.figure()
        fig.patch.set_facecolor('#343a40')
        cav_T_time = FigureCanvas(fig)  # 创建matplotlib画布
        self.ax_pdos_omega = fig.subplots()
        self.ax_pdos_omega.spines['right'].set_visible(False)
        self.ax_pdos_omega.spines['top'].set_visible(False)
        self.ax_pdos_omega.set_facecolor('#343a40')
        self.ax_pdos_omega.grid(alpha=0.1)
        plt.text(0.99, -0.025, '>', fontdict={'size': 12})
        plt.text(-0.02, 0.98, '>', fontdict={'size': 12, 'rotation' : 90})
        self.i_pdos = 0
        self.verticalLayout_31.addWidget(cav_T_time)
        plt.close()


class Work(QThread):
    signal = pyqtSignal(object)
    
    def __init__(self, filename, filename_potential, temperature0, iterate, ensemble_name, timestep,
                 Tot_data, velocity, force, heat, iterate_1, timestep_1, Tot_data_initial, x):
        super(Work, self).__init__()
        self.filename_detailed = filename
        self.filename_potential = filename_potential
        self.temperature0 = temperature0
        self.iterate = iterate
        self.ensemble_name = ensemble_name
        self.timestep = timestep
        self.Tot_data = Tot_data
        self.velocity = velocity
        self.force = force
        self.heat = heat
        self.iterate_1 = iterate_1
        self.timestep_1 = timestep_1
        self.Tot_data_initial = Tot_data_initial
        self.x = x
    
    def run(self):
        self.T_axis = []
        self.Pe_axis = []
        self.Time_axis = []
        for i in range(self.iterate):
            if i == 0:
                self.Temperature = self.temperature0
            EAM = eam_force(self.filename_potential, self.Tot_data)
            EAM.read_eam()
            EAM.compute_eam()
            [self.Temperature, self.Tot_data, self.velocity, EAM] = integrate(self.Tot_data, EAM, self.velocity, self.ensemble_name, self.Temperature, self.temperature0, 1, self.timestep)
            self.T_axis.append(self.Temperature)
            self.Pe_axis.append(EAM.pe)
            self.Time_axis.append(i * self.timestep)
        self.T_chunk, self.Temperature, self.dT_dx, self.heat, self.x_chunk = NEMD(self.Tot_data, self.velocity, EAM, self.timestep_1, self.temperature0, self.heat, self.iterate_1, self.x)
        self.t_conductivity = compute_result(self.Tot_data_initial, self.dT_dx, self.heat)
        self.Thermal_conductivity = [self.T_chunk, self.x_chunk, self.t_conductivity]
        self.omega = np.arange(1, 380.5, 0.5)
        [self.vacf_output, self.pdos] = find_pdos(self.velocity, 100, omega=self.omega)
        self.signal.emit([self.Tot_data, self.T_axis, self.Pe_axis, self.Time_axis, self.Thermal_conductivity])


app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
sys.exit(app.exec())