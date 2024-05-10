# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
sys.path.append("../..")

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QStackedWidget, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1264, 773)
        icon = QIcon()
        icon.addFile(u":/background/\u8f6f\u4ef6\u56fe\u6807.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 39, 270, 740))
        self.widget.setStyleSheet(u"background-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);\n"
"border-right: 1px solid white;\n"
"")
        self.sys_stackedWidget = QStackedWidget(self.widget)
        self.sys_stackedWidget.setObjectName(u"sys_stackedWidget")
        self.sys_stackedWidget.setGeometry(QRect(0, 0, 270, 240))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        font.setBold(True)
        self.sys_stackedWidget.setFont(font)
        self.sys_stackedWidget.setStyleSheet(u"background-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);\n"
"border-right: 1px solid rgb(173, 181, 189);\n"
"")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 121, 21))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"border-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp1_ele1_comboBox = QComboBox(self.page_3)
        self.exp1_ele1_comboBox.setObjectName(u"exp1_ele1_comboBox")
        self.exp1_ele1_comboBox.setGeometry(QRect(20, 60, 135, 30))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.exp1_ele1_comboBox.setFont(font2)
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
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(65, 30, 50, 30))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"border-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(220, 57, 40, 35))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setStyleSheet(u"border-image: url(:/background/\u539f\u5b50.png);")
        self.exp1_ele1x_spinBox = QSpinBox(self.page_3)
        self.exp1_ele1x_spinBox.setObjectName(u"exp1_ele1x_spinBox")
        self.exp1_ele1x_spinBox.setGeometry(QRect(20, 110, 135, 30))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.exp1_ele1x_spinBox.sizePolicy().hasHeightForWidth())
        self.exp1_ele1x_spinBox.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setBold(True)
        self.exp1_ele1x_spinBox.setFont(font3)
        self.exp1_ele1x_spinBox.setStyleSheet(u"QSpinBox{\n"
"\n"
"	border: 1px solid white;\n"
"    border-radius: 3px;\n"
"    padding: 1px 2px 1px 2px;\n"
"    min-width: 3em;\n"
"	background-color: #f8f9fa;\n"
"}\n"
"	color: rgb(0\uff0c0\uff0c0);\n"
"\n"
"")
        self.exp1_ele1x_spinBox.setMaximum(1000000000)
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(155, 110, 30, 30))
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setItalic(True)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"border-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp1_ele1y_spinBox = QSpinBox(self.page_3)
        self.exp1_ele1y_spinBox.setObjectName(u"exp1_ele1y_spinBox")
        self.exp1_ele1y_spinBox.setGeometry(QRect(20, 160, 135, 30))
        sizePolicy1.setHeightForWidth(self.exp1_ele1y_spinBox.sizePolicy().hasHeightForWidth())
        self.exp1_ele1y_spinBox.setSizePolicy(sizePolicy1)
        self.exp1_ele1y_spinBox.setFont(font3)
        self.exp1_ele1y_spinBox.setStyleSheet(u"QSpinBox{\n"
"\n"
"	border: 1px solid white;\n"
"    border-radius: 3px;\n"
"    padding: 1px 2px 1px 2px;\n"
"    min-width: 3em;\n"
"	background-color: #f8f9fa;\n"
"}\n"
"	color: rgb(0\uff0c0\uff0c0);\n"
"")
        self.exp1_ele1y_spinBox.setMaximum(1000000000)
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(155, 160, 30, 30))
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"border-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp1_ele1z_spinBox = QSpinBox(self.page_3)
        self.exp1_ele1z_spinBox.setObjectName(u"exp1_ele1z_spinBox")
        self.exp1_ele1z_spinBox.setGeometry(QRect(20, 210, 135, 30))
        sizePolicy1.setHeightForWidth(self.exp1_ele1z_spinBox.sizePolicy().hasHeightForWidth())
        self.exp1_ele1z_spinBox.setSizePolicy(sizePolicy1)
        self.exp1_ele1z_spinBox.setFont(font3)
        self.exp1_ele1z_spinBox.setStyleSheet(u"QSpinBox{\n"
"\n"
"	border: 1px solid white;\n"
"    border-radius: 3px;\n"
"    padding: 1px 2px 1px 2px;\n"
"    min-width: 3em;\n"
"	background-color: #f8f9fa;\n"
"}\n"
"	color: rgb(0\uff0c0\uff0c0);\n"
"")
        self.exp1_ele1z_spinBox.setMaximum(1000000000)
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(155, 210, 30, 30))
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"border-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(220, 107, 40, 35))
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setStyleSheet(u"border-image: url(:/background/\u5750\u6807\u8f74.png);")
        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(220, 157, 40, 35))
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setStyleSheet(u"border-image: url(:/background/\u5750\u6807\u8f74.png);")
        self.label_11 = QLabel(self.page_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(220, 207, 40, 35))
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setStyleSheet(u"border-image: url(:/background/\u5750\u6807\u8f74.png);")
        self.sys_stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 10, 121, 21))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"border-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp2_ele1_comboBox = QComboBox(self.page_4)
        self.exp2_ele1_comboBox.setObjectName(u"exp2_ele1_comboBox")
        self.exp2_ele1_comboBox.setGeometry(QRect(20, 60, 65, 30))
        self.exp2_ele1_comboBox.setFont(font2)
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
        self.exp2_ele2_comboBox = QComboBox(self.page_4)
        self.exp2_ele2_comboBox.setObjectName(u"exp2_ele2_comboBox")
        self.exp2_ele2_comboBox.setGeometry(QRect(90, 60, 65, 30))
        self.exp2_ele2_comboBox.setFont(font2)
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
        self.label_12 = QLabel(self.page_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(28, 30, 50, 30))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"border-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_13 = QLabel(self.page_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(96, 30, 50, 30))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"border-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14 = QLabel(self.page_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(220, 57, 40, 35))
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setStyleSheet(u"border-image: url(:/background/\u539f\u5b50.png);")
        self.exp2_ele1x_spinBox = QSpinBox(self.page_4)
        self.exp2_ele1x_spinBox.setObjectName(u"exp2_ele1x_spinBox")
        self.exp2_ele1x_spinBox.setGeometry(QRect(20, 110, 65, 30))
        sizePolicy1.setHeightForWidth(self.exp2_ele1x_spinBox.sizePolicy().hasHeightForWidth())
        self.exp2_ele1x_spinBox.setSizePolicy(sizePolicy1)
        self.exp2_ele1x_spinBox.setFont(font3)
        self.exp2_ele1x_spinBox.setStyleSheet(u"QSpinBox{\n"
"	border: 1px solid white;\n"
"    border-radius: 3px;\n"
"    padding: 1px 2px 1px 2px;\n"
"    min-width: 3em;\n"
"	background-color: #f8f9fa;\n"
"}\n"
"color: rgb(0, 0, 0);\n"
"\n"
"")
        self.exp2_ele2x_spinBox = QSpinBox(self.page_4)
        self.exp2_ele2x_spinBox.setObjectName(u"exp2_ele2x_spinBox")
        self.exp2_ele2x_spinBox.setGeometry(QRect(90, 110, 65, 30))
        sizePolicy1.setHeightForWidth(self.exp2_ele2x_spinBox.sizePolicy().hasHeightForWidth())
        self.exp2_ele2x_spinBox.setSizePolicy(sizePolicy1)
        self.exp2_ele2x_spinBox.setFont(font3)
        self.exp2_ele2x_spinBox.setStyleSheet(u"QSpinBox{\n"
"\n"
"	border: 1px solid white;\n"
"    border-radius: 3px;\n"
"    padding: 1px 2px 1px 2px;\n"
"    min-width: 3em;\n"
"	background-color: #f8f9fa;\n"
"}\n"
"	color: rgb(0\uff0c0\uff0c0);\n"
"\n"
"")
        self.exp2_ele1y_spinBox = QSpinBox(self.page_4)
        self.exp2_ele1y_spinBox.setObjectName(u"exp2_ele1y_spinBox")
        self.exp2_ele1y_spinBox.setGeometry(QRect(20, 160, 65, 30))
        sizePolicy1.setHeightForWidth(self.exp2_ele1y_spinBox.sizePolicy().hasHeightForWidth())
        self.exp2_ele1y_spinBox.setSizePolicy(sizePolicy1)
        self.exp2_ele1y_spinBox.setFont(font3)
        self.exp2_ele1y_spinBox.setStyleSheet(u"QSpinBox{\n"
"\n"
"	border: 1px solid white;\n"
"    border-radius: 3px;\n"
"    padding: 1px 2px 1px 2px;\n"
"    min-width: 3em;\n"
"	background-color: #f8f9fa;\n"
"}\n"
"	color: rgb(0\uff0c0\uff0c0);\n"
"\n"
"")
        self.exp2_ele2y_spinBox = QSpinBox(self.page_4)
        self.exp2_ele2y_spinBox.setObjectName(u"exp2_ele2y_spinBox")
        self.exp2_ele2y_spinBox.setGeometry(QRect(90, 160, 65, 30))
        sizePolicy1.setHeightForWidth(self.exp2_ele2y_spinBox.sizePolicy().hasHeightForWidth())
        self.exp2_ele2y_spinBox.setSizePolicy(sizePolicy1)
        self.exp2_ele2y_spinBox.setFont(font3)
        self.exp2_ele2y_spinBox.setStyleSheet(u"QSpinBox{\n"
"\n"
"	border: 1px solid white;\n"
"    border-radius: 3px;\n"
"    padding: 1px 2px 1px 2px;\n"
"    min-width: 3em;\n"
"	background-color: #f8f9fa;\n"
"}\n"
"color: rgb(0\uff0c0\uff0c0);\n"
"\n"
"")
        self.exp2_ele1z_spinBox = QSpinBox(self.page_4)
        self.exp2_ele1z_spinBox.setObjectName(u"exp2_ele1z_spinBox")
        self.exp2_ele1z_spinBox.setGeometry(QRect(20, 210, 65, 30))
        sizePolicy1.setHeightForWidth(self.exp2_ele1z_spinBox.sizePolicy().hasHeightForWidth())
        self.exp2_ele1z_spinBox.setSizePolicy(sizePolicy1)
        self.exp2_ele1z_spinBox.setFont(font3)
        self.exp2_ele1z_spinBox.setStyleSheet(u"QSpinBox{\n"
"	color: rgb(0\uff0c0\uff0c0);\n"
"	border: 1px solid white;\n"
"    border-radius: 3px;\n"
"    padding: 1px 2px 1px 2px;\n"
"    min-width: 3em;\n"
"	background-color: #f8f9fa;\n"
"}\n"
"\n"
"")
        self.exp2_ele2z_spinBox = QSpinBox(self.page_4)
        self.exp2_ele2z_spinBox.setObjectName(u"exp2_ele2z_spinBox")
        self.exp2_ele2z_spinBox.setGeometry(QRect(90, 210, 65, 30))
        sizePolicy1.setHeightForWidth(self.exp2_ele2z_spinBox.sizePolicy().hasHeightForWidth())
        self.exp2_ele2z_spinBox.setSizePolicy(sizePolicy1)
        self.exp2_ele2z_spinBox.setFont(font3)
        self.exp2_ele2z_spinBox.setStyleSheet(u"QSpinBox{\n"
"\n"
"	border: 1px solid white;\n"
"    border-radius: 3px;\n"
"    padding: 1px 2px 1px 2px;\n"
"    min-width: 3em;\n"
"	background-color: #f8f9fa;\n"
"}\n"
"	color: rgb(0\uff0c0\uff0c0);\n"
"\n"
"")
        self.label_15 = QLabel(self.page_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(220, 107, 40, 35))
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setStyleSheet(u"border-image: url(:/background/\u5750\u6807\u8f74.png);")
        self.label_16 = QLabel(self.page_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(220, 157, 40, 35))
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setStyleSheet(u"border-image: url(:/background/\u5750\u6807\u8f74.png);")
        self.label_17 = QLabel(self.page_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(220, 207, 40, 35))
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setStyleSheet(u"border-image: url(:/background/\u5750\u6807\u8f74.png);")
        self.label_18 = QLabel(self.page_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(155, 110, 30, 30))
        self.label_18.setFont(font4)
        self.label_18.setStyleSheet(u"color: rgb(0\uff0c0\uff0c0);\n"
"border-color: rgb(233, 236, 239);")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_19 = QLabel(self.page_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(155, 160, 30, 30))
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"color: rgb(0\uff0c0\uff0c0);\n"
"border-color: rgb(233, 236, 239);")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_20 = QLabel(self.page_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(155, 210, 30, 30))
        self.label_20.setFont(font4)
        self.label_20.setStyleSheet(u"color: rgb(0\uff0c0\uff0c0);\n"
"border-color: rgb(233, 236, 239);")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sys_stackedWidget.addWidget(self.page_4)
        self.rel_tem_lineEdit = QLineEdit(self.widget)
        self.rel_tem_lineEdit.setObjectName(u"rel_tem_lineEdit")
        self.rel_tem_lineEdit.setGeometry(QRect(20, 300, 135, 30))
        self.rel_tem_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 250, 121, 21))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"border-color: rgb(233, 236, 239);\n"
