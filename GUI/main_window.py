import sys
sys.path.append("../..")
from PySide6.QtWidgets import QApplication, QWidget
from GUI.gui_ui import Ui_Form
from ovito.modifiers import ExpressionSelectionModifier, WignerSeitzAnalysisModifier
from ovito.vis import Viewport
import os
import numpy as np
import copy
os.environ['OVITO_GUI_MODE'] = '1'
from output import lattice_set, render_3d, Work, read_datafile

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
        self.gap_checkBox_2.clicked.connect(lambda:self.set_occupancy())
        self.zon_tem_checkBox_2.clicked.connect(lambda: self.set_tempareture_display())

    def setting(self):
        self.atom_all = ["Cu", "Ag", "Au", "Ni", "Pd", "Pt", "Al", "Pb", "Fe", "Mo", "Ta", "W"]
        self.atomic_mass = ['63.546', '107.87', '196.97', '58.693', '106.42', '195.08', 
                            '26.982', '207.2', '55.845','95.95', '180.95', '183.84']
        self.rel_sys_comboBox.addItem('nvt')
        self.rel_sys_comboBox.addItem('nve')
        self.Them_sys_comboBox.addItem('nvt')
        self.Them_sys_comboBox.addItem('nve')
        self.exp2_ele1x_lineEdit.setText('0')
        self.exp2_ele1y_lineEdit.setText('0')
        self.exp2_ele1z_lineEdit.setText('0')
        self.exp2_ele2x_lineEdit.setText('0')
        self.exp2_ele2y_lineEdit.setText('0')
        self.exp2_ele2z_lineEdit.setText('0')
        self.exp1_ele1x_lineEdit.setText('0')
        self.exp1_ele1y_lineEdit.setText('0')
        self.exp1_ele1z_lineEdit.setText('0')
        self.defect_lineEdit.setText('0')
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
        self.exp1_ele1x_lineEdit.setText('20')
        self.exp1_ele1y_lineEdit.setText('5')
        self.exp1_ele1z_lineEdit.setText('5')
        self.defect_lineEdit.setText('0')
        self.rel_tem_lineEdit.setText('300')
        self.rel_sys_comboBox.setCurrentIndex(0)
        self.rel_tim_lineEdiT.setText('1')
        self.Them_lineEdit.setText('5')
        self.Them_sys_comboBox.setCurrentIndex(0)
        self.Them_tim_lineEdit.setText('1')

    def recommend_experiment_2(self):
        self.exp2_ele1_comboBox.setCurrentIndex(0)
        self.exp2_ele2_comboBox.setCurrentIndex(1)
        self.exp2_ele1x_lineEdit.setText('10')
        self.exp2_ele1y_lineEdit.setText('6')
        self.exp2_ele1z_lineEdit.setText('6')
        self.exp2_ele2x_lineEdit.setText('10')
        self.exp2_ele2y_lineEdit.setText('5')
        self.exp2_ele2z_lineEdit.setText('5')
        self.defect_lineEdit.setText('0')
        self.rel_tem_lineEdit.setText('300')
        self.rel_sys_comboBox.setCurrentIndex(0)
        self.rel_tim_lineEdiT.setText('1')
        self.Them_lineEdit.setText('5')
        self.Them_sys_comboBox.setCurrentIndex(0)
        self.Them_tim_lineEdit.setText('1')

    def choose_page_0(self):
        self.exp1_ele1_comboBox.setCurrentIndex(-1)
        self.exp2_ele1_comboBox.setCurrentIndex(-1)
        self.exp2_ele2_comboBox.setCurrentIndex(-1)
        self.sys_stackedWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(0)
        self.exp2_ele1x_lineEdit.setText('0')
        self.exp2_ele1y_lineEdit.setText('0')
        self.exp2_ele1z_lineEdit.setText('0')
        self.exp2_ele2x_lineEdit.setText('0')
        self.exp2_ele2y_lineEdit.setText('0')
        self.exp2_ele2z_lineEdit.setText('0')
        self.defect_lineEdit.setText('0')
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
        self.exp_res_lineEdit_2.clear()
        self.exp2_reslineEdit_2.clear()
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
        self.exp1_ele1x_lineEdit.setText('0')
        self.exp1_ele1y_lineEdit.setText('0')
        self.exp1_ele1z_lineEdit.setText('0')
        self.defect_lineEdit.setText('0')
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
        self.exp_res_lineEdit_2.clear()
        self.exp2_reslineEdit_2.clear()
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
        defect_num = int(self.defect_lineEdit.text())
        size1 = [int(self.exp1_ele1x_lineEdit.text()), int(self.exp1_ele1y_lineEdit.text()), int(self.exp1_ele1z_lineEdit.text())]
        size2 = [int(self.exp2_ele1x_lineEdit.text()), int(self.exp2_ele1y_lineEdit.text()), int(self.exp2_ele1z_lineEdit.text())]
        size3 = [int(self.exp2_ele2x_lineEdit.text()), int(self.exp2_ele2y_lineEdit.text()), int(self.exp2_ele2z_lineEdit.text())]
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
                        iterate_1, x, defect_num)
        self.t.start()
        self.t.signal_3.connect(self.plot)
        self.t.signal_2.connect(self.plot)
        self.t.signal.connect(self.plot)   
    
    def pause_main(self):
        self.t.pause()

    def resume_main(self):
        self.t.resume()

    def stop_main(self):
        self.t.terminate()
        self.t.wait()

    def plot(self):
        if self.verticalLayout_2.itemAt(0) != None: # 清空T-Time图像，防止暂停时重复绘图
            self.verticalLayout_2.itemAt(0).widget().deleteLater()
        if self.verticalLayout_3.itemAt(0) != None:
            self.verticalLayout_3.itemAt(0).widget().deleteLater()
        if self.verticalLayout_6.itemAt(0) != None:
            self.verticalLayout_6.itemAt(0).widget().deleteLater()
        if self.verticalLayout_5.itemAt(0) != None:
            self.verticalLayout_5.itemAt(0).widget().deleteLater()

        renew(self.t.Tot_data)
        render_3d.set_file('data\lattice_final.lmp')
        if self.gap_checkBox_2.isChecked():
            self.set_occupancy()
        if self.zon_tem_checkBox_2.isChecked():
            self.set_tempareture_display()
        if self.t.temp != 2:    # 保证暂停时不输出热导率
            self.exp_res_lineEdit_2.setText(str(round(self.t.t_conductivity, 3)))
            self.exp2_reslineEdit_2.setText(str(round(self.t.t_conductivity, 3)))
        if len(self.t.Time_axis) != 1:
            cav = plot_2d(np.array(self.t.Time_axis) * 1e15, self.t.T_axis, 'Time/fs', 'Temperature/K', 'Temperature', '体系温度曲线_单元素')
            self.verticalLayout_2.addWidget(cav)
            cav = plot_2d(np.array(self.t.Time_axis) * 1e15, self.t.T_axis, 'Time/fs', 'Temperature/K', 'Temperature', '体系温度曲线_多元素')
            self.verticalLayout_6.addWidget(cav)
        if len(self.t.x_chunk) != 0:     # 保证暂停时不绘图
            cav = plot_2d(np.array(self.t.x_chunk) * 1e9, self.t.T_chunk, 'X/nm', 'Temperature/K', 'Temperature', '体系区域温度_单元素')
            self.verticalLayout_3.addWidget(cav)
            cav = plot_2d(np.array(self.t.x_chunk) * 1e9, self.t.T_chunk, 'X/nm', 'Temperature/K', 'Temperature', '体系区域温度_多元素')
            self.verticalLayout_5.addWidget(cav)
        if len(self.t.omega) != 0:      # 保证暂停时不绘图
            cav = plot_2d(self.t.omega, self.t.pdos, 'Omega', 'Pdos', 'Pdos', '声子态密度曲线_多元素')
            self.verticalLayout_4.addWidget(cav)
        
    def set_occupancy(self):
        self.zon_tem_checkBox_2.setChecked(False)
        if self.painting_zoom.itemAt(1) != None:
            self.painting_zoom.itemAt(1).widget().deleteLater() # 删除温度条
        if (not self.gap_checkBox_2.isChecked()):
            render_3d.clear_modifiers()
        else:
            render_3d.set_occupancy()
            

    def set_tempareture_display(self):
        from output.tempareture_color_bar import create_tem_color_bar
        self.gap_checkBox_2.setChecked(False)
        if self.zon_tem_checkBox_2.isChecked() == False:
            render_3d.clear_modifiers()
            if self.painting_zoom.itemAt(1) != None:
                self.painting_zoom.itemAt(1).widget().deleteLater()
        else:
            render_3d.set_color_by_tempareture(self.t.T_chunk)
            self.painting_zoom.addWidget(create_tem_color_bar(self.t.T_chunk), 1)
            

        