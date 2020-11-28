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

    def scan(self):
        #collect(self.building_comboBox.currentText(),self.RP_comboBox.currentText())
        position = self.building_comboBox.currentText()
        rp = self.RP_comboBox.currentText()

        script_path = Path(__file__).parent
        data_path = script_path / '../signal_data'
        # 데이터 파일 폴더 생성
        data_path.mkdir(parents=True, exist_ok=True)
        (data_path/position).mkdir(parents=True, exist_ok=True)

        wifi_list = []
        bssid_set = set()

        overlap_cnt = 0
        scan_cnt = 1
        self.dialog.setStyleSheet("background-color: rgb(255, 255, 238);\n")
        ja = 0
        while True:
            print('-----------------------------------------')
            a=0
            b=0
            scan_wifis = get_wifis()
            scan_wifis = []
            for i in range(1):
                scan_wifis += get_wifis()
                for wifi in scan_wifis:
                    b += 1
                    if int(wifi['signal']) > 40:
                        a += 1  
            if ja != 0:
                self.dialog.close()
            print('completed scan #', scan_cnt)
            label0 = QLabel(f"{scan_cnt} 번째 스캔중입니다.", self.dialog)
            label0.setGeometry(120, 70, 500, 30)
            label0.move(100, 50)
            label0.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(255, 255, 238);"
"border-style: outset;\n"
"border-radius: 15px;\n"
"padding: 1px;\n")

            print('total bssid cnt : ', len(scan_wifis))
            label00 = QLabel(f"총 bssid 갯수 : {len(scan_wifis)}", self.dialog)
            label00.setGeometry(120, 70, 500, 30)
            label00.move(100, 100)
            label00.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(255, 255, 238);"
"border-style: outset;\n"
"border-radius: 15px;\n"
"padding: 1px;\n")

            new_bssids = [ w['bssid'] for w in scan_wifis if w['bssid'] not in bssid_set ]
            bssid_set.update(new_bssids)

            print(len(new_bssids), 'new bssids : [ ', end='')
            for bssid in new_bssids:
                print('~'+bssid[-8:], end=', ')
            print(' ]')

            label01 = QLabel(f"새로운 bssid 갯수 : {len(new_bssids)} ", self.dialog)
            label01.setGeometry(120, 70, 500, 30)
            label01.move(100, 150)
            label01.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(255, 255, 238);"
"border-style: outset;\n"
"border-radius: 15px;\n"
"padding: 1px;\n")

            label02 = QLabel("새로운 bssid 목록(최대 10개만 표시): ", self.dialog)
            label02.setGeometry(120, 70, 600, 30)
            label02.move(100, 200)
            label02.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
    "background-color: rgb(255, 255, 238);"
    "border-style: outset;\n"
    "border-radius: 15px;\n"
    "padding: 1px;\n")

            k = 500
            l = 300
            w = 0
            if len(new_bssids) == 0:
                label22 = QLabel("                 ", self.dialog)
                label22.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(255, 255, 238);"
"border-style: outset;\n"
"border-radius: 15px;\n"
"padding: 1px;\n")
                label22.setGeometry(120, 70, 800, 30)
                label22.move(100, 200)
                label23 = QLabel("                 ", self.dialog)
                label23.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(255, 255, 238);"
"border-style: outset;\n"
"border-radius: 15px;\n"
"padding: 1px;\n")
                label23.setGeometry(120, 70, 800, 30)
                label23.move(100, 250)

            else:
                for bssid in new_bssids:
                    bssidnw= bssid[-8:]
                    #print('~'+bssid[-8:], end=', ')
                    label22 = QLabel(f"{bssid[-8:]} ", self.dialog)
                    if w > 2:
                            label22.setGeometry(120, 70, 120, 30)
                            label22.move(l, 250)
                            l += 100
                    else:
                        label22.setGeometry(120, 70, 120, 30)
                        label22.move(k, 200)
                    w += 1
                    k += 110
                    label22.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
            "background-color: rgb(255, 255, 238);"
            "border-style: outset;\n"
            "border-radius: 15px;\n"
            "padding: 1px;\n")


            overlap_cnt = overlap_cnt+1 if len(new_bssids) == 0 else 0
            ja += 1
            self.dialog.resize(900, 880)
            self.dialog.show()
            self.dialog.setWindowTitle('scanning')
            self.dialog.setWindowModality(Qt.ApplicationModal)
            self.sleep(1)

            if overlap_cnt == 3:
                break

            if new_bssids:
                wifi_list += scan_wifis
            scan_cnt += 1
        
        # (position) 폴더 안의 (rp).csv 안에 저장
        df = pd.DataFrame(wifi_list)
        df.to_csv(data_path/position/(rp+'.csv'), mode='a', index=False, header=False)

        # position, rp 정보 column을 추가해서 통합 데이터파일에도 저장
        df['position'] = position
        df['rp'] = rp
        df.to_csv(data_path/'signal_all.csv', mode='a', index=False, header=False)
        self.dialog.close()

        label = QLabel("스캔이 성공적으로 완료됐습니다", self.dialog)
        label.setGeometry(120, 70, 400, 30)
        label.move(100, 50)
        label.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(239, 240, 255);"
"background-color: rgb(255, 251, 194);"
"border-style: outset;\n"
"border-radius: 15px;\n"
"padding: 1px;\n")
        label.setObjectName("label")

        label3 = QLabel(f"모든 wifi의 갯수는 {b} 입니다", self.dialog)
        label3.setGeometry(120, 70, 400, 30)
        label3.move(100, 100)
        label3.setObjectName("label")
        label3.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(239, 240, 255);"
"background-color: rgb(255, 251, 194);"
"border-style: outset;\n"
"border-radius: 15px;\n"
"padding: 1px;\n")

        label2 = QLabel(f"threshold보다 높은 wifi의 갯수는 {a} 입니다", self.dialog)
        label2.setGeometry(120, 70, 470, 30)
        label2.move(100, 150)
        label2.setObjectName("label")
        label2.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(239, 240, 255);"
"background-color: rgb(255, 251, 194);"
"border-style: outset;\n"
"border-radius: 15px;\n"
"padding: 1px;\n")

        label3 = QLabel(f"     ", self.dialog)
        label3.setGeometry(120, 70, 900, 30)
        label3.move(100, 200)
        label3.setObjectName("label")
        label3.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(255, 255, 238);"
"border-style: outset;\n"
"border-radius: 15px;\n"
"padding: 1px;\n")

        label4 = QLabel(f"     ", self.dialog)
        label4.setGeometry(120, 70, 900, 30)
        label4.move(100, 250)
        label4.setObjectName("label")
        label4.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(255, 255, 238);"
"border-style: outset;\n"
"border-radius: 15px;\n"
"padding: 1px;\n")

        btnDialog2 = QPushButton("서버로 전송", self.dialog)
        btnDialog2.setGeometry(50, 50, 200, 50)
        btnDialog2.move(100, 400)
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
        btnDialog2.move(320, 400)
        btnDialog2.setStyleSheet("font: 9pt \"마루 부리OTF Beta\";\n"
"background-color: rgb(198, 199, 255);"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 1px;\n")
        btnDialog2.clicked.connect(self.remove_data)
        self.dialog.show()
        self.dialog.resize(800, 800)
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

