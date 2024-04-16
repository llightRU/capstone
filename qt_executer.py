from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QSizePolicy, QWidget, QPushButton, QGraphicsScene, \
    QGraphicsView, QGraphicsProxyWidget, QDialog, QHBoxLayout, QLineEdit, QLabel
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QBarSet, QPercentBarSeries, QBarCategoryAxis, QBoxPlotSeries, \
    QBoxSet
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import data_executer as de
import model_executer as me
import os
import shutil
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QVBoxLayout
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_graphviz
import xgboost as xgb
from sklearn.metrics import roc_curve, auc


class savePredictDialog(QWidget):
    def __init__(self):
        super().__init__()

    def show_save_data_dialog(self):
        # Create a custom dialog for the save data option
        dialog = QDialog()
        dialog.setWindowTitle("Save Data Option")

        # Create a vertical layout
        layout = QVBoxLayout()

        # Add a label for the prompt
        prompt_label = QLabel("Enter the name for the data:")
        layout.addWidget(prompt_label)

        # Add a line edit for entering the name
        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)

        # Add buttons for the options
        avg_button = QPushButton("Data only Yes")
        default_button = QPushButton("All data")
        cancel_button = QPushButton("Cancel")

        # Add the buttons to the layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(avg_button)
        button_layout.addWidget(default_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        # Add layout to the dialog
        dialog.setLayout(layout)

        # Initialize variables to capture the choice
        choice = None

        # Connect buttons to set choice and accept the dialog
        def set_choice_and_accept(selected_choice):
            nonlocal choice
            choice = selected_choice
            dialog.accept()

        avg_button.clicked.connect(lambda: set_choice_and_accept('yes'))
        default_button.clicked.connect(lambda: set_choice_and_accept('all'))
        cancel_button.clicked.connect(dialog.reject)

        # Execute the dialog and wait for the user to respond
        result = dialog.exec_()

        if result == QDialog.Accepted:
            # Return the name and the choice
            return self.name_input.text(), choice
        else:
            # If the dialog is rejected, return None
            return None, None


class FillNullDialog(QWidget):
    def __init__(self):
        super().__init__()


    def show_fill_null_dialog(self):
        # Tạo hộp thoại với ba nút tùy chọn
        message_box = QMessageBox()
        message_box.setWindowTitle("Fill Null Values")
        message_box.setText("How would you like to execute null values?")

        # Thêm các nút tùy chọn
        avg_button = message_box.addButton("Avg of Data", QMessageBox.AcceptRole)
        clear_button = message_box.addButton("Clear Null", QMessageBox.AcceptRole)
        cancel_button = message_box.addButton("Cancel", QMessageBox.RejectRole)

        # Hiển thị hộp thoại và đợi người dùng chọn một trong các nút
        message_box.exec()

        # Xác định nút nào đã được nhấn
        if message_box.clickedButton() == avg_button:
            return 'avg_of_data'
        elif message_box.clickedButton() == clear_button:
            return 'clear'
        else:
            return 'cancel'


class ZoomableView(QtWidgets.QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)

        # Set up the view
        self.setRenderHints(QtGui.QPainter.Antialiasing)
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)

    def wheelEvent(self, event):
        # Calculate the zoom factor based on the mouse wheel movement
        delta = event.angleDelta().y()
        zoom_factor = 1.0015 ** delta

        # Apply the scaling to zoom in or out
        self.scale(zoom_factor, zoom_factor)

