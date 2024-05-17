# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QStackedWidget,
    QTabWidget, QVBoxLayout, QWidget)
import GUI.picture_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1329, 791)
        icon = QIcon()
        icon.addFile(u":/background/\u8f6f\u4ef6\u56fe\u6807.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout_11 = QHBoxLayout(Form)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QSize(16777215, 40))
        self.widget_2.setStyleSheet(u"background-color: rgb(233, 236, 239);\n"
"border-bottom:1px solid #868e96;")
        self.exp1_radioButton = QRadioButton(self.widget_2)
        self.exp1_radioButton.setObjectName(u"exp1_radioButton")
        self.exp1_radioButton.setGeometry(QRect(20, 6, 101, 31))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        font.setBold(True)
        self.exp1_radioButton.setFont(font)
        self.exp1_radioButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.exp1_radioButton.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px bolid #495057;\n"
"color: rgb(0, 0, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/background/\u5b9e\u9a8c\u5ba4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exp1_radioButton.setIcon(icon1)
        self.exp2_radioButton = QRadioButton(self.widget_2)
        self.exp2_radioButton.setObjectName(u"exp2_radioButton")
        self.exp2_radioButton.setGeometry(QRect(130, 6, 101, 31))
        self.exp2_radioButton.setFont(font)
        self.exp2_radioButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.exp2_radioButton.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px bolid #495057;\n"
"color: rgb(0, 0, 0);")
        self.exp2_radioButton.setIcon(icon1)
        self.exp1_arg_pushButton = QPushButton(self.widget_2)
        self.exp1_arg_pushButton.setObjectName(u"exp1_arg_pushButton")
        self.exp1_arg_pushButton.setGeometry(QRect(240, 3, 141, 35))
        self.exp1_arg_pushButton.setFont(font)
        self.exp1_arg_pushButton.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px bolid #495057;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        icon2 = QIcon()
        icon2.addFile(u":/background/\u53c2\u6570.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exp1_arg_pushButton.setIcon(icon2)
        self.exp2_arg_pushButton = QPushButton(self.widget_2)
        self.exp2_arg_pushButton.setObjectName(u"exp2_arg_pushButton")
        self.exp2_arg_pushButton.setGeometry(QRect(400, 3, 141, 35))
        self.exp2_arg_pushButton.setFont(font)
        self.exp2_arg_pushButton.setStyleSheet(u"border-radius: 3px;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px bolid #495057;\n"
"background-color: rgb(255, 255, 255);")
        self.exp2_arg_pushButton.setIcon(icon2)

        self.verticalLayout_8.addWidget(self.widget_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(285, 16777215))
        self.widget.setStyleSheet(u"background-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);\n"
"border-right:1 solid #868e96;")
        self.sys_stackedWidget = QStackedWidget(self.widget)
        self.sys_stackedWidget.setObjectName(u"sys_stackedWidget")
        self.sys_stackedWidget.setGeometry(QRect(0, 0, 270, 240))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.sys_stackedWidget.setFont(font1)
        self.sys_stackedWidget.setStyleSheet(u"background-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);\n"
"border-right: rgb(233, 236, 239);\n"
"")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 121, 21))
        self.label.setFont(font)
        self.label.setStyleSheet(u"border-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp1_ele1_comboBox = QComboBox(self.page_3)
        self.exp1_ele1_comboBox.setObjectName(u"exp1_ele1_comboBox")
        self.exp1_ele1_comboBox.setGeometry(QRect(20, 60, 135, 30))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(9)
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
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"border-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(220, 57, 40, 35))
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
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"border-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp2_ele1_comboBox = QComboBox(self.page_4)
        self.exp2_ele1_comboBox.setObjectName(u"exp2_ele1_comboBox")
        self.exp2_ele1_comboBox.setGeometry(QRect(20, 60, 65, 30))
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setPointSize(9)
        font5.setBold(True)
        font5.setItalic(True)
        self.exp2_ele1_comboBox.setFont(font5)
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
        self.exp2_ele2_comboBox.setFont(font5)
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
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"border-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_13 = QLabel(self.page_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(96, 30, 50, 30))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"border-color: rgb(233, 236, 239);\n"
"color: rgb(0, 0, 0);")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14 = QLabel(self.page_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(220, 57, 40, 35))
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setStyleSheet(u"border-image: url(:/background/\u539f\u5b50.png);\n"
"border-color: rgb(233, 236, 239);")
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
        self.label_15.setStyleSheet(u"border-image: url(:/background/\u5750\u6807\u8f74.png);\n"
"border-color: rgb(233, 236, 239);")
        self.label_16 = QLabel(self.page_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(220, 157, 40, 35))
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setStyleSheet(u"border-image: url(:/background/\u5750\u6807\u8f74.png);\n"
"border-color: rgb(233, 236, 239);")
        self.label_17 = QLabel(self.page_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(220, 207, 40, 35))
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setStyleSheet(u"border-image: url(:/background/\u5750\u6807\u8f74.png);\n"
"border-color: rgb(233, 236, 239);")
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
        self.rel_tem_lineEdit.setFont(font3)
        self.rel_tem_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 250, 121, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"border-color: rgb(233, 236, 239);\n"
