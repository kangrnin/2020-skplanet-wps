import sys
import pyautogui
from skplanet import Ui_MainWindow
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox

class indoor(QMainWindow,Ui_MainWindow): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
    def new_building(self):
        building_newButton= pyautogui.prompt(title='건물 추가',text='추가하려는 새로운 건물 이름을 입력하시오')
        print(building_newButton)

    def new_rp(self):
        RP_newButton= pyautogui.prompt(title='구역 추가',text='추가하려는 새로운 구역 이름을 입력하시오')
        print(RP_newButton)

    def scan(self):
        label = QLabel("스캔이 완료되었습니다", self.dialog)
        label.setGeometry(120, 70, 250, 24)
        label.setObjectName("label")

        btnDialog = QPushButton("위치별 수집내역 확인", self.dialog)
        btnDialog.setGeometry(1700, 1000, 250, 50)
        btnDialog.move(130, 150)
        btnDialog.clicked.connect(self.scan_check)

        btnDialog2 = QPushButton("종료하기", self.dialog)
        btnDialog2.setGeometry(1700, 1000, 250, 50)
        btnDialog2.move(130, 250)
        btnDialog2.clicked.connect(self.dialog_close)

        self.dialog.setWindowTitle('scan complete')
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(600, 400)
        self.dialog.show()

    def dialog_close(self):
        self.dialog.close(self)

    def scan_check(self):
        #label2 = QLabel("찾으시려는 새로운 건물 이름을 입력하시오", self.dialog)
        #label2.setGeometry(120, 70, 250, 24)
        #label2.setObjectName("label")

        #self.dialog.setWindowTitle('scan complete')
        #self.dialog.setWindowModality(Qt.ApplicationModal)
        #self.dialog.resize(600, 400)
        #self.dialog.show()
        buildingfind_newButton= pyautogui.prompt(title='건물 및 구역 확인', text='찾으시려는 새로운 건물과 구역 이름을 입력하시오\n ex: 제1과학관(31동) / 1층 1구역')
        if buildingfind_newButton == '제1과학관(31동) / 1층 1구역':
            btn_1= pyautogui.alert("스캔이 성공적으로 완료되었습니다")


app =QApplication([])
main_dialog = indoor() #해당부분 위 class name과 동일하게 작성
QApplication.processEvents()
app.exit(app.exec_())