"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(160, 307, 50, 15))
        font5 = QFont()
        font5.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font5.setBold(True)
        self.label_21.setFont(font5)
        self.label_21.setStyleSheet(u"\n"
"\n"
"border-right-color: rgb(173\uff0c181\uff0c189);")
        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(129, 305, 20, 20))
        font6 = QFont()
        font6.setFamilies([u"Times New Roman"])
        font6.setBold(True)
        font6.setItalic(True)
        self.label_22.setFont(font6)
        self.label_22.setStyleSheet(u"color: rgb(0\uff0c0\uff0c0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(220, 297, 40, 35))
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setStyleSheet(u"border-image: url(:/background/\u6e29\u5ea6.png);")
        self.rel_sys_comboBox = QComboBox(self.widget)
        self.rel_sys_comboBox.setObjectName(u"rel_sys_comboBox")
        self.rel_sys_comboBox.setGeometry(QRect(20, 350, 135, 30))
        self.rel_sys_comboBox.setFont(font2)
        self.rel_sys_comboBox.setCursor(QCursor(Qt.OpenHandCursor))
        self.rel_sys_comboBox.setStyleSheet(u"QComboBox{\n"
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
        self.label_24 = QLabel(self.widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(160, 357, 50, 15))
        self.label_24.setFont(font5)
        self.label_24.setStyleSheet(u"\n"
"border-right-color: rgb(173\uff0c181\uff0c189);")
        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(220, 346, 40, 35))
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setStyleSheet(u"border-image: url(:/background/\u7cfb\u7efc\u9009\u62e9.png);")
        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(65, 270, 50, 30))
        self.label_26.setFont(font1)
        self.label_26.setStyleSheet(u"border-color: rgb(233, 236, 239);")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rel_tim_lineEdiT = QLineEdit(self.widget)
        self.rel_tim_lineEdiT.setObjectName(u"rel_tim_lineEdiT")
        self.rel_tim_lineEdiT.setGeometry(QRect(20, 400, 135, 30))
        self.rel_tim_lineEdiT.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(130, 404, 20, 20))
        self.label_27.setFont(font6)
        self.label_27.setStyleSheet(u"color: rgb(0\uff0c0\uff0c0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_28 = QLabel(self.widget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(160, 407, 50, 15))
        self.label_28.setFont(font5)
        self.label_28.setStyleSheet(u"\n"
"border-right-color: rgb(173\uff0c181\uff0c189);")
        self.label_29 = QLabel(self.widget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(225, 400, 30, 29))
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setStyleSheet(u"border-image: url(:/background/\u65f6\u95f4.png);")
        self.label_30 = QLabel(self.widget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(60, 440, 60, 30))
        self.label_30.setFont(font1)
        self.label_30.setStyleSheet(u"\n"
"border-color: rgb(233, 236, 239);")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_31 = QLabel(self.widget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(160, 476, 50, 15))
        self.label_31.setFont(font5)
        self.label_31.setStyleSheet(u"border-right-color: rgb(173\uff0c181\uff0c189);")
        self.Them_lineEdit = QLineEdit(self.widget)
        self.Them_lineEdit.setObjectName(u"Them_lineEdit")
        self.Them_lineEdit.setGeometry(QRect(20, 470, 135, 30))
        self.Them_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_32 = QLabel(self.widget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(129, 474, 20, 20))
        self.label_32.setFont(font6)
        self.label_32.setStyleSheet(u"color: rgb(0\uff0c0\uff0c0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_33 = QLabel(self.widget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(225, 467, 30, 30))
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setStyleSheet(u"border-image: url(:/background/\u70ed\u6d41.png);")
        self.Them_sys_comboBox = QComboBox(self.widget)
        self.Them_sys_comboBox.setObjectName(u"Them_sys_comboBox")
        self.Them_sys_comboBox.setGeometry(QRect(20, 520, 135, 30))
        self.Them_sys_comboBox.setFont(font2)
        self.Them_sys_comboBox.setCursor(QCursor(Qt.OpenHandCursor))
        self.Them_sys_comboBox.setStyleSheet(u"QComboBox{\n"
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
        self.label_34 = QLabel(self.widget)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(160, 527, 50, 15))
        self.label_34.setFont(font5)
        self.label_34.setStyleSheet(u"\n"
"border-right-color: rgb(173\uff0c181\uff0c189);")
        self.label_35 = QLabel(self.widget)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(220, 516, 40, 35))
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setStyleSheet(u"border-image: url(:/background/\u7cfb\u7efc\u9009\u62e9.png);")
        self.Them_tim_lineEdit = QLineEdit(self.widget)
        self.Them_tim_lineEdit.setObjectName(u"Them_tim_lineEdit")
        self.Them_tim_lineEdit.setGeometry(QRect(20, 570, 135, 30))
        self.Them_tim_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_36 = QLabel(self.widget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(130, 576, 20, 20))
        self.label_36.setFont(font6)
        self.label_36.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0\uff0c0\uff0c0);")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_37 = QLabel(self.widget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(160, 577, 50, 15))
        self.label_37.setFont(font5)
        self.label_37.setStyleSheet(u"\n"
"border-right-color: rgb(173\uff0c181\uff0c189);")
        self.label_38 = QLabel(self.widget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(225, 570, 30, 29))
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)
        self.label_38.setStyleSheet(u"border-image: url(:/background/\u65f6\u95f4.png);")
        self.label_39 = QLabel(self.widget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(30, 615, 120, 20))
        self.label_39.setFont(font1)
        self.label_39.setStyleSheet(u"border-color: rgb(233, 236, 239);")
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.defect_spinBox = QSpinBox(self.widget)
        self.defect_spinBox.setObjectName(u"defect_spinBox")
        self.defect_spinBox.setGeometry(QRect(20, 670, 135, 30))
        sizePolicy1.setHeightForWidth(self.defect_spinBox.sizePolicy().hasHeightForWidth())
        self.defect_spinBox.setSizePolicy(sizePolicy1)
        self.defect_spinBox.setFont(font3)
        self.defect_spinBox.setStyleSheet(u"QSpinBox{\n"
"\n"
"	border: 1px solid white;\n"
"    border-radius: 3px;\n"
"    padding: 1px 2px 1px 2px;\n"
"    min-width: 3em;\n"
"	background-color: #f8f9fa;\n"
"}\n"
"\n"
"")
        self.defect_spinBox.setMaximum(1000000000)
        self.label_40 = QLabel(self.widget)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(33, 635, 111, 30))
        self.label_40.setFont(font1)
        self.label_40.setStyleSheet(u"border-color: rgb(233, 236, 239);")
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_41 = QLabel(self.widget)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(220, 664, 40, 35))
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        self.label_41.setStyleSheet(u"border-image: url(:/background/\u6676\u4f53\u7f3a\u9677.png);")
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, -1, 1261, 41))
        self.widget_2.setStyleSheet(u"background-color: rgb(233, 236, 239);\n"
"border-bottom:1px solid #868e96;")
        self.exp1_radioButton = QRadioButton(self.widget_2)
        self.exp1_radioButton.setObjectName(u"exp1_radioButton")
        self.exp1_radioButton.setGeometry(QRect(20, 6, 81, 31))
        self.exp1_radioButton.setFont(font1)
        self.exp1_radioButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.exp1_radioButton.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px bolid #495057;\n"
