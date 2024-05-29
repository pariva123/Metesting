# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OtherWindow(object):
    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(1366, 768)
        OtherWindow.setStyleSheet("background-image:url(i/pic.jpg)")
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(335, 90, 731, 51))
        self.label.setStyleSheet("font: 75 48pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label.setObjectName("label")
        self.nexbutton = QtWidgets.QPushButton(self.centralwidget)
        self.nexbutton.setGeometry(QtCore.QRect(335, 430, 221, 71))
        self.nexbutton.setStyleSheet("font: 75 22pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.nexbutton.setObjectName("nexbutton")
        self.nextbutton = QtWidgets.QPushButton(self.centralwidget)
        self.nextbutton.setGeometry(QtCore.QRect(650, 430, 391, 71))
        self.nextbutton.setStyleSheet("font: 75 22pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.nextbutton.setObjectName("nextbutton")
        OtherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1053, 21))
        self.menubar.setObjectName("menubar")
        OtherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "MainWindow"))
        self.label.setText(_translate("OtherWindow", "ABOUT HOTEL SERVICE"))
        self.nexbutton.setText(_translate("OtherWindow", "ROOMS"))
        self.nextbutton.setText(_translate("OtherWindow", "ROOM SERVICE MENU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())

