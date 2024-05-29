import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout, \
    QTableView
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel


class Ui_Ap(object):
    pass


class Ui_Ap(object):
    def setupUi(self,Ap):
        Ap.setObject("mainwindow")
        Ap.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(Ap)
        self.centralwidget.setObjectName("centralwidget")

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("hotelinfo.db")
        db.open()
        projectModel = QSqlQueryModel()
        # city='JALANDHAR'
        # projectModel.setQuery("select * From hotel Where city="+str(city))
        projectModel.setQuery("select * from hotel")
        projectView = QTableView()
        projectView.move(20, 20)
        projectView.setModel(projectModel)
        projectView.show()
        vbox = QVBoxLayout()
        vbox.addWidget(projectView)
        self.setLayout(vbox)
        self.show()

    if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        Ap = QtWidgets.QMainWindow()
        ui= Ui_Ap()
        ui.setupUi(Ap)
        Ap.show()

        sys.exit(app.exec_())