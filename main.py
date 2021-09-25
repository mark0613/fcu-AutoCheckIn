import os
import sys
import json
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QCheckBox, QLabel, QLineEdit, QMessageBox, QPushButton, QWidget

from control import AutoCheckIn
from src.load import *

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
LESSONS = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14"]
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
CLASS_DATA_PATH = f"{CURRENT_PATH}/data/class_time.json"
ACCOUNT_DATA_PATH = f"{CURRENT_PATH}/data/account.json"

class CheckInWindow(QWidget):
    def __init__(self):
        super().__init__()
        class_time = load_json(CLASS_DATA_PATH)
        account = ""
        password = ""

        self.setMinimumSize(QtCore.QSize(500, 500))
        self.setMaximumSize(QtCore.QSize(500, 500))

        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(61, 24, 241, 451))
        self.label.setMaximumSize(QtCore.QSize(241, 451))
        self.label.setStyleSheet(f"background-image: url({CURRENT_PATH}/image/background-image.png)")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(CURRENT_PATH + "/image/background-image.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        #Build CheckBox UI
        self.checkBox = []
        for i, day in zip(range(100, 310, 30), range(0, 7)):
            for j, lesson in zip(range(60, 480, 30), range(0, 14)):
                checkBoxElement = QCheckBox(self)
                checkBoxElement.setGeometry(QtCore.QRect(i, j, 16, 20))
                checkBoxElement.setText("")
                checkBoxElement.setObjectName(DAYS[day]+" "+LESSONS[lesson])
                if class_time[DAYS[day]][LESSONS[lesson]] == True:
                    checkBoxElement.setChecked(True)
                self.checkBox.append(checkBoxElement)

        accountData = load_json(ACCOUNT_DATA_PATH)
        account = accountData["account"]
        password = accountData["password"]

        self.accountLabel = QLabel(self)
        self.accountLabel.setGeometry(QtCore.QRect(320, 30, 61, 21))
        self.accountLabel.setObjectName("accountLabel")
        self.passwordLabel = QLabel(self)
        self.passwordLabel.setGeometry(QtCore.QRect(320, 70, 61, 21))
        self.passwordLabel.setObjectName("passwordLabel")
        self.accountEdit = QLineEdit(self)
        self.accountEdit.setGeometry(QtCore.QRect(360, 30, 113, 21))
        self.accountEdit.setObjectName("accountEdit")
        self.accountEdit.setText(account)
        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setGeometry(QtCore.QRect(360, 70, 113, 21))
        self.passwordEdit.setObjectName("passwordEdit")
        self.passwordEdit.setText(password)
        self.passwordEdit.setEchoMode(QLineEdit.Password)

        self.rememberCheckBox = QCheckBox(self)
        self.rememberCheckBox.setGeometry(QtCore.QRect(340, 110, 113, 21))
        self.rememberCheckBox.setObjectName("rememberCheckBox")
        if account == "" or password == "":
            self.rememberCheckBox.setChecked(False)
        else:
            self.rememberCheckBox.setChecked(True)
        
        self.saveButton = QPushButton(self)
        self.saveButton.setGeometry(QtCore.QRect(340, 370, 113, 28))
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.onSave)
        self.exeButton = QPushButton(self)
        self.exeButton.setGeometry(QtCore.QRect(340, 410, 113, 28))
        self.exeButton.setObjectName("cancelButton")
        self.exeButton.clicked.connect(self.onExecute)
        self.clearButton = QPushButton(self)
        self.clearButton.setGeometry(QtCore.QRect(340, 450, 113, 28))
        self.clearButton.setObjectName("clearButton")
        self.clearButton.clicked.connect(self.onClear)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Auto Check In"))
        self.saveButton.setText(_translate("Form", "儲存"))
        self.exeButton.setText(_translate("Form", "執行"))
        self.clearButton.setText(_translate("Form", "清除"))
        self.accountLabel.setText(_translate("Form", "學號: "))
        self.passwordLabel.setText(_translate("Form", "密碼: "))
        self.rememberCheckBox.setText(_translate("Form", "記住我的資訊"))

    def errorMessage(self, message):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText(message)
        self.msg.setWindowTitle("Error")
        # self.textLabel = self.msg.findChild(QLabel, "qt_msgbox_label")
        # self.textLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setStyleSheet("QMessageBox QLabel#qt_msgbox_label { min-height: 40px; min-width: 100px; } QMessageBox QLabel#qt_msgboxex_icon_label { min-height: 40px }")
        self.msg.exec_()
    
    def informationMessage(self, message):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText(message)
        self.msg.setWindowTitle("Success")
        # self.textLabel = self.msg.findChild(QLabel, "qt_msgbox_label")
        # self.textLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.msg.setStyleSheet("QMessageBox QLabel#qt_msgbox_label { min-height: 40px; min-width: 100px; } QMessageBox QLabel#qt_msgboxex_icon_label { min-height: 40px }")
        self.msg.exec_()

    def onSave(self):
        checks = []

        for item in self.checkBox:
            if (item.isChecked()):
                checks.append(item.objectName().split(' '))

        if len(checks) == 0:
            self.errorMessage("你還沒選擇課堂！")
            return
        
        self.writeToJson(checks)
        

    def onExecute(self):
        if self.accountEdit.text() == "" or self.passwordEdit.text() == "":
            self.errorMessage("帳號或密碼為空！")
            return
        
        if self.rememberCheckBox.isChecked():
            accountData = {"account": self.accountEdit.text(), "password": self.passwordEdit.text()}
            with open(ACCOUNT_DATA_PATH, "w") as file:
                json.dump(accountData, file)
        else:
            accountData = {"account": "", "password": ""}
            with open(ACCOUNT_DATA_PATH, "w") as file:
                json.dump(accountData, file)

        auto = AutoCheckIn()
        auto.login(self.accountEdit.text(), self.passwordEdit.text())
        auto.execute()
    
    def onClear(self):
        for item in self.checkBox:
            item.setChecked(False)
        
    def writeToJson(self, checks):
        class_time = load_json(CLASS_DATA_PATH)

        for i in DAYS:
            for j in LESSONS:
                class_time[i][j] = False

        for i in checks:
            class_time[i[0]][i[1]] = True

        with open(CLASS_DATA_PATH, "w") as file:
            json.dump(class_time, file)
        
        self.informationMessage("寫入成功")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkInWindow = CheckInWindow()
    checkInWindow.show()
    sys.exit(app.exec_())