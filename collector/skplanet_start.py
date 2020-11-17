import sys
import pyautogui
from skplanet import Ui_MainWindow
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from collector import collect
from pathlib import Path
import pandas as pd
from os import listdir
from os.path import isdir, join, splitext
from wifi_scan import get_wifis

class indoor(QMainWindow,Ui_MainWindow): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
    def new_building(self):
        building_newButton= pyautogui.prompt(title='건물 추가',text='추가하려는 새로운 건물 이름을 입력하시오')
        #print(building_newButton)
        #self.building_comboBox.addItem(building_newButton) #need new file
        position = building_newButton
        script_path = Path(__file__).parent
        data_path = script_path / '../signal_data'
        data_path.mkdir(parents=True, exist_ok=True)
        (data_path/position).mkdir(parents=True, exist_ok=True)
        self.building_comboBox.addItem(building_newButton)

    def new_rp(self):
        RP_newButton= pyautogui.prompt(title='구역 추가',text='추가하려는 새로운 구역 이름을 입력하시오')
        #print(RP_newButton)
        print(self.building_comboBox)
        #open(self.building_comboBox, RP_newButton).close()
        self.RP_comboBox.addItem(splitext(RP_newButton)[0])
        
    def scanning(self):
        label = QLabel("스캔중입니다. 조금만 기다려주세요", self.dialog)
        label.setGeometry(120, 70, 500, 24)
        label.move(100, 100)
        label.setObjectName("label")
        self.dialog.setWindowTitle('scanning')
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(600, 400)
        self.dialog.show()

    def scan(self):
        collect(self.building_comboBox.currentText(),self.RP_comboBox.currentText() ,1)
        #
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
        #
        label = QLabel("스캔이 성공적으로 완료됐습니다", self.dialog)
        label.setGeometry(120, 70, 500, 24)
        label.move(100, 100)
        label.setObjectName("label")

        label3 = QLabel(f"모든 wifi의 갯수는 {b} 입니다", self.dialog)
        label3.setGeometry(120, 70, 700, 24)
        label3.move(40, 200)
        label3.setObjectName("label")

        label2 = QLabel(f"threshold보다 높은 wifi의 갯수는 {a} 입니다", self.dialog)
        label2.setGeometry(120, 70, 700, 24)
        label2.move(40, 300)
        label2.setObjectName("label")

        btnDialog2 = QPushButton("서버로 전송", self.dialog)
        btnDialog2.setGeometry(50, 50, 250, 50)
        btnDialog2.move(50, 400)
        btnDialog2.clicked.connect(self.dialog_close)

        btnDialog2 = QPushButton("데이터 전송 취소하기", self.dialog)
        btnDialog2.setGeometry(50, 50, 250, 50)
        btnDialog2.move(300, 400)
        btnDialog2.clicked.connect(self.dialog_close)

        self.dialog.setWindowTitle('scan complete')
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(600, 400)
        self.dialog.show()

    def dialog_close(self):
        self.dialog.close()

    def scan_check(self):
        #label2 = QLabel("찾으시려는 새로운 건물 이름을 입력하시오", self.dialog)
        #label2.setGeometry(120, 70, 250, 24)
        #label2.setObjectName("label")

        #self.dialog.setWindowTitle('scan complete')
        #self.dialog.setWindowModality(Qt.ApplicationModal)
        #self.dialog.resize(600, 400)
        #self.dialog.show()
        #buildingfind_newButton= pyautogui.prompt(title='건물 및 구역 확인', text='찾으시려는 새로운 건물과 구역 이름을 입력하시오\n ex: 반도체관 6층 / opensource2(400621)')
        #if buildingfind_newButton == '반도체관 6층 / opensource2(400621)':
           btn_1= pyautogui.alert("스캔이 성공적으로 완료되었습니다")

       # if buildingfind_newButton == '반도체관 6층 / opensource1(400620)':
       #     btn_1= pyautogui.alert("스캔이 성공적으로 완료되었습니다")


app =QApplication([])
main_dialog = indoor() #해당부분 위 class name과 동일하게 작성
QApplication.processEvents()
app.exit(app.exec_())