"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(160, 307, 61, 16))
        font6 = QFont()
        font6.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font6.setBold(True)
        self.label_21.setFont(font6)
        self.label_21.setStyleSheet(u"\n"
"\n"
"border-right-color: rgb(233, 236, 239);")
        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(129, 305, 20, 20))
        font7 = QFont()
        font7.setFamilies([u"Times New Roman"])
        font7.setBold(True)
        font7.setItalic(True)
        self.label_22.setFont(font7)
        self.label_22.setStyleSheet(u"color: rgb(0\uff0c0\uff0c0);\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(220, 297, 40, 35))
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setStyleSheet(u"border-image: url(:/background/\u6e29\u5ea6.png);\n"
"border-color: rgb(233, 236, 239);")
        self.rel_sys_comboBox = QComboBox(self.widget)
        self.rel_sys_comboBox.setObjectName(u"rel_sys_comboBox")
        self.rel_sys_comboBox.setGeometry(QRect(20, 350, 135, 30))
        self.rel_sys_comboBox.setFont(font5)
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
        self.label_24.setFont(font6)
        self.label_24.setStyleSheet(u"\n"
"border-right-color: rgb(233, 236, 239);")
        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(220, 346, 40, 35))
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setStyleSheet(u"border-image: url(:/background/\u7cfb\u7efc\u9009\u62e9.png);\n"
"border-color: rgb(233, 236, 239);")
        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(65, 270, 50, 30))
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(u"border-color: rgb(233, 236, 239);")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rel_tim_lineEdiT = QLineEdit(self.widget)
        self.rel_tim_lineEdiT.setObjectName(u"rel_tim_lineEdiT")
        self.rel_tim_lineEdiT.setGeometry(QRect(20, 400, 135, 30))
        self.rel_tim_lineEdiT.setFont(font3)
        self.rel_tim_lineEdiT.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(130, 404, 20, 20))
        self.label_27.setFont(font7)
        self.label_27.setStyleSheet(u"color: rgb(0\uff0c0\uff0c0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_28 = QLabel(self.widget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(160, 407, 61, 16))
        self.label_28.setFont(font6)
        self.label_28.setStyleSheet(u"border-right-color: rgb(233, 236, 239);")
        self.label_29 = QLabel(self.widget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(225, 400, 30, 29))
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setStyleSheet(u"border-image: url(:/background/\u65f6\u95f4.png);\n"
"border-color: rgb(233, 236, 239);")
        self.label_30 = QLabel(self.widget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(50, 440, 81, 30))
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"\n"
"border-color: rgb(233, 236, 239);")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_31 = QLabel(self.widget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(160, 476, 50, 15))
        self.label_31.setFont(font6)
        self.label_31.setStyleSheet(u"border-right-color: rgb(233, 236, 239);")
        self.Them_lineEdit = QLineEdit(self.widget)
        self.Them_lineEdit.setObjectName(u"Them_lineEdit")
        self.Them_lineEdit.setGeometry(QRect(20, 470, 135, 30))
        self.Them_lineEdit.setFont(font3)
        self.Them_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_32 = QLabel(self.widget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(103, 474, 49, 20))
        self.label_32.setFont(font7)
        self.label_32.setStyleSheet(u"color: rgb(0\uff0c0\uff0c0);\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_33 = QLabel(self.widget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(225, 467, 30, 30))
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setStyleSheet(u"border-image: url(:/background/\u70ed\u6d41.png);\n"
"border-color: rgb(233, 236, 239);")
        self.Them_sys_comboBox = QComboBox(self.widget)
        self.Them_sys_comboBox.setObjectName(u"Them_sys_comboBox")
        self.Them_sys_comboBox.setGeometry(QRect(20, 520, 135, 30))
        self.Them_sys_comboBox.setFont(font5)
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
        self.label_34.setFont(font6)
        self.label_34.setStyleSheet(u"border-right-color: rgb(233, 236, 239);")
        self.label_35 = QLabel(self.widget)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(220, 516, 40, 35))
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setStyleSheet(u"border-image: url(:/background/\u7cfb\u7efc\u9009\u62e9.png);\n"
"border-color: rgb(233, 236, 239);")
        self.Them_tim_lineEdit = QLineEdit(self.widget)
        self.Them_tim_lineEdit.setObjectName(u"Them_tim_lineEdit")
        self.Them_tim_lineEdit.setGeometry(QRect(20, 570, 135, 30))
        self.Them_tim_lineEdit.setFont(font3)
        self.Them_tim_lineEdit.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_36 = QLabel(self.widget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(130, 576, 20, 20))
        self.label_36.setFont(font7)
        self.label_36.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(0\uff0c0\uff0c0);")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_37 = QLabel(self.widget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(160, 577, 61, 16))
        self.label_37.setFont(font6)
        self.label_37.setStyleSheet(u"border-right-color: rgb(233, 236, 239);")
        self.label_38 = QLabel(self.widget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(225, 570, 30, 29))
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)
        self.label_38.setStyleSheet(u"border-image: url(:/background/\u65f6\u95f4.png);\n"
"border-color: rgb(233, 236, 239);")
        self.label_39 = QLabel(self.widget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(18, 615, 141, 20))
        self.label_39.setFont(font)
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
        self.label_40.setGeometry(QRect(11, 635, 151, 30))
        self.label_40.setFont(font)
        self.label_40.setStyleSheet(u"border-color: rgb(233, 236, 239);")
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_41 = QLabel(self.widget)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(220, 664, 40, 35))
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        self.label_41.setStyleSheet(u"border-image: url(:/background/\u6676\u4f53\u7f3a\u9677.png);\n"
"border-color: rgb(233, 236, 239);")
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 720, 261, 20))
        self.line.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-right: rgb(233, 236, 239);\n"
