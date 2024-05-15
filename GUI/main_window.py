import sys
sys.path.append("../..")

from PySide6.QtWidgets import QApplication, QWidget
from GUI.gui_ui import Ui_Form
from ovito.modifiers import ExpressionSelectionModifier, WignerSeitzAnalysisModifier
from ovito.vis import Viewport
import os
import copy
os.environ['OVITO_GUI_MODE'] = '1'
from output.lattice_set import lattice_set
from output.render_3d import render_3d
from output.read_datafile import read_datafile
from output.main_calculation import Work
from output.plot_2d import plot_2d
from output.renew import renew

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setting()
        self.exp1_arg_pushButton.clicked.connect(self.recommend_experiment_1)
        self.exp2_arg_pushButton.clicked.connect(self.recommend_experiment_2)
        self.exp1_radioButton.clicked.connect(self.choose_page_0)
        self.exp2_radioButton.clicked.connect(self.choose_page_1)
        self.start_pushButton.clicked.connect(self.start_main)
        self.pause_pushButton.clicked.connect(self.pause_main)
        self.restart_pushButton.clicked.connect(self.resume_main)
        self.vacan_checkBox_2.clicked.connect(lambda:self.set_occupancy(0))
        self.gap_checkBox_2.clicked.connect(lambda:self.set_occupancy(2))

    def setting(self):
        self.atom_all = ["Cu", "Ag", "Au", "Ni", "Pd", "Pt", "Al", "Pb", "Fe", "Mo", "Ta", "W"]
        self.atomic_mass = ['63.546', '107.87', '196.97', '58.693', '106.42', '195.08', 
                            '26.982', '207.2', '55.845','95.95', '180.95', '183.84']
        self.rel_sys_comboBox.addItem('nvt')
        self.rel_sys_comboBox.addItem('nve')
        self.Them_sys_comboBox.addItem('nvt')
        self.Them_sys_comboBox.addItem('nve')
        self.exp1_ele1_comboBox.addItems(self.atom_all)
        self.exp2_ele1_comboBox.addItems(self.atom_all)
        self.exp2_ele2_comboBox.addItems(self.atom_all)
        self.exp1_ele1_comboBox.setCurrentIndex(-1)
        self.exp2_ele1_comboBox.setCurrentIndex(-1)
        self.exp2_ele2_comboBox.setCurrentIndex(-1)
        self.exp1_radioButton.setChecked(True)  # 选择实验一
        self.sys_stackedWidget.setCurrentIndex(0)
        self.exp2_arg_pushButton.setEnabled(False)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(0)

    def recommend_experiment_1(self):
        self.exp1_ele1_comboBox.setCurrentIndex(0)
        self.exp2_ele2_comboBox.setCurrentIndex(-1)
        self.exp1_ele1x_spinBox.setValue(5)
        self.exp1_ele1y_spinBox.setValue(5)
        self.exp1_ele1z_spinBox.setValue(5)
        self.rel_tem_lineEdit.setText('300')
        self.rel_sys_comboBox.setCurrentIndex(0)
        self.rel_tim_lineEdiT.setText('0.01')
        self.Them_lineEdit.setText('5')
        self.Them_sys_comboBox.setCurrentIndex(0)
        self.Them_tim_lineEdit.setText('0.01')

    def recommend_experiment_2(self):
        self.exp2_ele1_comboBox.setCurrentIndex(0)
        self.exp2_ele2_comboBox.setCurrentIndex(1)
        self.exp2_ele1x_spinBox.setValue(5)
        self.exp2_ele1y_spinBox.setValue(5)
        self.exp2_ele1z_spinBox.setValue(5)
        self.exp2_ele2x_spinBox.setValue(5)
        self.exp2_ele2y_spinBox.setValue(5)
        self.exp2_ele2z_spinBox.setValue(5)
        self.rel_tem_lineEdit.setText('300')
        self.rel_sys_comboBox.setCurrentIndex(0)
        self.rel_tim_lineEdiT.setText('0.01')
        self.Them_lineEdit.setText('5')
        self.Them_sys_comboBox.setCurrentIndex(0)
        self.Them_tim_lineEdit.setText('0.01')

    def choose_page_0(self):
        self.exp1_ele1_comboBox.setCurrentIndex(-1)
        self.exp2_ele1_comboBox.setCurrentIndex(-1)
        self.exp2_ele2_comboBox.setCurrentIndex(-1)
        self.sys_stackedWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(0)
        self.exp2_ele1x_spinBox.setValue(0)
        self.exp2_ele1y_spinBox.setValue(0)
        self.exp2_ele1z_spinBox.setValue(0)
        self.exp2_ele2x_spinBox.setValue(0)
        self.exp2_ele2y_spinBox.setValue(0)
        self.exp2_ele2z_spinBox.setValue(0)
        self.rel_tem_lineEdit.clear()
        self.rel_sys_comboBox.setCurrentIndex(0)
        self.rel_tim_lineEdiT.clear()
        self.Them_lineEdit.clear()
        self.Them_sys_comboBox.setCurrentIndex(0)
        self.Them_tim_lineEdit.clear()
        self.exp1_arg_pushButton.setEnabled(True)
        self.exp2_arg_pushButton.setEnabled(False)
        self.exp2_ele1_lineEdit_2.clear()
        self.exp2_ele2_lineEdit_2.clear()
        self.exp1_ele1_lineEdit_2.clear()
        self.exp2_ele1_mass_lineEdit_2.clear()
        self.exp2_ele2_mass_lineEdit_2.clear()
        self.exp1_ele1_mass_lineEdit_2.clear()
        self.exp2_ele1_num_lineEdit_2.clear()
        self.exp2_ele2_num_lineEdit_2.clear()
        self.exp1_ele1_num_lineEdit_2.clear()
        self.exp2_reslineEdit_2.clear()
        self.exp2_reslineEdit_2.clear()    
        if self.verticalLayout_2.itemAt(0) != None:
            self.verticalLayout_2.itemAt(0).widget().deleteLater()
            self.verticalLayout_3.itemAt(0).widget().deleteLater()
            self.verticalLayout_4.itemAt(0).widget().deleteLater()
        if self.verticalLayout_5.itemAt(0) != None:
            self.verticalLayout_5.itemAt(0).widget().deleteLater()
            self.verticalLayout_6.itemAt(0).widget().deleteLater()

    def choose_page_1(self):
        self.exp1_ele1_comboBox.setCurrentIndex(-1)
        self.exp2_ele1_comboBox.setCurrentIndex(-1)
        self.exp2_ele2_comboBox.setCurrentIndex(-1)
        self.sys_stackedWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_4.setCurrentIndex(1)
        self.exp1_ele1x_spinBox.setValue(0)
        self.exp1_ele1y_spinBox.setValue(0)
        self.exp1_ele1z_spinBox.setValue(0)
        self.rel_tem_lineEdit.clear()
        self.rel_sys_comboBox.setCurrentIndex(0)
        self.rel_tim_lineEdiT.clear()
        self.Them_lineEdit.clear()
        self.Them_sys_comboBox.setCurrentIndex(0)
        self.Them_tim_lineEdit.clear()
        self.exp1_arg_pushButton.setEnabled(False)
        self.exp2_arg_pushButton.setEnabled(True)
        self.exp2_ele1_lineEdit_2.clear()
        self.exp2_ele2_lineEdit_2.clear()
        self.exp1_ele1_lineEdit_2.clear()
        self.exp2_ele1_mass_lineEdit_2.clear()
        self.exp2_ele2_mass_lineEdit_2.clear()
        self.exp1_ele1_mass_lineEdit_2.clear()
        self.exp2_ele1_num_lineEdit_2.clear()
        self.exp2_ele2_num_lineEdit_2.clear()
        self.exp1_ele1_num_lineEdit_2.clear()
        self.exp2_reslineEdit_2.clear()
        self.exp2_reslineEdit_2.clear()  
        if self.verticalLayout_2.itemAt(0) != None:
            self.verticalLayout_2.itemAt(0).widget().deleteLater()
            self.verticalLayout_3.itemAt(0).widget().deleteLater()
            self.verticalLayout_4.itemAt(0).widget().deleteLater()
        if self.verticalLayout_5.itemAt(0) != None:
            self.verticalLayout_5.itemAt(0).widget().deleteLater()
            self.verticalLayout_6.itemAt(0).widget().deleteLater()

    def start_main(self):
        # 清除画布
        if self.verticalLayout_2.itemAt(0) != None:
            self.verticalLayout_2.itemAt(0).widget().deleteLater()
            self.verticalLayout_3.itemAt(0).widget().deleteLater()
            self.verticalLayout_4.itemAt(0).widget().deleteLater()
        if self.verticalLayout_5.itemAt(0) != None:
            self.verticalLayout_5.itemAt(0).widget().deleteLater()
            self.verticalLayout_6.itemAt(0).widget().deleteLater()
        # 读取GUI数据
        element1 = self.exp1_ele1_comboBox.currentText()
        element2 = self.exp2_ele1_comboBox.currentText()
        element3 = self.exp2_ele2_comboBox.currentText()
        size1 = [self.exp1_ele1x_spinBox.value(), self.exp1_ele1y_spinBox.value(), self.exp1_ele1z_spinBox.value()]
        size2 = [self.exp2_ele1x_spinBox.value(), self.exp2_ele1y_spinBox.value(), self.exp2_ele1z_spinBox.value()]
        size3 = [self.exp2_ele2x_spinBox.value(), self.exp2_ele2y_spinBox.value(), self.exp2_ele2z_spinBox.value()]
        # 建立晶体数据文件
        x = lattice_set(element1, element2, element3, size1, size2, size3)
        render_3d.set_file('data\lattice.lmp')
        # 体系参数填入
        if element1 == '':
            self.exp2_ele1_lineEdit_2.setText(element2)
            self.exp2_ele2_lineEdit_2.setText(element3)
            self.exp2_ele1_mass_lineEdit_2.setText(self.atomic_mass[self.atom_all.index(element2)])
            self.exp2_ele2_mass_lineEdit_2.setText(self.atomic_mass[self.atom_all.index(element3)])
            atom_num_1 = read_datafile('data\lattice_1.lmp').atom_num
            atom_num_2 = read_datafile('data\lattice_2.lmp').atom_num
            self.exp2_ele1_num_lineEdit_2.setText(str(atom_num_1))
            self.exp2_ele2_num_lineEdit_2.setText(str(atom_num_2))
        if element2 == '' and element3 == '':
            self.exp1_ele1_lineEdit_2.setText(element1)
            self.exp1_ele1_mass_lineEdit_2.setText(self.atomic_mass[self.atom_all.index(element1)])
            atom_num = read_datafile('data\lattice.lmp').atom_num
            self.exp1_ele1_num_lineEdit_2.setText(str(atom_num))
        # 读取计算所需内容
        filepath = 'data\lattice.lmp'
        temperature0 = float(self.rel_tem_lineEdit.text())
        iterate = int(float(self.rel_tim_lineEdiT.text()) / 0.001)
        ensemble_name = self.rel_sys_comboBox.currentText()
        heat = int(self.Them_lineEdit.text())
        iterate_1 = int(float(self.Them_tim_lineEdit.text()) / 0.001)
        ensemble_name_1 = self.Them_sys_comboBox.currentText()
        self.t = Work(element1, element2, element3, filepath, temperature0, 
                        iterate, ensemble_name, ensemble_name_1, heat, 
                        iterate_1, x)
        self.t.start()
        self.t.signal.connect(self.plot)   
    
    def pause_main(self):
        self.t.pause()

    def resume_main(self):
        self.t.resume()

    def stop_main(self):
        self.t.terminate()
        self.t.wait()

    def plot(self):
        renew(self.t.Tot_data)
        render_3d.set_file('data\small 2.data')
        if self.gap_checkBox_2.isChecked():
            render_3d.set_occuppancy(2)
        if self.vacan_checkBox_2.isChecked():
            render_3d.set_occuppancy(0)
        if self.zon_tem_checkBox_2.isChecked():
            ...
        # TODO
        self.exp_res_lineEdit_2.setText(str(round(self.t.t_conductivity, 3)))
        self.exp2_reslineEdit_2.setText(str(round(self.t.t_conductivity, 3)))
        cav = plot_2d(self.t.Time_axis, self.t.T_axis, 'Time', 'Temperature')
        self.verticalLayout_2.addWidget(cav)
        cav = plot_2d(self.t.Time_axis, self.t.T_axis, 'Time', 'Temperature')
        self.verticalLayout_6.addWidget(cav)
        cav = plot_2d(self.t.x_chunk, self.t.T_chunk, 'X', 'Temperature')
        self.verticalLayout_3.addWidget(cav)
        cav = plot_2d(self.t.x_chunk, self.t.T_chunk, 'X', 'Temperature')
        self.verticalLayout_5.addWidget(cav)
        cav = plot_2d(self.t.omega, self.t.pdos, 'Omega', 'Pdos')
        self.verticalLayout_4.addWidget(cav)
        
    def set_occupancy(self, num):
        print(num)
        render_3d.set_occuppancy(0)
        if num == 0:
            self.gap_checkBox_2.setChecked(False)
        else:
            self.vacan_checkBox_2.setChecked(False)
        self.zon_tem_checkBox_2.setChecked(False)

        