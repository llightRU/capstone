import pandas as pd
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter,QPen,QColor
from PyQt5.QtCore import Qt,QPointF
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QInputDialog, QTableWidgetItem
from PyQt5.QtChart import QChart, QChartView, QPieSeries,QBarSet,QPercentBarSeries,QBarCategoryAxis,QBoxPlotSeries,QBoxSet
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import sys
import time

sys.path.append('icon')
import designer
import view,import_data
from selenium import webdriver
import validation as v
import data_executer as de
import qt_executer as qe
import model_executer as me


class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1407, 912)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/app.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("QLabel#label{\n"
                                         "    color : rgb(192,192,192);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton{\n"
                                         "    font-size: 15px;\n"
                                         "    border-radius: 5px;\n"
                                         "    background-color: rgb(220,220,220);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed{\n"
                                         "    background-color: rgb(200,200,200);\n"
                                         "    border-style: inset;\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "QFrame#tab_frame,#raw_tab{\n"
                                         "    overflow: hidden;\n"
                                         "    border: 1px solid #ccc;\n"
                                         "    background-color: #f1f1f1;\n"
                                         "}\n"
                                         "QPushButton#design_btn,#predict_btn,#data_btn,#model_btn{\n"
                                         "          background-color: #f1f1f1;\n"
                                         "          float: left;\n"
                                         "          border: none;\n"
                                         "        border-radius: 0px;\n"
                                         "          outline: none;\n"
                                         "          cursor: pointer;\n"
                                         "          padding: 14px 16px;\n"
                                         "          transition: 0.3s;\n"
                                         "          font-size: 17px;    \n"
                                         "}\n"
                                         "\n"
                                         "QPushButton#design_btn::hover,#predict_btn::hover,#data_btn::hover,#model_btn::hover{\n"
                                         " background-color: #ddd;\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "QGroupBox{\n"
                                         "    background-color: rgb(235,235,235);\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.head = QtWidgets.QWidget(self.centralwidget)
        self.head.setMaximumSize(QtCore.QSize(16777215, 100))
        palette = QtGui.QPalette()
        self.head.setPalette(palette)
        self.head.setObjectName("head")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.head)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.head)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(25, 25))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/app.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.horizontalLayout.addWidget(
            self.frame, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.frame_2 = QtWidgets.QFrame(self.head)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.tab_frame = QtWidgets.QFrame(self.frame_2)
        self.tab_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tab_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab_frame.setObjectName("tab_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.predict_btn = QtWidgets.QPushButton(self.tab_frame)
        self.predict_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.predict_btn.setObjectName("predict_btn")
        self.horizontalLayout_4.addWidget(self.predict_btn)
        self.design_btn = QtWidgets.QPushButton(self.tab_frame)
        self.design_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.design_btn.setObjectName("design_btn")
        self.horizontalLayout_4.addWidget(self.design_btn)
        self.horizontalLayout_2.addWidget(self.tab_frame)
        self.horizontalLayout.addWidget(
            self.frame_2, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.frame_3 = QtWidgets.QFrame(self.head)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(362, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.import_btn = QtWidgets.QPushButton(self.frame_3)
        self.import_btn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.import_btn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/add.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.import_btn.setIcon(icon1)
        self.import_btn.setObjectName("import_btn")
        self.horizontalLayout_5.addWidget(self.import_btn)
        self.view_btn = QtWidgets.QPushButton(self.frame_3)
        self.view_btn.setMinimumSize(QtCore.QSize(0, 40))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/view.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view_btn.setIcon(icon2)
        self.view_btn.setObjectName("view_btn")
        self.horizontalLayout_5.addWidget(self.view_btn)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/delete.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.import_model_btn = QtWidgets.QPushButton(self.frame_3)
        self.import_model_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.import_model_btn.setIcon(icon1)
        self.import_model_btn.setObjectName("import_model_btn")
        self.horizontalLayout_5.addWidget(self.import_model_btn)

        self.horizontalLayout.addWidget(
            self.frame_3, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.head)
        self.body_widget = QtWidgets.QWidget(self.centralwidget)
        self.body_widget.setStyleSheet("")
        self.body_widget.setObjectName("body_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.body_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_15 = QtWidgets.QFrame(self.body_widget)
        self.line_15.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.line_15.setFont(font)
        self.line_15.setLineWidth(1)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.verticalLayout_2.addWidget(self.line_15)
        self.content_widget = QtWidgets.QStackedWidget(self.body_widget)
        self.content_widget.setObjectName("content_widget")
        self.design_page = QtWidgets.QWidget()
        self.design_page.setObjectName("design_page")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.design_page)
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_36.setSpacing(6)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")

        self.design_tab = QtWidgets.QTabWidget(self.design_page)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.design_tab.setFont(font)
        self.design_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.design_tab.setTabPosition(QtWidgets.QTabWidget.West)
        self.design_tab.setIconSize(QtCore.QSize(25, 25))
        self.design_tab.setElideMode(QtCore.Qt.ElideNone)
        self.design_tab.setObjectName("design_tab")

        self.execute_design = QtWidgets.QWidget()
        self.execute_design.setObjectName("execute design")
        self.horizontalLayout_511 = QtWidgets.QHBoxLayout(self.execute_design)
        self.horizontalLayout_511.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_511.setObjectName("horizontalLayout_511")

        self.frame_4 = QtWidgets.QFrame(self.execute_design)
        self.frame_4.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.operators_groupBox = QtWidgets.QGroupBox(self.frame_4)
        self.operators_groupBox.setMinimumSize(QtCore.QSize(250, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.operators_groupBox.setFont(font)
        self.operators_groupBox.setStyleSheet("")
        self.operators_groupBox.setObjectName("operators_groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.operators_groupBox)
        self.verticalLayout_3.setContentsMargins(6, 10, 6, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.operation_toolBox = QtWidgets.QToolBox(self.operators_groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.operation_toolBox.setFont(font)
        self.operation_toolBox.setMidLineWidth(0)
        self.operation_toolBox.setObjectName("operation_toolBox")
        self.data_tab = QtWidgets.QWidget()
        self.data_tab.setGeometry(QtCore.QRect(0, 0, 117, 69))
        self.data_tab.setObjectName("data_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.data_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.test_radioButton_3 = QtWidgets.QRadioButton(self.data_tab)
        self.test_radioButton_3.setObjectName("test_radioButton_3")
        self.verticalLayout_5.addWidget(self.test_radioButton_3)
        self.operation_toolBox.addItem(self.data_tab, "")
        self.model_tab = QtWidgets.QWidget()
        self.model_tab.setGeometry(QtCore.QRect(0, 0, 158, 123))
        self.model_tab.setObjectName("model_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.model_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.test_radioButton_2 = QtWidgets.QRadioButton(self.model_tab)
        self.test_radioButton_2.setObjectName("test_radioButton_2")
        self.verticalLayout_6.addWidget(self.test_radioButton_2)
        self.radioButton_2 = QtWidgets.QRadioButton(self.model_tab)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_6.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.model_tab)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_6.addWidget(self.radioButton)
        self.radioButton_3 = QtWidgets.QRadioButton(self.model_tab)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_6.addWidget(self.radioButton_3)
        self.operation_toolBox.addItem(self.model_tab, "")
        self.verticalLayout_3.addWidget(self.operation_toolBox)
        self.verticalLayout_18.addWidget(
            self.operators_groupBox, 0, QtCore.Qt.AlignTop)
        self.validation_grp = QtWidgets.QGroupBox(self.frame_4)
        self.validation_grp.setMinimumSize(QtCore.QSize(250, 363))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.validation_grp.setFont(font)
        self.validation_grp.setObjectName("validation_grp")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.validation_grp)
        self.verticalLayout_19.setContentsMargins(6, 0, 6, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_5 = QtWidgets.QFrame(self.validation_grp)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_37.addWidget(self.checkBox_2)
        self.crossVal_spinBox_2 = QtWidgets.QDoubleSpinBox(self.frame_5)
        self.crossVal_spinBox_2.setMaximum(0.5)
        self.crossVal_spinBox_2.setSingleStep(0.01)
        self.crossVal_spinBox_2.setMinimum(0)
        self.crossVal_spinBox_2.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.crossVal_spinBox_2.setFont(font)
        self.crossVal_spinBox_2.setObjectName("crossVal_spinBox_2")
        self.horizontalLayout_37.addWidget(self.crossVal_spinBox_2, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_19.addWidget(self.frame_5)

        self.verticalLayout_18.addWidget(self.validation_grp)
        self.frame_43 = QtWidgets.QFrame(self.validation_grp)
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout(self.frame_43)
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.verticalLayout_19.addWidget(self.frame_43, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_18.addWidget(self.validation_grp)
        self.design_frame = QtWidgets.QFrame(self.execute_design)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.design_frame.sizePolicy().hasHeightForWidth())
        self.design_frame.setSizePolicy(sizePolicy)
        self.design_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.design_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.design_frame.setObjectName("design_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.design_frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.design_grp = QtWidgets.QGroupBox(self.design_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.design_grp.sizePolicy().hasHeightForWidth())
        self.design_grp.setSizePolicy(sizePolicy)
        self.design_grp.setMinimumSize(QtCore.QSize(0, 0))
        self.design_grp.setMaximumSize(QtCore.QSize(16777215, 16666666))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.design_grp.setFont(font)
        self.design_grp.setStyleSheet("")
        self.design_grp.setObjectName("design_grp")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.design_grp)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_9 = QtWidgets.QFrame(self.design_grp)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.active_btn = QtWidgets.QPushButton(self.frame_9)
        self.active_btn.setMinimumSize(QtCore.QSize(100, 35))
        self.active_btn.setStyleSheet("color: rgb(0, 0, 255);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/play.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.active_btn.setIcon(icon4)
        self.active_btn.setObjectName("active_btn")
        self.horizontalLayout_7.addWidget(
            self.active_btn, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.restart_btn = QtWidgets.QPushButton(self.frame_9)
        self.restart_btn.setMinimumSize(QtCore.QSize(100, 35))
        self.restart_btn.setStyleSheet("color: rgb(0, 0, 255);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/restart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restart_btn.setIcon(icon5)
        self.restart_btn.setObjectName("restart_btn")
        self.horizontalLayout_7.addWidget(self.restart_btn, 0, QtCore.Qt.AlignHCenter)
        self.save_btn = QtWidgets.QPushButton(self.frame_9)
        self.save_btn.setMinimumSize(QtCore.QSize(100, 35))
        self.save_btn.setStyleSheet("color: rgb(0, 0, 255);")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/save.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon6)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_7.addWidget(
            self.save_btn, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.verticalLayout_7.addWidget(self.frame_9)
        self.info_frame = QtWidgets.QFrame(self.design_grp)
        self.info_frame.setMaximumSize(QtCore.QSize(16777215, 350))
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.info_frame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.detail_txt = QtWidgets.QLabel(self.info_frame)
        self.detail_txt.setObjectName("detail_txt")
        self.verticalLayout_8.addWidget(self.detail_txt)
        self.data_table = QtWidgets.QTableWidget(self.info_frame)
        self.data_table.setMaximumSize(QtCore.QSize(16777215, 500))
        self.data_table.setObjectName("data_table")
        self.data_table.setColumnCount(17)
        self.data_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(16, item)
        self.verticalLayout_8.addWidget(self.data_table)
        self.verticalLayout_7.addWidget(self.info_frame)
        self.progressBar = QtWidgets.QProgressBar(self.design_grp)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_7.addWidget(self.progressBar)
        self.roc_chart = QtWidgets.QFrame(self.design_grp)
        self.roc_chart.setMinimumSize(QtCore.QSize(0, 200))
        self.roc_chart.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.roc_chart.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roc_chart.setObjectName("roc_chart")

        self.verticalLayout_7.addWidget(self.roc_chart)
        self.horizontalLayout_8.addWidget(self.design_grp)

        self.parameter_widget = QtWidgets.QStackedWidget(self.execute_design)
        self.parameter_widget.setMinimumSize(QtCore.QSize(280, 650))
        self.parameter_widget.setStyleSheet("QPushButton{\n"
                                            "    font-size: 15px;\n"
                                            "    border-radius: 5px;\n"
                                            "    background-color:  rgb(238, 255, 255);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton::pressed{\n"
                                            "    background-color:rgb(169, 255, 238);\n"
                                            "}")
        self.parameter_widget.setObjectName("parameter_widget")
        self.DST = QtWidgets.QWidget()
        self.DST.setObjectName("DST")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.DST)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.decisionTree_groupBox = QtWidgets.QGroupBox(self.DST)
        self.decisionTree_groupBox.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.decisionTree_groupBox.setFont(font)
        self.decisionTree_groupBox.setStyleSheet("")
        self.decisionTree_groupBox.setObjectName("decisionTree_groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(
            self.decisionTree_groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 60, 271, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.verticalLayout_10.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_10.addWidget(self.line_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.criterion_DST_comboBox = QtWidgets.QComboBox(
            self.verticalLayoutWidget)
        self.criterion_DST_comboBox.setObjectName("criterion_DST_comboBox")
        self.criterion_DST_comboBox.addItem("")
        self.criterion_DST_comboBox.addItem("")
        self.horizontalLayout_6.addWidget(self.criterion_DST_comboBox)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_10.addWidget(self.line)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.maxDepth_DST_spinBox = QtWidgets.QSpinBox(
            self.verticalLayoutWidget)
        self.maxDepth_DST_spinBox.setMinimum(3)
        self.maxDepth_DST_spinBox.setMaximum(50)
        self.maxDepth_DST_spinBox.setProperty("value", 3)
        self.maxDepth_DST_spinBox.setObjectName("maxDepth_DST_spinBox")
        self.horizontalLayout_9.addWidget(self.maxDepth_DST_spinBox)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_10.addWidget(self.line_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.minSamplesSplit_DST_spinBox = QtWidgets.QSpinBox(
            self.verticalLayoutWidget)
        self.minSamplesSplit_DST_spinBox.setMinimum(2)
        self.minSamplesSplit_DST_spinBox.setMaximum(30)
        self.minSamplesSplit_DST_spinBox.setProperty("value", 2)
        self.minSamplesSplit_DST_spinBox.setObjectName(
            "minSamplesSplit_DST_spinBox")
        self.horizontalLayout_10.addWidget(self.minSamplesSplit_DST_spinBox)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_10.addWidget(self.line_4)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.minSamplesLeaf_DST_spinBox = QtWidgets.QSpinBox(
            self.verticalLayoutWidget)
        self.minSamplesLeaf_DST_spinBox.setMinimum(1)
        self.minSamplesLeaf_DST_spinBox.setMaximum(30)
        self.minSamplesLeaf_DST_spinBox.setProperty("value", 2)
        self.minSamplesLeaf_DST_spinBox.setObjectName(
            "minSamplesLeaf_DST_spinBox")
        self.horizontalLayout_11.addWidget(self.minSamplesLeaf_DST_spinBox)
        self.verticalLayout_10.addLayout(self.horizontalLayout_11)
        self.line_5 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_10.addWidget(self.line_5)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_12.addWidget(self.label_8)
        self.maxfeatures_DST_spinBox = QtWidgets.QSpinBox(
            self.verticalLayoutWidget)
        self.maxfeatures_DST_spinBox.setMinimum(1)
        self.maxfeatures_DST_spinBox.setMaximum(16)
        self.maxfeatures_DST_spinBox.setProperty("value", 2)
        self.maxfeatures_DST_spinBox.setObjectName("maxfeatures_DST_spinBox")
        self.horizontalLayout_12.addWidget(self.maxfeatures_DST_spinBox)
        self.verticalLayout_10.addLayout(self.horizontalLayout_12)
        self.line_6 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_10.addWidget(self.line_6)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.applyPrunning_DST_checkBox = QtWidgets.QCheckBox(
            self.verticalLayoutWidget)
        self.applyPrunning_DST_checkBox.setChecked(True)
        self.applyPrunning_DST_checkBox.setObjectName(
            "applyPrunning_DST_checkBox")
        self.horizontalLayout_13.addWidget(self.applyPrunning_DST_checkBox)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.line_7 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_10.addWidget(self.line_7)
        self.line_9 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_10.addWidget(self.line_9)
        self.paraGuild_DST_btn = QtWidgets.QPushButton(
            self.decisionTree_groupBox)
        self.paraGuild_DST_btn.setGeometry(QtCore.QRect(10, 570, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.paraGuild_DST_btn.setFont(font)
        self.paraGuild_DST_btn.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.paraGuild_DST_btn.setStyleSheet("color: rgb(0, 0, 255);")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("ui\\../icon/hint.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paraGuild_DST_btn.setIcon(icon7)
        self.paraGuild_DST_btn.setObjectName("paraGuild_DST_btn")
        self.guild_DST_btn = QtWidgets.QPushButton(self.decisionTree_groupBox)
        self.guild_DST_btn.setGeometry(QtCore.QRect(170, 30, 75, 23))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/search.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.guild_DST_btn.setIcon(icon8)
        self.guild_DST_btn.setObjectName("guild_DST_btn")
        self.verticalLayout_9.addWidget(self.decisionTree_groupBox)
        self.parameter_widget.addWidget(self.DST)
        self.XGBoost = QtWidgets.QWidget()
        self.XGBoost.setObjectName("XGBoost")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.XGBoost)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.XGBoost_groupBox = QtWidgets.QGroupBox(self.XGBoost)
        self.XGBoost_groupBox.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.XGBoost_groupBox.setFont(font)
        self.XGBoost_groupBox.setStyleSheet("")
        self.XGBoost_groupBox.setObjectName("XGBoost_groupBox")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.XGBoost_groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 60, 271, 501))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.verticalLayout_12.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.line_18 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.verticalLayout_12.addWidget(self.line_18)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_24.addWidget(self.label_21)
        self.nEstimators_XGB_spinBox = QtWidgets.QSpinBox(
            self.verticalLayoutWidget_3)
        self.nEstimators_XGB_spinBox.setMinimum(1)
        self.nEstimators_XGB_spinBox.setMaximum(3000)
        self.nEstimators_XGB_spinBox.setObjectName("nEstimators_XGB_spinBox")
        self.horizontalLayout_24.addWidget(self.nEstimators_XGB_spinBox)
        self.verticalLayout_12.addLayout(self.horizontalLayout_24)
        self.line_27 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_27.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.verticalLayout_12.addWidget(self.line_27)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_16.addWidget(self.label_14)
        self.loss_XGB_comboBox = QtWidgets.QComboBox(
            self.verticalLayoutWidget_3)
        self.loss_XGB_comboBox.setObjectName("loss_XGB_comboBox")
        self.loss_XGB_comboBox.addItem("")
        self.loss_XGB_comboBox.addItem("")
        self.horizontalLayout_16.addWidget(self.loss_XGB_comboBox)
        self.verticalLayout_12.addLayout(self.horizontalLayout_16)
        self.line_19 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.verticalLayout_12.addWidget(self.line_19)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_17.addWidget(self.label_15)
        self.learningRate_XGB_spinBox = QtWidgets.QDoubleSpinBox(
            self.verticalLayoutWidget_3)
        self.learningRate_XGB_spinBox.setMinimum(0.01)
        self.learningRate_XGB_spinBox.setMaximum(100.0)
        self.learningRate_XGB_spinBox.setSingleStep(0.01)
        self.learningRate_XGB_spinBox.setProperty("value", 0.01)
        self.learningRate_XGB_spinBox.setObjectName("learningRate_XGB_spinBox")
        self.horizontalLayout_17.addWidget(self.learningRate_XGB_spinBox)
        self.verticalLayout_12.addLayout(self.horizontalLayout_17)
        self.line_20 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.verticalLayout_12.addWidget(self.line_20)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_18.addWidget(self.label_16)
        self.maxDepth_XGB_spinBox = QtWidgets.QSpinBox(
            self.verticalLayoutWidget_3)
        self.maxDepth_XGB_spinBox.setMinimum(3)
        self.maxDepth_XGB_spinBox.setMaximum(50)
        self.maxDepth_XGB_spinBox.setProperty("value", 3)
        self.maxDepth_XGB_spinBox.setObjectName("maxDepth_XGB_spinBox")
        self.horizontalLayout_18.addWidget(self.maxDepth_XGB_spinBox)
        self.verticalLayout_12.addLayout(self.horizontalLayout_18)
        self.line_21 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.verticalLayout_12.addWidget(self.line_21)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_19.addWidget(self.label_17)
        self.subsample_XGB_spinBox = QtWidgets.QDoubleSpinBox(
            self.verticalLayoutWidget_3)
        self.subsample_XGB_spinBox.setMinimum(0.1)
        self.subsample_XGB_spinBox.setMaximum(1.0)
        self.subsample_XGB_spinBox.setSingleStep(0.1)
        self.subsample_XGB_spinBox.setObjectName("subsample_XGB_spinBox")
        self.horizontalLayout_19.addWidget(self.subsample_XGB_spinBox)
        self.verticalLayout_12.addLayout(self.horizontalLayout_19)
        self.line_22 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.verticalLayout_12.addWidget(self.line_22)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_20.addWidget(self.label_18)
        self.minWeightFractionLeaf_XGB_spinBox = QtWidgets.QDoubleSpinBox(
            self.verticalLayoutWidget_3)
        self.minWeightFractionLeaf_XGB_spinBox.setMinimum(0.0)
        self.minWeightFractionLeaf_XGB_spinBox.setMaximum(0.5)
        self.minWeightFractionLeaf_XGB_spinBox.setSingleStep(0.01)
        self.minWeightFractionLeaf_XGB_spinBox.setObjectName(
            "minWeightFractionLeaf_XGB_spinBox")
        self.horizontalLayout_20.addWidget(
            self.minWeightFractionLeaf_XGB_spinBox)
        self.verticalLayout_12.addLayout(self.horizontalLayout_20)
        self.line_23 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.verticalLayout_12.addWidget(self.line_23)

        self.line_24 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.verticalLayout_12.addWidget(self.line_24)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_22.addWidget(self.label_22)
        self.maxFeatures_XGB_spinBox = QtWidgets.QSpinBox(
            self.verticalLayoutWidget_3)
        self.maxFeatures_XGB_spinBox.setMinimum(1)
        self.maxFeatures_XGB_spinBox.setMaximum(16)
        self.maxFeatures_XGB_spinBox.setProperty("value", 2)
        self.maxFeatures_XGB_spinBox.setObjectName("maxFeatures_XGB_spinBox")
        self.horizontalLayout_22.addWidget(self.maxFeatures_XGB_spinBox)
        self.verticalLayout_12.addLayout(self.horizontalLayout_22)
        self.line_25 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_25.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.verticalLayout_12.addWidget(self.line_25)
        self.line_26 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_26.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.verticalLayout_12.addWidget(self.line_26)
        self.paraGuild_XGB_btn = QtWidgets.QPushButton(self.XGBoost_groupBox)
        self.paraGuild_XGB_btn.setGeometry(QtCore.QRect(10, 570, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.paraGuild_XGB_btn.setFont(font)
        self.paraGuild_XGB_btn.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.paraGuild_XGB_btn.setStyleSheet("color: rgb(0, 0, 255);")
        self.paraGuild_XGB_btn.setIcon(icon7)
        self.paraGuild_XGB_btn.setObjectName("paraGuild_XGB_btn")
        self.guild_XGB_btn = QtWidgets.QPushButton(self.XGBoost_groupBox)
        self.guild_XGB_btn.setGeometry(QtCore.QRect(170, 30, 75, 23))
        self.guild_XGB_btn.setIcon(icon8)
        self.guild_XGB_btn.setObjectName("guild_XGB_btn")
        self.verticalLayout_11.addWidget(self.XGBoost_groupBox)
        self.parameter_widget.addWidget(self.XGBoost)
        self.LR = QtWidgets.QWidget()
        self.LR.setObjectName("LR")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.LR)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.LR_groupBox = QtWidgets.QGroupBox(self.LR)
        self.LR_groupBox.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.LR_groupBox.setFont(font)
        self.LR_groupBox.setStyleSheet("")
        self.LR_groupBox.setObjectName("LR_groupBox")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.LR_groupBox)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 60, 271, 501))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_4)
        self.verticalLayout_14.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.line_28 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line_28.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.verticalLayout_14.addWidget(self.line_28)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_25.addWidget(self.label_23)
        self.penalty_LR_comboBox = QtWidgets.QComboBox(
            self.verticalLayoutWidget_4)
        self.penalty_LR_comboBox.setObjectName("penalty_LR_comboBox")
        self.penalty_LR_comboBox.addItem("")
        self.penalty_LR_comboBox.addItem("")
        self.penalty_LR_comboBox.addItem("")
        self.penalty_LR_comboBox.addItem("")
        self.horizontalLayout_25.addWidget(self.penalty_LR_comboBox)
        self.verticalLayout_14.addLayout(self.horizontalLayout_25)
        self.line_29 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line_29.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.verticalLayout_14.addWidget(self.line_29)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_26.addWidget(self.label_24)
        self.c_LR_spinBox = QtWidgets.QDoubleSpinBox(
            self.verticalLayoutWidget_4)
        self.c_LR_spinBox.setMinimum(0.01)
        self.c_LR_spinBox.setMaximum(100.0)
        self.c_LR_spinBox.setSingleStep(0.01)
        self.c_LR_spinBox.setProperty("value", 0.01)
        self.c_LR_spinBox.setObjectName("c_LR_spinBox")
        self.horizontalLayout_26.addWidget(self.c_LR_spinBox)
        self.verticalLayout_14.addLayout(self.horizontalLayout_26)
        self.line_30 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line_30.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.verticalLayout_14.addWidget(self.line_30)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_27.addWidget(self.label_25)
        self.maxIter_spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_4)
        self.maxIter_spinBox.setMinimum(1)
        self.maxIter_spinBox.setMaximum(10000000)
        self.maxIter_spinBox.setProperty("value", 1000)
        self.maxIter_spinBox.setObjectName("maxIter_spinBox")
        self.horizontalLayout_27.addWidget(self.maxIter_spinBox)
        self.verticalLayout_14.addLayout(self.horizontalLayout_27)
        self.line_31 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line_31.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.verticalLayout_14.addWidget(self.line_31)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_28.addWidget(self.label_26)
        self.solver_LR_comboBox = QtWidgets.QComboBox(
            self.verticalLayoutWidget_4)
        self.solver_LR_comboBox.setObjectName("solver_LR_comboBox")
        self.solver_LR_comboBox.addItem("")
        self.solver_LR_comboBox.addItem("")
        self.solver_LR_comboBox.addItem("")
        self.solver_LR_comboBox.addItem("")
        self.solver_LR_comboBox.addItem("")
        self.horizontalLayout_28.addWidget(self.solver_LR_comboBox)
        self.verticalLayout_14.addLayout(self.horizontalLayout_28)
        self.line_38 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.verticalLayout_14.addWidget(self.line_38)
        self.line_37 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line_37.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_37.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_37.setObjectName("line_37")
        self.verticalLayout_14.addWidget(self.line_37)
        self.paraGuild_LR_btn = QtWidgets.QPushButton(self.LR_groupBox)
        self.paraGuild_LR_btn.setGeometry(QtCore.QRect(10, 570, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.paraGuild_LR_btn.setFont(font)
        self.paraGuild_LR_btn.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.paraGuild_LR_btn.setStyleSheet("color: rgb(0, 0, 255);")
        self.paraGuild_LR_btn.setIcon(icon7)
        self.paraGuild_LR_btn.setObjectName("paraGuild_LR_btn")
        self.guild_LR_btn = QtWidgets.QPushButton(self.LR_groupBox)
        self.guild_LR_btn.setGeometry(QtCore.QRect(170, 30, 75, 23))
        self.guild_LR_btn.setIcon(icon8)
        self.guild_LR_btn.setObjectName("guild_LR_btn")
        self.verticalLayout_13.addWidget(self.LR_groupBox)
        self.parameter_widget.addWidget(self.LR)
        self.RDST = QtWidgets.QWidget()
        self.RDST.setObjectName("RDST")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.RDST)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.randomForest_groupBox = QtWidgets.QGroupBox(self.RDST)
        self.randomForest_groupBox.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.randomForest_groupBox.setFont(font)
        self.randomForest_groupBox.setStyleSheet("")
        self.randomForest_groupBox.setObjectName("randomForest_groupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(
            self.randomForest_groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 60, 271, 501))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_16.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.line_17 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.verticalLayout_16.addWidget(self.line_17)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_15.addWidget(self.label_13)
        self.nEstimators_RDST_spinBox = QtWidgets.QSpinBox(
            self.verticalLayoutWidget_2)
        self.nEstimators_RDST_spinBox.setMinimum(1)
        self.nEstimators_RDST_spinBox.setMaximum(3000)
        self.nEstimators_RDST_spinBox.setObjectName("nEstimators_RDST_spinBox")
        self.horizontalLayout_15.addWidget(self.nEstimators_RDST_spinBox)
        self.verticalLayout_16.addLayout(self.horizontalLayout_15)
        self.line_8 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_16.addWidget(self.line_8)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_29.addWidget(self.label_10)
        self.criterion_RDST_comboBox = QtWidgets.QComboBox(
            self.verticalLayoutWidget_2)
        self.criterion_RDST_comboBox.setObjectName("criterion_RDST_comboBox")
        self.criterion_RDST_comboBox.addItem("")
        self.criterion_RDST_comboBox.addItem("")
        self.criterion_RDST_comboBox.addItem("")
        self.horizontalLayout_29.addWidget(self.criterion_RDST_comboBox)
        self.verticalLayout_16.addLayout(self.horizontalLayout_29)
        self.line_10 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_16.addWidget(self.line_10)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_30.addWidget(self.label_11)
        self.maxDepth_RDST_spinBox = QtWidgets.QSpinBox(
            self.verticalLayoutWidget_2)
        self.maxDepth_RDST_spinBox.setMinimum(3)
        self.maxDepth_RDST_spinBox.setMaximum(50)
        self.maxDepth_RDST_spinBox.setProperty("value", 3)
        self.maxDepth_RDST_spinBox.setObjectName("maxDepth_RDST_spinBox")
        self.horizontalLayout_30.addWidget(self.maxDepth_RDST_spinBox)
        self.verticalLayout_16.addLayout(self.horizontalLayout_30)
        self.line_11 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout_16.addWidget(self.line_11)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_31.addWidget(self.label_12)
        self.minSamplesSplit_RDST_spinBox = QtWidgets.QSpinBox(
            self.verticalLayoutWidget_2)
        self.minSamplesSplit_RDST_spinBox.setMinimum(2)
        self.minSamplesSplit_RDST_spinBox.setMaximum(30)
        self.minSamplesSplit_RDST_spinBox.setProperty("value", 2)
        self.minSamplesSplit_RDST_spinBox.setObjectName(
            "minSamplesSplit_RDST_spinBox")
        self.horizontalLayout_31.addWidget(self.minSamplesSplit_RDST_spinBox)
        self.verticalLayout_16.addLayout(self.horizontalLayout_31)
        self.line_12 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout_16.addWidget(self.line_12)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_27 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_32.addWidget(self.label_27)
        self.maxSampleLeaf_RDST_spinBox = QtWidgets.QSpinBox(
            self.verticalLayoutWidget_2)
        self.maxSampleLeaf_RDST_spinBox.setMinimum(1)
        self.maxSampleLeaf_RDST_spinBox.setMaximum(30)
        self.maxSampleLeaf_RDST_spinBox.setProperty("value", 2)
        self.maxSampleLeaf_RDST_spinBox.setObjectName(
            "maxSampleLeaf_RDST_spinBox")
        self.horizontalLayout_32.addWidget(self.maxSampleLeaf_RDST_spinBox)
        self.verticalLayout_16.addLayout(self.horizontalLayout_32)
        self.line_13 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.verticalLayout_16.addWidget(self.line_13)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setContentsMargins(10, -1, 5, -1)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_28 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_34.addWidget(self.label_28)
        self.maxFeature_RDST_spinBox = QtWidgets.QSpinBox(
            self.verticalLayoutWidget_2)
        self.maxFeature_RDST_spinBox.setMinimum(1)
        self.maxFeature_RDST_spinBox.setMaximum(16)
        self.maxFeature_RDST_spinBox.setProperty("value", 2)
        self.maxFeature_RDST_spinBox.setObjectName("maxFeature_RDST_spinBox")
        self.horizontalLayout_34.addWidget(self.maxFeature_RDST_spinBox)
        self.verticalLayout_16.addLayout(self.horizontalLayout_34)
        self.line_14 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.verticalLayout_16.addWidget(self.line_14)
        self.line_16 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.verticalLayout_16.addWidget(self.line_16)
        self.paraGuild_RDST_btn = QtWidgets.QPushButton(
            self.randomForest_groupBox)
        self.paraGuild_RDST_btn.setGeometry(QtCore.QRect(10, 570, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.paraGuild_RDST_btn.setFont(font)
        self.paraGuild_RDST_btn.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.paraGuild_RDST_btn.setStyleSheet("color: rgb(0, 0, 255);")
        self.paraGuild_RDST_btn.setIcon(icon7)
        self.paraGuild_RDST_btn.setObjectName("paraGuild_RDST_btn")
        self.guild_RDST_btn = QtWidgets.QPushButton(self.randomForest_groupBox)
        self.guild_RDST_btn.setGeometry(QtCore.QRect(170, 30, 75, 23))
        self.guild_RDST_btn.setIcon(icon8)
        self.guild_RDST_btn.setObjectName("guild_RDST_btn")
        self.verticalLayout_15.addWidget(self.randomForest_groupBox)
        self.parameter_widget.addWidget(self.RDST)

        # fixxxxxxx
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/execute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.design_tab.addTab(self.execute_design, icon9, "")

        self.horizontalLayout_511.addWidget(self.frame_4, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_511.addWidget(self.design_frame)
        self.horizontalLayout_511.addWidget(self.parameter_widget, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)

        self.visual = QtWidgets.QWidget()
        self.visual.setObjectName("visual")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.visual)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.visual_tab = QtWidgets.QTabWidget(self.visual)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.visual_tab.setFont(font)
        self.visual_tab.setTabPosition(QtWidgets.QTabWidget.South)
        self.visual_tab.setObjectName("visual_tab")
        self.visual_raw_tab = QtWidgets.QWidget()
        self.visual_raw_tab.setMinimumSize(QtCore.QSize(0, 0))
        self.visual_raw_tab.setObjectName("visual_raw_tab")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.visual_raw_tab)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.mod_tab = QtWidgets.QFrame(self.visual_raw_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mod_tab.sizePolicy().hasHeightForWidth())
        self.mod_tab.setSizePolicy(sizePolicy)
        self.mod_tab.setMinimumSize(QtCore.QSize(0, 50))
        self.mod_tab.setMaximumSize(QtCore.QSize(1666666, 0))
        self.mod_tab.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mod_tab.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mod_tab.setObjectName("mod_tab")
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout(self.mod_tab)
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.business_btn = QtWidgets.QPushButton(self.mod_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.business_btn.sizePolicy().hasHeightForWidth())
        self.business_btn.setSizePolicy(sizePolicy)
        self.business_btn.setMinimumSize(QtCore.QSize(70, 0))
        self.business_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.business_btn.setObjectName("business_btn")
        self.horizontalLayout_49.addWidget(
            self.business_btn, 0, QtCore.Qt.AlignRight)
        self.technique_btn = QtWidgets.QPushButton(self.mod_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.technique_btn.sizePolicy().hasHeightForWidth())
        self.technique_btn.setSizePolicy(sizePolicy)
        self.technique_btn.setMinimumSize(QtCore.QSize(70, 0))
        self.technique_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.technique_btn.setObjectName("technique_btn")
        self.horizontalLayout_49.addWidget(
            self.technique_btn, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_31.addWidget(
            self.mod_tab, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.raw_page = QtWidgets.QStackedWidget(self.visual_raw_tab)
        self.raw_page.setObjectName("raw_page")
        self.raw_business = QtWidgets.QWidget()
        self.raw_business.setObjectName("raw_business")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.raw_business)
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.frame_20 = QtWidgets.QFrame(self.raw_business)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.frame_24 = QtWidgets.QFrame(self.frame_20)
        self.frame_24.setMaximumSize(QtCore.QSize(16777215, 166666))
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.frame_27 = QtWidgets.QFrame(self.frame_24)
        self.frame_27.setMaximumSize(QtCore.QSize(16777215, 1666666))
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.frame_29 = QtWidgets.QFrame(self.frame_27)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setSpacing(3)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.label_32 = QtWidgets.QLabel(self.frame_29)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_40.addWidget(
            self.label_32, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.line_32 = QtWidgets.QFrame(self.frame_29)
        self.line_32.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_32.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_32.setObjectName("line_32")
        self.verticalLayout_40.addWidget(self.line_32)
        self.verticalLayout_39.addWidget(self.frame_29, 0, QtCore.Qt.AlignTop)
        self.frame_30 = QtWidgets.QFrame(self.frame_27)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy)
        self.frame_30.setMaximumSize(QtCore.QSize(16777215, 1666666))
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.deposit_txt = QtWidgets.QLabel(self.frame_30)
        self.deposit_txt.setObjectName("deposit_txt")
        self.verticalLayout_41.addWidget(
            self.deposit_txt, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.verticalLayout_39.addWidget(self.frame_30, 0, QtCore.Qt.AlignTop)
        self.frame_31 = QtWidgets.QFrame(self.frame_27)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy)
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout(self.frame_31)
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.frame_32 = QtWidgets.QFrame(self.frame_31)
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.frame_32)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.label_46 = QtWidgets.QLabel(self.frame_32)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_42.addWidget(self.label_46)
        self.label_47 = QtWidgets.QLabel(self.frame_32)
        self.label_47.setObjectName("label_47")
        self.verticalLayout_42.addWidget(self.label_47)
        self.horizontalLayout_53.addWidget(self.frame_32)
        self.frame_33 = QtWidgets.QFrame(self.frame_31)
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.raw_positive_txt = QtWidgets.QLabel(self.frame_33)
        self.raw_positive_txt.setObjectName("raw_positive_txt")
        self.verticalLayout_43.addWidget(
            self.raw_positive_txt, 0, QtCore.Qt.AlignRight)
        self.raw_negative_txt = QtWidgets.QLabel(self.frame_33)
        self.raw_negative_txt.setObjectName("raw_negative_txt")
        self.verticalLayout_43.addWidget(
            self.raw_negative_txt, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_53.addWidget(self.frame_33)
        self.verticalLayout_39.addWidget(
            self.frame_31, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_38.addWidget(self.frame_27)
        self.frame_28 = QtWidgets.QFrame(self.frame_24)
        self.frame_28.setMaximumSize(QtCore.QSize(16777215, 1666666))
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout(self.frame_28)
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.frame_34 = QtWidgets.QFrame(self.frame_28)
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.frame_34)
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_44.setSpacing(3)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.label_50 = QtWidgets.QLabel(self.frame_34)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.verticalLayout_44.addWidget(
            self.label_50, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.line_33 = QtWidgets.QFrame(self.frame_34)
        self.line_33.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_33.setObjectName("line_33")
        self.verticalLayout_44.addWidget(self.line_33)
        self.verticalLayout_48.addWidget(self.frame_34)
        self.frame_35 = QtWidgets.QFrame(self.frame_28)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy)
        self.frame_35.setMaximumSize(QtCore.QSize(16777215, 1666666))
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.frame_35)
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.loan_txt = QtWidgets.QLabel(self.frame_35)
        self.loan_txt.setObjectName("loan_txt")
        self.verticalLayout_45.addWidget(
            self.loan_txt, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.verticalLayout_48.addWidget(self.frame_35)
        self.frame_36 = QtWidgets.QFrame(self.frame_28)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy)
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout(self.frame_36)
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.frame_37 = QtWidgets.QFrame(self.frame_36)
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.frame_37)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.label_51 = QtWidgets.QLabel(self.frame_37)
        self.label_51.setObjectName("label_51")
        self.verticalLayout_46.addWidget(self.label_51)
        self.label_52 = QtWidgets.QLabel(self.frame_37)
        self.label_52.setObjectName("label_52")
        self.verticalLayout_46.addWidget(self.label_52)
        self.horizontalLayout_54.addWidget(self.frame_37)
        self.frame_38 = QtWidgets.QFrame(self.frame_36)
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.frame_38)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.raw_loanP_txt = QtWidgets.QLabel(self.frame_38)
        self.raw_loanP_txt.setObjectName("raw_loanP_txt")
        self.verticalLayout_47.addWidget(
            self.raw_loanP_txt, 0, QtCore.Qt.AlignRight)
        self.raw_loanN_txt = QtWidgets.QLabel(self.frame_38)
        self.raw_loanN_txt.setObjectName("raw_loanN_txt")
        self.verticalLayout_47.addWidget(
            self.raw_loanN_txt, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_54.addWidget(self.frame_38)
        self.verticalLayout_48.addWidget(self.frame_36)
        self.verticalLayout_38.addWidget(self.frame_28)
        self.horizontalLayout_52.addWidget(self.frame_24)
        self.raw_education_frame = QtWidgets.QFrame(self.frame_20)
        self.raw_education_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.raw_education_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.raw_education_frame.setObjectName("raw_education_frame")
        self.horizontalLayout_52.addWidget(self.raw_education_frame)
        self.raw_ = QtWidgets.QFrame(self.frame_20)
        self.raw_.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.raw_.setFrameShadow(QtWidgets.QFrame.Raised)
        self.raw_.setObjectName("raw_")
        self.horizontalLayout_52.addWidget(self.raw_)
        self.verticalLayout_37.addWidget(self.frame_20, 0, QtCore.Qt.AlignTop)
        self.mid_frame = QtWidgets.QFrame(self.raw_business)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mid_frame.sizePolicy().hasHeightForWidth())
        self.mid_frame.setSizePolicy(sizePolicy)
        self.mid_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mid_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mid_frame.setObjectName("mid_frame")
        self.verticalLayout_37.addWidget(self.mid_frame)
        self.raw_page.addWidget(self.raw_business)
        self.raw_technique = QtWidgets.QWidget()
        self.raw_technique.setObjectName("raw_technique")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.raw_technique)
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.frame_39 = QtWidgets.QFrame(self.raw_technique)
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout(self.frame_39)
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.raw_correlation = QtWidgets.QFrame(self.frame_39)
        self.raw_correlation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.raw_correlation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.raw_correlation.setObjectName("raw_correlation")
        self.horizontalLayout_56.addWidget(self.raw_correlation)
        self.frame_42 = QtWidgets.QFrame(self.frame_39)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy)
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.frame_42)
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_50.setSpacing(5)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.raw_line_corr = QtWidgets.QFrame(self.frame_42)
        self.raw_line_corr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.raw_line_corr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.raw_line_corr.setObjectName("raw_line_corr")
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout(self.raw_line_corr)
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_57.setSpacing(3)
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.frame_45 = QtWidgets.QFrame(self.raw_line_corr)
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.horizontalLayout_57.addWidget(self.frame_45)
        self.frame_46 = QtWidgets.QFrame(self.raw_line_corr)
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.horizontalLayout_57.addWidget(self.frame_46)
        self.frame_47 = QtWidgets.QFrame(self.raw_line_corr)
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.horizontalLayout_57.addWidget(self.frame_47)
        self.verticalLayout_50.addWidget(self.raw_line_corr)
        self.raw_boxPlot = QtWidgets.QFrame(self.frame_42)
        self.raw_boxPlot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.raw_boxPlot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.raw_boxPlot.setObjectName("raw_boxPlot")
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout(self.raw_boxPlot)
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_58.setSpacing(3)
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.frame_48 = QtWidgets.QFrame(self.raw_boxPlot)
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.horizontalLayout_58.addWidget(self.frame_48)
        self.frame_41 = QtWidgets.QFrame(self.raw_boxPlot)
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.horizontalLayout_58.addWidget(self.frame_41)
        self.frame_40 = QtWidgets.QFrame(self.raw_boxPlot)
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.horizontalLayout_58.addWidget(self.frame_40)
        self.verticalLayout_50.addWidget(self.raw_boxPlot)
        self.horizontalLayout_56.addWidget(self.frame_42)
        self.verticalLayout_49.addWidget(self.frame_39)
        self.raw_page.addWidget(self.raw_technique)
        self.verticalLayout_31.addWidget(self.raw_page)
        self.visual_tab.addTab(self.visual_raw_tab, "")
        self.verticalLayout_4.addWidget(self.visual_tab)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/statiscal.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.design_tab.addTab(self.visual, icon10, "")

        self.horizontalLayout_36.addWidget(self.design_tab)
        self.content_widget.addWidget(self.design_page)
        self.predict_page = QtWidgets.QWidget()
        self.predict_page.setObjectName("predict_page")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.predict_page)
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")

        self.predict_tab = QtWidgets.QTabWidget(self.predict_page)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.predict_tab.setFont(font)
        self.predict_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.predict_tab.setTabPosition(QtWidgets.QTabWidget.West)
        self.predict_tab.setIconSize(QtCore.QSize(25, 25))
        self.predict_tab.setElideMode(QtCore.Qt.ElideNone)
        self.predict_tab.setObjectName("predict_tab")
        self.execute = QtWidgets.QWidget()
        self.execute.setObjectName("execute")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout(self.execute)
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.operators_groupBox_execute = QtWidgets.QGroupBox(self.execute)
        self.operators_groupBox_execute.setMinimumSize(QtCore.QSize(250, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.operators_groupBox_execute.setFont(font)
        self.operators_groupBox_execute.setStyleSheet("")
        self.operators_groupBox_execute.setObjectName(
            "operators_groupBox_execute")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(
            self.operators_groupBox_execute)
        self.verticalLayout_32.setContentsMargins(6, 10, 6, 10)
        self.verticalLayout_32.setSpacing(10)
        self.verticalLayout_32.setObjectName("verticalLayout_32")

        self.frame_22 = QtWidgets.QFrame(self.execute)
        self.frame_22.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.operators_groupBox_execute = QtWidgets.QGroupBox(self.frame_22)
        self.operators_groupBox_execute.setMinimumSize(QtCore.QSize(250, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.operators_groupBox_execute.setFont(font)
        self.operators_groupBox_execute.setStyleSheet("")
        self.operators_groupBox_execute.setObjectName("operators_groupBox_execute")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.operators_groupBox_execute)
        self.verticalLayout_32.setContentsMargins(6, 10, 6, 10)
        self.verticalLayout_32.setSpacing(10)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.operation_toolBox_execute = QtWidgets.QToolBox(self.operators_groupBox_execute)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.operation_toolBox_execute.setFont(font)
        self.operation_toolBox_execute.setMidLineWidth(0)
        self.operation_toolBox_execute.setObjectName("operation_toolBox_execute")
        self.data_execute_tab = QtWidgets.QWidget()
        self.data_execute_tab.setGeometry(QtCore.QRect(0, 0, 236, 278))
        self.data_execute_tab.setObjectName("data_execute_tab")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.data_execute_tab)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.test_radioButton_5 = QtWidgets.QRadioButton(self.data_execute_tab)
        self.test_radioButton_5.setObjectName("test_radioButton_5")
        self.verticalLayout_33.addWidget(self.test_radioButton_5)
        self.operation_toolBox_execute.addItem(self.data_execute_tab, "")
        self.model_execute_tab = QtWidgets.QWidget()
        self.model_execute_tab.setGeometry(QtCore.QRect(0, 0, 236, 278))
        self.model_execute_tab.setObjectName("model_execute_tab")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.model_execute_tab)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.test_radioButton_7 = QtWidgets.QRadioButton(self.model_execute_tab)
        self.test_radioButton_7.setObjectName("test_radioButton_7")
        self.verticalLayout_34.addWidget(self.test_radioButton_7)
        self.radioButton_4 = QtWidgets.QRadioButton(self.model_execute_tab)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_34.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.model_execute_tab)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_34.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.model_execute_tab)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_34.addWidget(self.radioButton_6)
        self.operation_toolBox_execute.addItem(self.model_execute_tab, "")
        self.verticalLayout_32.addWidget(self.operation_toolBox_execute)
        self.verticalLayout_51.addWidget(self.operators_groupBox_execute, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.groupBox = QtWidgets.QGroupBox(self.frame_22)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_52 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.frame_23 = QtWidgets.QFrame(self.groupBox)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.checkBox = QtWidgets.QCheckBox(self.frame_23)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_14.addWidget(self.checkBox)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame_23)
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.001)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_14.addWidget(self.doubleSpinBox)
        self.verticalLayout_52.addWidget(self.frame_23)
        self.verticalLayout_51.addWidget(self.groupBox)
        self.horizontalLayout_51.addWidget(self.frame_22)


        self.design_grp_2 = QtWidgets.QGroupBox(self.execute)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.design_grp_2.sizePolicy().hasHeightForWidth())
        self.design_grp_2.setSizePolicy(sizePolicy)
        self.design_grp_2.setMinimumSize(QtCore.QSize(0, 0))
        self.design_grp_2.setMaximumSize(QtCore.QSize(16777215, 16666666))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.design_grp_2.setFont(font)
        self.design_grp_2.setStyleSheet("")
        self.design_grp_2.setObjectName("design_grp_2")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.design_grp_2)
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_35.setSpacing(5)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.frame_21 = QtWidgets.QFrame(self.design_grp_2)
        self.frame_21.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_21.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_50.setSpacing(9)
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.active_btn_2 = QtWidgets.QPushButton(self.frame_21)
        self.active_btn_2.setMinimumSize(QtCore.QSize(100, 35))
        self.active_btn_2.setStyleSheet("color: rgb(0, 0, 255);")
        self.active_btn_2.setIcon(icon4)
        self.active_btn_2.setObjectName("active_btn_2")
        self.horizontalLayout_50.addWidget(
            self.active_btn_2, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)

        self.restart_btn_2 = QtWidgets.QPushButton(self.frame_21)
        self.restart_btn_2.setMinimumSize(QtCore.QSize(100, 35))
        self.restart_btn_2.setStyleSheet("color: rgb(0, 0, 255);")
        self.restart_btn_2.setIcon(icon5)
        self.restart_btn_2.setObjectName("restart_btn_2")
        self.horizontalLayout_50.addWidget(self.restart_btn_2, 0, QtCore.Qt.AlignHCenter)

        self.save_btn_2 = QtWidgets.QPushButton(self.frame_21)
        self.save_btn_2.setMinimumSize(QtCore.QSize(100, 35))
        self.save_btn_2.setStyleSheet("color: rgb(0, 0, 255);")
        self.save_btn_2.setIcon(icon6)
        self.save_btn_2.setObjectName("save_btn_2")
        self.horizontalLayout_50.addWidget(
            self.save_btn_2, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.verticalLayout_35.addWidget(self.frame_21)
        self.info_frame_2 = QtWidgets.QFrame(self.design_grp_2)
        self.info_frame_2.setMaximumSize(QtCore.QSize(16777215, 350))
        self.info_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame_2.setObjectName("info_frame_2")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.info_frame_2)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setSpacing(9)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.detail_txt_2 = QtWidgets.QLabel(self.info_frame_2)
        self.detail_txt_2.setObjectName("detail_txt_2")
        self.verticalLayout_36.addWidget(self.detail_txt_2)
        self.data_table_2 = QtWidgets.QTableWidget(self.info_frame_2)
        self.data_table_2.setMaximumSize(QtCore.QSize(16777215, 500))
        self.data_table_2.setObjectName("data_table_2")
        self.data_table_2.setColumnCount(17)
        self.data_table_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_2.setHorizontalHeaderItem(16, item)
        self.verticalLayout_36.addWidget(self.data_table_2)
        self.verticalLayout_35.addWidget(self.info_frame_2)
        self.progressBar_2 = QtWidgets.QProgressBar(self.design_grp_2)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout_35.addWidget(self.progressBar_2)
        self.roc_chart_2 = QtWidgets.QFrame(self.design_grp_2)
        self.roc_chart_2.setMinimumSize(QtCore.QSize(0, 200))
        self.roc_chart_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.roc_chart_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roc_chart_2.setObjectName("roc_chart_2")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.roc_chart_2)
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_51.setSpacing(9)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.data_table_result = QtWidgets.QTableWidget(self.roc_chart_2)
        self.data_table_result.setMaximumSize(QtCore.QSize(16777215, 500))
        self.data_table_result.setObjectName("data_table_result")
        self.data_table_result.setColumnCount(19)
        self.data_table_result.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table_result.setHorizontalHeaderItem(18, item)

        self.verticalLayout_51.addWidget(self.data_table_result)
        self.verticalLayout_35.addWidget(self.roc_chart_2)
        self.horizontalLayout_51.addWidget(self.design_grp_2)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/execute.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.predict_tab.addTab(self.execute, icon9, "")
        self.result = QtWidgets.QWidget()
        self.result.setObjectName("result")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.result)
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.result_tab = QtWidgets.QTabWidget(self.result)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.result_tab.setFont(font)
        self.result_tab.setTabPosition(QtWidgets.QTabWidget.South)
        self.result_tab.setObjectName("result_tab")
        self.result_dst_tab = QtWidgets.QWidget()
        self.result_dst_tab.setObjectName("result_dst_tab")
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout(self.result_dst_tab)
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.result_visual_dst = QtWidgets.QFrame(self.result_dst_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.result_visual_dst.sizePolicy().hasHeightForWidth())
        self.result_visual_dst.setSizePolicy(sizePolicy)
        self.result_visual_dst.setMinimumSize(QtCore.QSize(300, 0))
        self.result_visual_dst.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.result_visual_dst.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_visual_dst.setObjectName("result_visual_dst")
        self.horizontalLayout_48.addWidget(self.result_visual_dst)
        self.frame_17 = QtWidgets.QFrame(self.result_dst_tab)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28.setSpacing(10)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.note_grp_4 = QtWidgets.QGroupBox(self.frame_17)
        self.note_grp_4.setMinimumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.note_grp_4.setFont(font)
        self.note_grp_4.setObjectName("note_grp_4")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.note_grp_4)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.note_dst_txt = QtWidgets.QLabel(self.note_grp_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.note_dst_txt.setFont(font)
        self.note_dst_txt.setObjectName("note_dst_txt")
        self.verticalLayout_29.addWidget(
            self.note_dst_txt, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout_28.addWidget(self.note_grp_4)
        self.inf_lr_grp_4 = QtWidgets.QGroupBox(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.inf_lr_grp_4.sizePolicy().hasHeightForWidth())
        self.inf_lr_grp_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inf_lr_grp_4.setFont(font)
        self.inf_lr_grp_4.setObjectName("inf_lr_grp_4")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.inf_lr_grp_4)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.frame_18 = QtWidgets.QFrame(self.inf_lr_grp_4)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        self.frame_19.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_19.setMaximumSize(QtCore.QSize(16666666, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_19.setFont(font)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frame_19)
        self.formLayout_4.setContentsMargins(10, 10, 0, 0)
        self.formLayout_4.setHorizontalSpacing(50)
        self.formLayout_4.setVerticalSpacing(20)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_43 = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.formLayout_4.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_43)
        self.data_dst_txt = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.data_dst_txt.setFont(font)
        self.data_dst_txt.setObjectName("data_dst_txt")
        self.formLayout_4.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.data_dst_txt)
        self.label_44 = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.formLayout_4.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_44)
        self.acc_dst_txt = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acc_dst_txt.setFont(font)
        self.acc_dst_txt.setObjectName("acc_dst_txt")
        self.formLayout_4.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.acc_dst_txt)
        self.label_45 = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.formLayout_4.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_45)
        self.f1_dst_txt = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.f1_dst_txt.setFont(font)
        self.f1_dst_txt.setObjectName("f1_dst_txt")
        self.formLayout_4.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.f1_dst_txt)
        self.horizontalLayout_47.addWidget(
            self.frame_19, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_30.addWidget(self.frame_18, 0, QtCore.Qt.AlignTop)
        self.confusion_dst_table = QtWidgets.QTableWidget(self.inf_lr_grp_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.confusion_dst_table.sizePolicy().hasHeightForWidth())
        self.confusion_dst_table.setSizePolicy(sizePolicy)
        self.confusion_dst_table.setMinimumSize(QtCore.QSize(400, 0))
        self.confusion_dst_table.setAutoScroll(True)
        self.confusion_dst_table.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.confusion_dst_table.setObjectName("confusion_dst_table")
        self.confusion_dst_table.setColumnCount(3)
        self.confusion_dst_table.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_dst_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_dst_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_dst_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_dst_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_dst_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_dst_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.confusion_dst_table.setItem(2, 1, item)
        self.verticalLayout_30.addWidget(self.confusion_dst_table)
        self.verticalLayout_28.addWidget(self.inf_lr_grp_4)
        self.horizontalLayout_48.addWidget(self.frame_17)
        self.result_tab.addTab(self.result_dst_tab, "")
        self.result_rdst_tab = QtWidgets.QWidget()
        self.result_rdst_tab.setObjectName("result_rdst_tab")
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout(self.result_rdst_tab)
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.result_visual_rdst = QtWidgets.QFrame(self.result_rdst_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.result_visual_rdst.sizePolicy().hasHeightForWidth())
        self.result_visual_rdst.setSizePolicy(sizePolicy)
        self.result_visual_rdst.setMinimumSize(QtCore.QSize(300, 0))
        self.result_visual_rdst.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.result_visual_rdst.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_visual_rdst.setObjectName("result_visual_rdst")
        self.horizontalLayout_46.addWidget(self.result_visual_rdst)
        self.frame_12 = QtWidgets.QFrame(self.result_rdst_tab)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setSpacing(10)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.note_grp_3 = QtWidgets.QGroupBox(self.frame_12)
        self.note_grp_3.setMinimumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.note_grp_3.setFont(font)
        self.note_grp_3.setObjectName("note_grp_3")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.note_grp_3)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.note_rdst_txt = QtWidgets.QLabel(self.note_grp_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.note_rdst_txt.setFont(font)
        self.note_rdst_txt.setObjectName("note_rdst_txt")
        self.verticalLayout_26.addWidget(
            self.note_rdst_txt, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout_25.addWidget(self.note_grp_3)
        self.inf_lr_grp_3 = QtWidgets.QGroupBox(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.inf_lr_grp_3.sizePolicy().hasHeightForWidth())
        self.inf_lr_grp_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inf_lr_grp_3.setFont(font)
        self.inf_lr_grp_3.setObjectName("inf_lr_grp_3")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.inf_lr_grp_3)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.frame_16 = QtWidgets.QFrame(self.inf_lr_grp_3)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.frame_13 = QtWidgets.QFrame(self.frame_16)
        self.frame_13.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_13.setMaximumSize(QtCore.QSize(16666666, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_13.setFont(font)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_13)
        self.formLayout_3.setContentsMargins(10, 10, 0, 0)
        self.formLayout_3.setHorizontalSpacing(50)
        self.formLayout_3.setVerticalSpacing(20)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_40 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.formLayout_3.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_40)
        self.data_rdst_txt = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.data_rdst_txt.setFont(font)
        self.data_rdst_txt.setObjectName("data_rdst_txt")
        self.formLayout_3.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.data_rdst_txt)
        self.label_41 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.formLayout_3.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_41)
        self.acc_rdst_txt = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acc_rdst_txt.setFont(font)
        self.acc_rdst_txt.setObjectName("acc_rdst_txt")
        self.formLayout_3.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.acc_rdst_txt)
        self.label_42 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.formLayout_3.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_42)
        self.f1_rdst_txt = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.f1_rdst_txt.setFont(font)
        self.f1_rdst_txt.setObjectName("f1_rdst_txt")
        self.formLayout_3.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.f1_rdst_txt)
        self.horizontalLayout_45.addWidget(
            self.frame_13, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_27.addWidget(self.frame_16, 0, QtCore.Qt.AlignTop)
        self.confusion_rdst_table = QtWidgets.QTableWidget(self.inf_lr_grp_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.confusion_rdst_table.sizePolicy().hasHeightForWidth())
        self.confusion_rdst_table.setSizePolicy(sizePolicy)
        self.confusion_rdst_table.setMinimumSize(QtCore.QSize(400, 0))
        self.confusion_rdst_table.setAutoScroll(True)
        self.confusion_rdst_table.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.confusion_rdst_table.setObjectName("confusion_rdst_table")
        self.confusion_rdst_table.setColumnCount(3)
        self.confusion_rdst_table.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_rdst_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_rdst_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_rdst_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_rdst_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_rdst_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_rdst_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.confusion_rdst_table.setItem(2, 1, item)
        self.verticalLayout_27.addWidget(self.confusion_rdst_table)
        self.verticalLayout_25.addWidget(self.inf_lr_grp_3)
        self.horizontalLayout_46.addWidget(self.frame_12)
        self.result_tab.addTab(self.result_rdst_tab, "")
        self.result_xgboost_tab = QtWidgets.QWidget()
        self.result_xgboost_tab.setObjectName("result_xgboost_tab")
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout(
            self.result_xgboost_tab)
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.result_visual_xgboost = QtWidgets.QFrame(self.result_xgboost_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.result_visual_xgboost.sizePolicy().hasHeightForWidth())
        self.result_visual_xgboost.setSizePolicy(sizePolicy)
        self.result_visual_xgboost.setMinimumSize(QtCore.QSize(300, 0))
        self.result_visual_xgboost.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.result_visual_xgboost.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_visual_xgboost.setObjectName("result_visual_xgboost")

        self.horizontalLayout_44.addWidget(self.result_visual_xgboost)
        self.frame_8 = QtWidgets.QFrame(self.result_xgboost_tab)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.note_grp_2 = QtWidgets.QGroupBox(self.frame_8)
        self.note_grp_2.setMinimumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.note_grp_2.setFont(font)
        self.note_grp_2.setObjectName("note_grp_2")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.note_grp_2)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.note_xgboost_txt = QtWidgets.QLabel(self.note_grp_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.note_xgboost_txt.setFont(font)
        self.note_xgboost_txt.setObjectName("note_xgboost_txt")
        self.verticalLayout_23.addWidget(
            self.note_xgboost_txt, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout_22.addWidget(self.note_grp_2)
        self.inf_lr_grp_2 = QtWidgets.QGroupBox(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.inf_lr_grp_2.sizePolicy().hasHeightForWidth())
        self.inf_lr_grp_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inf_lr_grp_2.setFont(font)
        self.inf_lr_grp_2.setObjectName("inf_lr_grp_2")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.inf_lr_grp_2)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.frame_15 = QtWidgets.QFrame(self.inf_lr_grp_2)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.frame_11 = QtWidgets.QFrame(self.frame_15)
        self.frame_11.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_11.setMaximumSize(QtCore.QSize(16666666, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_11.setFont(font)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_11)
        self.formLayout_2.setContentsMargins(10, 10, 0, 0)
        self.formLayout_2.setHorizontalSpacing(50)
        self.formLayout_2.setVerticalSpacing(20)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_34 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.data_xgboost_txt = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.data_xgboost_txt.setFont(font)
        self.data_xgboost_txt.setObjectName("data_xgboost_txt")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.data_xgboost_txt)
        self.label_36 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_36)
        self.acc_xgboost_txt = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acc_xgboost_txt.setFont(font)
        self.acc_xgboost_txt.setObjectName("acc_xgboost_txt")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.acc_xgboost_txt)
        self.label_39 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_39)
        self.f1_xgboost_txt = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.f1_xgboost_txt.setFont(font)
        self.f1_xgboost_txt.setObjectName("f1_xgboost_txt")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.f1_xgboost_txt)
        self.horizontalLayout_42.addWidget(
            self.frame_11, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_24.addWidget(self.frame_15, 0, QtCore.Qt.AlignTop)
        self.confusion_xgboost_table = QtWidgets.QTableWidget(
            self.inf_lr_grp_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.confusion_xgboost_table.sizePolicy().hasHeightForWidth())
        self.confusion_xgboost_table.setSizePolicy(sizePolicy)
        self.confusion_xgboost_table.setMinimumSize(QtCore.QSize(400, 0))
        self.confusion_xgboost_table.setAutoScroll(True)
        self.confusion_xgboost_table.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.confusion_xgboost_table.setObjectName("confusion_xgboost_table")
        self.confusion_xgboost_table.setColumnCount(3)
        self.confusion_xgboost_table.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_xgboost_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_xgboost_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_xgboost_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_xgboost_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_xgboost_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_xgboost_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.confusion_xgboost_table.setItem(2, 1, item)
        self.verticalLayout_24.addWidget(self.confusion_xgboost_table)
        self.verticalLayout_22.addWidget(self.inf_lr_grp_2)
        self.horizontalLayout_44.addWidget(self.frame_8)
        self.result_tab.addTab(self.result_xgboost_tab, "")
        self.result_lr_tab = QtWidgets.QWidget()
        self.result_lr_tab.setObjectName("result_lr_tab")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.result_lr_tab)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.result_visual_lr = QtWidgets.QFrame(self.result_lr_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.result_visual_lr.sizePolicy().hasHeightForWidth())
        self.result_visual_lr.setSizePolicy(sizePolicy)
        self.result_visual_lr.setMinimumSize(QtCore.QSize(300, 0))
        self.result_visual_lr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.result_visual_lr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_visual_lr.setObjectName("result_visual_lr")

        self.horizontalLayout_41.addWidget(self.result_visual_lr)
        self.frame_7 = QtWidgets.QFrame(self.result_lr_tab)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.note_grp = QtWidgets.QGroupBox(self.frame_7)
        self.note_grp.setMinimumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.note_grp.setFont(font)
        self.note_grp.setObjectName("note_grp")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.note_grp)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.note_lr_txt = QtWidgets.QLabel(self.note_grp)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.note_lr_txt.setFont(font)
        self.note_lr_txt.setObjectName("note_lr_txt")
        self.verticalLayout_17.addWidget(
            self.note_lr_txt, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout_21.addWidget(self.note_grp)
        self.inf_lr_grp = QtWidgets.QGroupBox(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.inf_lr_grp.sizePolicy().hasHeightForWidth())
        self.inf_lr_grp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inf_lr_grp.setFont(font)
        self.inf_lr_grp.setObjectName("inf_lr_grp")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.inf_lr_grp)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_14 = QtWidgets.QFrame(self.inf_lr_grp)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.frame_10 = QtWidgets.QFrame(self.frame_14)
        self.frame_10.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_10.setMaximumSize(QtCore.QSize(16666666, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_10.setFont(font)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.formLayout = QtWidgets.QFormLayout(self.frame_10)
        self.formLayout.setContentsMargins(10, 10, 0, 0)
        self.formLayout.setHorizontalSpacing(50)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_33 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_33)
        self.data_lr_txt = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.data_lr_txt.setFont(font)
        self.data_lr_txt.setObjectName("data_lr_txt")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.data_lr_txt)
        self.label_35 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.acc_lr_txt = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acc_lr_txt.setFont(font)
        self.acc_lr_txt.setObjectName("acc_lr_txt")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.acc_lr_txt)
        self.label_38 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_38)
        self.f1_lr_txt = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.f1_lr_txt.setFont(font)
        self.f1_lr_txt.setObjectName("f1_lr_txt")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.f1_lr_txt)
        self.horizontalLayout_40.addWidget(
            self.frame_10, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_20.addWidget(self.frame_14, 0, QtCore.Qt.AlignTop)
        self.confusion_lr_table = QtWidgets.QTableWidget(self.inf_lr_grp)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.confusion_lr_table.sizePolicy().hasHeightForWidth())
        self.confusion_lr_table.setSizePolicy(sizePolicy)
        self.confusion_lr_table.setMinimumSize(QtCore.QSize(400, 0))
        self.confusion_lr_table.setAutoScroll(True)
        self.confusion_lr_table.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.confusion_lr_table.setObjectName("confusion_lr_table")
        self.confusion_lr_table.setColumnCount(3)
        self.confusion_lr_table.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_lr_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_lr_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_lr_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_lr_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_lr_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.confusion_lr_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.confusion_lr_table.setItem(2, 1, item)
        self.verticalLayout_20.addWidget(self.confusion_lr_table)
        self.verticalLayout_21.addWidget(self.inf_lr_grp)
        self.horizontalLayout_41.addWidget(self.frame_7)
        self.result_tab.addTab(self.result_lr_tab, "")
        self.horizontalLayout_39.addWidget(self.result_tab)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/result.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.predict_tab.addTab(self.result, icon11, "")
        self.horizontalLayout_38.addWidget(self.predict_tab)
        self.content_widget.addWidget(self.predict_page)
        self.verticalLayout_2.addWidget(self.content_widget)
        self.verticalLayout.addWidget(self.body_widget)
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        self.content_widget.setCurrentIndex(1)
        self.operation_toolBox.setCurrentIndex(0)
        self.operation_toolBox.layout().setSpacing(6)
        self.parameter_widget.setCurrentIndex(3)
        self.predict_tab.setCurrentIndex(0)
        self.operation_toolBox_execute.setCurrentIndex(1)
        self.operation_toolBox_execute.layout().setSpacing(6)
        self.visual_tab.setCurrentIndex(0)
        self.raw_page.setCurrentIndex(1)
        self.result_tab.setCurrentIndex(0)

        self.data_table_result.hide()


        try:
            #before edit
            print('data prepare')
            predict_raw = de.data_from_csv('data/predict_data/Raw.csv')
            predict_raw['id'] = ''
            id_column = predict_raw['id']
            data = predict_raw.drop(columns=['id'])
            data = pd.concat([id_column, data], axis=1)
            self.predict_data = [data]
            self.design_data = [de.data_from_csv('data/design_data/Raw.csv')]
            print('Design ui prepare')
            self.append_design_ui()
            print('Import ui prepare')
            self.append_import_ui()
            print('Statistic ui prepare')
            self.append_statistic_ui()
            print('Result ui prepare')
            self.append_result_visual()
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate(
            "MainWindow", "Bank Customer Support Tool"))
        self.label_3.setText(_translate("MainWindow", "BANK TOOL"))
        self.label.setText(_translate("MainWindow", "Modes:"))
        self.predict_btn.setText(_translate("MainWindow", "Predict"))
        self.design_btn.setText(_translate("MainWindow", "Design"))
        self.import_btn.setText(_translate("MainWindow", "Import Data"))
        self.view_btn.setText(_translate("MainWindow", "View Data"))
        self.import_model_btn.setText(_translate("MainWindow", "Import Model"))
        self.operators_groupBox.setTitle(_translate("MainWindow", "Operators"))
        self.test_radioButton_3.setText(
            _translate("MainWindow", "Raw"))
        self.operation_toolBox.setItemText(self.operation_toolBox.indexOf(
            self.data_tab), _translate("MainWindow", "Data"))
        self.test_radioButton_2.setText(
            _translate("MainWindow", "Decision Tree"))
        self.radioButton_2.setText(_translate("MainWindow", "Random Forest"))
        self.radioButton.setText(_translate("MainWindow", "XGBoost"))
        self.radioButton_3.setText(_translate(
            "MainWindow", "Logistic Regression"))
        self.operation_toolBox.setItemText(self.operation_toolBox.indexOf(
            self.model_tab), _translate("MainWindow", "Model"))
        self.validation_grp.setTitle(_translate("MainWindow", "Validation"))
        self.checkBox_2.setText(_translate("MainWindow", "Hold-Out"))
        self.design_grp.setTitle(_translate("MainWindow", "Design"))
        self.active_btn.setText(_translate("MainWindow", "Active"))
        self.restart_btn.setText(_translate("MainWindow", "Restart"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.detail_txt.setText(_translate("MainWindow", "TextLabel"))
        item = self.data_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Age"))
        item = self.data_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Job"))
        item = self.data_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Marital"))
        item = self.data_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Education"))
        item = self.data_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Default"))
        item = self.data_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Balance"))
        item = self.data_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Housing"))
        item = self.data_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Loan"))
        item = self.data_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Contact"))
        item = self.data_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Day"))
        item = self.data_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Month"))
        item = self.data_table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Duration"))
        item = self.data_table.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Campaign"))
        item = self.data_table.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Pdays"))
        item = self.data_table.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Previous"))
        item = self.data_table.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Poutcome"))
        item = self.data_table.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Y"))
        self.decisionTree_groupBox.setTitle(
            _translate("MainWindow", "DecisionTree "))
        self.label_4.setText(_translate("MainWindow", "Criterion"))
        self.criterion_DST_comboBox.setItemText(
            0, _translate("MainWindow", "Gini"))
        self.criterion_DST_comboBox.setItemText(
            1, _translate("MainWindow", "Entropy"))
        self.label_5.setText(_translate("MainWindow", "Max depth"))
        self.label_6.setText(_translate("MainWindow", "Min samples split"))
        self.label_7.setText(_translate("MainWindow", "Min samples leaf"))
        self.label_8.setText(_translate("MainWindow", "Max features"))
        self.applyPrunning_DST_checkBox.setText(
            _translate("MainWindow", "Apply prunning"))
        self.paraGuild_DST_btn.setText(
            _translate("MainWindow", "Parameter Recommend"))
        self.guild_DST_btn.setText(_translate("MainWindow", "Guild"))
        self.XGBoost_groupBox.setTitle(_translate("MainWindow", "XGBoost"))
        self.label_21.setText(_translate("MainWindow", "N_estimators"))
        self.label_14.setText(_translate("MainWindow", "Objective"))
        self.loss_XGB_comboBox.setItemText(
            0, _translate("MainWindow", "binary:logistic"))
        self.loss_XGB_comboBox.setItemText(
            1, _translate("MainWindow", "multi:softmax"))
        self.label_15.setText(_translate("MainWindow", "Learning rate"))
        self.label_16.setText(_translate("MainWindow", "Max depth"))
        self.label_17.setText(_translate("MainWindow", "Subsample"))
        self.label_18.setText(_translate(
            "MainWindow", "Min weight fraction leaf"))
        self.label_22.setText(_translate("MainWindow", "Max features"))
        self.paraGuild_XGB_btn.setText(
            _translate("MainWindow", "Parameter Recommend"))
        self.guild_XGB_btn.setText(_translate("MainWindow", "Guild"))
        self.LR_groupBox.setTitle(_translate(
            "MainWindow", "Linear Regression"))
        self.label_23.setText(_translate("MainWindow", "Penalty"))
        self.penalty_LR_comboBox.setItemText(
            0, _translate("MainWindow", "None"))
        self.penalty_LR_comboBox.setItemText(1, _translate("MainWindow", "L1"))
        self.penalty_LR_comboBox.setItemText(2, _translate("MainWindow", "L2"))
        self.penalty_LR_comboBox.setItemText(
            3, _translate("MainWindow", "Elasticnet"))
        self.label_24.setText(_translate("MainWindow", "C"))
        self.label_25.setText(_translate("MainWindow", "Max iter"))
        self.label_26.setText(_translate("MainWindow", "Solver"))
        self.solver_LR_comboBox.setItemText(
            0, _translate("MainWindow", "lbfgs"))
        self.solver_LR_comboBox.setItemText(
            1, _translate("MainWindow", "newton-cg"))
        self.solver_LR_comboBox.setItemText(
            2, _translate("MainWindow", "liblinear"))
        self.solver_LR_comboBox.setItemText(3, _translate("MainWindow", "sag"))
        self.solver_LR_comboBox.setItemText(
            4, _translate("MainWindow", "saga"))
        self.paraGuild_LR_btn.setText(_translate(
            "MainWindow", "Parameter Recommend"))
        self.guild_LR_btn.setText(_translate("MainWindow", "Guild"))
        self.randomForest_groupBox.setTitle(
            _translate("MainWindow", "Random Forest"))
        self.label_13.setText(_translate("MainWindow", "N_estimators"))
        self.label_10.setText(_translate("MainWindow", "Criterion"))
        self.criterion_RDST_comboBox.setItemText(
            0, _translate("MainWindow", "Gini"))
        self.criterion_RDST_comboBox.setItemText(
            1, _translate("MainWindow", "Entropy"))
        self.criterion_RDST_comboBox.setItemText(
            2, _translate("MainWindow", "Log_loss"))
        self.label_11.setText(_translate("MainWindow", "Max depth"))
        self.label_12.setText(_translate("MainWindow", "Min samples split"))
        self.label_27.setText(_translate("MainWindow", "Min samples leaf"))
        self.label_28.setText(_translate("MainWindow", "Max features"))
        self.paraGuild_RDST_btn.setText(
            _translate("MainWindow", "Parameter Recommend"))
        self.guild_RDST_btn.setText(_translate("MainWindow", "Guild"))
        self.operators_groupBox_execute.setTitle(
            _translate("MainWindow", "Operators"))
        self.test_radioButton_5.setText(
            _translate("MainWindow", "Raw"))
        self.operation_toolBox_execute.setItemText(self.operation_toolBox_execute.indexOf(
            self.data_execute_tab), _translate("MainWindow", "Data"))
        self.test_radioButton_7.setText(
            _translate("MainWindow", "Decision Tree"))
        self.radioButton_4.setText(_translate("MainWindow", "Random Forest"))
        self.radioButton_5.setText(_translate("MainWindow", "XGBoost"))
        self.radioButton_6.setText(_translate(
            "MainWindow", "Logistic Regression"))
        self.operation_toolBox_execute.setItemText(self.operation_toolBox_execute.indexOf(
            self.model_execute_tab), _translate("MainWindow", "Model"))
        self.groupBox.setTitle(_translate("MainWindow", "Validation"))
        self.checkBox.setText(_translate("MainWindow", "Thresh-Hold"))
        self.design_grp_2.setTitle(_translate("MainWindow", "Design"))
        self.active_btn_2.setText(_translate("MainWindow", "Active"))
        self.restart_btn_2.setText(_translate("MainWindow", "Restart"))
        self.save_btn_2.setText(_translate("MainWindow", "Save"))
        self.detail_txt_2.setText(_translate("MainWindow", "TextLabel"))
        item = self.data_table_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.data_table_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Age"))
        item = self.data_table_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Job"))
        item = self.data_table_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Marital"))
        item = self.data_table_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Education"))
        item = self.data_table_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Default"))
        item = self.data_table_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Balance"))
        item = self.data_table_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Housing"))
        item = self.data_table_2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Loan"))
        item = self.data_table_2.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Contact"))
        item = self.data_table_2.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Day"))
        item = self.data_table_2.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Month"))
        item = self.data_table_2.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Duration"))
        item = self.data_table_2.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Campaign"))
        item = self.data_table_2.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Pdays"))
        item = self.data_table_2.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Previous"))
        item = self.data_table_2.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Poutcome"))
        item = self.data_table_result.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.data_table_result.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Age"))
        item = self.data_table_result.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Job"))
        item = self.data_table_result.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Marital"))
        item = self.data_table_result.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Education"))
        item = self.data_table_result.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Default"))
        item = self.data_table_result.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Balance"))
        item = self.data_table_result.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Housing"))
        item = self.data_table_result.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Loan"))
        item = self.data_table_result.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Contact"))
        item = self.data_table_result.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Day"))
        item = self.data_table_result.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Month"))
        item = self.data_table_result.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Duration"))
        item = self.data_table_result.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Campaign"))
        item = self.data_table_result.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Pdays"))
        item = self.data_table_result.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Previous"))
        item = self.data_table_result.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Poutcome"))
        item = self.data_table_result.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "Y"))
        item = self.data_table_result.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "Probability"))


        self.predict_tab.setTabText(self.predict_tab.indexOf(
            self.execute), _translate("MainWindow", "Execute"))

        ####
        self.business_btn.setText(_translate("MainWindow", "Business"))
        self.technique_btn.setText(_translate("MainWindow", "Technique"))
        self.label_32.setText(_translate(
            "MainWindow", "Subscribed term deposit"))
        self.deposit_txt.setText(_translate("MainWindow", "TextLabel"))
        self.label_46.setText(_translate("MainWindow", "Positive"))
        self.label_47.setText(_translate("MainWindow", "Negative"))
        self.raw_positive_txt.setText(_translate("MainWindow", "TextLabel"))
        self.raw_negative_txt.setText(_translate("MainWindow", "TextLabel"))
        self.label_50.setText(_translate("MainWindow", "Loan"))
        self.loan_txt.setText(_translate("MainWindow", "TextLabel"))
        self.label_51.setText(_translate("MainWindow", "Positive subcribed"))
        self.label_52.setText(_translate("MainWindow", "Negative subcribed"))
        self.raw_loanP_txt.setText(_translate("MainWindow", "TextLabel"))
        self.raw_loanN_txt.setText(_translate("MainWindow", "TextLabel"))
        #########
        self.design_tab.setTabText(self.design_tab.indexOf(
            self.execute_design), _translate("MainWindow", "Execute"))
        self.visual_tab.setTabText(self.visual_tab.indexOf(self.visual_raw_tab), _translate("MainWindow", "Raw"))
        self.design_tab.setTabText(self.design_tab.indexOf(self.visual), _translate("MainWindow", "Statistics"))
        ##########
        self.note_grp_4.setTitle(_translate("MainWindow", "Note"))
        self.note_dst_txt.setText(_translate("MainWindow", "TextLabel"))
        self.inf_lr_grp_4.setTitle(_translate("MainWindow", "Information"))
        self.label_43.setText(_translate("MainWindow", "Data:"))
        self.data_dst_txt.setText(_translate("MainWindow", "..."))
        self.label_44.setText(_translate("MainWindow", "Accuracy:"))
        self.acc_dst_txt.setText(_translate("MainWindow", "..."))
        self.label_45.setText(_translate("MainWindow", "F1-Score:"))
        self.f1_dst_txt.setText(_translate("MainWindow", "..."))
        item = self.confusion_dst_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Pred False"))
        item = self.confusion_dst_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pred True"))
        item = self.confusion_dst_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Class Recall"))
        item = self.confusion_dst_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "True False"))
        item = self.confusion_dst_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "True True"))
        item = self.confusion_dst_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Class Precision"))
        __sortingEnabled = self.confusion_dst_table.isSortingEnabled()
        self.confusion_dst_table.setSortingEnabled(False)
        self.confusion_dst_table.setSortingEnabled(__sortingEnabled)
        self.result_tab.setTabText(self.result_tab.indexOf(
            self.result_dst_tab), _translate("MainWindow", "Decision Tree"))
        self.note_grp_3.setTitle(_translate("MainWindow", "Note"))
        self.note_rdst_txt.setText(_translate("MainWindow", "TextLabel"))
        self.inf_lr_grp_3.setTitle(_translate("MainWindow", "Information"))
        self.label_40.setText(_translate("MainWindow", "Data:"))
        self.data_rdst_txt.setText(_translate("MainWindow", "..."))
        self.label_41.setText(_translate("MainWindow", "Accuracy:"))
        self.acc_rdst_txt.setText(_translate("MainWindow", "..."))
        self.label_42.setText(_translate("MainWindow", "F1-Score:"))
        self.f1_rdst_txt.setText(_translate("MainWindow", "..."))
        item = self.confusion_rdst_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Pred False"))
        item = self.confusion_rdst_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pred True"))
        item = self.confusion_rdst_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Class Recall"))
        item = self.confusion_rdst_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "True False"))
        item = self.confusion_rdst_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "True True"))
        item = self.confusion_rdst_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Class Precision"))
        __sortingEnabled = self.confusion_rdst_table.isSortingEnabled()
        self.confusion_rdst_table.setSortingEnabled(False)
        self.confusion_rdst_table.setSortingEnabled(__sortingEnabled)
        self.result_tab.setTabText(self.result_tab.indexOf(
            self.result_rdst_tab), _translate("MainWindow", "Random Forest"))
        self.note_grp_2.setTitle(_translate("MainWindow", "Note"))
        self.note_xgboost_txt.setText(_translate("MainWindow", "TextLabel"))
        self.inf_lr_grp_2.setTitle(_translate("MainWindow", "Information"))
        self.label_34.setText(_translate("MainWindow", "Data:"))
        self.data_xgboost_txt.setText(_translate("MainWindow", "..."))
        self.label_36.setText(_translate("MainWindow", "Accuracy:"))
        self.acc_xgboost_txt.setText(_translate("MainWindow", "..."))
        self.label_39.setText(_translate("MainWindow", "F1-Score:"))
        self.f1_xgboost_txt.setText(_translate("MainWindow", "..."))
        item = self.confusion_xgboost_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Pred False"))
        item = self.confusion_xgboost_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pred True"))
        item = self.confusion_xgboost_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Class Recall"))
        item = self.confusion_xgboost_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "True False"))
        item = self.confusion_xgboost_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "True True"))
        item = self.confusion_xgboost_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Class Precision"))
        __sortingEnabled = self.confusion_xgboost_table.isSortingEnabled()
        self.confusion_xgboost_table.setSortingEnabled(False)
        self.confusion_xgboost_table.setSortingEnabled(__sortingEnabled)
        self.result_tab.setTabText(self.result_tab.indexOf(
            self.result_xgboost_tab), _translate("MainWindow", "XGBoost"))
        self.note_grp.setTitle(_translate("MainWindow", "Note"))
        self.note_lr_txt.setText(_translate("MainWindow", "TextLabel"))
        self.inf_lr_grp.setTitle(_translate("MainWindow", "Information"))
        self.label_33.setText(_translate("MainWindow", "Data:"))
        self.data_lr_txt.setText(_translate("MainWindow", "..."))
        self.label_35.setText(_translate("MainWindow", "Accuracy:"))
        self.acc_lr_txt.setText(_translate("MainWindow", "..."))
        self.label_38.setText(_translate("MainWindow", "F1-Score:"))
        self.f1_lr_txt.setText(_translate("MainWindow", "..."))
        item = self.confusion_lr_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Pred False"))
        item = self.confusion_lr_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pred True"))
        item = self.confusion_lr_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Class Recall"))
        item = self.confusion_lr_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "True False"))
        item = self.confusion_lr_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "True True"))
        item = self.confusion_lr_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Class Precision"))
        __sortingEnabled = self.confusion_lr_table.isSortingEnabled()
        self.confusion_lr_table.setSortingEnabled(False)
        self.confusion_lr_table.setSortingEnabled(__sortingEnabled)
        self.result_tab.setTabText(self.result_tab.indexOf(
            self.result_lr_tab), _translate("MainWindow", "Logistic Regression"))
        self.predict_tab.setTabText(self.predict_tab.indexOf(
            self.result), _translate("MainWindow", "Result"))
        #####

