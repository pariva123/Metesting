# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newteeji.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from frth import Ui_MAINWindow
import sqlite3
class Ui_MainWindow(object):


    def opwindow(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MAINWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, -30, 1366, 371))
        self.label.setStyleSheet("background-image:url(i/pic4.jpg)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-4, 340, 1366, 371))
        self.label_2.setStyleSheet("background-image:url(i/pic3.jpg)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 281, 31))
        self.label_3.setStyleSheet("font: 75 24pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 346, 296, 31))
        self.label_4.setStyleSheet("font: 75 24pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton=1
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220., 130, 121, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.opwindow)
        self.pushButton_2=2
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 130, 121, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.opwindow)
        self.pushButton_3=3
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 130, 121, 41))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.opwindow)
        self.pushButton_4=4
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(820, 130, 121, 41))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setMouseTracking(True)
        self.pushButton_4.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.opwindow)
        self.pushButton_5=5
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1020, 130, 121, 41))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setMouseTracking(True)
        self.pushButton_5.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.opwindow)
        self.pushButton_6=6
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 190, 121, 41))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setMouseTracking(True)
        self.pushButton_6.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.opwindow)
        self.pushButton_7=7
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(820, 190, 121, 41))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setMouseTracking(True)
        self.pushButton_7.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.opwindow)
        self.pushButton_8=8
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(420, 190, 121, 41))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setMouseTracking(True)
        self.pushButton_8.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.opwindow)
        self.pushButton_9=9
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(620, 190, 121, 41))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setMouseTracking(True)
        self.pushButton_9.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.opwindow)
        self.pushButton_10=10
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(1020, 190, 121, 41))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setMouseTracking(True)
        self.pushButton_10.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.opwindow)
        self.pushButton_11 = 11
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(220, 440, 121, 39))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setMouseTracking(True)
        self.pushButton_11.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.opwindow)
        self.pushButton_12 = 12
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(620, 500, 121, 41))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setMouseTracking(True)
        self.pushButton_12.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.opwindow)
        self.pushButton_13 = 13
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(820, 440, 121, 39))
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setMouseTracking(True)
        self.pushButton_13.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.opwindow)
        self.pushButton_14 =14
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(420, 440, 121, 39))
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setMouseTracking(True)
        self.pushButton_14.setStyleSheet("\n"
"font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(self.opwindow)
        self.pushButton_15 = 15
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(1020, 440, 121, 39))
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setMouseTracking(True)
        self.pushButton_15.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(self.opwindow)
        self.pushButton_16 = 16
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(420, 500, 121, 41))
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setMouseTracking(True)
        self.pushButton_16.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(self.opwindow)
        self.pushButton_17 = 17
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(820, 500, 121, 41))
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_17.setMouseTracking(True)
        self.pushButton_17.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(self.opwindow)
        self.pushButton_18 = 18
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(220, 500, 121, 41))
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_18.setMouseTracking(True)
        self.pushButton_18.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(self.opwindow)
        self.pushButton_19 =19
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(620, 440, 121, 39))
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_19.setMouseTracking(True)
        self.pushButton_19.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.clicked.connect(self.opwindow)
        self.pushButton_20 = 20
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(1020, 500, 121, 41))
        self.pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_20.setMouseTracking(True)
        self.pushButton_20.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.clicked.connect(self.opwindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btn_exit = QtWidgets.QPushButton(MainWindow)
        self.btn_exit.setGeometry(1250, 650, 75, 41)
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setMouseTracking(True)
        self.btn_exit.setStyleSheet("font: 75 16pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")

        self.retranslateUi(MainWindow)
        self.btn_exit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ROOMS"))
        self.pushButton.setText(_translate("MainWindow", "ROOM NO 1"))
        self.pushButton_2.setText(_translate("MainWindow", "ROOM NO 2"))
        self.pushButton_3.setText(_translate("MainWindow", "ROOM NO 3"))
        self.pushButton_4.setText(_translate("MainWindow", "ROOM NO 4"))
        self.pushButton_5.setText(_translate("MainWindow", "ROOM NO 5"))
        self.pushButton_6.setText(_translate("MainWindow", "ROOM NO 6"))
        self.pushButton_7.setText(_translate("MainWindow", "ROOM NO 9"))
        self.pushButton_8.setText(_translate("MainWindow", "ROOM NO 7"))
        self.pushButton_9.setText(_translate("MainWindow", "ROOM NO 8"))
        self.pushButton_10.setText(_translate("MainWindow", "ROOM NO 10"))
        self.pushButton_11.setText(_translate("MainWindow", "ROOM NO 11"))
        self.pushButton_12.setText(_translate("MainWindow", "ROOM NO 18"))
        self.pushButton_13.setText(_translate("MainWindow", "ROOM NO 14"))
        self.pushButton_14.setText(_translate("MainWindow", "ROOM NO 12"))
        self.pushButton_15.setText(_translate("MainWindow", "ROOM NO 15"))
        self.pushButton_16.setText(_translate("MainWindow", "ROOM NO 17"))
        self.pushButton_17.setText(_translate("MainWindow", "ROOM NO 19"))
        self.pushButton_18.setText(_translate("MainWindow", "ROOM NO 16"))
        self.pushButton_19.setText(_translate("MainWindow", "ROOM NO 13"))
        self.pushButton_20.setText(_translate("MainWindow", "ROOM NO 20"))
        self.label_3.setText(_translate("MainWindow", "ROOM WITH 1 BED"))
        self.label_4.setText(_translate("MainWindow", "ROOM WITH 2 BEDS"))
        self.btn_exit.setText(_translate("MainWindow", "Back"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

