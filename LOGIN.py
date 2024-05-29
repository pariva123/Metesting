# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LOGIN.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from report import Ui_MainWindOw
import sqlite3

class Ui_MainWindOW(object):
    def cl(self, m):
        self.main=m
        self.setupUi(self.main)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700,400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 180, 161, 31))
        self.label.setStyleSheet("font: 75 20pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 240, 191, 31))
        self.label_2.setStyleSheet("font: 75 20pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 180, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 240, 181, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 320, 121, 41))
        self.pushButton.setStyleSheet("font: 75 20pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.open)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LOGIN"))
        self.label.setText(_translate("MainWindow", "USER NAME"))
        self.label_2.setText(_translate("MainWindow", "PASSWORD"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))

    def open(self):
        u1=self.lineEdit.text()
        u2=self.lineEdit_2.text()
        if (u1.__len__() == 0 or u2.__len__() == 0):
            answer = QtWidgets.QMessageBox.warning(None, 'Warning', 'Kinldy Fill All Fields Properly',QtWidgets.QMessageBox.Ok)
        else:
            conn = sqlite3.connect('hotelinfo.db')
            result=conn.execute("SELECT * FROM LOGIN WHERE USERNAME=? AND PASSWORD=?",(u1,u2))
            if(len(result.fetchall())>0):
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindOw()
                self.ui.setupUi(self.window)

            else:
                answer = QtWidgets.QMessageBox.warning(
                None, 'Warning', 'Invalid Username or Password',
                QtWidgets.QMessageBox.Ok)

        #conn.commit()
      #  conn.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindOW()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