"color: rgb(0, 0, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/background/\u5b9e\u9a8c\u5ba4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exp1_radioButton.setIcon(icon1)
        self.exp2_radioButton = QRadioButton(self.widget_2)
        self.exp2_radioButton.setObjectName(u"exp2_radioButton")
        self.exp2_radioButton.setGeometry(QRect(110, 6, 81, 31))
        self.exp2_radioButton.setFont(font1)
        self.exp2_radioButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.exp2_radioButton.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px bolid #495057;\n"
"color: rgb(0, 0, 0);")
        self.exp2_radioButton.setIcon(icon1)
        self.exp1_arg_pushButton = QPushButton(self.widget_2)
        self.exp1_arg_pushButton.setObjectName(u"exp1_arg_pushButton")
        self.exp1_arg_pushButton.setGeometry(QRect(220, 3, 120, 35))
        self.exp1_arg_pushButton.setFont(font1)
        self.exp1_arg_pushButton.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px bolid #495057;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        icon2 = QIcon()
        icon2.addFile(u":/background/\u53c2\u6570.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exp1_arg_pushButton.setIcon(icon2)
        self.exp2_arg_pushButton = QPushButton(self.widget_2)
        self.exp2_arg_pushButton.setObjectName(u"exp2_arg_pushButton")
        self.exp2_arg_pushButton.setGeometry(QRect(350, 3, 120, 35))
        self.exp2_arg_pushButton.setFont(font1)
        self.exp2_arg_pushButton.setStyleSheet(u"border-radius: 3px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px bolid #495057;\n"
"background-color: rgb(255, 255, 255);")
        self.exp2_arg_pushButton.setIcon(icon2)
        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(270, 40, 991, 731))
        self.widget_3.setStyleSheet(u"background-color: rgb(233, 236, 239);\n"
"border-top:1px solid #868e96;\n"
"border-left: 1px solid rgb(173, 181, 189);")
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 10, 981, 471))
        self.widget_4.setStyleSheet(u"background-color: rgb(248, 249, 250);\n"
"border: 1px solid rgb(248, 249, 250);")
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(9, 9, 721, 451))
        self.widget_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label_42 = QLabel(self.widget_5)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(600, 410, 111, 31))
        self.label_42.setFont(font1)
        self.label_42.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayoutWidget_6 = QWidget(self.widget_5)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(-1, -1, 721, 451))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_6.raise_()
        self.label_42.raise_()
        self.vacan_checkBox = QCheckBox(self.widget_4)
        self.vacan_checkBox.setObjectName(u"vacan_checkBox")
        self.vacan_checkBox.setGeometry(QRect(750, 20, 95, 40))
        sizePolicy.setHeightForWidth(self.vacan_checkBox.sizePolicy().hasHeightForWidth())
        self.vacan_checkBox.setSizePolicy(sizePolicy)
        font7 = QFont()
        font7.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font7.setPointSize(9)
        font7.setBold(True)
        self.vacan_checkBox.setFont(font7)
        self.vacan_checkBox.setStyleSheet(u"background-color: #e9ecef;\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);")
        self.gap_checkBox = QCheckBox(self.widget_4)
        self.gap_checkBox.setObjectName(u"gap_checkBox")
        self.gap_checkBox.setGeometry(QRect(870, 20, 95, 40))
        sizePolicy.setHeightForWidth(self.gap_checkBox.sizePolicy().hasHeightForWidth())
        self.gap_checkBox.setSizePolicy(sizePolicy)
        self.gap_checkBox.setFont(font7)
        self.gap_checkBox.setStyleSheet(u"background-color: #e9ecef;\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);")
        self.label_43 = QLabel(self.widget_4)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(825, 33, 16, 16))
        self.label_43.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius: 5px;")
        self.label_44 = QLabel(self.widget_4)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(944, 33, 16, 16))
        self.label_44.setStyleSheet(u"background-color: rgb(85, 170, 0);\n"
"border-radius: 5px;")
        self.stackedWidget_3 = QStackedWidget(self.widget_4)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setGeometry(QRect(750, 120, 221, 321))
        self.stackedWidget_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.widget_8 = QWidget(self.page_5)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(0, 20, 201, 201))
        self.widget_8.setStyleSheet(u"border-top-color: rgb(130, 130, 130);\n"
"border-bottom-color: rgb(130, 130, 130);\n"
"border-left-color: rgb(130, 130, 130);")
        self.label_55 = QLabel(self.widget_8)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(60, 10, 80, 20))
        font8 = QFont()
        font8.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font8.setPointSize(11)
        font8.setBold(True)
        self.label_55.setFont(font8)
        self.label_55.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_55.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_56 = QLabel(self.widget_8)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(1, 60, 55, 20))
        font9 = QFont()
        font9.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font9.setPointSize(8)
        font9.setBold(True)
        self.label_56.setFont(font9)
        self.label_56.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_57 = QLabel(self.widget_8)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(140, 30, 50, 20))
        self.label_57.setFont(font9)
        self.label_57.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_57.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_58 = QLabel(self.widget_8)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(1, 90, 70, 20))
        self.label_58.setFont(font9)
        self.label_58.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_59 = QLabel(self.widget_8)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(1, 120, 70, 20))
        self.label_59.setFont(font9)
        self.label_59.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.exp1_ele1_lineEdit = QLineEdit(self.widget_8)
        self.exp1_ele1_lineEdit.setObjectName(u"exp1_ele1_lineEdit")
        self.exp1_ele1_lineEdit.setGeometry(QRect(152, 60, 25, 20))
        self.exp1_ele1_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp1_ele1_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp1_ele1_mass_lineEdit = QLineEdit(self.widget_8)
        self.exp1_ele1_mass_lineEdit.setObjectName(u"exp1_ele1_mass_lineEdit")
        self.exp1_ele1_mass_lineEdit.setGeometry(QRect(147, 90, 35, 20))
        self.exp1_ele1_mass_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp1_ele1_mass_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp1_ele1_num_lineEdit = QLineEdit(self.widget_8)
        self.exp1_ele1_num_lineEdit.setObjectName(u"exp1_ele1_num_lineEdit")
        self.exp1_ele1_num_lineEdit.setGeometry(QRect(145, 120, 40, 20))
        self.exp1_ele1_num_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp1_ele1_num_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_61 = QLabel(self.page_5)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(0, 250, 70, 20))
        self.label_61.setFont(font9)
        self.label_61.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.exp_res_lineEdit = QLineEdit(self.page_5)
        self.exp_res_lineEdit.setObjectName(u"exp_res_lineEdit")
        self.exp_res_lineEdit.setGeometry(QRect(90, 250, 60, 20))
        self.exp_res_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp_res_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_45 = QLabel(self.page_5)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(150, 250, 71, 20))
        font10 = QFont()
        font10.setFamilies([u"Times New Roman"])
        font10.setPointSize(9)
        font10.setBold(True)
        font10.setItalic(True)
        self.label_45.setFont(font10)
        self.label_45.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.stackedWidget_3.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.widget_7 = QWidget(self.page_6)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(0, 20, 201, 201))
        self.widget_7.setStyleSheet(u"border-top-color: rgb(130, 130, 130);\n"
"border-bottom-color: rgb(130, 130, 130);\n"
"border-left-color: rgb(130, 130, 130);")
        self.label_50 = QLabel(self.widget_7)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(60, 10, 80, 20))
        self.label_50.setFont(font8)
        self.label_50.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_50.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_51 = QLabel(self.widget_7)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(1, 60, 55, 20))
        self.label_51.setFont(font9)
        self.label_51.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_52 = QLabel(self.widget_7)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(140, 30, 50, 20))
        self.label_52.setFont(font9)
        self.label_52.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_52.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_53 = QLabel(self.widget_7)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(1, 90, 70, 20))
        self.label_53.setFont(font9)
        self.label_53.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_54 = QLabel(self.widget_7)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(1, 120, 70, 20))
        self.label_54.setFont(font9)
        self.label_54.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_60 = QLabel(self.widget_7)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(90, 30, 50, 20))
        self.label_60.setFont(font9)
        self.label_60.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_60.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp2_ele1_lineEdit = QLineEdit(self.widget_7)
        self.exp2_ele1_lineEdit.setObjectName(u"exp2_ele1_lineEdit")
        self.exp2_ele1_lineEdit.setGeometry(QRect(103, 60, 25, 20))
        self.exp2_ele1_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp2_ele1_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp2_ele2_lineEdit = QLineEdit(self.widget_7)
        self.exp2_ele2_lineEdit.setObjectName(u"exp2_ele2_lineEdit")
        self.exp2_ele2_lineEdit.setGeometry(QRect(153, 60, 25, 20))
        self.exp2_ele2_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp2_ele2_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp2_ele1_mass_lineEdit = QLineEdit(self.widget_7)
        self.exp2_ele1_mass_lineEdit.setObjectName(u"exp2_ele1_mass_lineEdit")
        self.exp2_ele1_mass_lineEdit.setGeometry(QRect(98, 90, 35, 20))
        self.exp2_ele1_mass_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp2_ele1_mass_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp2_ele2_mass_lineEdit = QLineEdit(self.widget_7)
        self.exp2_ele2_mass_lineEdit.setObjectName(u"exp2_ele2_mass_lineEdit")
        self.exp2_ele2_mass_lineEdit.setGeometry(QRect(148, 90, 35, 20))
        self.exp2_ele2_mass_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp2_ele2_mass_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp2_ele1_num_lineEdit = QLineEdit(self.widget_7)
        self.exp2_ele1_num_lineEdit.setObjectName(u"exp2_ele1_num_lineEdit")
        self.exp2_ele1_num_lineEdit.setGeometry(QRect(95, 120, 40, 20))
        self.exp2_ele1_num_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp2_ele1_num_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp2_ele2_num_lineEdit = QLineEdit(self.widget_7)
        self.exp2_ele2_num_lineEdit.setObjectName(u"exp2_ele2_num_lineEdit")
        self.exp2_ele2_num_lineEdit.setGeometry(QRect(145, 120, 40, 20))
        self.exp2_ele2_num_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp2_ele2_num_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_62 = QLabel(self.page_6)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(0, 250, 70, 20))
        self.label_62.setFont(font9)
        self.label_62.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.exp2_reslineEdit = QLineEdit(self.page_6)
        self.exp2_reslineEdit.setObjectName(u"exp2_reslineEdit")
        self.exp2_reslineEdit.setGeometry(QRect(90, 250, 60, 20))
        self.exp2_reslineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp2_reslineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_46 = QLabel(self.page_6)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(150, 250, 71, 20))
        self.label_46.setFont(font10)
        self.stackedWidget_3.addWidget(self.page_6)
        self.zon_tem_checkBox = QCheckBox(self.widget_4)
        self.zon_tem_checkBox.setObjectName(u"zon_tem_checkBox")
        self.zon_tem_checkBox.setGeometry(QRect(800, 70, 125, 40))
        sizePolicy.setHeightForWidth(self.zon_tem_checkBox.sizePolicy().hasHeightForWidth())
        self.zon_tem_checkBox.setSizePolicy(sizePolicy)
        self.zon_tem_checkBox.setFont(font7)
        self.zon_tem_checkBox.setStyleSheet(u"background-color: #e9ecef;\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);")
        icon3 = QIcon()
        icon3.addFile(u":/background/\u53ef\u89c6\u5316.png", QSize(), QIcon.Normal, QIcon.Off)
        self.zon_tem_checkBox.setIcon(icon3)
        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 489, 731, 241))
        self.stackedWidget.setFont(font8)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(248, 249, 250);\n"
