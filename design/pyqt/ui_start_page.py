# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_page.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 557)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 24pt \"Agency FB\";")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 23))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton.setStyleSheet("font: 14pt \"Agency FB\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(150, 23))
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_4.setStyleSheet("font: 14pt \"Agency FB\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 23))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_2.setStyleSheet("font: 14pt \"Agency FB\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 50, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 23))
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_3.setStyleSheet("font: 14pt \"Agency FB\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 50)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(150, 23))
        self.pushButton_5.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_5.setStyleSheet("font: 14pt \"Agency FB\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_8.addWidget(self.pushButton_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">云南大学学生排班工具</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "查看课表"))
        self.pushButton_4.setText(_translate("MainWindow", "查看空闲表"))
        self.pushButton_2.setText(_translate("MainWindow", "导入课表"))
        self.pushButton_3.setText(_translate("MainWindow", "生成排班表"))
        self.pushButton_5.setText(_translate("MainWindow", "生成空闲表"))
