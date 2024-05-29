# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout,QTableView,QLayoutItem,QLayout,QBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

class Ui_MainWindOw(QWidget):
    def setupUi(self,MainWindow):
    #    MainWindow.setObjectName("MainWindow")
    #    MainWindow.resize(1366,768)
     #   self.centralwidget = QtWidgets.QWidget(MainWindow)
     #   self.centralwidget.setObjectName("centralwidget")
   #     self.tableView = QtWidgets.QTableView(self.centralwidget)
      #  self.tableView.setGeometry(QtCore.QRect(0, 0, 1366, 768))
       # self.tableView.setMaximumSize(QtCore.QSize(1366, 768))
    #    self.tableView.setObjectName("tableView")
       # MainWindow.setCentralWidget(self.centralwidget)
      #  self.setWindowTitle(self.title)
       # self.setGeometry(self.left, self.top, self.width, self.height)

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("hotelinfo.db")
        db.open()
        projectModel = QSqlQueryModel()
        # city='JALANDHAR'
        # projectModel.setQuery("select * From hotel Where city="+str(city))
        projectModel.setQuery("select * from hotel")
        projectView = QTableView()
        projectView.move(500, 500)
        projectView.setModel(projectModel)
        projectView.show()
        vbox = QVBoxLayout()
        vbox.addWidget(projectView)
        self.setLayout(vbox)
        self.show()

       # self.retranslateUi(MainWindow)
       # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #def retranslateUi(self, MainWindow):
        #_translate = QtCore.QCoreApplication.translate
     #   MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindOw()
    ui.setupUi(MainWindow)
   # MainWindow.show()
    sys.exit(app.exec_())




