# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_page_bak.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 477)
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
        self.pb_view_t = QtWidgets.QPushButton(self.centralwidget)
        self.pb_view_t.setMinimumSize(QtCore.QSize(150, 23))
        self.pb_view_t.setMaximumSize(QtCore.QSize(200, 50))
        self.pb_view_t.setStyleSheet("font: 14pt \"Agency FB\";")
        self.pb_view_t.setObjectName("pb_view_t")
        self.horizontalLayout_3.addWidget(self.pb_view_t)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pb_import_t = QtWidgets.QPushButton(self.centralwidget)
        self.pb_import_t.setMinimumSize(QtCore.QSize(150, 23))
        self.pb_import_t.setMaximumSize(QtCore.QSize(200, 50))
        self.pb_import_t.setStyleSheet("font: 14pt \"Agency FB\";")
        self.pb_import_t.setObjectName("pb_import_t")
        self.horizontalLayout_5.addWidget(self.pb_import_t)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pb_gen_duty_t = QtWidgets.QPushButton(self.centralwidget)
        self.pb_gen_duty_t.setMinimumSize(QtCore.QSize(150, 23))
        self.pb_gen_duty_t.setMaximumSize(QtCore.QSize(200, 50))
        self.pb_gen_duty_t.setStyleSheet("font: 14pt \"Agency FB\";")
        self.pb_gen_duty_t.setObjectName("pb_gen_duty_t")
        self.horizontalLayout_7.addWidget(self.pb_gen_duty_t)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pb_gen_free_t = QtWidgets.QPushButton(self.centralwidget)
        self.pb_gen_free_t.setMinimumSize(QtCore.QSize(150, 23))
        self.pb_gen_free_t.setMaximumSize(QtCore.QSize(200, 50))
        self.pb_gen_free_t.setStyleSheet("font: 14pt \"Agency FB\";")
        self.pb_gen_free_t.setObjectName("pb_gen_free_t")
        self.horizontalLayout_8.addWidget(self.pb_gen_free_t)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 23))
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
        self.pb_view_t.setText(_translate("MainWindow", "查看课表"))
        self.pb_import_t.setText(_translate("MainWindow", "导入课表"))
        self.pb_gen_duty_t.setText(_translate("MainWindow", "生成排班表"))
        self.pb_gen_free_t.setText(_translate("MainWindow", "生成空闲表"))