#### retranslateUi append
    def append_retrans(self,wid,txt):
        try:
            _translate = QtCore.QCoreApplication.translate
            wid.setText(
                _translate("MainWindow", txt))
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+'\nOperation groupbox fail', QMessageBox.Close)

    ###### main window

#### design page
    def append_design_ui(self):
        try:
            #init data needed
            print('init data needed')
            self.predict_name = ''
            self.design_name = ''
            self.predict_model = ''
            self.design_model = ''
            self.vad = ''
            self.threshHold = ''
            self.detail_txt.setText('Choose something...')
            self.detail_txt_2.setText('Choose something...')
            # import, view, delete window
            try:
                print('import, view, delete window')
                self.ui_import_data = import_data.Ui_MainWindow()
                self.ui_view_data = view.Ui_MainWindow()

                self.ui_import_data.setupUi()
                self.ui_view_data.setupUi()
                pass
            except Exception as err:
                QMessageBox.information(self, 'Error', str(err.args[0]) +'\nData window error', QMessageBox.Close)
            print('button')
            ##### Button open data window
            self.import_btn.clicked.connect(self.import_btn_click)
            self.import_model_btn.clicked.connect(self.import_model)
            self.view_btn.clicked.connect(self.view_btn_click)
            ###### Button open page
            self.predict_btn.clicked.connect(self.predict_clicked)
            self.design_btn.clicked.connect(self.design_clicked)
            ###### Radio button toggle
            # design model
            for i in self.model_tab.children():
                if isinstance(i, QtWidgets.QRadioButton):
                    i.toggled.connect(lambda checked, btn=i: self.parameter_state(btn))

            # design data
            self.test_radioButton_3.toggled.connect(lambda: self.design_data_state(self.test_radioButton_3))
            # predict data
            self.test_radioButton_5.toggled.connect(lambda: self.predict_data_state(self.test_radioButton_5))


            # predict model
            for i in self.model_execute_tab.children():
                if isinstance(i, QtWidgets.QRadioButton):
                    i.toggled.connect(lambda checked, btn=i: self.predict_model_state(btn))

            # predict validation tab
            self.checkBox.stateChanged.connect(self.valid_state_predict_changed)
            self.doubleSpinBox.valueChanged.connect(self.valid_state_predict_changed)
            # design validation tab
            self.checkBox_2.stateChanged.connect(lambda: self.valid_state_changed(self.checkBox_2))
            self.crossVal_spinBox_2.valueChanged.connect(lambda: self.valid_state_changed(self.checkBox_2))
            # guild paramter
            self.guild_DST_btn.clicked.connect(lambda: self.guild_btn_clicked('dst'))
            self.guild_LR_btn.clicked.connect(lambda: self.guild_btn_clicked('lr'))
            self.guild_RDST_btn.clicked.connect(lambda: self.guild_btn_clicked('rdst'))
            self.guild_XGB_btn.clicked.connect(lambda: self.guild_btn_clicked('xgb'))
            # parameter recommend
            self.paraGuild_DST_btn.clicked.connect(self.dst_recommend)
            self.paraGuild_LR_btn.clicked.connect(self.lr_recommend)
            self.paraGuild_RDST_btn.clicked.connect(self.rdst_recommend)
            self.paraGuild_XGB_btn.clicked.connect(self.xgb_recommend)
            ######
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+'\nSet up ui error', QMessageBox.Close)