class plot_roc_curve(QWidget):
    def __init__(self, parent=None,title=''):
        super().__init__(parent)
        self.title = title
        self.figure = Figure(figsize=(10, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        parent.setLayout(layout)

    def visual_roc_curve(self,data,model):
        self.figure.clear()
        if not model:

            return
        if data.size == 0:

            return

        X_test = data[:, :-1]
        y_test = data[:, -1]
        # Predict probabilities on the test set
        y_prob = model.predict_proba(X_test)[:, 1]  # Probability of positive class

        # Calculate ROC curve and AUC
        fpr, tpr, thresholds = roc_curve(y_test, y_prob)
        roc_auc = auc(fpr, tpr)

        # Plot the ROC curve and AUC
        ax = self.figure.add_subplot(111)
        ax.plot(fpr, tpr, color='blue', label=f'ROC curve (AUC = {roc_auc:.2f})')
        ax.plot([0, 1], [0, 1], color='gray', linestyle='--')
        ax.set_xlim([0, 1])
        ax.set_ylim([0, 1])
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.set_title('ROC Curve')
        ax.legend(loc='lower right')

        # Redraw the canvas to show the plot
        self.canvas.draw()
    def clear_parent_interface(self):
        """Clear the parent interface by removing all widgets from its layout."""
        layout = self.parent.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                # Recursively clear any nested layouts
                sub_layout = item.layout()
                if sub_layout:
                    self.clear_layout(sub_layout)

    def clear_layout(self, layout):
        """Recursively clear a layout by removing all its widgets."""
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                sub_layout = item.layout()
                if sub_layout:
                    self.clear_layout(sub_layout)

def init_visual_data_tab_ui(visual_tab, name, df):
    visual_raw_tab = QtWidgets.QWidget()
    visual_raw_tab.setMinimumSize(QtCore.QSize(0, 0))
    visual_raw_tab.setObjectName(name + "visual_raw_tab")
    verticalLayout_31 = QtWidgets.QVBoxLayout(visual_raw_tab)
    verticalLayout_31.setContentsMargins(0, 0, 0, 0)
    verticalLayout_31.setSpacing(0)
    verticalLayout_31.setObjectName(name + "verticalLayout_31")
    mod_tab = QtWidgets.QFrame(visual_raw_tab)
    sizePolicy = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        mod_tab.sizePolicy().hasHeightForWidth())
    mod_tab.setSizePolicy(sizePolicy)
    mod_tab.setMinimumSize(QtCore.QSize(0, 50))
    mod_tab.setMaximumSize(QtCore.QSize(1666666, 0))
    mod_tab.setFrameShape(QtWidgets.QFrame.StyledPanel)
    mod_tab.setFrameShadow(QtWidgets.QFrame.Raised)
    mod_tab.setObjectName(name + "mod_tab")
    horizontalLayout_49 = QtWidgets.QHBoxLayout(mod_tab)
    horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
    horizontalLayout_49.setSpacing(0)
    horizontalLayout_49.setObjectName(name + "horizontalLayout_49")
    business_btn = QtWidgets.QPushButton(mod_tab)
    sizePolicy = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        business_btn.sizePolicy().hasHeightForWidth())
    business_btn.setSizePolicy(sizePolicy)
    business_btn.setMinimumSize(QtCore.QSize(70, 0))
    business_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
    business_btn.setObjectName(name + "business_btn")
    horizontalLayout_49.addWidget(
        business_btn, 0, QtCore.Qt.AlignRight)
    technique_btn = QtWidgets.QPushButton(mod_tab)
    sizePolicy = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        technique_btn.sizePolicy().hasHeightForWidth())
    technique_btn.setSizePolicy(sizePolicy)
    technique_btn.setMinimumSize(QtCore.QSize(70, 0))
    technique_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
    technique_btn.setObjectName(name + "technique_btn")
    horizontalLayout_49.addWidget(
        technique_btn, 0, QtCore.Qt.AlignLeft)
    verticalLayout_31.addWidget(
        mod_tab, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
    raw_page = QtWidgets.QStackedWidget(visual_raw_tab)
    raw_page.setObjectName(name + "raw_page")
    raw_business = QtWidgets.QWidget()
    raw_business.setObjectName(name + "raw_business")
    verticalLayout_37 = QtWidgets.QVBoxLayout(raw_business)
    verticalLayout_37.setContentsMargins(0, 0, 0, 0)
    verticalLayout_37.setSpacing(0)
    verticalLayout_37.setObjectName(name + "verticalLayout_37")
    frame_20 = QtWidgets.QFrame(raw_business)
    frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_20.setObjectName(name + "frame_20")
    horizontalLayout_52 = QtWidgets.QHBoxLayout(frame_20)
    horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
    horizontalLayout_52.setSpacing(0)
    horizontalLayout_52.setObjectName(name + "horizontalLayout_52")
    frame_24 = QtWidgets.QFrame(frame_20)
    frame_24.setMaximumSize(QtCore.QSize(16777215, 166666))
    frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_24.setObjectName(name + "frame_24")
    verticalLayout_38 = QtWidgets.QVBoxLayout(frame_24)
    verticalLayout_38.setContentsMargins(0, 0, 0, 0)
    verticalLayout_38.setSpacing(0)
    verticalLayout_38.setObjectName(name + "verticalLayout_38")
    frame_27 = QtWidgets.QFrame(frame_24)
    frame_27.setMaximumSize(QtCore.QSize(16777215, 1666666))
    frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_27.setObjectName(name + "frame_27")
    verticalLayout_39 = QtWidgets.QVBoxLayout(frame_27)
    verticalLayout_39.setContentsMargins(0, 0, 0, 0)
    verticalLayout_39.setSpacing(0)
    verticalLayout_39.setObjectName(name + "verticalLayout_39")
    frame_29 = QtWidgets.QFrame(frame_27)
    frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_29.setObjectName(name + "frame_29")
    verticalLayout_40 = QtWidgets.QVBoxLayout(frame_29)
    verticalLayout_40.setContentsMargins(0, 0, 0, 0)
    verticalLayout_40.setSpacing(3)
    verticalLayout_40.setObjectName(name + "verticalLayout_40")
    label_32 = QtWidgets.QLabel(frame_29)
    font = QtGui.QFont()
    font.setPointSize(10)
    label_32.setFont(font)
    label_32.setObjectName(name + "label_32")
    verticalLayout_40.addWidget(
        label_32, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
    line_32 = QtWidgets.QFrame(frame_29)
    line_32.setFrameShape(QtWidgets.QFrame.HLine)
    line_32.setFrameShadow(QtWidgets.QFrame.Sunken)
    line_32.setObjectName(name + "line_32")
    verticalLayout_40.addWidget(line_32)
    verticalLayout_39.addWidget(frame_29, 0, QtCore.Qt.AlignTop)
    frame_30 = QtWidgets.QFrame(frame_27)
    sizePolicy = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        frame_30.sizePolicy().hasHeightForWidth())
    frame_30.setSizePolicy(sizePolicy)
    frame_30.setMaximumSize(QtCore.QSize(16777215, 1666666))
    frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_30.setObjectName(name + "frame_30")
    verticalLayout_41 = QtWidgets.QVBoxLayout(frame_30)
    verticalLayout_41.setContentsMargins(0, 0, 0, 0)
    verticalLayout_41.setSpacing(0)
    verticalLayout_41.setObjectName(name + "verticalLayout_41")
    deposit_txt = QtWidgets.QLabel(frame_30)
    deposit_txt.setObjectName(name + "deposit_txt")
    verticalLayout_41.addWidget(
        deposit_txt, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
    verticalLayout_39.addWidget(frame_30, 0, QtCore.Qt.AlignTop)
    frame_31 = QtWidgets.QFrame(frame_27)
    sizePolicy = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        frame_31.sizePolicy().hasHeightForWidth())
    frame_31.setSizePolicy(sizePolicy)
    frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_31.setObjectName(name + "frame_31")
    horizontalLayout_53 = QtWidgets.QHBoxLayout(frame_31)
    horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
    horizontalLayout_53.setSpacing(0)
    horizontalLayout_53.setObjectName(name + "horizontalLayout_53")
    frame_32 = QtWidgets.QFrame(frame_31)
    frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_32.setObjectName(name + "frame_32")
    verticalLayout_42 = QtWidgets.QVBoxLayout(frame_32)
    verticalLayout_42.setObjectName(name + "verticalLayout_42")
    label_46 = QtWidgets.QLabel(frame_32)
    label_46.setObjectName(name + "label_46")
    verticalLayout_42.addWidget(label_46)
    label_47 = QtWidgets.QLabel(frame_32)
    label_47.setObjectName(name + "label_47")
    verticalLayout_42.addWidget(label_47)
    horizontalLayout_53.addWidget(frame_32)
    frame_33 = QtWidgets.QFrame(frame_31)
    frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_33.setObjectName(name + "frame_33")
    verticalLayout_43 = QtWidgets.QVBoxLayout(frame_33)
    verticalLayout_43.setObjectName(name + "verticalLayout_43")
    raw_positive_txt = QtWidgets.QLabel(frame_33)
    raw_positive_txt.setObjectName(name + "raw_positive_txt")
    verticalLayout_43.addWidget(
        raw_positive_txt, 0, QtCore.Qt.AlignRight)
    raw_negative_txt = QtWidgets.QLabel(frame_33)
    raw_negative_txt.setObjectName(name + "raw_negative_txt")
    verticalLayout_43.addWidget(
        raw_negative_txt, 0, QtCore.Qt.AlignRight)
    horizontalLayout_53.addWidget(frame_33)
    verticalLayout_39.addWidget(
        frame_31, 0, QtCore.Qt.AlignBottom)
    verticalLayout_38.addWidget(frame_27)
    frame_28 = QtWidgets.QFrame(frame_24)
    frame_28.setMaximumSize(QtCore.QSize(16777215, 1666666))
    frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_28.setObjectName(name + "frame_28")
    verticalLayout_48 = QtWidgets.QVBoxLayout(frame_28)
    verticalLayout_48.setContentsMargins(0, 0, 0, 0)
    verticalLayout_48.setSpacing(0)
    verticalLayout_48.setObjectName(name + "verticalLayout_48")
    frame_34 = QtWidgets.QFrame(frame_28)
    frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_34.setObjectName(name + "frame_34")
    verticalLayout_44 = QtWidgets.QVBoxLayout(frame_34)
    verticalLayout_44.setContentsMargins(0, 0, 0, 0)
    verticalLayout_44.setSpacing(3)
    verticalLayout_44.setObjectName(name + "verticalLayout_44")
    label_50 = QtWidgets.QLabel(frame_34)
    font = QtGui.QFont()
    font.setPointSize(10)
    label_50.setFont(font)
    label_50.setObjectName(name + "label_50")
    verticalLayout_44.addWidget(
        label_50, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
    line_33 = QtWidgets.QFrame(frame_34)
    line_33.setFrameShape(QtWidgets.QFrame.HLine)
    line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
    line_33.setObjectName(name + "line_33")
    verticalLayout_44.addWidget(line_33)
    verticalLayout_48.addWidget(frame_34)
    frame_35 = QtWidgets.QFrame(frame_28)
    sizePolicy = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        frame_35.sizePolicy().hasHeightForWidth())
    frame_35.setSizePolicy(sizePolicy)
    frame_35.setMaximumSize(QtCore.QSize(16777215, 1666666))
    frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_35.setObjectName(name + "frame_35")
    verticalLayout_45 = QtWidgets.QVBoxLayout(frame_35)
    verticalLayout_45.setContentsMargins(0, 0, 0, 0)
    verticalLayout_45.setSpacing(0)
    verticalLayout_45.setObjectName(name + "verticalLayout_45")
    loan_txt = QtWidgets.QLabel(frame_35)
    loan_txt.setObjectName(name + "loan_txt")
    verticalLayout_45.addWidget(
        loan_txt, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
    verticalLayout_48.addWidget(frame_35)
    frame_36 = QtWidgets.QFrame(frame_28)
    sizePolicy = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        frame_36.sizePolicy().hasHeightForWidth())
    frame_36.setSizePolicy(sizePolicy)
    frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_36.setObjectName(name + "frame_36")
    horizontalLayout_54 = QtWidgets.QHBoxLayout(frame_36)
    horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
    horizontalLayout_54.setSpacing(0)
    horizontalLayout_54.setObjectName(name + "horizontalLayout_54")
    frame_37 = QtWidgets.QFrame(frame_36)
    frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_37.setObjectName(name + "frame_37")
    verticalLayout_46 = QtWidgets.QVBoxLayout(frame_37)
    verticalLayout_46.setObjectName(name + "verticalLayout_46")
    label_51 = QtWidgets.QLabel(frame_37)
    label_51.setObjectName(name + "label_51")
    verticalLayout_46.addWidget(label_51)
    label_52 = QtWidgets.QLabel(frame_37)
    label_52.setObjectName(name + "label_52")
    verticalLayout_46.addWidget(label_52)
    horizontalLayout_54.addWidget(frame_37)
    frame_38 = QtWidgets.QFrame(frame_36)
    frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_38.setObjectName(name + "frame_38")
    verticalLayout_47 = QtWidgets.QVBoxLayout(frame_38)
    verticalLayout_47.setObjectName(name + "verticalLayout_47")
    raw_loanP_txt = QtWidgets.QLabel(frame_38)
    raw_loanP_txt.setObjectName(name + "raw_loanP_txt")
    verticalLayout_47.addWidget(
        raw_loanP_txt, 0, QtCore.Qt.AlignRight)
    raw_loanN_txt = QtWidgets.QLabel(frame_38)
    raw_loanN_txt.setObjectName(name + "raw_loanN_txt")
    verticalLayout_47.addWidget(
        raw_loanN_txt, 0, QtCore.Qt.AlignRight)
    horizontalLayout_54.addWidget(frame_38)
    verticalLayout_48.addWidget(frame_36)
    verticalLayout_38.addWidget(frame_28)
    horizontalLayout_52.addWidget(frame_24)
    raw_education_frame = QtWidgets.QFrame(frame_20)
    raw_education_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    raw_education_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    raw_education_frame.setObjectName(name + "raw_education_frame")
    horizontalLayout_52.addWidget(raw_education_frame)
    raw_ = QtWidgets.QFrame(frame_20)
    raw_.setFrameShape(QtWidgets.QFrame.StyledPanel)
    raw_.setFrameShadow(QtWidgets.QFrame.Raised)
    raw_.setObjectName(name + "raw_")
    horizontalLayout_52.addWidget(raw_)
    verticalLayout_37.addWidget(frame_20, 0, QtCore.Qt.AlignTop)
    mid_frame = QtWidgets.QFrame(raw_business)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(mid_frame.sizePolicy().hasHeightForWidth())
    mid_frame.setSizePolicy(sizePolicy)
    mid_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    mid_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    mid_frame.setObjectName(name + "mid_frame")
    verticalLayout_37.addWidget(mid_frame)
    raw_page.addWidget(raw_business)
    raw_technique = QtWidgets.QWidget()
    raw_technique.setObjectName(name + "raw_technique")
    verticalLayout_49 = QtWidgets.QVBoxLayout(raw_technique)
    verticalLayout_49.setContentsMargins(0, 0, 0, 0)
    verticalLayout_49.setSpacing(0)
    verticalLayout_49.setObjectName(name + "verticalLayout_49")
    frame_39 = QtWidgets.QFrame(raw_technique)
    frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_39.setObjectName(name + "frame_39")
    horizontalLayout_56 = QtWidgets.QHBoxLayout(frame_39)
    horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
    horizontalLayout_56.setSpacing(0)
    horizontalLayout_56.setObjectName(name + "horizontalLayout_56")
    raw_correlation = QtWidgets.QFrame(frame_39)
    raw_correlation.setFrameShape(QtWidgets.QFrame.StyledPanel)
    raw_correlation.setFrameShadow(QtWidgets.QFrame.Raised)
    raw_correlation.setObjectName(name + "raw_correlation")
    horizontalLayout_56.addWidget(raw_correlation)
    frame_42 = QtWidgets.QFrame(frame_39)
    sizePolicy = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        frame_42.sizePolicy().hasHeightForWidth())
    frame_42.setSizePolicy(sizePolicy)
    frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_42.setObjectName(name + "frame_42")
    verticalLayout_50 = QtWidgets.QVBoxLayout(frame_42)
    verticalLayout_50.setContentsMargins(0, 0, 0, 0)
    verticalLayout_50.setSpacing(5)
    verticalLayout_50.setObjectName(name + "verticalLayout_50")
    raw_line_corr = QtWidgets.QFrame(frame_42)
    raw_line_corr.setFrameShape(QtWidgets.QFrame.StyledPanel)
    raw_line_corr.setFrameShadow(QtWidgets.QFrame.Raised)
    raw_line_corr.setObjectName(name + "raw_line_corr")
    horizontalLayout_57 = QtWidgets.QHBoxLayout(raw_line_corr)
    horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
    horizontalLayout_57.setSpacing(3)
    horizontalLayout_57.setObjectName(name + "horizontalLayout_57")
    frame_45 = QtWidgets.QFrame(raw_line_corr)
    frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_45.setObjectName(name + "frame_45")
    horizontalLayout_57.addWidget(frame_45)
    frame_46 = QtWidgets.QFrame(raw_line_corr)
    frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_46.setObjectName(name + "frame_46")
    horizontalLayout_57.addWidget(frame_46)
    frame_47 = QtWidgets.QFrame(raw_line_corr)
    frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_47.setObjectName(name + "frame_47")
    horizontalLayout_57.addWidget(frame_47)
    verticalLayout_50.addWidget(raw_line_corr)
    raw_boxPlot = QtWidgets.QFrame(frame_42)
    raw_boxPlot.setFrameShape(QtWidgets.QFrame.StyledPanel)
    raw_boxPlot.setFrameShadow(QtWidgets.QFrame.Raised)
    raw_boxPlot.setObjectName(name + "raw_boxPlot")
    horizontalLayout_58 = QtWidgets.QHBoxLayout(raw_boxPlot)
    horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
    horizontalLayout_58.setSpacing(3)
    horizontalLayout_58.setObjectName(name + "horizontalLayout_58")
    frame_48 = QtWidgets.QFrame(raw_boxPlot)
    frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_48.setObjectName(name + "frame_48")
    horizontalLayout_58.addWidget(frame_48)
    frame_41 = QtWidgets.QFrame(raw_boxPlot)
    frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_41.setObjectName(name + "frame_41")
    horizontalLayout_58.addWidget(frame_41)
    frame_40 = QtWidgets.QFrame(raw_boxPlot)
    frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_40.setObjectName(name + "frame_40")
    horizontalLayout_58.addWidget(frame_40)
    verticalLayout_50.addWidget(raw_boxPlot)
    horizontalLayout_56.addWidget(frame_42)
    verticalLayout_49.addWidget(frame_39)
    raw_page.addWidget(raw_technique)
    verticalLayout_31.addWidget(raw_page)
    visual_tab.addTab(visual_raw_tab, "")

    _translate = QtCore.QCoreApplication.translate
    business_btn.setText(_translate("MainWindow", "Business"))
    technique_btn.setText(_translate("MainWindow", "Technique"))
    label_32.setText(_translate(
        "MainWindow", "Subscribed term deposit"))
    deposit_txt.setText(_translate("MainWindow", "TextLabel"))
    label_46.setText(_translate("MainWindow", "Positive"))
    label_47.setText(_translate("MainWindow", "Negative"))
    raw_positive_txt.setText(_translate("MainWindow", "TextLabel"))
    raw_negative_txt.setText(_translate("MainWindow", "TextLabel"))
    label_50.setText(_translate("MainWindow", "Loan"))
    loan_txt.setText(_translate("MainWindow", "TextLabel"))
    label_51.setText(_translate("MainWindow", "Positive subcribed"))
    label_52.setText(_translate("MainWindow", "Negative subcribed"))
    raw_loanP_txt.setText(_translate("MainWindow", "TextLabel"))
    raw_loanN_txt.setText(_translate("MainWindow", "TextLabel"))
    visual_tab.setTabText(visual_tab.indexOf(
        visual_raw_tab), _translate("MainWindow", name))

    ##### function
    business_btn.clicked.connect(lambda: raw_page.setCurrentIndex(0))
    technique_btn.clicked.connect(lambda: raw_page.setCurrentIndex(1))
    vis_1 = de.samples_0_1_values(df)
    deposit_txt.setText(vis_1[0])
    raw_positive_txt.setText(vis_1[1])
    raw_negative_txt.setText(vis_1[2])
    vis_2 = de.loan(df)
    loan_txt.setText(str(vis_2[0]))
    raw_loanP_txt.setText(str(vis_2[1]))
    raw_loanN_txt.setText(str(vis_2[2]))

    edu = de.education(df)
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
    raw_education_frame.setLayout(vbox)

    mon = de.month_y(df)
    categories = ["Jan", 'Feb',
                  'Mar', 'Apr', 'May',
                  'Jun', 'July', 'Aug',
                  'Sep', 'Oct', 'Nov', 'Dec']
    term_deposit = BarPlot(parent=raw_, data=mon,
                              title='Subcribed Term Deposit', categories=categories)

    ### vis_5

    vis_5 = QPercentBarSeries()
    job_age = de.job_age_y_chat(df)

    categories = [str(key) for key in job_age.keys()]
    age_labels = ['0_30', '31_40', '41_50', '51_60', '61_70', '71_80', '81_inf']
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
    mid_frame.setLayout(vbox)
    ### Correlation matrixn

    data_label = de.des_data_label(df)

    cor = CorrelationMatrixWidget(parent=raw_correlation, data=data_label)
    #### Bar Plot
    top3_cor_ = de.top3_corr(data_label)

    top3_cor = BarPlot(parent=frame_45, data=top3_cor_[1], title='Top 3 Correlation Matrix',
                          categories=top3_cor_[0])


    top1_bar = de.calculate_monthly(df, top3_cor_[0][0])

    top1_feature_importance_bar = BarPlot(parent=frame_46, data=top1_bar,
                                             title='{} BarPlot'.format(top3_cor_[0][0]),
                                             categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                                                         'Oct', 'Nov', 'Dec'])

    #### Distribution
    top1_distribution = DistributionPlot(parent=frame_47, data=df[top3_cor_[0][0]], title=top3_cor_[0][0])

    ### Box Age
    draw_boxPlot('Age', de.calculate_min_median_max(df['age']), frame_48)
    ### Box Balance
    draw_boxPlot('Balance', de.calculate_min_median_max(df['balance']), frame_41)
    ### Box Duration
    draw_boxPlot('Duration', de.calculate_min_median_max(df['duration']), frame_40)

