# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frth.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_MAINWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 611, 51))
        self.label.setStyleSheet("font: 75 36pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 211, 31))
        self.label_2.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 90, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 121, 31))
        self.label_3.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 130, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 61, 21))
        self.label_4.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 170, 113, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 71, 21))
        self.label_5.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 210, 113, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 260, 111, 21))
        self.label_6.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(250, 250, 113, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 300, 191, 21))
        self.label_7.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(250, 290, 113, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 340, 201, 21))
        self.label_8.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(250, 330, 113, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(250, 370, 113, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 380, 161, 21))
        self.label_9.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 420, 151, 21))
        self.label_10.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.label_10.setObjectName("label_10")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(250, 410, 113, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(480, 100, 111, 21))
        self.label_11.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.label_11.setObjectName("label_11")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(660, 90, 113, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(480, 140, 121, 21))
        self.label_12.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.label_12.setObjectName("label_12")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(660, 130, 113, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(480, 180, 141, 21))
        self.label_13.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.label_13.setObjectName("label_13")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(660, 170, 113, 31))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(480, 270, 151, 21))
        self.label_14.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.label_14.setObjectName("label_14")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(660, 260, 113, 31))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 470, 171, 51))
        self.pushButton.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 470, 91, 51))
        self.pushButton_2.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_2.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "USER INFORMATION"))
        self.label.setText(_translate("MainWindow", "CUSTOMER INFORMATION"))
        self.label_2.setText(_translate("MainWindow", "CUSTOMER NAME"))
        self.label_3.setText(_translate("MainWindow", "PHONE NO"))
        self.label_4.setText(_translate("MainWindow", "CITY"))
        self.label_5.setText(_translate("MainWindow", "STATE"))
        self.label_6.setText(_translate("MainWindow", "EMAIL ID"))
        self.label_7.setText(_translate("MainWindow", "CHECK-IN DATE"))
        self.label_8.setText(_translate("MainWindow", "CHECK-OUT DATE"))
        self.label_9.setText(_translate("MainWindow", "NO OF NIGHTS"))
        self.label_10.setText(_translate("MainWindow", "ROOM PRICE"))
        self.label_11.setText(_translate("MainWindow", "ROOM NO"))
        self.label_12.setText(_translate("MainWindow", "IN TIMING"))
        self.label_13.setText(_translate("MainWindow", "OUT TIMING"))
        self.label_14.setText(_translate("MainWindow", "TOTAL PRICE"))
        self.pushButton.setText(_translate("MainWindow", "SUBMIT"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK"))
    def on_click(self):
        try:
            v1 = self.lineEdit.text()
            v2 = self.lineEdit_2.text()
            v3 = self.lineEdit_3.text()
            v4 = self.lineEdit_4.text()
            v5 = self.lineEdit_5.text()
            v6 = self.lineEdit_6.text()
            v7 = self.lineEdit_7.text()
            v8 = self.lineEdit_8.text()
            v9 = self.lineEdit_9.text()
            v10 = self.lineEdit_10.text()
            v11 = self.lineEdit_11.text()
            v12 = self.lineEdit_12.text()
            v13 = self.lineEdit_13.text()
            u = self.lineEdit_10.text()

            if(v1.__len__()==0 or v2.__len__()>=10 or v2.__len__()==0 or v3.__len__()==0 or v4.__len__()==0 or v5.__len__()==0 or v6.__len__()==0 or v7.__len__()==0 or v8.__len__()==0 or v9.__len__()==0 or v10.__len__()==0 or v11.__len__()==0 or v12.__len__()==0 or v13.__len__()==0):
                answer = QtWidgets.QMessageBox.warning(None, 'Warning', 'Kinldy Fill All Fields Properly', QtWidgets.QMessageBox.Ok)

            else:

                print(u)
                conn = sqlite3.connect('hotelinfo.db')
                result =conn.execute("SELECT * FROM hotel WHERE roomno=?", (u,))
                if (len(result.fetchall()) >0):
                    answer = QtWidgets.QMessageBox.warning(None, 'Warning', 'Sorry Room is Booked',QtWidgets.QMessageBox.Ok)
                    #conn.close()
                else:
                    conn = sqlite3.connect('hotelinfo.db')
                    print("hello")
                    conn.execute("INSERT INTO hotel VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13))
                    conn.commit()
                    answer = QtWidgets.QMessageBox.information(None, 'Success', 'THANK YOU',QtWidgets.QMessageBox.Ok)
        except Exception as m:
            QtWidgets.QMessageBox.question(None, 'Message-From Students', m.a, QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MAINWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