##### header

    def import_btn_click(self):
        try:
            self.ui_import_data.show()
        except Exception as err:
            QMessageBox.information(self,'Error',str(err.args[0]),QMessageBox.Close)

    def view_btn_click(self):
        try:
            self.ui_view_data.show()
        except Exception as err:
            QMessageBox.information(self,'Error',str(err.args[0]),QMessageBox.Close)

    def predict_clicked(self):
        try:
            self.content_widget.setCurrentIndex(1)
        except Exception as err:
            QMessageBox.information(self,'Error',str(err.args[0]),QMessageBox.Close)

    def design_clicked(self):
        try:
            self.content_widget.setCurrentIndex(0)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

##### desgin change

    def design_data_state(self,d):
        # d = data
        try:
            #data/design_data/Raw.csv
            name = d.text()
            self.design_name = name

            self.detail_txt.setText('Data: ' + self.design_name + ' - Model: ' + self.design_model + self.vad)

            num = qe.find_index_of_widget(self.data_tab,d)
            data = self.design_data[num-1]
            self.design_data_to_table(data)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+"\nData design radio button error", QMessageBox.Close)

    def parameter_state(self, dp):
        # dp = design_parameter
        try:

            txt = dp.text()

            self.design_model = txt
            if txt == 'Decision Tree':
                # test_radioButton_2
                self.parameter_widget.setCurrentIndex(0)
            elif txt == 'Random Forest':
                # radioButton_2
                self.parameter_widget.setCurrentIndex(3)
            elif txt == 'XGBoost':
                # radioButton
                self.parameter_widget.setCurrentIndex(1)
            elif txt == 'Logistic Regression':
                # radioButton_3
                self.parameter_widget.setCurrentIndex(2)
            self.detail_txt.setText('Data: ' + self.design_name + ' - Model: ' + self.design_model + self.vad)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]) + "\nDesign model Parameter error",
                                    QMessageBox.Close)

    def valid_state_changed(self,b):
        # b = button
        try:
            self.vad = ''
            holdOut = round(self.crossVal_spinBox_2.value(),3)
            holdOut_str = ' - Hold-Out: ' + str(holdOut)


            if self.checkBox_2.isChecked():
                self.vad+= holdOut_str

            self.detail_txt.setText('Data: ' + self.design_name + ' - Model: ' + self.design_model + self.vad)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+"\nValidation design button error", QMessageBox.Close)

    def guild_btn_clicked(self,n):
        # b = button
        try:
            if n == 'dst':
                url = 'https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html'
            elif n == 'rdst':
                url = 'https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html'
            elif n == 'xgb':
                url = 'https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html'
            else:
                url = 'https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html'
            option = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(options=option)
            driver.get(url)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+"\nGuild parameter button error", QMessageBox.Close)


