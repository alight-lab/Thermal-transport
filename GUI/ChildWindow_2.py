# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChildWindow_2.ui'
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
        self.exp2_ele1z_lineEdit = QLineEdit(Form)
        self.exp2_ele1z_lineEdit.setObjectName(u"exp2_ele1z_lineEdit")
        self.exp2_ele1z_lineEdit.setGeometry(QRect(60, 275, 135, 30))
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(12)
        font.setBold(True)
        self.exp2_ele1z_lineEdit.setFont(font)
        self.exp2_ele1z_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(390, 140, 101, 20))
        font1 = QFont()
        font1.setFamilies([u"\u5b8b\u4f53"])
        font1.setPointSize(12)
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.rel_tim_lineEdiT = QLineEdit(Form)
        self.rel_tim_lineEdiT.setObjectName(u"rel_tim_lineEdiT")
        self.rel_tim_lineEdiT.setGeometry(QRect(500, 275, 135, 30))
        self.rel_tim_lineEdiT.setFont(font)
        self.rel_tim_lineEdiT.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(640, 270, 101, 40))
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(390, 210, 101, 20))
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-50, 70, 101, 20))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(640, 140, 101, 20))
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.exp2_ele1_comboBox = QComboBox(Form)
        self.exp2_ele1_comboBox.setObjectName(u"exp2_ele1_comboBox")
        self.exp2_ele1_comboBox.setGeometry(QRect(60, 65, 135, 30))
        self.exp2_ele1_comboBox.setFont(font)
        self.exp2_ele1_comboBox.setCursor(QCursor(Qt.OpenHandCursor))
        self.exp2_ele1_comboBox.setStyleSheet(u"QComboBox{\n"
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
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(390, 280, 101, 20))
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.defect_lineEdit = QLineEdit(Form)
        self.defect_lineEdit.setObjectName(u"defect_lineEdit")
        self.defect_lineEdit.setGeometry(QRect(750, 275, 135, 30))
        self.defect_lineEdit.setFont(font)
        self.defect_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.Them_sys_lineEdit = QLineEdit(Form)
        self.Them_sys_lineEdit.setObjectName(u"Them_sys_lineEdit")
        self.Them_sys_lineEdit.setGeometry(QRect(750, 135, 135, 30))
        self.Them_sys_lineEdit.setFont(font)
        self.Them_sys_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.exp2_ele1y_lineEdit = QLineEdit(Form)
        self.exp2_ele1y_lineEdit.setObjectName(u"exp2_ele1y_lineEdit")
        self.exp2_ele1y_lineEdit.setGeometry(QRect(60, 205, 135, 30))
        self.exp2_ele1y_lineEdit.setFont(font)
        self.exp2_ele1y_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.finish = QPushButton(Form)
        self.finish.setObjectName(u"finish")
        self.finish.setGeometry(QRect(790, 320, 95, 30))
        self.finish.setFont(font1)
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(640, 210, 101, 20))
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Them_lineEdit = QLineEdit(Form)
        self.Them_lineEdit.setObjectName(u"Them_lineEdit")
        self.Them_lineEdit.setGeometry(QRect(750, 65, 135, 30))
        self.Them_lineEdit.setFont(font)
        self.Them_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(390, 70, 101, 20))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.rel_tem_lineEdit_2 = QLineEdit(Form)
        self.rel_tem_lineEdit_2.setObjectName(u"rel_tem_lineEdit_2")
        self.rel_tem_lineEdit_2.setGeometry(QRect(500, 135, 135, 30))
        self.rel_tem_lineEdit_2.setFont(font)
        self.rel_tem_lineEdit_2.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 101, 21))
        self.label.setFont(font1)
        self.exp2_ele1x_lineEdit = QLineEdit(Form)
        self.exp2_ele1x_lineEdit.setObjectName(u"exp2_ele1x_lineEdit")
        self.exp2_ele1x_lineEdit.setGeometry(QRect(60, 135, 135, 30))
        self.exp2_ele1x_lineEdit.setFont(font)
        self.exp2_ele1x_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.rel_tem_lineEdit = QLineEdit(Form)
        self.rel_tem_lineEdit.setObjectName(u"rel_tem_lineEdit")
        self.rel_tem_lineEdit.setGeometry(QRect(500, 65, 135, 30))
        self.rel_tem_lineEdit.setFont(font)
        self.rel_tem_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(-50, 280, 101, 20))
        self.label_5.setFont(font1)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(640, 70, 101, 20))
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Them_tim_lineEdit = QLineEdit(Form)
        self.Them_tim_lineEdit.setObjectName(u"Them_tim_lineEdit")
        self.Them_tim_lineEdit.setGeometry(QRect(750, 205, 135, 30))
        self.Them_tim_lineEdit.setFont(font)
        self.Them_tim_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-50, 140, 101, 20))
        self.label_3.setFont(font1)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-50, 210, 101, 20))
        self.label_4.setFont(font1)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.exp2_ele2z_lineEdit = QLineEdit(Form)
        self.exp2_ele2z_lineEdit.setObjectName(u"exp2_ele2z_lineEdit")
        self.exp2_ele2z_lineEdit.setGeometry(QRect(260, 275, 135, 30))
        self.exp2_ele2z_lineEdit.setFont(font)
        self.exp2_ele2z_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.exp2_ele2x_lineEdit = QLineEdit(Form)
        self.exp2_ele2x_lineEdit.setObjectName(u"exp2_ele2x_lineEdit")
        self.exp2_ele2x_lineEdit.setGeometry(QRect(260, 135, 135, 30))
        self.exp2_ele2x_lineEdit.setFont(font)
        self.exp2_ele2x_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.exp2_ele2y_lineEdit = QLineEdit(Form)
        self.exp2_ele2y_lineEdit.setObjectName(u"exp2_ele2y_lineEdit")
        self.exp2_ele2y_lineEdit.setGeometry(QRect(260, 205, 135, 30))
        self.exp2_ele2y_lineEdit.setFont(font)
        self.exp2_ele2y_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(150, 140, 101, 20))
        self.label_14.setFont(font1)
        self.label_14.setLayoutDirection(Qt.LeftToRight)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.exp2_ele2_comboBox = QComboBox(Form)
        self.exp2_ele2_comboBox.setObjectName(u"exp2_ele2_comboBox")
        self.exp2_ele2_comboBox.setGeometry(QRect(260, 65, 135, 30))
        self.exp2_ele2_comboBox.setFont(font)
        self.exp2_ele2_comboBox.setCursor(QCursor(Qt.OpenHandCursor))
        self.exp2_ele2_comboBox.setStyleSheet(u"QComboBox{\n"
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
        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(150, 280, 101, 20))
        self.label_15.setFont(font1)
        self.label_15.setLayoutDirection(Qt.LeftToRight)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(150, 210, 101, 20))
        self.label_16.setFont(font1)
        self.label_16.setLayoutDirection(Qt.LeftToRight)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(150, 70, 101, 20))
        self.label_17.setFont(font1)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_18 = QLabel(Form)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(550, 280, 80, 20))
        self.label_18.setFont(font1)
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_19 = QLabel(Form)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(550, 140, 80, 20))
        self.label_19.setFont(font1)
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_20 = QLabel(Form)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(550, 70, 80, 20))
        self.label_20.setFont(font1)
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_21 = QLabel(Form)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(800, 210, 80, 20))
        self.label_21.setFont(font1)
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_22 = QLabel(Form)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(800, 70, 80, 20))
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.exp2_arg_pushButton = QPushButton(Form)
        self.exp2_arg_pushButton.setObjectName(u"exp2_arg_pushButton")
        self.exp2_arg_pushButton.setGeometry(QRect(100, 10, 95, 30))
        self.exp2_arg_pushButton.setFont(font1)
        self.rel_sys_comboBox = QComboBox(Form)
        self.rel_sys_comboBox.setObjectName(u"rel_sys_comboBox")
        self.rel_sys_comboBox.setGeometry(QRect(500, 205, 135, 30))
        self.rel_sys_comboBox.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u6e29\u5ea6", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u5f17\u5170\u514b\u5c14\n"
"\u7f3a\u9677\u5bf9\u6570\u91cf", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u7cfb\u7efc", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5143\u7d20", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u7cfb\u7efc", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u5f1b\u8c6b\u65f6\u95f4", None))
        self.finish.setText(QCoreApplication.translate("Form", u"\u5b8c\u6210", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u6a21\u62df\u65f6\u95f4", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u521d\u59cb\u6e29\u5ea6", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5b9e\u9a8c\u4e8c", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Z", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u70ed\u6d41", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Y", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Z", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Y", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u5143\u7d20", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"ps", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"K", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"K", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"ps", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"eV/ps", None))
        self.exp2_arg_pushButton.setText(QCoreApplication.translate("Form", u"\u63a8\u8350\u53c2\u6570", None))
    # retranslateUi

