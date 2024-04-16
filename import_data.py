import pandas as pd
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import re
import qt_executer as qe
import data_executer as de
import validation as v

class Ui_MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(Ui_MainWindow,self).__init__(parent)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(808, 703)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/add.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setStyleSheet("QFrame#tab_frame,#raw_tab{\n"
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
                                         "QWidget#guild_tab{\n"
                                         "    background-image: url(:/images/back-ground.jpg);\n"
                                         "}\n"
                                         "QLabel#label_8{\n"
                                         "    color: blue;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_12 = QtWidgets.QFrame(self.frame)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout.addWidget(self.frame_12)
        self.tab_frame = QtWidgets.QFrame(self.frame)
        self.tab_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tab_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab_frame.setObjectName("tab_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.predict_btn = QtWidgets.QPushButton(self.tab_frame)
        self.predict_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.predict_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.predict_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.predict_btn.setObjectName("predict_btn")
        self.horizontalLayout_4.addWidget(
            self.predict_btn, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.design_btn = QtWidgets.QPushButton(self.tab_frame)
        self.design_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.design_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.design_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.design_btn.setObjectName("design_btn")
        self.horizontalLayout_4.addWidget(
            self.design_btn, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(
            self.tab_frame, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.guild_btn = QtWidgets.QPushButton(self.frame)
        self.guild_btn.setObjectName("guild_btn")
        self.horizontalLayout.addWidget(
            self.guild_btn, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.frame)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 650))
        self.stackedWidget.setObjectName("stackedWidget")
        self.guild_widget = QtWidgets.QWidget()
        self.guild_widget.setObjectName("guild_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.guild_widget)
        self.verticalLayout_2.setContentsMargins(6, 8, 6, 8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.guild_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        self.label_4 = QtWidgets.QLabel(self.guild_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.guild_widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignBottom)
        self.label_8 = QtWidgets.QLabel(self.guild_widget)
        self.label_8.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.stackedWidget.addWidget(self.guild_widget)
        self.predict_widget = QtWidgets.QWidget()
        self.predict_widget.setObjectName("predict_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.predict_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.predict_widget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(
            self.label_3, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(
            self.frame_2, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.predict_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.predict_table = QtWidgets.QTableWidget(self.frame_5)
        self.predict_table.setMaximumSize(QtCore.QSize(16777215, 500))
        self.predict_table.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.predict_table.setObjectName("predict_table")
        self.predict_table.setColumnCount(17)
        self.predict_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.predict_table.setHorizontalHeaderItem(16, item)
        self.horizontalLayout_7.addWidget(self.predict_table)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.predict_import_btn = QtWidgets.QPushButton(self.frame_6)
        self.predict_import_btn.setIcon(icon)
        self.predict_import_btn.setObjectName("predict_import_btn")
        self.verticalLayout_5.addWidget(self.predict_import_btn)
        self.predict_save_btn = QtWidgets.QPushButton(self.frame_6)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/save.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.predict_save_btn.setIcon(icon1)
        self.predict_save_btn.setObjectName("predict_save_btn")
        self.verticalLayout_5.addWidget(self.predict_save_btn)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.verticalLayout_3.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.predict_widget)
        self.train_widget = QtWidgets.QWidget()
        self.train_widget.setObjectName("train_widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.train_widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_7 = QtWidgets.QFrame(self.train_widget)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(
            self.label_6, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.train_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMinimumSize(QtCore.QSize(120, 0))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.train_table = QtWidgets.QTableWidget(self.frame_10)
        self.train_table.setMaximumSize(QtCore.QSize(16777215, 500))
        self.train_table.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.train_table.setObjectName("train_table")
        self.train_table.setColumnCount(17)
        self.train_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(16, item)
        self.horizontalLayout_11.addWidget(self.train_table)
        self.frame_9 = QtWidgets.QFrame(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.train_import_btn = QtWidgets.QPushButton(self.frame_9)
        self.train_import_btn.setIcon(icon)
        self.train_import_btn.setObjectName("train_import_btn")
        self.verticalLayout_4.addWidget(self.train_import_btn)
        self.train_save_btn = QtWidgets.QPushButton(self.frame_9)
        self.train_save_btn.setIcon(icon1)
        self.train_save_btn.setObjectName("train_save_btn")
        self.verticalLayout_4.addWidget(self.train_save_btn)
        self.horizontalLayout_11.addWidget(self.frame_9)
        self.horizontalLayout_9.addWidget(self.frame_10)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.stackedWidget.addWidget(self.train_widget)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        self.stackedWidget.setCurrentIndex(0)
        self.append_ui()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "ImportData"))
        self.predict_btn.setText(_translate("MainWindow", "Predict"))
        self.design_btn.setText(_translate("MainWindow", "Design"))
        self.guild_btn.setText(_translate("MainWindow", "Guild"))
        self.label.setText(_translate("MainWindow", "To predict whether customers will decide to deposit money into a bank savings account or not, we need to use an appropriate dataset and apply a prediction model. Below is a guide on how to import and prepare data for the model training process:"))
        self.label_4.setText(_translate("MainWindow", "The data should contain two main parts: the prediction data and the training data. Here are some basic requirements for each part:\n"
                                        "\n"
                                        "Prediction Data:\n"
                                        "\n"
                                        "Should contain 16 columns: Id, Age, Job, Marital, Education, Default, Balance, Housing, Loan, Contact, Day, Month, Campaign, Pdays, Poutcome.\n"
                                        "This data will be used to predict whether a customer decides to deposit money into a bank savings account or not.\n"
                                        "Training Data:\n"
                                        "\n"
                                        "Consists of 16 columns: Age, Job, Marital, Education, Default, Balance, Housing, Loan, Contact, Day, Month, Campaign, Pdays, Poutcome, \"Choice\".\n"
                                        "The \"Choice\" column is the target column that we want the model to predict. In this case, it will contain information about the customer\'s decision to deposit money into a bank savings account or not."))
        self.label_2.setText(_translate("MainWindow", "\n"
                                        "The data acquisition process can be described as follows:\n"
                                        "\n"
                                        "Import Button: When users click on this button, they can upload a dataset from their computer to the software. Subsequently, the system will check the data, ensuring its format and integrity. If necessary, users can add data to the existing dataset.\n"
                                        "\n"
                                        "Save Button: Once the data has been checked and confirmed to be accurate, users can press the Save button to store the data into the database. Afterward, the data will be ready for further processing and analysis steps in the workflow."))
        self.label_8.setText(_translate(
            "MainWindow", "The data DEMO is in data folder"))
        self.label_3.setText(_translate("MainWindow", "Predict"))
        item = self.predict_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.predict_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Age"))
        item = self.predict_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Job"))
        item = self.predict_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Marital"))
        item = self.predict_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Education"))
        item = self.predict_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Default"))
        item = self.predict_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Balance"))
        item = self.predict_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Housing"))
        item = self.predict_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Loan"))
        item = self.predict_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Contact"))
        item = self.predict_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Day"))
        item = self.predict_table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Month"))
        item = self.predict_table.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Duration"))
        item = self.predict_table.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Campaign"))
        item = self.predict_table.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Pdays"))
        item = self.predict_table.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Previous"))
        item = self.predict_table.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Poutcome"))
        self.predict_import_btn.setText(_translate("MainWindow", "Import"))
        self.predict_save_btn.setText(_translate("MainWindow", "Save"))
        self.label_6.setText(_translate("MainWindow", "Design"))
        item = self.train_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Age"))
        item = self.train_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Job"))
        item = self.train_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Marital"))
        item = self.train_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Education"))
        item = self.train_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Default"))
        item = self.train_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Balance"))
        item = self.train_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Housing"))
        item = self.train_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Loan"))
        item = self.train_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Contact"))
        item = self.train_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Day"))
        item = self.train_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Month"))
        item = self.train_table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Duration"))
        item = self.train_table.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Campaign"))
        item = self.train_table.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Pdays"))
        item = self.train_table.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Previous"))
        item = self.train_table.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Poutcome"))
        item = self.train_table.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Term Deposit"))
        self.train_import_btn.setText(_translate("MainWindow", "Import"))
        self.train_save_btn.setText(_translate("MainWindow", "Save"))

    def append_ui(self):
        try:
            self.dataP = []
            self.dataT = []
            self. guild_btn.clicked.connect(self.guildTab_click)
            self.predict_btn.clicked.connect(self.predictTab_click)
            self.design_btn.clicked.connect(self.designTab_click)
            self.predict_import_btn.clicked.connect(self.importP_click)
            self.train_import_btn.clicked.connect(self.importT_click)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]) +'\nSomething gone wrong', QMessageBox.Close)

    def guildTab_click(self):
        try:
            self.stackedWidget.setCurrentIndex(0)
        except Exception as err:
            QMessageBox.information(self,'Error',str(err.args[0]),QMessageBox.Close)

    def predictTab_click(self):
        try:
            self.stackedWidget.setCurrentIndex(1)
        except Exception as err:
            QMessageBox.information(self,'Error',str(err.args[0]),QMessageBox.Close)

    def designTab_click(self):
        try:
            self.stackedWidget.setCurrentIndex(2)
        except Exception as err:
            QMessageBox.information(self,'Error',str(err.args[0]),QMessageBox.Close)

    def importP_click(self):
        try:
            self.dataP = []
            self.predict_table.clearContents()
            Tk().withdraw()
            filename = askopenfilename(filetypes=[("CSV file", "*.csv"), ("Excel file", "*.xlsx")])
            if filename == '':
                return
            duoi = ''.join(re.findall("[.]{1}\w+$", filename))
            if duoi == '.csv':
                raw_data = de.data_from_csv(filename)
            else:
                raw_data = de.data_from_excel(filename)
            if 'id' not in raw_data.columns:
                raw_data['id'] = ''

            id_column = raw_data['id'].astype(str)
            data = raw_data.drop(columns=['id'])

            data = v.file_check_label('predict',data)
            if data is None:
                QMessageBox.information(self,'Format Error','\nFile import is wrong format\nPlease follow instruction in guild tab\nDemo file is in data/predict_data/ folder',QMessageBox.Close)
                return

            if len(data) <1:
                QMessageBox.information(self,'Data Error','\nWe need larger data (>1 samples)',QMessageBox.Close)
                return

            if v.find_columns_with_only_nulls(data):
                QMessageBox.information(self,'Data Error','\nHave col with only null',QMessageBox.Close)
                return

            col_num = v.find_null_columns(data)
            if col_num:
                dialog = qe.FillNullDialog()
                decision = dialog.show_fill_null_dialog()
                if decision == 'cancel':
                    return
                elif decision == 'clear':
                    data =de.clear_null_predict(data,id_column)
                    id_column = data[1]
                    data = data[0]
                    if len(data) <1:
                        QMessageBox.information(self,'Data Error','\nWe need larger data (>1 samples)',QMessageBox.Close)
                        return
                else:
                    data = v.fill_nulls_based_on_type(data)
            print('after fill null')
            print(data)
            data = v.check_value(data,'predict')
            if data is None:
                QMessageBox.information(self, 'Data Error',
                                        '\nData must be follow the format',
                                        QMessageBox.Close)
                return
            data = pd.concat([id_column, data], axis=1)
            self.dataP = [data,filename]
            qe.data_to_table(self.predict_table,data)
            QMessageBox.information(self, 'Success', 'Import Predict file success', QMessageBox.Close)
        except Exception as err:
            QMessageBox.information(self,'Error',str(err.args[0])+'\nImport Predict file fail',QMessageBox.Close)

    def importT_click(self):
        try:
            self.dataT = []
            self.train_table.clearContents()
            Tk().withdraw()
            #filename = askopenfilename(filetypes=[("CSV file", "*.csv")])
            filename = askopenfilename(filetypes=[("CSV file","*.csv"),("Excel file", "*.xlsx")])
            if filename == '':
                return
            duoi = ''.join(re.findall("[.]{1}\w+$", filename))
            if duoi == '.csv':
                data = de.data_from_csv(filename)
            else:
                data = de.data_from_excel(filename)
            print(data)
            data = v.file_check_label('design',data)
            if data is None:
                QMessageBox.information(self,'Format Error','\nFile import is wrong format\nPlease follow instruction in guild tab\nDemo file is in data/design_data/ folder',QMessageBox.Close)
                return

            if len(data) <100:
                QMessageBox.information(self,'Data Error','\nWe need larger data (>100 samples)',QMessageBox.Close)
                return

            if v.find_columns_with_only_nulls(data):
                QMessageBox.information(self,'Data Error','\nHave col with only null',QMessageBox.Close)
                return

            col_num = v.find_null_columns(data)
            if col_num:
                dialog = qe.FillNullDialog()
                decision = dialog.show_fill_null_dialog()
                if decision == 'cancel':
                    return
                elif decision == 'clear':
                    data = de.clear_null_design(data)
                    if len(data) <100:
                        QMessageBox.information(self,'Data Error','\nWe need larger data (>100 samples)',QMessageBox.Close)
                        return
                else:
                    data = v.fill_nulls_based_on_type(data)
            print('after fill null')
            print(data)
            data = v.check_value(data,'design')
            if data is None:
                QMessageBox.information(self, 'Data Error',
                                        '\nData must be follow the format',
                                        QMessageBox.Close)
                return
            self.dataT = [data,filename]
            qe.data_to_table(self.train_table, data)
            QMessageBox.information(self, 'Success', 'Import Train file success', QMessageBox.Close)
        except Exception as err:
            QMessageBox.information(self,'Error',str(err.args[0])+'\nImport Train file fail',QMessageBox.Close)


if __name__ == "__main__":
    import sys
    sys.path.append('icon')
    import designer
    app = QtWidgets.QApplication(sys.argv)
    ui_import = Ui_MainWindow()
    ui_import.setupUi()
    ui_import.show()
    sys.exit(app.exec_())
