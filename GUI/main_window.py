import sys
sys.path.append("../..")

from PySide6.QtWidgets import QApplication, QWidget
from GUI.gui_ui import Ui_Form
from ovito.modifiers import ExpressionSelectionModifier, WignerSeitzAnalysisModifier
from ovito.vis import Viewport
import os
os.environ['OVITO_GUI_MODE'] = '1'
from pipeline.pipeline import *
from pipeline.lattice_set import lattice_set

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
    def setting(self):
        atom_all = ["Cu", "Ag", "Au", "Ni", "Pd", "Pt", "Al", "Pb", "Fe", "Mo", "Ta", "W"]
        self.rel_sys_comboBox.addItem('nvt')
        self.rel_sys_comboBox.addItem('nve')
        self.Them_sys_comboBox.addItem('nvt')
        self.Them_sys_comboBox.addItem('nve')
        self.exp1_ele1_comboBox.addItems(atom_all)
        self.exp2_ele1_comboBox.addItems(atom_all)
        self.exp2_ele2_comboBox.addItems(atom_all)
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
        self.rel_tim_lineEdiT.setText('10')
        self.Them_lineEdit.setText('5')
        self.Them_sys_comboBox.setCurrentIndex(0)
        self.Them_tim_lineEdit.setText('10')

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
        self.rel_tim_lineEdiT.setText('10')
        self.Them_lineEdit.setText('5')
        self.Them_sys_comboBox.setCurrentIndex(0)
        self.Them_tim_lineEdit.setText('10')

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

    def start_main(self):
        # 读取GUI数据
        element1 = self.exp1_ele1_comboBox.currentText()
        element2 = self.exp2_ele1_comboBox.currentText()
        element3 = self.exp2_ele2_comboBox.currentText()
        size1 = [self.exp1_ele1x_spinBox.value(), self.exp1_ele1y_spinBox.value(), self.exp1_ele1z_spinBox.value()]
        size2 = [self.exp2_ele1x_spinBox.value(), self.exp2_ele1y_spinBox.value(), self.exp2_ele1z_spinBox.value()]
        size3 = [self.exp2_ele2x_spinBox.value(), self.exp2_ele2y_spinBox.value(), self.exp2_ele2z_spinBox.value()]
        # 建立晶体数据文件
        lattice_set(element1, element2, element3, size1, size2, size3)
        set_file('data\lattice.lmp', )
