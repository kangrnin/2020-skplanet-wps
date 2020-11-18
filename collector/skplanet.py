# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'skplanet.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from os import listdir
from os.path import isdir, join, splitext
from pathlib import Path

class Ui_MainWindow(object):
    def __init__(self):
        self.script_path = Path(__file__).parent
        self.data_path = (self.script_path/"../signal_data").resolve()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.dialog = QDialog()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ScanButton = QtWidgets.QPushButton(self.centralwidget)
        self.ScanButton.setGeometry(QtCore.QRect(310, 470, 150, 46)) 
        self.ScanButton.setObjectName("ScanButton")

        self.building_ID = QtWidgets.QLabel(self.centralwidget)
        self.building_ID.setGeometry(QtCore.QRect(110, 70, 241, 24)) 
        self.building_ID.setObjectName("building_ID")
        self.RP_ID = QtWidgets.QLabel(self.centralwidget)
        self.RP_ID.setGeometry(QtCore.QRect(120, 240, 241, 24))
        self.RP_ID.setObjectName("RP_ID")
        #
        self.building_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.building_comboBox.setGeometry(QtCore.QRect(120, 100, 261, 41)) 
        self.building_comboBox.setObjectName("building_comboBox")
        self.RP_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.RP_comboBox.setGeometry(QtCore.QRect(120, 280, 261, 41))
        self.RP_comboBox.setObjectName("RP_comboBox")
        #
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(120, 190, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.building_newbutton = QtWidgets.QPushButton(self.centralwidget)
        self.building_newbutton.setGeometry(QtCore.QRect(440, 90, 150, 46))
        self.building_newbutton.setObjectName("building_newbutton")
        self.RP_newbutton = QtWidgets.QPushButton(self.centralwidget)
        self.RP_newbutton.setGeometry(QtCore.QRect(450, 280, 150, 46))
        self.RP_newbutton.setObjectName("RP_newbutton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 38))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.building_newbutton.clicked.connect(MainWindow.new_building)
        self.ScanButton.clicked.connect(MainWindow.scan)
        self.RP_newbutton.clicked.connect(MainWindow.new_rp)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        print(self.data_path)
        #
        self.building_comboBox.clear()
        for building in listdir(self.data_path):
            if isdir(join(self.data_path, building)):
                self.building_comboBox.addItem(building)
        
        self.building_comboBox.currentTextChanged.connect(self.onBuildingChanged)

    def onBuildingChanged(self, value):
        self.RP_comboBox.clear()
        for RP in listdir(join(self.data_path, value)):
            self.RP_comboBox.addItem(splitext(RP)[0])
    #
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ScanButton.setText(_translate("MainWindow", "scan"))
        self.building_ID.setText(_translate("MainWindow", "건물을 입력하시오"))
        self.RP_ID.setText(_translate("MainWindow", "구역을 입력하시오"))
        self.building_newbutton.setText(_translate("MainWindow", "new"))
        self.RP_newbutton.setText(_translate("MainWindow", "new"))