def new_model(result_tab,name,link):
    try:
        result_dst_tab = QtWidgets.QWidget()
        result_dst_tab.setObjectName("result_dst_tab")
        horizontalLayout_48 = QtWidgets.QHBoxLayout(result_dst_tab)
        horizontalLayout_48.setObjectName("horizontalLayout_48")
        result_visual_dst = QtWidgets.QFrame(result_dst_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            result_visual_dst.sizePolicy().hasHeightForWidth())
        result_visual_dst.setSizePolicy(sizePolicy)
        result_visual_dst.setMinimumSize(QtCore.QSize(300, 0))
        result_visual_dst.setFrameShape(QtWidgets.QFrame.StyledPanel)
        result_visual_dst.setFrameShadow(QtWidgets.QFrame.Raised)
        result_visual_dst.setObjectName("result_visual_dst")
        horizontalLayout_48.addWidget(result_visual_dst)
        frame_17 = QtWidgets.QFrame(result_dst_tab)
        frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_17.setObjectName("frame_17")
        verticalLayout_28 = QtWidgets.QVBoxLayout(frame_17)
        verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        verticalLayout_28.setSpacing(10)
        verticalLayout_28.setObjectName("verticalLayout_28")
        note_grp_4 = QtWidgets.QGroupBox(frame_17)
        note_grp_4.setMinimumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        note_grp_4.setFont(font)
        note_grp_4.setObjectName("note_grp_4")
        verticalLayout_29 = QtWidgets.QVBoxLayout(note_grp_4)
        verticalLayout_29.setObjectName("verticalLayout_29")
        note_dst_txt = QtWidgets.QLabel(note_grp_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        note_dst_txt.setFont(font)
        note_dst_txt.setObjectName("note_dst_txt")
        verticalLayout_29.addWidget(
            note_dst_txt, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        verticalLayout_28.addWidget(note_grp_4)
        inf_lr_grp_4 = QtWidgets.QGroupBox(frame_17)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            inf_lr_grp_4.sizePolicy().hasHeightForWidth())
        inf_lr_grp_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        inf_lr_grp_4.setFont(font)
        inf_lr_grp_4.setObjectName("inf_lr_grp_4")
        verticalLayout_30 = QtWidgets.QVBoxLayout(inf_lr_grp_4)
        verticalLayout_30.setObjectName("verticalLayout_30")
        frame_18 = QtWidgets.QFrame(inf_lr_grp_4)
        frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_18.setObjectName("frame_18")
        horizontalLayout_47 = QtWidgets.QHBoxLayout(frame_18)
        horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_47.setSpacing(0)
        horizontalLayout_47.setObjectName("horizontalLayout_47")
        frame_19 = QtWidgets.QFrame(frame_18)
        frame_19.setMinimumSize(QtCore.QSize(150, 0))
        frame_19.setMaximumSize(QtCore.QSize(16666666, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        frame_19.setFont(font)
        frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_19.setObjectName("frame_19")
        formLayout_4 = QtWidgets.QFormLayout(frame_19)
        formLayout_4.setContentsMargins(10, 10, 0, 0)
        formLayout_4.setHorizontalSpacing(50)
        formLayout_4.setVerticalSpacing(20)
        formLayout_4.setObjectName("formLayout_4")
        label_43 = QtWidgets.QLabel(frame_19)
        font = QtGui.QFont()
        font.setPointSize(12)
        label_43.setFont(font)
        label_43.setObjectName("label_43")
        formLayout_4.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, label_43)
        data_dst_txt = QtWidgets.QLabel(frame_19)
        font = QtGui.QFont()
        font.setPointSize(12)
        data_dst_txt.setFont(font)
        data_dst_txt.setObjectName("data_dst_txt")
        formLayout_4.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, data_dst_txt)
        label_44 = QtWidgets.QLabel(frame_19)
        font = QtGui.QFont()
        font.setPointSize(12)
        label_44.setFont(font)
        label_44.setObjectName("label_44")
        formLayout_4.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, label_44)
        acc_dst_txt = QtWidgets.QLabel(frame_19)
        font = QtGui.QFont()
        font.setPointSize(12)
        acc_dst_txt.setFont(font)
        acc_dst_txt.setObjectName("acc_dst_txt")
        formLayout_4.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, acc_dst_txt)
        label_45 = QtWidgets.QLabel(frame_19)
        font = QtGui.QFont()
        font.setPointSize(12)
        label_45.setFont(font)
        label_45.setObjectName("label_45")
        formLayout_4.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, label_45)
        f1_dst_txt = QtWidgets.QLabel(frame_19)
        font = QtGui.QFont()
        font.setPointSize(12)
        f1_dst_txt.setFont(font)
        f1_dst_txt.setObjectName("f1_dst_txt")
        formLayout_4.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, f1_dst_txt)
        horizontalLayout_47.addWidget(
            frame_19, 0, QtCore.Qt.AlignTop)
        verticalLayout_30.addWidget(frame_18, 0, QtCore.Qt.AlignTop)
        confusion_dst_table = QtWidgets.QTableWidget(inf_lr_grp_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            confusion_dst_table.sizePolicy().hasHeightForWidth())
        confusion_dst_table.setSizePolicy(sizePolicy)
        confusion_dst_table.setMinimumSize(QtCore.QSize(400, 0))
        confusion_dst_table.setAutoScroll(True)
        confusion_dst_table.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        confusion_dst_table.setObjectName("confusion_dst_table")
        confusion_dst_table.setColumnCount(3)
        confusion_dst_table.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        confusion_dst_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        confusion_dst_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        confusion_dst_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        confusion_dst_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        confusion_dst_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        confusion_dst_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        confusion_dst_table.setItem(2, 1, item)
        verticalLayout_30.addWidget(confusion_dst_table)
        verticalLayout_28.addWidget(inf_lr_grp_4)
        horizontalLayout_48.addWidget(frame_17)
        result_tab.addTab(result_dst_tab, "")


        _translate = QtCore.QCoreApplication.translate
        note_grp_4.setTitle(_translate("MainWindow", "Note"))
        note_dst_txt.setText(_translate("MainWindow", "TextLabel"))
        inf_lr_grp_4.setTitle(_translate("MainWindow", "Information"))
        label_43.setText(_translate("MainWindow", "Data:"))
        data_dst_txt.setText(_translate("MainWindow", "..."))
        label_44.setText(_translate("MainWindow", "Accuracy:"))
        acc_dst_txt.setText(_translate("MainWindow", "..."))
        label_45.setText(_translate("MainWindow", "F1-Score:"))
        f1_dst_txt.setText(_translate("MainWindow", "..."))
        item = confusion_dst_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Pred False"))
        item = confusion_dst_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pred True"))
        item = confusion_dst_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Class Recall"))
        item = confusion_dst_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "True False"))
        item = confusion_dst_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "True True"))
        item = confusion_dst_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Class Precision"))
        __sortingEnabled = confusion_dst_table.isSortingEnabled()
        confusion_dst_table.setSortingEnabled(False)
        confusion_dst_table.setSortingEnabled(__sortingEnabled)
        result_tab.setTabText(result_tab.indexOf(
            result_dst_tab), _translate("MainWindow", name))

    except Exception as err:
        print(err)