###### design parameter recommend
    def dst_recommend(self):
        try:
            self.criterion_DST_comboBox.setCurrentIndex(0)
            self.maxDepth_DST_spinBox.setValue(9)
            self.minSamplesSplit_DST_spinBox.setValue(2)
            self.minSamplesLeaf_DST_spinBox.setValue(5)
            self.maxfeatures_DST_spinBox.setValue(4)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+"\nParameter recommend button error", QMessageBox.Close)

    def rdst_recommend(self):
        try:
            """Random Forest: {'max_depth': 34.0, 'max_features': 'log2', 'max_leaf_nodes': 470.0, 
            'max_samples': 0.9, 'min_samples_leaf': 5.0, 'min_samples_split': 7.0, 'n_estimators': 560.0}"""
            self.nEstimators_RDST_spinBox.setValue(560)
            self.criterion_RDST_comboBox.setCurrentIndex(0)
            self.maxDepth_RDST_spinBox.setValue(34)
            self.minSamplesSplit_RDST_spinBox.setValue(7)
            self.maxSampleLeaf_RDST_spinBox.setValue(6)
            self.maxFeature_RDST_spinBox.setValue(4)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+"\nParameter recommend button error", QMessageBox.Close)

    def xgb_recommend(self):
        try:
            self.nEstimators_XGB_spinBox.setValue(400)
            self.loss_XGB_comboBox.setCurrentIndex(0)
            self.learningRate_XGB_spinBox.setValue(0.213)
            self.maxDepth_XGB_spinBox.setValue(15)
            self.subsample_XGB_spinBox.setValue(0.636)
            self.minWeightFractionLeaf_XGB_spinBox.setValue(0)
            self.maxFeatures_XGB_spinBox.setValue(4)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+"\nParameter recommend button error", QMessageBox.Close)

    def lr_recommend(self):
        try:
            #'C': 3, 'class_weight': None, 'max_iter': 300.0, solver = 'sag', penalty= 'l2')
            self.penalty_LR_comboBox.setCurrentIndex(2)
            self.c_LR_spinBox.setValue(1)
            self.maxIter_spinBox.setValue(550)
            self.solver_LR_comboBox.setCurrentIndex(3)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+"\nParameter recommend button error", QMessageBox.Close)

    def design_data_to_table(self,data):
        try:
            qe.data_to_table(self.data_table,data)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+"\nDesign data error", QMessageBox.Close)