"border: 1px solid rgb(248, 249, 250);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.tabWidget = QTabWidget(self.page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 731, 241))
        self.tabWidget.setFont(font8)
        self.tabWidget.setStyleSheet(u"background-color: rgb(248, 249, 250);\n"
"border: 1px solid rgb(248, 249, 250);\n"
"color: rgb(0, 0, 0);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 711, 181))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        icon4 = QIcon()
        icon4.addFile(u":/background/\u6e29\u5ea6.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget_2 = QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 711, 181))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_2, icon4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayoutWidget_3 = QWidget(self.tab_3)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 10, 711, 181))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        icon5 = QIcon()
        icon5.addFile(u":/background/\u58f0\u5b50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon5, "")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.tabWidget_2 = QTabWidget(self.page_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 731, 241))
        self.tabWidget_2.setFont(font8)
        self.tabWidget_2.setStyleSheet(u"background-color: rgb(248, 249, 250);\n"
"border: 1px solid rgb(248, 249, 250);")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayoutWidget_5 = QWidget(self.tab_4)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 10, 711, 181))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2.addTab(self.tab_4, icon4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayoutWidget_4 = QWidget(self.tab_5)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 10, 711, 181))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2.addTab(self.tab_5, icon4, "")
        self.stackedWidget.addWidget(self.page_2)
        self.start_pushButton = QPushButton(self.widget_3)
        self.start_pushButton.setObjectName(u"start_pushButton")
        self.start_pushButton.setGeometry(QRect(760, 500, 110, 40))
        self.start_pushButton.setFont(font8)
        self.start_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: rgb(165, 216, 255);\n"
