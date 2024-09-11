# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChildWindow_1.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(986, 365)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 101, 21))
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 70, 80, 20))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 140, 80, 20))
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 210, 80, 20))
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 280, 80, 20))
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(350, 70, 80, 20))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(350, 140, 80, 20))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(350, 210, 80, 20))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(350, 280, 80, 20))
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(700, 70, 80, 20))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(700, 140, 80, 20))
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(700, 210, 80, 20))
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(679, 275, 101, 40))
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.exp1_ele1_comboBox = QComboBox(Form)
        self.exp1_ele1_comboBox.setObjectName(u"exp1_ele1_comboBox")
        self.exp1_ele1_comboBox.setGeometry(QRect(90, 65, 135, 30))
        font1 = QFont()
        font1.setFamilies([u"\u5b8b\u4f53"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.exp1_ele1_comboBox.setFont(font1)
        self.exp1_ele1_comboBox.setCursor(QCursor(Qt.OpenHandCursor))
        self.exp1_ele1_comboBox.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid white;\n"
"	border-top-right-radius: 2px;\n"
"	border-bottom-right-radius: 2px;\n"
"    border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"    padding: 2px 3px 2px 3px;\n"
"    min-width: 3em;\n"
"	background-color: #f8f9fa;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"")
        self.exp1_ele1x_lineEdit = QLineEdit(Form)
        self.exp1_ele1x_lineEdit.setObjectName(u"exp1_ele1x_lineEdit")
        self.exp1_ele1x_lineEdit.setGeometry(QRect(90, 135, 135, 30))
        self.exp1_ele1x_lineEdit.setFont(font1)
        self.exp1_ele1x_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.exp1_ele1y_lineEdit = QLineEdit(Form)
        self.exp1_ele1y_lineEdit.setObjectName(u"exp1_ele1y_lineEdit")
        self.exp1_ele1y_lineEdit.setGeometry(QRect(90, 205, 135, 30))
        self.exp1_ele1y_lineEdit.setFont(font1)
        self.exp1_ele1y_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.exp1_ele1z_lineEdit = QLineEdit(Form)
        self.exp1_ele1z_lineEdit.setObjectName(u"exp1_ele1z_lineEdit")
        self.exp1_ele1z_lineEdit.setGeometry(QRect(90, 275, 135, 30))
        self.exp1_ele1z_lineEdit.setFont(font1)
        self.exp1_ele1z_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.rel_tem_lineEdit = QLineEdit(Form)
        self.rel_tem_lineEdit.setObjectName(u"rel_tem_lineEdit")
        self.rel_tem_lineEdit.setGeometry(QRect(440, 65, 135, 30))
        self.rel_tem_lineEdit.setFont(font1)
        self.rel_tem_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.rel_tem_lineEdit_2 = QLineEdit(Form)
        self.rel_tem_lineEdit_2.setObjectName(u"rel_tem_lineEdit_2")
        self.rel_tem_lineEdit_2.setGeometry(QRect(440, 135, 135, 30))
        self.rel_tem_lineEdit_2.setFont(font1)
        self.rel_tem_lineEdit_2.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.rel_tim_lineEdiT = QLineEdit(Form)
        self.rel_tim_lineEdiT.setObjectName(u"rel_tim_lineEdiT")
        self.rel_tim_lineEdiT.setGeometry(QRect(440, 275, 135, 30))
        self.rel_tim_lineEdiT.setFont(font1)
        self.rel_tim_lineEdiT.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Them_lineEdit = QLineEdit(Form)
        self.Them_lineEdit.setObjectName(u"Them_lineEdit")
        self.Them_lineEdit.setGeometry(QRect(790, 65, 135, 30))
        self.Them_lineEdit.setFont(font1)
        self.Them_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.defect_lineEdit = QLineEdit(Form)
        self.defect_lineEdit.setObjectName(u"defect_lineEdit")
        self.defect_lineEdit.setGeometry(QRect(790, 275, 135, 30))
        self.defect_lineEdit.setFont(font1)
        self.defect_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Them_tim_lineEdit = QLineEdit(Form)
        self.Them_tim_lineEdit.setObjectName(u"Them_tim_lineEdit")
        self.Them_tim_lineEdit.setGeometry(QRect(790, 205, 135, 30))
        self.Them_tim_lineEdit.setFont(font1)
        self.Them_tim_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Them_sys_lineEdit = QLineEdit(Form)
        self.Them_sys_lineEdit.setObjectName(u"Them_sys_lineEdit")
        self.Them_sys_lineEdit.setGeometry(QRect(790, 135, 135, 30))
        self.Them_sys_lineEdit.setFont(font1)
        self.Them_sys_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.finish = QPushButton(Form)
        self.finish.setObjectName(u"finish")
        self.finish.setGeometry(QRect(830, 320, 95, 30))
        self.finish.setFont(font)
        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(490, 70, 80, 20))
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(490, 140, 80, 20))
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(490, 280, 80, 20))
        self.label_16.setFont(font)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(840, 70, 80, 20))
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_18 = QLabel(Form)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(840, 210, 80, 20))
        self.label_18.setFont(font)
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.exp1_arg_pushButton = QPushButton(Form)
        self.exp1_arg_pushButton.setObjectName(u"exp1_arg_pushButton")
        self.exp1_arg_pushButton.setGeometry(QRect(100, 10, 95, 30))
        self.exp1_arg_pushButton.setFont(font)
        self.rel_sys_comboBox = QComboBox(Form)
        self.rel_sys_comboBox.setObjectName(u"rel_sys_comboBox")
        self.rel_sys_comboBox.setGeometry(QRect(440, 205, 135, 30))
        self.rel_sys_comboBox.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5b9e\u9a8c\u4e00", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5143\u7d20", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Y", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Z", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u521d\u59cb\u6e29\u5ea6", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u6e29\u5ea6", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u7cfb\u7efc", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u5f1b\u8c6b\u65f6\u95f4", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u70ed\u6d41", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u7cfb\u7efc", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u6a21\u62df\u65f6\u95f4", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u5f17\u5170\u514b\u5c14\n"
"\u7f3a\u9677\u5bf9\u6570\u91cf", None))
        self.finish.setText(QCoreApplication.translate("Form", u"\u5b8c\u6210", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"K", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"K", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"ps", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"eV/ps", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"ps", None))
        self.exp1_arg_pushButton.setText(QCoreApplication.translate("Form", u"\u63a8\u8350\u53c2\u6570", None))
    # retranslateUi