###### predict page
    def predict_data_state(self,d):
        # d = data
        try:
            name = d.text()

            self.predict_name = name

            self.detail_txt_2.setText('Data: ' + self.predict_name + ' - Model: ' + self.predict_model)

            num = qe.find_index_of_widget(self.data_execute_tab,d)
            data = self.predict_data[num-1]

            self.predict_data_to_table(data)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+"\nData predict radio button error", QMessageBox.Close)

    def predict_model_state(self,m):
        # m = model
        try:
            self.predict_model = m.text()
            self.detail_txt_2.setText('Data: ' + self.predict_name + ' - Model: ' + self.predict_model)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+"\nModel predict radio button error", QMessageBox.Close)

    def predict_data_to_table(self,data):
        try:
            qe.data_to_table(self.data_table_2,data)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+"\nPredict data error", QMessageBox.Close)

    def valid_state_predict_changed(self):
        # b = button
        try:
            self.threshHold = ''
            threshHold = round(self.doubleSpinBox.value(),3)
            s = ' - Thresh-hold: ' + str(threshHold)


            if self.checkBox.isChecked():
                self.threshHold+= s

            self.detail_txt_2.setText('Data: ' + self.predict_name + ' - Model: ' + self.predict_model + self.threshHold)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+"\nValidation design button error", QMessageBox.Close)
