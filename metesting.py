# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metesting.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from secondslide import Ui_newWindow
class Ui_Form(object):
#    def cl(self,m):
 #       self.main=m
  #      self.setupUi(self.main)

    def openWindow(self):

        self.Window=QtWidgets.QMainWindow()
        self.ui= Ui_newWindow()
        self.ui.setupUi(self.Window)
        self.Window.show()
#        self.main.hide()
    def setupUi(self, Form):
        Form.setObjectName("PROJECT HOTEL")
        Form.resize(1366, 768)
        Form.setStyleSheet("background-image:url(i/pic.jpg)")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 20, 811, 51))
        self.label.setStyleSheet("font: 75 48pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.btn_open = QtWidgets.QPushButton(Form)
        self.btn_open.setGeometry(QtCore.QRect(600, 350, 191, 61))
        self.btn_open.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_open.setMouseTracking(True)
        self.btn_open.setStyleSheet("font: 75 22pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.btn_open.setObjectName("btn_open")
        self.btn_open.clicked.connect(self.openWindow)
        self.btn_exit = QtWidgets.QPushButton(Form)
        self.btn_exit.setGeometry(1250,650,75,41)
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setMouseTracking(True)
        self.btn_exit.setStyleSheet("font: 75 16pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.retranslateUi(Form)
        self.btn_exit.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("PROJECT HOTEL", "PROJECT HOTEL"))
        self.label.setText(_translate("PROJECT HOTEL", "WELCOME TO TAJ HOTEL"))
        self.btn_open.setText(_translate("PROJECT HOTEL", "ENTER"))
        self.btn_exit.setText(_translate("PROJECT HOTEL","EXIT"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

