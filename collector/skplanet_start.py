import sys, threading, time, random
import pyautogui
from skplanet import Ui_MainWindow
from PyQt5 import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox

from collector import collect
from pathlib import Path
import pandas as pd
from os import listdir
from os.path import isdir, join, splitext
from wifi_scan import get_wifis

from PyQt5 import QtTest

class indoor(QMainWindow,Ui_MainWindow): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
    def new_building(self):
        building_newButton= pyautogui.prompt(title='건물 추가',text='추가하려는 새로운 건물 이름을 입력하시오')
        position = building_newButton
        script_path = Path(__file__).parent
        data_path = script_path / '../signal_data'
        data_path.mkdir(parents=True, exist_ok=True)
        (data_path/position).mkdir(parents=True, exist_ok=True)
        self.building_comboBox.addItem(building_newButton)

    def new_rp(self):
        RP_newButton= pyautogui.prompt(title='구역 추가',text='추가하려는 새로운 구역 이름을 입력하시오')
        self.RP_comboBox.addItem(splitext(RP_newButton)[0])
    
    def sleep(self,n):
       QtTest.QTest.qWait(n*1000)

    def scanning(self):
        self.dialog.setStyleSheet("background-color: rgb(255, 255, 238);\n")
        i = 1
        c = 50
        A = 5
        B = A-2
        C = A-1
        while i < A:
            label0 = QLabel(f"{i}회 스캔중입니다.", self.dialog)
            label0.setGeometry(120, 70, 200, 30)
            label0.move(100, c)
            label0.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(255, 251, 194);"
"border-style: outset;\n"
"border-radius: 15px;\n"
"padding: 1px;\n")
            self.dialog.resize(900, 900)
            self.dialog.show()
            self.sleep(0.1)
            self.dialog.setWindowTitle('scanning')
            self.dialog.setWindowModality(Qt.ApplicationModal)
            if i < B :
                self.dialog.close()
            i += 1
            c += 50
            if i == C:
                self.scanning()

    def scan(self):
        self.dialog.setStyleSheet("background-color: rgb(255, 255, 238);\n")
        collect(self.building_comboBox.currentText(),self.RP_comboBox.currentText() ,1)

        a=0
        b=0
        wifis = get_wifis()
        wifis = []
        for i in range(1):
            wifis += get_wifis()
            for wifi in wifis:
                b += 1
                if int(wifi['signal']) > 40:
                    a += 1      
        self.dialog.close()
        label = QLabel("스캔이 성공적으로 완료됐습니다", self.dialog)
        label.setGeometry(120, 70, 400, 30)
        label.move(100, 300)
        label.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(239, 240, 255);"
"background-color: rgb(255, 251, 194);"
"border-style: outset;\n"
"border-radius: 15px;\n"
"padding: 1px;\n")
        label.setObjectName("label")

        label3 = QLabel(f"모든 wifi의 갯수는 {b} 입니다", self.dialog)
        label3.setGeometry(120, 70, 400, 30)
        label3.move(100, 350)
        label3.setObjectName("label")
        label3.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(239, 240, 255);"
"background-color: rgb(255, 251, 194);"
"border-style: outset;\n"
"border-radius: 15px;\n"
"padding: 1px;\n")

        label2 = QLabel(f"threshold보다 높은 wifi의 갯수는 {a} 입니다", self.dialog)
        label2.setGeometry(120, 70, 470, 30)
        label2.move(100, 400)
        label2.setObjectName("label")
        label2.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(239, 240, 255);"
"background-color: rgb(255, 251, 194);"
"border-style: outset;\n"
"border-radius: 15px;\n"
"padding: 1px;\n")

        btnDialog2 = QPushButton("서버로 전송", self.dialog)
        btnDialog2.setGeometry(50, 50, 200, 50)
        btnDialog2.move(100, 500)
        btnDialog2.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(198, 199, 255);"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 1px;\n")
        btnDialog2.clicked.connect(self.scan_check)

        btnDialog2 = QPushButton("데이터 전송 취소하기", self.dialog)
        btnDialog2.setGeometry(50, 50, 250, 50)
        btnDialog2.move(320, 500)
        btnDialog2.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(198, 199, 255);"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 1px;\n")
        btnDialog2.clicked.connect(self.remove_data)

        self.dialog.show()
        self.dialog.resize(800, 700)
        self.dialog.setWindowTitle('scan complete')
        self.dialog.setStyleSheet("background-color: rgb(255, 255, 238);\n")
        self.dialog.setWindowModality(Qt.ApplicationModal)

    def dialog_close(self):
        self.dialog.close()

    def send(self):
        print("send")

    def location(self):
        print("location")

    def remove_data(self): #remove .csv file
        #self.dialog.close()
        #directory = f"./{building_comboBox.currentText()}/{RP_comboBox.currentText()}"
        #os.remove(directory)
         btn_2= pyautogui.alert("데이터 전송이 취소되었습니다.")
         self.dialog.close()

    # execute detector 
    def scan_check(self):
           btn_1= pyautogui.alert("서버에 성공적으로 전송되었습니다.")
           self.dialog.close()

app =QApplication([])
main_dialog = indoor() #해당부분 위 class name과 동일하게 작성
QApplication.processEvents()
app.exit(app.exec_())

