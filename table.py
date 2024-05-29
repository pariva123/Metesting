
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout, \
    QTableView
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Example Table View'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("hotelinfo.db")
        db.open()
        projectModel = QSqlQueryModel()
        #city='JALANDHAR'
        #projectModel.setQuery("select * From hotel Where city="+str(city))
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
    import sys
    app = QApplication(sys.argv)

    ui = App()
    sys.exit(app.exec_())