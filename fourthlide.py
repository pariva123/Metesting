# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fourthlide.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_ManWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 20, 271, 31))
        self.label.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 80, 101, 20))
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 130, 121, 20))
        self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 180, 47, 13))
        self.label_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 220, 47, 13))
        self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 260, 47, 13))
        self.label_6.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 300, 111, 16))
        self.label_7.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(90, 340, 121, 16))
        self.label_8.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(90, 380, 47, 13))
        self.label_9.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(90, 380, 101, 16))
        self.label_10.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(90, 420, 91, 16))
        self.label_11.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
      #  self.label_12 = QtWidgets.QLabel(self.centralwidget)
       # self.label_12.setGeometry(QtCore.QRect(90, 460, 81, 16))
        #self.label_12.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        #self.label_12.setObjectName("label_12")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 80, 81, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 130, 81, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 180, 81, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 220, 81, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 260, 81, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(230, 300, 81, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(230, 340, 81, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(230, 380, 81, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(230, 420, 81, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
     #   self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        #self.lineEdit_10.setGeometry(QtCore.QRect(230, 460, 81, 20))
     #   self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(420, 80, 121, 20))
        self.label_13.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(540, 80, 81, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        #self.label_14 = QtWidgets.QLabel(self.centralwidget)
       # self.label_14.setGeometry(QtCore.QRect(380, 130, 141, 20))
      #  self.label_14.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
       # self.label_14.setObjectName("label_14")
       # self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
      #  self.lineEdit_12.setGeometry(QtCore.QRect(540, 130, 81, 20))
        #self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(420, 380, 91, 16))
        self.label_16.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_16.setObjectName("label_16")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(540, 380, 81, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(90, 460, 111, 20))
        self.label_15.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(230, 460, 51, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(420, 460, 81, 16))
        self.label_17.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_17.setObjectName("label_17")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(540, 460, 51, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(420, 300, 71, 21))
        self.label_18.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(420, 340, 61, 21))
        self.label_19.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_19.setObjectName("label_19")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(540, 300, 81, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(540, 340, 81, 20))
        self.lineEdit_17.setObjectName("lineEdit_17")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btn_submit = QtWidgets.QPushButton(MainWindow)
        self.btn_submit.setGeometry(350, 500, 90, 41)
        self.btn_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_submit.setMouseTracking(True)
        self.btn_submit.setStyleSheet("font: 75 16pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.btn_exit = QtWidgets.QPushButton(MainWindow)
        self.btn_exit.setGeometry(700, 500, 75, 41)
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setMouseTracking(True)
        self.btn_exit.setStyleSheet("font: 75 16pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")

        self.retranslateUi(MainWindow)
        self.btn_exit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ROOM  BOOKING"))
        self.label_2.setText(_translate("MainWindow", "Customer-Id"))
        self.label_3.setText(_translate("MainWindow", "Customer-Name"))
        self.label_4.setText(_translate("MainWindow", "City"))
        self.label_5.setText(_translate("MainWindow", "State"))
        self.label_6.setText(_translate("MainWindow", "Email-Id"))
        self.label_7.setText(_translate("MainWindow", "Check-In-Date"))
        self.label_8.setText(_translate("MainWindow", "Check-Out-Date"))
        self.label_10.setText(_translate("MainWindow", "No.Of Nights"))
        self.label_11.setText(_translate("MainWindow", "Room Price"))
      #  self.label_12.setText(_translate("MainWindow", "Discount"))
        self.label_13.setText(_translate("MainWindow", "Room No."))
        #self.label_14.setText(_translate("MainWindow", "Customer Surname"))
        self.label_16.setText(_translate("MainWindow", "Room Type"))
        self.label_15.setText(_translate("MainWindow", "Additional Fees"))
        self.label_17.setText(_translate("MainWindow", "Total Price"))
        self.label_18.setText(_translate("MainWindow", "Timing"))
        self.label_19.setText(_translate("MainWindow", "Timing"))
        self.btn_exit.setText(_translate("MainWindow", "Back"))
        self.btn_submit.setText(_translate("MainWinodw","SUBMIT"))
        self.btn_submit.clicked.connect(self.onclick)

    def onclick(self):

        v1=self.lineEdit_2.text()
        v2 = self.lineEdit_3.text()
        v3 = self.lineEdit_4.text()
        v4 = self.lineEdit_5.text()
        v5 = self.lineEdit_6.text()
        v6 = self.lineEdit_7.text()
        v7= self.lineEdit_8.text()
        v8 = self.lineEdit_9.text()
        v9 = self.lineEdit_10.text()
        v10 = self.lineEdit_11.text()
        v11= self.lineEdit_12.text()
        v12= self.lineEdit_13.text()
        v13= self.lineEdit_14.text()
        v14 = self.lineEdit_15.text()
        v15 = self.lineEdit_.text()

        print(v1)
        print(v2)
        print(v3)
        print(v4)
        print(v5)
        print(v6)
        print(v7)
        print(v8)
        print(v9)
        print(v10)
        print(v11)
        print(v12)
        print(v13)
        print(v14)
        print(v15)

        #conn=sqlite3.connect('hotelinfo.db')
        #conn.execute("INSERT INTO hotel VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15))
        #conn.commit()
        #conn.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ManWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