class CorrelationMatrixWidget:
    def __init__(self, parent=None, width=10, height=10, dpi=100, data=None):
        self.data = data

        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        parent.setLayout(layout)

        self.plot_correlation_matrix()

    def plot_correlation_matrix(self):
        if self.data is None:
            return

        corr_matrix = self.data.corr()  # Calculate correlation matrix

        cax = self.axes.matshow(corr_matrix, cmap='coolwarm')
        self.figure.colorbar(cax)
        num_columns = len(self.data.columns)
        self.axes.set_xticks(np.arange(num_columns))
        self.axes.set_yticks(np.arange(num_columns))
        self.axes.set_xticklabels(list(self.data.columns), rotation=90)
        self.axes.set_yticklabels(list(self.data.columns))

        self.canvas.draw()


def draw_boxPlot(title, lst, frame):
    series = QBoxPlotSeries()
    set = QBoxSet()
    set.append(lst)
    series.append(set)

    chart = QChart()
    chart.setTitle(title)

    chart.addSeries(series)
    chart.createDefaultAxes()
    chart.legend().setVisible(True)
    chart.legend().setAlignment(Qt.AlignBottom)

    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)

    vbox = QVBoxLayout()
    vbox.addWidget(chartView)

    frame.setLayout(vbox)


def find_index_of_widget(parent, widget_to_find):
    for index, child in enumerate(parent.children()):
        if child == widget_to_find:
            return index
    return -1  # Widget not found


