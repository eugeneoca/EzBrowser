# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/browser.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.MainFrame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 781, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_url = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txt_url.setObjectName("txt_url")
        self.horizontalLayout.addWidget(self.txt_url)
        self.btn_search = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout.addWidget(self.btn_search)
        self.gridLayoutWidget = QtWidgets.QWidget(self.MainFrame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 40, 781, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.browser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.browser.setOpenExternalLinks(True)
        self.browser.setObjectName("browser")
        self.gridLayout.addWidget(self.browser, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.MainFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EzBrowser"))
        self.btn_search.setText(_translate("MainWindow", "Search"))