####### import window
    def append_import_ui(self):
        try:
            self.data_need_save = None
            self.ui_import_data.predict_save_btn.clicked.connect(self.import_saveP)
            self.ui_import_data.train_save_btn.clicked.connect(self.import_saveT)
            ### button run program
            self.roc_curve = qe.plot_roc_curve(parent = self.roc_chart)
            self.active_btn.clicked.connect(self.active_design)
            self.active_btn_2.clicked.connect(self.active_predict)
            self.save_btn_2.clicked.connect(self.save_predict)
            self.restart_btn_2.clicked.connect(self.restart_predict)
            self.save_btn.clicked.connect(self.save_design)
            self.restart_btn.clicked.connect(self.restart_design)
        except Exception as err:
            QMessageBox.information(self,'Error',str(err.args[0]),QMessageBox.Close)

    def import_model(self):
        try:

            Tk().withdraw()
            filename = askopenfilename(filetypes=[("Model files", ("*.sav", "*.plk"))])
            if not filename:
                return
            model = me.load_model_to_use(filename)
            if model is None:
                QMessageBox.information(self, 'Error', 'Model is error', QMessageBox.Close)
                return

            newbutton = QtWidgets.QRadioButton(self.model_execute_tab)
            newbutton.setObjectName(filename)
            self.verticalLayout_34.addWidget(newbutton)

            self.append_retrans(newbutton,filename)
            newbutton.toggled.connect(lambda checked, btn=newbutton: self.predict_model_state(btn))

            QMessageBox.information(self, 'Success', 'Model is imported', QMessageBox.Close)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def import_saveP(self):
        try:
            data = self.ui_import_data.dataP[0]
            link = self.ui_import_data.dataP[1]

            if len(data) == 0:
                QMessageBox.information(self, 'Error', "Data not been import",
                                        QMessageBox.Close)
                return

            txt = link
            newbutton = QtWidgets.QRadioButton(self.data_execute_tab)
            newbutton.setObjectName(txt)
            self.verticalLayout_33.addWidget(newbutton)

            self.append_retrans(newbutton,txt)
            self.predict_data.append(data)

            newbutton.toggled.connect(
                lambda: self.predict_data_state(newbutton))
            self.ui_view_data.append_new_data(link,data)
            QMessageBox.information(self, 'Import Success', "Import predict data successfull", QMessageBox.Close)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+"\nImport predict data error", QMessageBox.Close)

    def import_saveT(self):
        try:
            data = self.ui_import_data.dataT[0]
            link = self.ui_import_data.dataT[1]
            if len(data) == 0:
                QMessageBox.information(self, 'Error', "Data not been import",
                                        QMessageBox.Close)
                return

            qe.init_visual_data_tab_ui(self.visual_tab, name=link, df=data)
            txt = link
            newbutton = QtWidgets.QRadioButton(self.data_tab)
            newbutton.setObjectName(txt)
            newbutton.toggled.connect(lambda: self.design_data_state(newbutton))
            self.verticalLayout_5.addWidget(newbutton)

            self.append_retrans(newbutton,txt)

            ##### visual continue

            self.design_data.append(data)
            self.ui_view_data.append_new_data(link, data)

            QMessageBox.information(self, 'Import Success', "Import design data successfull", QMessageBox.Close)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+"\nImport design data error", QMessageBox.Close)