def find_index_of_radio_by_name(parent, widget_name_to_find):
    for index, child in enumerate(parent.children()):
        if isinstance(child, QtWidgets.QRadioButton):

            if child.text() == widget_name_to_find:
                return index
    return -1  # Widget not found


def data_to_table(table, data):
    table.clearContents()
    table.setRowCount(0)
    # Số cột trong bảng
    num_columns = data.shape[1] if len(data.shape) > 1 else 0

    # Số hàng muốn hiển thị (trong trường hợp này, bạn lấy 20 hàng đầu tiên)
    num_rows = min(20, data.shape[0])

    # Chèn các hàng và điền dữ liệu vào bảng
    for i in range(num_rows):
        table.insertRow(i)  # Thêm một hàng vào bảng
        for j in range(num_columns):
            # Lấy giá trị từ DataFrame bằng cách sử dụng iloc
            value = data.iloc[i, j]

            # Chuyển đổi giá trị thành chuỗi và điền vào bảng
            item = QtWidgets.QTableWidgetItem(str(value))
            table.setItem(i, j, item)

            # Đặt cờ để mục là không thể chỉnh sửa
            item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)


def data_to_view_table(table, data):
    table.clearContents()
    table.setRowCount(0)
    # Số cột trong bảng
    num_columns = data.shape[1] if len(data.shape) > 1 else 0

    # Chèn các hàng và điền dữ liệu vào bảng
    for i in range(data.shape[0]):
        table.insertRow(i)  # Thêm một hàng vào bảng
        for j in range(num_columns):
            # Lấy giá trị từ DataFrame bằng cách sử dụng iloc
            value = data.iloc[i, j]

            # Chuyển đổi giá trị thành chuỗi và điền vào bảng
            item = QtWidgets.QTableWidgetItem(str(value))
            table.setItem(i, j, item)

            # Đặt cờ để mục là không thể chỉnh sửa
            item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)