"")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.horizontalLayout_8.addWidget(self.widget)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgb(233, 236, 239);\n"
"border-top:1px solid #868e96;\n"
"border-left: 1px solid rgb(173, 181, 189);")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color: rgb(248, 249, 250);\n"
"border: 1px solid rgb(248, 249, 250);")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.verticalLayout_7.addLayout(self.verticalLayout_9)


        self.horizontalLayout_10.addLayout(self.verticalLayout_7)

        self.horizontalLayout_10.setStretch(0, 24)

        self.horizontalLayout_15.addLayout(self.horizontalLayout_10)


        self.horizontalLayout.addWidget(self.widget_5)


        self.horizontalLayout_6.addWidget(self.widget_4)

        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(250, 16777215))
        self.widget_7.setStyleSheet(u"background-color: rgb(248, 249, 250);\n"
"border: 1px solid rgb(248, 249, 250);")
        self.vacan_checkBox_2 = QCheckBox(self.widget_7)
        self.vacan_checkBox_2.setObjectName(u"vacan_checkBox_2")
        self.vacan_checkBox_2.setGeometry(QRect(10, 20, 111, 40))
        sizePolicy.setHeightForWidth(self.vacan_checkBox_2.sizePolicy().hasHeightForWidth())
        self.vacan_checkBox_2.setSizePolicy(sizePolicy)
        font8 = QFont()
        font8.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font8.setPointSize(9)
        font8.setBold(True)
        self.vacan_checkBox_2.setFont(font8)
        self.vacan_checkBox_2.setStyleSheet(u"background-color: #e9ecef;\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);")
        self.label_47 = QLabel(self.widget_7)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(100, 33, 15, 15))
        self.label_47.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius: 5px;")
        self.gap_checkBox_2 = QCheckBox(self.widget_7)
        self.gap_checkBox_2.setObjectName(u"gap_checkBox_2")
        self.gap_checkBox_2.setGeometry(QRect(130, 20, 111, 40))
        sizePolicy.setHeightForWidth(self.gap_checkBox_2.sizePolicy().hasHeightForWidth())
        self.gap_checkBox_2.setSizePolicy(sizePolicy)
        self.gap_checkBox_2.setFont(font8)
        self.gap_checkBox_2.setStyleSheet(u"background-color: #e9ecef;\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);")
        self.label_48 = QLabel(self.widget_7)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(220, 33, 16, 16))
        self.label_48.setStyleSheet(u"background-color: rgb(85, 170, 0);\n"
"border-radius: 5px;")
        self.zon_tem_checkBox_2 = QCheckBox(self.widget_7)
        self.zon_tem_checkBox_2.setObjectName(u"zon_tem_checkBox_2")
        self.zon_tem_checkBox_2.setGeometry(QRect(60, 70, 161, 40))
        sizePolicy.setHeightForWidth(self.zon_tem_checkBox_2.sizePolicy().hasHeightForWidth())
        self.zon_tem_checkBox_2.setSizePolicy(sizePolicy)
        self.zon_tem_checkBox_2.setFont(font8)
        self.zon_tem_checkBox_2.setStyleSheet(u"background-color: #e9ecef;\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 0);")
        icon3 = QIcon()
        icon3.addFile(u":/background/\u53ef\u89c6\u5316.png", QSize(), QIcon.Normal, QIcon.Off)
        self.zon_tem_checkBox_2.setIcon(icon3)
        self.stackedWidget_4 = QStackedWidget(self.widget_7)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.stackedWidget_4.setGeometry(QRect(10, 120, 241, 341))
        self.stackedWidget_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.widget_10 = QWidget(self.page_7)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(0, 20, 240, 250))
        self.widget_10.setStyleSheet(u"border-top-color: rgb(130, 130, 130);\n"
"border-bottom-color: rgb(130, 130, 130);\n"
"border-left-color: rgb(130, 130, 130);")
        self.label_63 = QLabel(self.widget_10)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(77, 10, 80, 20))
        font9 = QFont()
        font9.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font9.setPointSize(11)
        font9.setBold(True)
        self.label_63.setFont(font9)
        self.label_63.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_64 = QLabel(self.widget_10)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(1, 80, 71, 20))
        self.label_64.setFont(font8)
        self.label_64.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_65 = QLabel(self.widget_10)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(180, 50, 50, 20))
        self.label_65.setFont(font8)
        self.label_65.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_65.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_66 = QLabel(self.widget_10)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(1, 130, 101, 20))
        self.label_66.setFont(font8)
        self.label_66.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_67 = QLabel(self.widget_10)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(1, 180, 81, 20))
        self.label_67.setFont(font8)
        self.label_67.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.exp1_ele1_lineEdit_2 = QLineEdit(self.widget_10)
        self.exp1_ele1_lineEdit_2.setObjectName(u"exp1_ele1_lineEdit_2")
        self.exp1_ele1_lineEdit_2.setGeometry(QRect(188, 80, 25, 20))
        self.exp1_ele1_lineEdit_2.setFont(font7)
        self.exp1_ele1_lineEdit_2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp1_ele1_lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp1_ele1_mass_lineEdit_2 = QLineEdit(self.widget_10)
        self.exp1_ele1_mass_lineEdit_2.setObjectName(u"exp1_ele1_mass_lineEdit_2")
        self.exp1_ele1_mass_lineEdit_2.setGeometry(QRect(183, 130, 35, 20))
        self.exp1_ele1_mass_lineEdit_2.setFont(font3)
        self.exp1_ele1_mass_lineEdit_2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp1_ele1_mass_lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp1_ele1_num_lineEdit_2 = QLineEdit(self.widget_10)
        self.exp1_ele1_num_lineEdit_2.setObjectName(u"exp1_ele1_num_lineEdit_2")
        self.exp1_ele1_num_lineEdit_2.setGeometry(QRect(180, 180, 40, 20))
        self.exp1_ele1_num_lineEdit_2.setFont(font3)
        self.exp1_ele1_num_lineEdit_2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp1_ele1_num_lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_68 = QLabel(self.page_7)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(0, 300, 70, 20))
        font10 = QFont()
        font10.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font10.setPointSize(8)
        font10.setBold(True)
        self.label_68.setFont(font10)
        self.label_68.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.exp_res_lineEdit_2 = QLineEdit(self.page_7)
        self.exp_res_lineEdit_2.setObjectName(u"exp_res_lineEdit_2")
        self.exp_res_lineEdit_2.setGeometry(QRect(90, 300, 60, 20))
        self.exp_res_lineEdit_2.setFont(font3)
        self.exp_res_lineEdit_2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp_res_lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_49 = QLabel(self.page_7)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(150, 300, 81, 20))
        self.label_49.setFont(font5)
        self.label_49.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.stackedWidget_4.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.widget_11 = QWidget(self.page_8)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(0, 20, 240, 250))
        self.widget_11.setStyleSheet(u"border-top-color: rgb(130, 130, 130);\n"
"border-bottom-color: rgb(130, 130, 130);\n"
"border-left-color: rgb(130, 130, 130);")
        self.label_69 = QLabel(self.widget_11)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(77, 10, 80, 20))
        self.label_69.setFont(font9)
        self.label_69.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_70 = QLabel(self.widget_11)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(1, 80, 101, 20))
        self.label_70.setFont(font8)
        self.label_70.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_71 = QLabel(self.widget_11)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(180, 50, 50, 20))
        self.label_71.setFont(font8)
        self.label_71.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_71.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_72 = QLabel(self.widget_11)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(1, 130, 111, 20))
        self.label_72.setFont(font8)
        self.label_72.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_73 = QLabel(self.widget_11)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(1, 180, 91, 20))
        self.label_73.setFont(font8)
        self.label_73.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_74 = QLabel(self.widget_11)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(130, 50, 50, 20))
        self.label_74.setFont(font8)
        self.label_74.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_74.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp2_ele1_lineEdit_2 = QLineEdit(self.widget_11)
        self.exp2_ele1_lineEdit_2.setObjectName(u"exp2_ele1_lineEdit_2")
        self.exp2_ele1_lineEdit_2.setGeometry(QRect(143, 80, 25, 20))
        self.exp2_ele1_lineEdit_2.setFont(font7)
        self.exp2_ele1_lineEdit_2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp2_ele1_lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp2_ele2_lineEdit_2 = QLineEdit(self.widget_11)
        self.exp2_ele2_lineEdit_2.setObjectName(u"exp2_ele2_lineEdit_2")
        self.exp2_ele2_lineEdit_2.setGeometry(QRect(188, 80, 25, 20))
        self.exp2_ele2_lineEdit_2.setFont(font7)
        self.exp2_ele2_lineEdit_2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp2_ele2_lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp2_ele1_mass_lineEdit_2 = QLineEdit(self.widget_11)
        self.exp2_ele1_mass_lineEdit_2.setObjectName(u"exp2_ele1_mass_lineEdit_2")
        self.exp2_ele1_mass_lineEdit_2.setGeometry(QRect(139, 130, 35, 20))
        self.exp2_ele1_mass_lineEdit_2.setFont(font3)
        self.exp2_ele1_mass_lineEdit_2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp2_ele1_mass_lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp2_ele2_mass_lineEdit_2 = QLineEdit(self.widget_11)
        self.exp2_ele2_mass_lineEdit_2.setObjectName(u"exp2_ele2_mass_lineEdit_2")
        self.exp2_ele2_mass_lineEdit_2.setGeometry(QRect(183, 130, 35, 20))
        self.exp2_ele2_mass_lineEdit_2.setFont(font3)
        self.exp2_ele2_mass_lineEdit_2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp2_ele2_mass_lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp2_ele1_num_lineEdit_2 = QLineEdit(self.widget_11)
        self.exp2_ele1_num_lineEdit_2.setObjectName(u"exp2_ele1_num_lineEdit_2")
        self.exp2_ele1_num_lineEdit_2.setGeometry(QRect(137, 180, 40, 20))
        self.exp2_ele1_num_lineEdit_2.setFont(font3)
        self.exp2_ele1_num_lineEdit_2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp2_ele1_num_lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exp2_ele2_num_lineEdit_2 = QLineEdit(self.widget_11)
        self.exp2_ele2_num_lineEdit_2.setObjectName(u"exp2_ele2_num_lineEdit_2")
        self.exp2_ele2_num_lineEdit_2.setGeometry(QRect(180, 180, 40, 20))
        self.exp2_ele2_num_lineEdit_2.setFont(font3)
        self.exp2_ele2_num_lineEdit_2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp2_ele2_num_lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_75 = QLabel(self.page_8)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(0, 300, 80, 20))
        self.label_75.setFont(font10)
        self.label_75.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.exp2_reslineEdit_2 = QLineEdit(self.page_8)
        self.exp2_reslineEdit_2.setObjectName(u"exp2_reslineEdit_2")
        self.exp2_reslineEdit_2.setGeometry(QRect(80, 300, 60, 20))
        self.exp2_reslineEdit_2.setFont(font3)
        self.exp2_reslineEdit_2.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.exp2_reslineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_76 = QLabel(self.page_8)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(140, 300, 91, 20))
        self.label_76.setFont(font5)
        self.stackedWidget_4.addWidget(self.page_8)

        self.horizontalLayout_6.addWidget(self.widget_7)

        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMaximumSize(QSize(16777215, 300))
        self.stackedWidget.setFont(font9)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(248, 249, 250);\n"
