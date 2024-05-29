# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondslide.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from facilities import Ui_MWindow
from third import Ui_new1
from newteeji import Ui_MainWindow
from LOGIN import Ui_MainWindOW
class Ui_newWindow(object):
    def facwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openwindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui= Ui_new1()
        self.ui.setupUi(self.window)
        self.window.show()
    def openwiindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def login(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindOW()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, newWindow):
        newWindow.setObjectName("newWindow")
        newWindow.resize(1366, 768)
        newWindow.setStyleSheet("background-image:url(i/pic.jpg)")
        self.centralwidget = QtWidgets.QWidget(newWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(552, 10, 280, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 36pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(590,147 , 202, 41))
        self.button1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button1.setMouseTracking(True)
        self.button1.setStyleSheet("font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 italic 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";")
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.openwiindow)
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(300, 300, 202, 41))
        self.button3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button3.setMouseTracking(True)
        self.button3.setStyleSheet("\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 italic 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";")
        self.button3.setObjectName("button3")
        self.button3.clicked.connect(self.facwindow)
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(590, 300, 202, 41))
        self.button4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button4.setMouseTracking(True)
        self.button4.setStyleSheet("\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 italic 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";")
        self.button4.setObjectName("button4")
        self.button4.clicked.connect(self.openwindow)
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(890, 300, 202, 41))
        self.button5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button5.setMouseTracking(True)
        self.button5.setStyleSheet("\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";")
        self.button5.setObjectName("button5")
        self.button5.clicked.connect(self.login)
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(590, 472, 202, 41))
        self.button6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button6.setMouseTracking(True)
        self.button6.setStyleSheet("\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";\n"
"font: 75 22pt \"Times New Roman\";")
        self.button6.setObjectName("button6")
        newWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(newWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1086, 21))
        self.menubar.setObjectName("menubar")
        newWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(newWindow)
        self.statusbar.setObjectName("statusbar")
        newWindow.setStatusBar(self.statusbar)

        self.retranslateUi(newWindow)
        self.button6.clicked.connect(newWindow.close)
        QtCore.QMetaObject.connectSlotsByName(newWindow)

    def retranslateUi(self, newWindow):
        _translate = QtCore.QCoreApplication.translate
        newWindow.setWindowTitle(_translate("newWindow", "MAIN MENU"))
        self.label.setText(_translate("newWindow", "MAIN MENU"))
        self.button1.setText(_translate("newWindow", "ROOM TYPES"))
        self.button3.setText(_translate("newWindow", "FACILITIES"))
        self.button4.setText(_translate("newWindow", "RESTAURANT"))
        self.button5.setText(_translate("newWindow", "REPORT"))
        self.button6.setText(_translate("newWindow", "Back"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newWindow = QtWidgets.QMainWindow()
    ui = Ui_newWindow()
    ui.setupUi(newWindow)
    newWindow.show()
    sys.exit(app.exec_())