def cop_file(win, tp, source_path):
    destination_folder = ''
    if tp == 'predict':
        destination_folder = '/data/predict_data/'
    else:
        destination_folder = '/data/design_data/'
    # Kiểm tra xem thư mục đích có tồn tại không, nếu không thì tạo mới
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Tạo đường dẫn đích với tên tệp giống với tên tệp nguồn
    destination_path = os.path.join(destination_folder, os.path.basename(source_path))

    try:
        # Sao chép tệp từ nguồn đến đích
        shutil.copyfile(source_path, destination_path)
        QMessageBox.information(win, 'Success', "Import Sucessful", QMessageBox.Close)
    except FileNotFoundError:
        QMessageBox.information(win, 'Error', "Can not find file", QMessageBox.Close)
    except PermissionError:
        QMessageBox.information(win, 'Error', "Can't access file", QMessageBox.Close)
    except shutil.SameFileError:
        QMessageBox.information(win, 'Error', "Name existence", QMessageBox.Close)
    except Exception as e:
        QMessageBox.information(win, 'Error', str(e.args[0]), QMessageBox.Close)


class DistributionPlot(QWidget):
    def __init__(self, parent=None, data=None, title=''):
        super().__init__(parent)
        self.data = data
        self.title = title
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        parent.setLayout(layout)

        self.plot_distribution()

    def plot_distribution(self):
        if self.data is None:
            return

        ax = self.figure.add_subplot(111)
        ax.hist(self.data, bins=30, density=False, alpha=0.8, color='blue')
        ax.set_title('Distribution {} Plot'.format(self.title))
        ax.set_xlabel('Values')
        ax.set_ylabel('Density')

        self.canvas.draw()