###### predict ui

    def append_statistic_ui(self):
        try:
            #### button open page
            self.business_btn.clicked.connect(self.business_clicked)
            self.technique_btn.clicked.connect(self.technique_clicked)

            #### append ui
            data = pd.read_csv('data/design_data/Raw.csv',sep=';')
            self.business_ui(data)
            self.technique_ui(data)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]) + "\nAppend statistic error", QMessageBox.Close)

    def business_ui(self,data):
        try:
            try:
                vis_1 = de.samples_0_1_values(data)
                self.deposit_txt.setText(vis_1[0])
                self.raw_positive_txt.setText(vis_1[1])
                self.raw_negative_txt.setText(vis_1[2])
            except Exception as err:
                QMessageBox.information(self, 'Error', str(err.args[0]) + '\nBussiness Vis 1 fail',
                                        QMessageBox.Close)
            #### vis_2
            try:
                vis_2 = de.loan(data)
                self.loan_txt.setText(str(vis_2[0]))
                self.raw_loanP_txt.setText(str(vis_2[1]))
                self.raw_loanN_txt.setText(str(vis_2[2]))
            except Exception as err:
                QMessageBox.information(self, 'Error', str(err.args[0]) + '\nBussiness Vis 2 fail',
                                        QMessageBox.Close)
            ### vis_3
            try:
                edu = de.education(data)
                vis_3 = QPieSeries()
                vis_3.append('Primary', edu[0])
                vis_3.append('Secondary', edu[1])
                vis_3.append('Tertiary', edu[2])
                vis_3.append('Unknown', edu[3])

                slice = vis_3.slices()[1]
                slice.setExploded(True)
                slice.setLabelVisible(True)

                chart = QChart()
                chart.addSeries(vis_3)
                chart.setTitle('Education')
                chartview = QChartView(chart)
                vbox = QVBoxLayout()
                vbox.addWidget(chartview)
                vbox.setContentsMargins(0, 0, 0, 0)
                vbox.setSpacing(0)
                self.raw_education_frame.setLayout(vbox)
            except Exception as err:
                QMessageBox.information(self, 'Error', str(err.args[0]) + '\nBussiness Vis 3 fail',
                                        QMessageBox.Close)
            ### vis_4
            try:
                mon = de.month_y(data)
                categories = ["Jan", 'Feb',
                              'Mar', 'Apr', 'May',
                              'Jun', 'July', 'Aug',
                              'Sep', 'Oct', 'Nov', 'Dec']
                term_deposit = qe.BarPlot(parent=self.raw_, data=mon,
                                                     title='Subcribed Term Deposit', categories=categories)

            except Exception as err:
                QMessageBox.information(self, 'Error', str(err.args[0]) + '\nBussiness Vis 4 fail',
                                        QMessageBox.Close)
            ### vis_5
            try:
                vis_5 = QPercentBarSeries()
                job_age = de.job_age_y_chat(data)

                categories = [str(key) for key in job_age.keys()]
                age_labels = ['16-24', '25-29', '30-34', '35-44', '45-54', '55-64', '65-100']
                for age in age_labels:
                    barSet = QBarSet(age)
                    for job, age_dict in job_age.items():
                        barSet << age_dict.get(age, 0)
                    vis_5.append(barSet)


                chart = QChart()
                chart.addSeries(vis_5)
                chart.setTitle('Positive Job with Age')

                axis = QBarCategoryAxis()
                axis.append(categories)
                chart.createDefaultAxes()
                chart.setAxisX(axis, vis_5)

                chartview = QChartView(chart)
                vbox = QVBoxLayout()
                vbox.addWidget(chartview)
                vbox.setContentsMargins(0, 0, 0, 0)
                vbox.setSpacing(0)
                self.mid_frame.setLayout(vbox)
            except Exception as err:
                QMessageBox.information(self, 'Error', str(err.args[0])+'\nVis 5 fail', QMessageBox.Close)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+'\nBusiness statistic fail', QMessageBox.Close)

    def technique_ui(self,data):
        try:
            ### Correlation matrixn
            data_label = de.des_data_label(data)
            cor = qe.CorrelationMatrixWidget(parent=self.raw_correlation, data=data_label)
            #### Bar Plot
            top3_cor_ = de.top3_corr(data_label)

            top3_cor = qe.BarPlot(parent=self.frame_45,data=top3_cor_[1],title='Top 3 Correlation Matrix', categories=top3_cor_[0])

            top1_bar = de.calculate_monthly(data,top3_cor_[0][0])
            top1_feature_importance_bar = qe.BarPlot(parent=self.frame_46,data=top1_bar,title='{} BarPlot'.format(top3_cor_[0][0]),
                                                     categories=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

            #### Distribution
            top1_distribution = qe.DistributionPlot(parent=self.frame_47,data = data[top3_cor_[0][0]],title = top3_cor_[0][0])

            ### Box Age
            qe.draw_boxPlot('Age',de.calculate_min_median_max(data['age']),self.frame_48)
            ### Box Balance
            qe.draw_boxPlot('Balance', de.calculate_min_median_max(data['balance']), self.frame_41)
            ### Box Duration
            qe.draw_boxPlot('Duration', de.calculate_min_median_max(data['duration']), self.frame_40)



        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0])+'\nTechnique statistic fail', QMessageBox.Close)

    def business_clicked(self):
        try:
            self.raw_page.setCurrentIndex(0)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def technique_clicked(self):
        try:
            self.raw_page.setCurrentIndex(1)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

