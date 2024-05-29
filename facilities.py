# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'facilities.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -100, 400,460))
        self.label_2.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
                               #  "color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(255, 255, 255)")#;\n"
                                # "background-image:url(i/pic5.jpg)")
        self.label_2.setObjectName("label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 0, 1000,384))
        self.label.setStyleSheet("font: 75 48pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"background-image:url(i/pic5.jpg)")
        self.label.setObjectName("label")
        #self.label_2 = QtWidgets.QLabel(self.centralwidget)
       # self.label_2.setGeometry(QtCore.QRect(0, 231,1366, 231))
       # self.label_2.setStyleSheet("font: 75 26pt \"Times New Roman\";\n"
#"color: rgb(255, 255, 255);\n"
#"background-color: rgb(255, 255, 255);\n"
#"background-image:url(i/pic7.jpg)")
 #       self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 360, 1000, 384))
        self.label_4.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
                                 #"color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(255, 255, 255)")#;\n"
                                 #"background-image:url(i/pic6.jpg)")
        self.label_4.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 360, 1000,384))
        self.label_3.setStyleSheet("font: 75 48pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"background-image:url(i/pic6.jpg)")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.bttn_exit = QtWidgets.QPushButton(MainWindow)
        self.bttn_exit.setGeometry(1250, 650, 75, 41)
        self.bttn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bttn_exit.setMouseTracking(True)
        self.bttn_exit.setStyleSheet("font: 75 16pt \"Times New Roman\";\n"
                                     "background-color: rgb(255, 255, 255);")

        self.retranslateUi(MainWindow)
        self.bttn_exit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FACILITIES"))
        self.label.setText(_translate("MainWindow", "SWIMMING POOL"))
  #      self.label_2.setText(_translate("MainWindow", "GAMES"))
        self.label_3.setText(_translate("MainWindow", "GYM"))
        self.label_2.setText(_translate("MainWindow", "SWIMMING POOL\n\n SPECIFICATIONS :\n TIMINGS : 6:00 AM TO 11:30 PM\n DIMENSIONS: 16 ft x 40 ft \n DEPTH : 6ft "))
        self.label_4.setText(_translate("MainWindow", "GYM\n\n SPECIFICATIONS :\n TIMINGS: 4:00 AM TO 11:30 PM\n (PERSONAL TRAINER\n AVAILABLE)"))
        self.bttn_exit.setText(_translate("new1", "Back"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