class BarPlot(QWidget):
    def __init__(self, parent=None, data=None, title='', categories=[]):
        super().__init__(parent)
        self.data = data
        self.title = title
        self.categories = categories
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)
        parent.setLayout(layout)

        self.plot_bar()

    def plot_bar(self):
        if self.data == None:
            return
        ax = self.figure.add_subplot(111)
        ax.bar(self.categories, self.data, color='blue')
        ax.set_title('Bar Plot {}'.format(self.title))
        ax.set_xlabel('Categories')
        ax.set_ylabel('Values')

        self.canvas.draw()

class DecisionTreeWidget(QWidget):
    def __init__(self, parent=None, model=None):
        super().__init__(parent)

        # Create a QGraphicsScene and QGraphicsView
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, parent)

        # Configure the view
        self.view.setRenderHint(QtGui.QPainter.Antialiasing)
        self.view.setAlignment(Qt.AlignCenter)
        self.view.setDragMode(QGraphicsView.ScrollHandDrag)

        # Create a matplotlib figure and canvas
        self.figure = Figure(figsize=(8, 8), dpi=200)
        self.canvas = FigureCanvas(self.figure)

        # Add the canvas to a QGraphicsProxyWidget and add it to the scene
        proxy_widget = QGraphicsProxyWidget()
        proxy_widget.setWidget(self.canvas)
        self.scene.addItem(proxy_widget)

        # Set up zoom buttons
        self.zoom_in_button = QPushButton("Zoom In", self)
        self.zoom_out_button = QPushButton("Zoom Out", self)

        # Connect buttons to zoom functions
        self.zoom_in_button.clicked.connect(self.zoom_in)
        self.zoom_out_button.clicked.connect(self.zoom_out)

        # Create layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.view)  # Add the QGraphicsView
        layout.addWidget(self.zoom_in_button)
        layout.addWidget(self.zoom_out_button)
        parent.setLayout(layout)

        # Plot decision tree if model provided
        if model:
            self.plot_decision_tree(model)
        self.canvas.resize(800,750)

    def plot_decision_tree(self, model):
        # Plot the decision tree using matplotlib
        ax = self.figure.add_subplot(111)
        plot_tree(model, ax=ax)

        # Adjust the layout and redraw the canvas
        self.figure.tight_layout()
        self.canvas.draw()

    def zoom_in(self):
        # Zoom in by scaling the QGraphicsView
        self.view.scale(1.2, 1.2)

    def zoom_out(self):
        # Zoom out by scaling the QGraphicsView
        self.view.scale(1 / 1.2, 1 / 1.2)