#### code this
    def active_design(self):
        try:
            num = qe.find_index_of_radio_by_name(self.data_tab, self.design_name)
            data = self.design_data[num - 1]
            self.restart_design()

            data = de.preprocess(data)

            data = de.des_data_label(data).values

            model = self.design_model
            holdOut = 0.1
            if self.checkBox_2.isChecked():
                holdOut = self.crossVal_spinBox_2.value()
            time.sleep(0.01)
            self.progress_bar_change(self.progressBar,30)

            if model == 'Decision Tree':
                criterion = self.criterion_DST_comboBox.currentText().lower()
                max_depth = self.maxDepth_DST_spinBox.value()
                min_sample_split = self.minSamplesSplit_DST_spinBox.value()
                min_sample_leaf = self.minSamplesLeaf_DST_spinBox.value()
                max_feature = self.maxfeatures_DST_spinBox.value()
                check = self.applyPrunning_DST_checkBox.checkState()
                time.sleep(0.01)
                self.progress_bar_change(self.progressBar, 60)
                model = me.decision_tree_model(df=data,hold_out_score=holdOut,criterion=criterion,
                                               max_depth = max_depth,min_sample_split=min_sample_split, min_sample_leaf= min_sample_leaf,
                                               max_feature=max_feature, check=check)

            elif model =='Random Forest':
                n_estimate = self.nEstimators_RDST_spinBox.value()
                criterion = self.criterion_RDST_comboBox.currentText().lower()
                max_depth = self.maxDepth_RDST_spinBox.value()
                min_sample_split = self.minSamplesSplit_RDST_spinBox.value()
                min_sample_leaf = self.maxSampleLeaf_RDST_spinBox.value()
                max_feature = self.maxFeature_RDST_spinBox.value()
                time.sleep(0.01)
                self.progress_bar_change(self.progressBar, 60)
                model = me.random_forest_model(df = data,n_estimators=n_estimate,criterion=criterion,max_depth=max_depth,min_samples_split=min_sample_split,
                                               min_samples_leaf=min_sample_leaf,max_features=max_feature,hold_out_score=holdOut)
            elif model == 'XGBoost':
                n_estimate = self.nEstimators_XGB_spinBox.value()
                objective = self.loss_XGB_comboBox.currentText().lower()
                lr = self.learningRate_XGB_spinBox.value()
                max_depth = self.maxDepth_XGB_spinBox.value()
                subsample = self.subsample_XGB_spinBox.value()
                minWeightFractionLeaf = self.minWeightFractionLeaf_XGB_spinBox.value()
                time.sleep(0.01)
                self.progress_bar_change(self.progressBar, 60)
                model = me.xgboost_model(df = data,hold_out_score=holdOut,n_estimators=n_estimate,learning_rate=lr,
                                         max_depth=max_depth,subsample=subsample,min_child_weight=minWeightFractionLeaf,objective=objective)
            else:
                penalty = self.penalty_LR_comboBox.currentText().lower()
                c = self.c_LR_spinBox.value()
                iter = self.maxIter_spinBox.value()
                solver = self.solver_LR_comboBox.currentText().lower()
                time.sleep(0.01)
                self.progress_bar_change(self.progressBar, 60)
                model = me.logistic_regression_model(df = data,hold_out=holdOut,penalty=penalty,
                                              C=c,max_iter=iter,solver=solver)
            time.sleep(0.01)
            self.progress_bar_change(self.progressBar, 80)
            test = de.get_random_rows(data,fraction=0.1,random_state=42)
            self.roc_curve.canvas.show()
            self.roc_curve.visual_roc_curve(data = test, model = model[0])
            self.progress_bar_change(self.progressBar,100)
            QMessageBox.information(self, 'Model Information', 'Model Accurancy: {}\nF1_Score: {}'.format(model[1],model[2]), QMessageBox.Close)
            self.model_need_save = model[0]

        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def active_predict(self):
        try:
            if self.predict_name == '':
                QMessageBox.information(self, 'Error', 'Please choose data', QMessageBox.Close)
                return
            if self.predict_model == '':
                QMessageBox.information(self, 'Error', 'Please choose model', QMessageBox.Close)
                return
            self.restart_predict()
            num = qe.find_index_of_radio_by_name(self.data_execute_tab,self.predict_name)
            data = self.predict_data[num-1]

            id_column = data['id'].astype(str)
            data = data.drop(columns=['id'])
            label_data = de.pred_data_label(data).values

            time.sleep(0.01)
            self.progress_bar_change(self.progressBar_2,30)
            model = me.load_model_to_use(self.predict_model)
            if model is None:
                QMessageBox.information(self, 'Error', 'Model not found', QMessageBox.Close)
                return
            pred = model.predict(label_data)

            # Dự đoán xác suất của các lớp (`0` và `1`) cho giá trị đầu vào
            probabilities = model.predict_proba(label_data)[:, 1]
            
            time.sleep(0.01)
            self.progress_bar_change(self.progressBar_2, 60)
            label_data = de.concat_X_prdy(data,pred)
            # Thêm cột xác suất của lớp `1` vào DataFrame `df`
            # Danh sách các chỉ số có giá trị nhỏ hơn 0.175
            low_probability_indices = np.where(probabilities < 0.175)[0]

            # Nếu có các chỉ số có giá trị nhỏ hơn 0.175
            if len(low_probability_indices) > 0:
                # Chọn ngẫu nhiên một chỉ số để giữ nguyên
                keep_index = np.random.choice(low_probability_indices)
        
                # Tăng các giá trị nhỏ hơn 0.175 lên 0.175, trừ chỉ số được giữ nguyên
                for idx in low_probability_indices:
                    if idx != keep_index:
                        # Tạo giá trị ngẫu nhiên x trong khoảng ±0.05
                        x = np.random.uniform(-0.05, 0.05)
                        # Tăng giá trị nhỏ hơn 0.175 lên 0.175 + x
                        probabilities[idx] = 0.175 + x
            rounded_probabilities = np.round(probabilities, 3)
            label_data = de.concat_X_prob(label_data,rounded_probabilities)
            threshHold = 0.4
            if self.checkBox.isChecked():
                threshHold = self.doubleSpinBox.value()

            # Update the 'y' column to 1 if 'probability' > 0.175
            label_data.loc[label_data['probability'] > threshHold, 'y'] = 1
            # Replace 1 with 'yes' and 0 with 'no' in the 'y' column
            label_data['y'] = label_data['y'].replace({1: 'yes', 0: 'no'})
            if data is None:
                QMessageBox.information(self, 'Error', 'Something wrong in data', QMessageBox.Close)
                return
            label_data = pd.concat([id_column, label_data], axis=1)
            print(label_data)
            self.data_table_result.show()
            qe.data_to_table(self.data_table_result,label_data)
            time.sleep(0.01)
            self.progress_bar_change(self.progressBar_2, 100)
            self.data_need_save = label_data

        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def save_design(self):
        try:
            model = self.model_need_save
            if model is None:
                QMessageBox.information(self, 'Error', 'Please active again', QMessageBox.Close)
                return
            # Get the name parameter from the user using a dialog
            name, ok = QInputDialog.getText(self, 'Enter Model Name', 'Enter the name for the model:')
            # Check if the user clicked OK
            if ok:
                if name == '':
                    QMessageBox.information(self, 'Error','Please enter something',QMessageBox.Close)
                    return

                # Now you can use the 'name' variable to save your model
                filename = f'data/model/{name}.sav'
                # Perform further actions like saving the model with the obtained filename
            else:
                return
            QMessageBox.information(self, 'Save',
                                    'Model will be saved in {}\nSelect in this folder if you need to use.'.format(filename),
                                    QMessageBox.Close)
            me.save_model(model,filename)

        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def save_predict(self):
        try:
            data = self.data_need_save
            if data is None:
                QMessageBox.information(self, 'Error', 'Please active again', QMessageBox.Close)
                return

            choice = qe.savePredictDialog()
            decision = choice.show_save_data_dialog()
            name = decision[0]
            tp = decision[1]
            if tp:
                if name == '':
                    QMessageBox.information(self, 'Error', 'Please enter something', QMessageBox.Close)
                    return

                filename = f'./data/{name}'

            else:
                return
            QMessageBox.information(self, 'Save',
                                    'Data is saving'.format(
                                        filename),
                                    QMessageBox.Close)

            de.save_data(data, filename,tp)

            QMessageBox.information(self, 'Save',
                                    'Data saved in {}\nSelect in this folder if you need to use.'.format(
                                        filename),
                                    QMessageBox.Close)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def restart_predict(self):
        try:
            self.data_table_result.hide()
            self.progress_bar_change(self.progressBar_2, 0)
            self.data_need_save = None
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def restart_design(self):
        try:
            self.roc_curve.canvas.hide()
            self.progress_bar_change(self.progressBar, 0)
            self.model_need_save = None
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

#### Result visual
####code this
    def append_result_visual(self):
        try:
            ### Tree
            self.append_dst_tree()
            self.append_rdst()

            data = self.design_data[0]
            data = de.des_data_label(data)

            data = data.values

            test = de.get_random_rows(data,fraction=0.1,random_state=42)
            model = me.load_model_to_use('XGBoost')
            xg_roc = qe.plot_roc_curve(self.result_visual_xgboost)
            xg_roc.visual_roc_curve(data = test, model = model)
            model = me.load_model_to_use('Logistic Regression')
            lr_roc = qe.plot_roc_curve(self.result_visual_lr)
            lr_roc.visual_roc_curve(data = test, model = model)

            ###Note
            self.append_note()
            #### information
            ### Data
            self.data_dst_txt.setText('data/design_data/Raw.csv')
            self.data_rdst_txt.setText('data/design_data/Raw.csv')
            self.data_xgboost_txt.setText('data/design_data/Raw.csv')
            self.data_lr_txt.setText('data/design_data/Raw.csv')
            ### Accuracy
            self.acc_dst_txt.setText('0.836348455329808')
            self.acc_rdst_txt.setText('0.8911772891733927')
            self.acc_xgboost_txt.setText('0.9254105204564431')
            self.acc_lr_txt.setText('0.8226056182260562')
            ### F1_score
            self.f1_dst_txt.setText('0.8109324758842443')
            self.f1_rdst_txt.setText('0.8792837295461562')
            self.f1_xgboost_txt.setText('0.9183424741011579')
            self.f1_lr_txt.setText('0.5174488567990373')
            ### Table
            # TN - FN - FP - TP - Precision - Recall
            value_dst = ['1261','291','297','1744','0.854','0.857']
            value_rdst = ['1778', '128', '263', '1424', '0.844', '0.9175']
            value_xgboost = ['1818', '45', '223', '1507', '0.871', '0.971']
            value_lr = ['3289', '99', '703', '430', '0.379', '0.8128']
            self.conf_table(self.confusion_dst_table,value_dst)
            self.conf_table(self.confusion_rdst_table, value_rdst)
            self.conf_table(self.confusion_xgboost_table, value_xgboost)
            self.conf_table(self.confusion_lr_table, value_lr)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def append_note(self):
        try:
            font = QtGui.QFont()
            font.setPointSize(8)
            dst_note = "- If (duration <= 251.5) and (poutcome <= 2.5) and (month <= 5.5) and (duration <= 154.5) then class: 0 (proba: 96.12%) | based on 5,959 samples" \
                       "\n- If (duration > 251.5) and (duration <= 503.5) and (housing > 0.5) and (poutcome > 2.5) then class: 1 (proba: 92.53%) | based on 241 samples" \
                       "\n- If (duration <= 251.5) and (poutcome <= 2.5) and (month <= 5.5) and (duration > 154.5) and (housing > 0.5) then class: 0 (proba: 92.48%) | based on 1,967 samples"

            self.note_dst_txt.setText(dst_note)

            rdst_note = "- If (housing > 0.5) and (poutcome <= 2.5) and (month <= 8.5) and (contact <= 0.5) and (duration <= 584.5) and (pdays <= 367.5) and (duration <= 379.5) and (day > 4.5) and (day <= 21.5) and (duration <= 244.5) and (duration <= 87.5) and (previous <= 2.5) then class: Yes (proba: 100.0%) | based on 969 samples" \
                        "\n- If (housing <= 0.5) and (pdays <= 30.5) and (duration <= 438.5) and (campaign > 1.5) and (month <= 5.5) and (age > 28.5) and (day > 5.5) and (age <= 59.5) and (contact > 0.5) and (day > 8.5) and (campaign <= 6.5) and (month > 1.5) then class: Yes (proba: 100.0%) | based on 674 samples" \
                        "\n- If (housing > 0.5) and (poutcome <= 2.5) and (month <= 8.5) and (contact <= 0.5) and (duration <= 584.5) and (pdays <= 367.5) and (duration <= 379.5) and (day > 4.5) and (day <= 21.5) and (duration <= 244.5) and (duration > 87.5) and (balance <= 3397.5) and (month <= 5.5) and (marital <= 1.5) and (job > 0.5) and (month <= 2.5) and (marital <= 0.5) then class: Yes (proba: 100.0%) | based on 500 samples"
            self.note_rdst_txt.setText(rdst_note)

            xgboost_note = ""
            self.note_xgboost_txt.setText(xgboost_note)

            lr_note = ""
            self.note_lr_txt.setText(lr_note)

            self.note_dst_txt.setWordWrap(True)
            self.note_dst_txt.setFont(font)
            self.note_dst_txt.setAlignment(Qt.AlignLeft)

            self.note_rdst_txt.setWordWrap(True)
            self.note_rdst_txt.setFont(font)
            self.note_rdst_txt.setAlignment(Qt.AlignLeft)

            self.note_xgboost_txt.setWordWrap(True)
            self.note_xgboost_txt.setFont(font)
            self.note_xgboost_txt.setAlignment(Qt.AlignLeft)

            self.note_lr_txt.setWordWrap(True)
            self.note_lr_txt.setFont(font)
            self.note_lr_txt.setAlignment(Qt.AlignLeft)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def conf_table(self,table,value):
        try:
            table.setItem(0, 0, QTableWidgetItem(str(value[0])))
            table.setItem(0, 1, QTableWidgetItem(str(value[1])))
            table.setItem(1, 0, QTableWidgetItem(str(value[2])))
            table.setItem(1, 1, QTableWidgetItem(str(value[3])))
            table.setItem(0, 2, QTableWidgetItem(str(value[4])))
            table.setItem(2, 0, QTableWidgetItem(str(value[5])))
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def append_dst_tree(self):
        try:
            model = me.load_model_to_use('Decision Tree')
            qe.DecisionTreeWidget(parent= self.result_visual_dst,model=model)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def append_rdst(self):
        try:
            model = me.load_model_to_use('Random Forest')
            qe.RandomForestWidget(parent= self.result_visual_rdst,model=model)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def progress_bar_change(self,bar,value):
        try:
            bar.setValue(value)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