"border: 1px solid rgb(248, 249, 250);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_3 = QHBoxLayout(self.page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tabWidget = QTabWidget(self.page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font9)
        self.tabWidget.setStyleSheet(u"background-color: rgb(248, 249, 250);\n"
"border: 1px solid rgb(248, 249, 250);\n"
"color: rgb(0, 0, 0);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_13 = QHBoxLayout(self.tab)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout_13.addLayout(self.verticalLayout_2)

        icon4 = QIcon()
        icon4.addFile(u":/background/\u6e29\u5ea6.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_14 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.horizontalLayout_14.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.tab_2, icon4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        icon5 = QIcon()
        icon5.addFile(u":/background/\u58f0\u5b50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon5, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_2 = QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget_2 = QTabWidget(self.page_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setFont(font9)
        self.tabWidget_2.setStyleSheet(u"background-color: rgb(248, 249, 250);\n"
"border: 1px solid rgb(248, 249, 250);")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_12 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.horizontalLayout_12.addLayout(self.verticalLayout_6)

        self.tabWidget_2.addTab(self.tab_4, icon4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.horizontalLayout_9.addLayout(self.verticalLayout_5)

        self.tabWidget_2.addTab(self.tab_5, icon4, "")

        self.horizontalLayout_2.addWidget(self.tabWidget_2)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_5.addWidget(self.stackedWidget)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMaximumSize(QSize(250, 300))
        self.widget_6.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(248, 249, 250);")
        self.start_pushButton = QPushButton(self.widget_6)
        self.start_pushButton.setObjectName(u"start_pushButton")
        self.start_pushButton.setGeometry(QRect(10, 40, 110, 60))
        self.start_pushButton.setFont(font9)
        self.start_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: rgb(165, 216, 255);\n"
"")
        self.pause_pushButton = QPushButton(self.widget_6)
        self.pause_pushButton.setObjectName(u"pause_pushButton")
        self.pause_pushButton.setGeometry(QRect(130, 40, 110, 61))
        self.pause_pushButton.setFont(font9)
        self.pause_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: rgb(153, 233, 242);")
        self.restart_pushButton = QPushButton(self.widget_6)
        self.restart_pushButton.setObjectName(u"restart_pushButton")
        self.restart_pushButton.setGeometry(QRect(10, 140, 110, 60))
        self.restart_pushButton.setFont(font9)
        self.restart_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: rgb(150, 242, 215);")
        self.over_pushButton = QPushButton(self.widget_6)
        self.over_pushButton.setObjectName(u"over_pushButton")
        self.over_pushButton.setGeometry(QRect(130, 140, 110, 60))
        self.over_pushButton.setFont(font9)
        self.over_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: rgb(186, 200, 255);")

        self.horizontalLayout_5.addWidget(self.widget_6)

        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout_7.addLayout(self.verticalLayout)


        self.horizontalLayout_8.addWidget(self.widget_3)

        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 7)

        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 18)

        self.horizontalLayout_11.addLayout(self.verticalLayout_8)


        self.retranslateUi(Form)

        self.sys_stackedWidget.setCurrentIndex(1)
        self.stackedWidget_4.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8f90\u7167\u635f\u4f24\u6838\u6750\u6599\u539f\u5b50\u5c3a\u5ea6\u70ed\u8f93\u8fd0\u53ef\u89c6\u5316\u8f6f\u4ef6", None))
        self.exp1_radioButton.setText(QCoreApplication.translate("Form", u"\u5b9e\u9a8c\u4e00", None))
        self.exp2_radioButton.setText(QCoreApplication.translate("Form", u"\u5b9e\u9a8c\u4e8c", None))
        self.exp1_arg_pushButton.setText(QCoreApplication.translate("Form", u"\u5b9e\u9a8c\u4e00\u63a8\u8350\u53c2\u6570", None))
        self.exp2_arg_pushButton.setText(QCoreApplication.translate("Form", u"\u5b9e\u9a8c\u4e8c\u63a8\u8350\u53c2\u6570", None))
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
        self.label_32.setText(QCoreApplication.translate("Form", u"W/m^2", None))
        self.label_33.setText("")
        self.label_34.setText(QCoreApplication.translate("Form", u"\u7cfb\u7efc", None))
        self.label_35.setText("")
        self.label_36.setText(QCoreApplication.translate("Form", u"ps", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"\u6a21\u62df\u65f6\u95f4", None))
        self.label_38.setText("")
        self.label_39.setText(QCoreApplication.translate("Form", u"\u8f90\u7167\u6a21\u62df\u8bbe\u7f6e", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"\u5f17\u5170\u79d1\u5c14\u7f3a\u9677\u5bf9\u6570", None))
        self.label_41.setText("")
        self.vacan_checkBox_2.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u7a7a\u4f4d", None))
        self.label_47.setText("")
        self.gap_checkBox_2.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u95f4\u9699", None))
        self.label_48.setText("")
        self.zon_tem_checkBox_2.setText(QCoreApplication.translate("Form", u"\u533a\u57df\u6e29\u5ea6\u53ef\u89c6\u5316", None))
        self.label_63.setText(QCoreApplication.translate("Form", u"\u4f53\u7cfb\u53c2\u6570", None))
        self.label_64.setText(QCoreApplication.translate("Form", u"\u5143\u7d20\u79cd\u7c7b", None))
        self.label_65.setText(QCoreApplication.translate("Form", u"\u5143\u7d20\u4e00", None))
        self.label_66.setText(QCoreApplication.translate("Form", u"\u76f8\u5bf9\u539f\u5b50\u8d28\u91cf", None))
        self.label_67.setText(QCoreApplication.translate("Form", u"\u539f\u5b50\u6570\u91cf", None))
        self.label_68.setText(QCoreApplication.translate("Form", u"\u6750\u6599\u70ed\u5bfc\u7387", None))
        self.exp_res_lineEdit_2.setText("")
        self.label_49.setText(QCoreApplication.translate("Form", u"W*K-1*m-1", None))
        self.label_69.setText(QCoreApplication.translate("Form", u"\u4f53\u7cfb\u53c2\u6570", None))
        self.label_70.setText(QCoreApplication.translate("Form", u"\u5143\u7d20\u79cd\u7c7b", None))
        self.label_71.setText(QCoreApplication.translate("Form", u"\u5143\u7d20\u4e8c", None))
        self.label_72.setText(QCoreApplication.translate("Form", u"\u76f8\u5bf9\u539f\u5b50\u8d28\u91cf", None))
        self.label_73.setText(QCoreApplication.translate("Form", u"\u539f\u5b50\u6570\u91cf", None))
        self.label_74.setText(QCoreApplication.translate("Form", u"\u5143\u7d20\u4e00", None))
        self.label_75.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u70ed\u5bfc\u7387", None))
        self.exp2_reslineEdit_2.setText("")
        self.label_76.setText(QCoreApplication.translate("Form", u"W*K-1*m-1", None))
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