class RandomForestWidget(QWidget):
    def __init__(self, parent=None, model=None):
        super().__init__(parent)
        self.model = model
        # Tạo một đồ họa Matplotlib figure
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Thêm canvas vào layout
        # Tạo layout để chứa các thành phần đồ họa
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        parent.setLayout(layout)

        if model:
            self.plot_best_trees(model)

    def plot_best_trees(self, model):
        # Xóa nội dung đồ họa trước đó
        self.figure.clear()

        # Để lưu trữ điểm quan trọng của mỗi cây
        tree_importances = []

        # Tính tổng điểm quan trọng của từng cây trong mô hình
        for i, tree in enumerate(model.estimators_):
            # Tính tổng độ quan trọng của các đặc trưng
            total_importance = np.sum(tree.feature_importances_)
            # Lưu điểm quan trọng và chỉ số cây
            tree_importances.append((total_importance, i))

        # Sắp xếp cây dựa trên điểm quan trọng, giảm dần
        tree_importances.sort(reverse=True, key=lambda x: x[0])

        # Chọn 3 cây tốt nhất
        best_trees = tree_importances[:3]

        # Vẽ 3 cây tốt nhất
        for i, (importance, tree_index) in enumerate(best_trees):
            # Tạo một subplot mới cho mỗi cây được chọn
            ax = self.figure.add_subplot(1, 3, i + 1)
            # Vẽ cây được chọn
            plot_tree(model.estimators_[tree_index], ax=ax, filled=True, rounded=True)
            # Đặt tiêu đề cho cây
            ax.set_title(f'Cây {tree_index + 1} (Điểm quan trọng: {importance:.2f})')

        # Vẽ canvas
        self.canvas.draw()

class LogisticRegressionWidget(QWidget):
    def __init__(self, model=None, parent=None):
        super().__init__(parent)

        # Tạo một layout để chứa biểu đồ
        # Tạo một Figure và FigureCanvas
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        # Thêm canvas vào layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        parent.setLayout(layout)

        # Vẽ hồi quy logistic
        if model:
            self.plot_logistic_regression(model)

    def plot_logistic_regression(self, model):
        # Xóa nội dung cũ của biểu đồ
        self.figure.clear()

        # Tạo một trục (axis)
        ax = self.figure.add_subplot(111)

        # Tạo dữ liệu đầu vào với 16 đặc trưng giả lập
        # Bạn có thể thay đổi dải giá trị của 16 đặc trưng tùy ý
        X_values = np.random.uniform(low=-5, high=5, size=(100, 16))

        # Tính xác suất dự đoán của mô hình
        y_prob = model.predict_proba(X_values)[:, 1]

        # Vẽ đường cong dự đoán
        ax.plot(np.mean(X_values, axis=1), y_prob, color='red', label='Đường hồi quy logistic')

        # Thiết lập tiêu đề và nhãn trục
        ax.set_title('Hồi quy logistic')
        ax.set_xlabel('Tính năng trung bình')
        ax.set_ylabel('Xác suất')

        # Hiển thị chú thích
        ax.legend()

        # Vẽ canvas
        self.canvas.draw()

if __name__ == "__main__":
    class Ui_MainWindow(QMainWindow):
        def __init__(self, parent=None):
            super(Ui_MainWindow, self).__init__(parent)

        def setupUi(self):
            self.setObjectName("MainWindow")
            self.resize(809, 712)
            self.centralwidget = QtWidgets.QWidget()
            self.centralwidget.setObjectName("centralwidget")
            self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
            self.verticalLayout.setObjectName("verticalLayout")
            self.predict_table = QtWidgets.QTableWidget(self.centralwidget)
            self.predict_table.setMaximumSize(QtCore.QSize(16777215, 500))
            self.predict_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.predict_table.setObjectName("predict_table")
            self.predict_table.setColumnCount(16)
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
            self.verticalLayout.addWidget(self.predict_table)
            self.frame = QtWidgets.QFrame(self.centralwidget)
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.result_visual_dst = QtWidgets.QFrame(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.result_visual_dst.sizePolicy().hasHeightForWidth())
            self.result_visual_dst.setSizePolicy(sizePolicy)
            self.result_visual_dst.setMinimumSize(QtCore.QSize(300, 0))
            self.result_visual_dst.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.result_visual_dst.setFrameShadow(QtWidgets.QFrame.Raised)
            self.result_visual_dst.setObjectName("result_visual_dst")
            self.roc_chart_2 = QtWidgets.QFrame(self.frame)
            self.roc_chart_2.setMinimumSize(QtCore.QSize(0, 200))
            self.roc_chart_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.roc_chart_2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.roc_chart_2.setObjectName("roc_chart_2")
            self.horizontalLayout.addWidget(self.roc_chart_2)
            self.verticalLayout.addWidget(self.frame)
            self.setCentralWidget(self.centralwidget)

            #####
            self.test()
            #####
            self.retranslateUi()

        def retranslateUi(self):
            _translate = QtCore.QCoreApplication.translate
            self.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
            item.setText(_translate("MainWindow", "Poutcome"))

        def test(self):
            try:
                data = de.data_from_csv('data/predict_data/Raw.csv')
                data_to_table(self.predict_table,data)
            except Exception as err:
                print(err)

    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
