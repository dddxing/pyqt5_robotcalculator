# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from advancedsetting import Ui_Dialog_advancedSettings
from creditwindow import Ui_Dialog_credit
from requiredFieldsWarning import Ui_requiredFieldsWarning
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMessageBox
import sqlite3


class Ui_MainWindow():

    def calculation(self):        
        print(Ui_Dialog_advancedSettings.lineEdit_robotSpeed)
        

    def openSettingWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_advancedSettings()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openCreditWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_credit()
        self.ui.setupUi(self.window)
        self.window.show()

    def openRequiredFieldsWarningWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_requiredFieldsWarning()
        self.ui.setupUi(self.window)
        self.window.show()

    def clear_text(self):
        self.lineEdit_from.setText("")
        self.lineEdit_to.setText("")
        self.lineEdit_dailytarget.setText("")
        self.lineEdit_distance.setText("")

    def addTrip(self, data):
        if self.lineEdit_from.text() == '' or self.lineEdit_to.text() == '' or self.lineEdit_dailytarget.text() == '' or self.lineEdit_distance.text() == '':
            self.openRequiredFieldsWarningWindow()
            return
        rows = self.tableWidget_database.rowCount()
        self.tableWidget_database.setRowCount(rows+1)
        self.tableWidget_database.setItem(rows, 0, QtWidgets.QTableWidgetItem(self.lineEdit_from.text()))
        self.tableWidget_database.setItem(rows, 1, QtWidgets.QTableWidgetItem(self.lineEdit_to.text()))
        self.tableWidget_database.setItem(rows, 2, QtWidgets.QTableWidgetItem(self.lineEdit_dailytarget.text()))
        self.tableWidget_database.setItem(rows, 3, QtWidgets.QTableWidgetItem(self.lineEdit_distance.text()))
        print(rows)
        self.clear_text()

    def removeTrip(self):
        self.tableWidget_database.removeRow(self.tableWidget_database.currentRow())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.gridLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_from = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_from.setObjectName("lineEdit_from")
        self.gridLayout.addWidget(self.lineEdit_from, 1, 1, 1, 1)
        self.label_from = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_from.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_from.setObjectName("label_from")
        self.gridLayout.addWidget(self.label_from, 1, 0, 1, 1)
        self.lineEdit_to = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_to.setObjectName("lineEdit_to")
        self.gridLayout.addWidget(self.lineEdit_to, 2, 1, 1, 1)
        self.lineEdit_dailytarget = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_dailytarget.setObjectName("lineEdit_dailytarget")
        self.gridLayout.addWidget(self.lineEdit_dailytarget, 1, 3, 1, 1)
        self.label_dailytarget = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_dailytarget.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_dailytarget.setObjectName("label_dailytarget")
        self.gridLayout.addWidget(self.label_dailytarget, 1, 2, 1, 1)
        self.lineEdit_distance = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_distance.setObjectName("lineEdit_distance")
        self.gridLayout.addWidget(self.lineEdit_distance, 2, 3, 1, 1)
        self.label_to = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_to.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_to.setObjectName("label_to")
        self.gridLayout.addWidget(self.label_to, 2, 0, 1, 1)
        self.label_distance = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_distance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_distance.setObjectName("label_distance")
        self.gridLayout.addWidget(self.label_distance, 2, 2, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_addtrip = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_addtrip.setObjectName("pushButton_addtrip")
        self.horizontalLayout.addWidget(self.pushButton_addtrip)
        self.pushButton_removetrip = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_removetrip.setObjectName("pushButton_removetrip")
        self.horizontalLayout.addWidget(self.pushButton_removetrip)
        self.pushButton_updatetrip = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_updatetrip.setObjectName("pushButton_updatetrip")
        self.horizontalLayout.addWidget(self.pushButton_updatetrip)
        self.pushButton_clear = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        self.gridLayout_2.addWidget(self.splitter, 2, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 2)
        self.pushButton_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calculate.setObjectName("pushButton_calculate")
        self.gridLayout_2.addWidget(self.pushButton_calculate, 6, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.pushButton_advancedsetting = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_advancedsetting.setObjectName("pushButton_advancedsetting")
        self.gridLayout_2.addWidget(self.pushButton_advancedsetting, 4, 2, 1, 1)
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_title.setFont(font)
        self.label_title.setTextFormat(QtCore.Qt.AutoText)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.gridLayout_2.addWidget(self.label_title, 0, 1, 1, 1)
        self.tableWidget_database = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_database.setObjectName("tableWidget_database")
        self.tableWidget_database.setColumnCount(4)
        self.tableWidget_database.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_database.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_database.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_database.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_database.setHorizontalHeaderItem(3, item)
        self.gridLayout_2.addWidget(self.tableWidget_database, 6, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 603, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuInfo = QtWidgets.QMenu(self.menuBar)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu_about = QtWidgets.QAction(MainWindow)
        self.menu_about.setObjectName("menu_about")
        self.menuInfo.addAction(self.menu_about)
        self.menuBar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Signals Controls
        self.pushButton_advancedsetting.clicked.connect(self.openSettingWindow)
        self.menu_about.triggered.connect(self.openCreditWindow)
        self.pushButton_clear.clicked.connect(self.clear_text)
        self.pushButton_addtrip.clicked.connect(self.addTrip)
        self.pushButton_removetrip.clicked.connect(self.removeTrip)
        self.pushButton_calculate.clicked.connect(self.calculation)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_from.setText(_translate("MainWindow", "From"))
        self.label_dailytarget.setText(_translate("MainWindow", "Daily Target (Piece)"))
        self.label_to.setText(_translate("MainWindow", "To"))
        self.label_distance.setText(_translate("MainWindow", "One-Way Distance (ft)"))
        self.pushButton_addtrip.setText(_translate("MainWindow", "Add Trip"))
        self.pushButton_removetrip.setText(_translate("MainWindow", "Remove Trip"))
        self.pushButton_updatetrip.setText(_translate("MainWindow", "Update Trip"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_calculate.setText(_translate("MainWindow", "Calculate"))
        self.pushButton_advancedsetting.setText(_translate("MainWindow", "Advanced Setting"))
        self.label_title.setText(_translate("MainWindow", "CoE AMR Calculator"))
        item = self.tableWidget_database.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "From"))
        item = self.tableWidget_database.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "To"))
        item = self.tableWidget_database.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Daily Target (Piece)"))
        item = self.tableWidget_database.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Distance (ft)"))
        self.tableWidget_database.setColumnWidth(0, 100)
        self.tableWidget_database.setColumnWidth(1, 100)
        self.tableWidget_database.setColumnWidth(2, 150)
        self.tableWidget_database.setColumnWidth(3, 150)

        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.menu_about.setText(_translate("MainWindow", "About"))
        self.menu_about.setWhatsThis(_translate("MainWindow", "Show credit window"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    