"")
        self.pause_pushButton = QPushButton(self.widget_3)
        self.pause_pushButton.setObjectName(u"pause_pushButton")
        self.pause_pushButton.setGeometry(QRect(870, 556, 110, 41))
        self.pause_pushButton.setFont(font8)
        self.pause_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: rgb(153, 233, 242);")
        self.restart_pushButton = QPushButton(self.widget_3)
        self.restart_pushButton.setObjectName(u"restart_pushButton")
        self.restart_pushButton.setGeometry(QRect(760, 610, 110, 40))
        self.restart_pushButton.setFont(font8)
        self.restart_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: rgb(150, 242, 215);")
        self.over_pushButton = QPushButton(self.widget_3)
        self.over_pushButton.setObjectName(u"over_pushButton")
        self.over_pushButton.setGeometry(QRect(870, 660, 110, 40))
        self.over_pushButton.setFont(font8)
        self.over_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: rgb(186, 200, 255);")

        self.retranslateUi(Form)

        self.sys_stackedWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8f90\u7167\u635f\u4f24\u6838\u6750\u6599\u539f\u5b50\u5c3a\u5ea6\u70ed\u8f93\u8fd0\u53ef\u89c6\u5316\u8f6f\u4ef6", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u521d\u59cb\u4f53\u7cfb\u5efa\u7acb", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5143\u7d20\u4e00", None))
        self.label_8.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"x", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"y", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"z", None))
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"\u521d\u59cb\u4f53\u7cfb\u5efa\u7acb", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u5143\u7d20\u4e00", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u5143\u7d20\u4e8c", None))
        self.label_14.setText("")
        self.label_15.setText("")
        self.label_16.setText("")
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("Form", u"x", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"y", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"z", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6a21\u62df\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u521d\u59cb\u6e29\u5ea6", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"K", None))
        self.label_23.setText("")
        self.label_24.setText(QCoreApplication.translate("Form", u"\u7cfb\u7efc", None))
        self.label_25.setText("")
        self.label_26.setText(QCoreApplication.translate("Form", u"\u5f1b\u8c6b", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"ps", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"\u5f1b\u8c6b\u65f6\u95f4", None))
        self.label_29.setText("")
        self.label_30.setText(QCoreApplication.translate("Form", u"\u70ed\u5dee\u6a21\u62df", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"\u70ed\u6d41", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"J", None))
        self.label_33.setText("")
        self.label_34.setText(QCoreApplication.translate("Form", u"\u7cfb\u7efc", None))
        self.label_35.setText("")
        self.label_36.setText(QCoreApplication.translate("Form", u"ps", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"\u6a21\u62df\u65f6\u95f4", None))
        self.label_38.setText("")
        self.label_39.setText(QCoreApplication.translate("Form", u"\u8f90\u7167\u6a21\u62df\u8bbe\u7f6e", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"\u5f17\u5170\u79d1\u5c14\u7f3a\u9677\u5bf9\u6570", None))
        self.label_41.setText("")
        self.exp1_radioButton.setText(QCoreApplication.translate("Form", u"\u5b9e\u9a8c\u4e00", None))
        self.exp2_radioButton.setText(QCoreApplication.translate("Form", u"\u5b9e\u9a8c\u4e8c", None))
        self.exp1_arg_pushButton.setText(QCoreApplication.translate("Form", u"\u5b9e\u9a8c\u4e00\u63a8\u8350\u53c2\u6570", None))
        self.exp2_arg_pushButton.setText(QCoreApplication.translate("Form", u"\u5b9e\u9a8c\u4e8c\u63a8\u8350\u53c2\u6570", None))
        self.label_42.setText(QCoreApplication.translate("Form", u"\u6676\u4f533D\u7ed3\u6784\u89c6\u56fe", None))
        self.vacan_checkBox.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u7a7a\u4f4d", None))
        self.gap_checkBox.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u95f4\u9699", None))
        self.label_43.setText("")
        self.label_44.setText("")
        self.label_55.setText(QCoreApplication.translate("Form", u"\u4f53\u7cfb\u53c2\u6570", None))
        self.label_56.setText(QCoreApplication.translate("Form", u"\u5143\u7d20\u79cd\u7c7b", None))
        self.label_57.setText(QCoreApplication.translate("Form", u"\u5143\u7d20\u4e00", None))
        self.label_58.setText(QCoreApplication.translate("Form", u"\u76f8\u5bf9\u539f\u5b50\u8d28\u91cf", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"\u539f\u5b50\u6570\u91cf", None))
        self.label_61.setText(QCoreApplication.translate("Form", u"\u6750\u6599\u70ed\u5bfc\u7387", None))
        self.exp_res_lineEdit.setText("")
        self.label_45.setText(QCoreApplication.translate("Form", u"W*K-1*m-1", None))
        self.label_50.setText(QCoreApplication.translate("Form", u"\u4f53\u7cfb\u53c2\u6570", None))
        self.label_51.setText(QCoreApplication.translate("Form", u"\u5143\u7d20\u79cd\u7c7b", None))
        self.label_52.setText(QCoreApplication.translate("Form", u"\u5143\u7d20\u4e8c", None))
        self.label_53.setText(QCoreApplication.translate("Form", u"\u76f8\u5bf9\u539f\u5b50\u8d28\u91cf", None))
        self.label_54.setText(QCoreApplication.translate("Form", u"\u539f\u5b50\u6570\u91cf", None))
        self.label_60.setText(QCoreApplication.translate("Form", u"\u5143\u7d20\u4e00", None))
        self.label_62.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u70ed\u5bfc\u7387", None))
        self.exp2_reslineEdit.setText("")
        self.label_46.setText(QCoreApplication.translate("Form", u"W*K-1*m-1", None))
        self.zon_tem_checkBox.setText(QCoreApplication.translate("Form", u"\u533a\u57df\u6e29\u5ea6\u53ef\u89c6\u5316", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u4f53\u7cfb\u6e29\u5ea6\u66f2\u7ebf", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u4f53\u7cfb\u533a\u57df\u6e29\u5ea6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u58f0\u5b50\u6001\u5bc6\u5ea6\u66f2\u7ebf", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u4f53\u7cfb\u6e29\u5ea6\u66f2\u7ebf", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\u4f53\u7cfb\u533a\u57df\u6e29\u5ea6", None))
        self.start_pushButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.pause_pushButton.setText(QCoreApplication.translate("Form", u"\u6682\u505c", None))
        self.restart_pushButton.setText(QCoreApplication.translate("Form", u"\u91cd\u542f", None))
        self.over_pushButton.setText(QCoreApplication.translate("Form", u"\u7ed3\u675f", None))
    # retranslateUi

