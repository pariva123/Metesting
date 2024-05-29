
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lally.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtWidgets ,QtGui
from PyQt5.QtCore import pyqtSlot

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.manojClicked)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # @pyqtSlot()
    def manojClicked(self):
        # QtWidgets.QMessageBox.question(self, 'Good', "You typed: ", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        answer = QtWidgets.QMessageBox.question(
            None, 'Are You', 'Sure To Login?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No |
            QtWidgets.QMessageBox.Cancel,
            QtWidgets.QMessageBox.No)
        if answer == QtWidgets.QMessageBox.Yes:
        elif answer == QtWidgets.QMessageBox.No:
            # code to carry on without deleting

            print('No')
        else:
            # code to abort the whole operation
            print('Cancel')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())