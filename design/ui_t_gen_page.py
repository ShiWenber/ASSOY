# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 't_gen_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_t_gen_page(object):
    def setupUi(self, t_gen_page):
        t_gen_page.setObjectName("t_gen_page")
        t_gen_page.resize(837, 296)
        self.verticalLayout = QtWidgets.QVBoxLayout(t_gen_page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(t_gen_page)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_repro = QtWidgets.QPushButton(t_gen_page)
        self.pb_repro.setMaximumSize(QtCore.QSize(150, 23))
        self.pb_repro.setObjectName("pb_repro")
        self.horizontalLayout.addWidget(self.pb_repro)
        self.pb_clear = QtWidgets.QPushButton(t_gen_page)
        self.pb_clear.setMaximumSize(QtCore.QSize(150, 23))
        self.pb_clear.setObjectName("pb_clear")
        self.horizontalLayout.addWidget(self.pb_clear)
        self.pb_open_path = QtWidgets.QPushButton(t_gen_page)
        self.pb_open_path.setMaximumSize(QtCore.QSize(150, 23))
        self.pb_open_path.setObjectName("pb_open_path")
        self.horizontalLayout.addWidget(self.pb_open_path)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(t_gen_page)
        QtCore.QMetaObject.connectSlotsByName(t_gen_page)

    def retranslateUi(self, t_gen_page):
        _translate = QtCore.QCoreApplication.translate
        t_gen_page.setWindowTitle(_translate("t_gen_page", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("t_gen_page", "1-2节"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("t_gen_page", "3-4节"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("t_gen_page", "5-6节"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("t_gen_page", "7-8节"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("t_gen_page", "9-10节"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("t_gen_page", "周一"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("t_gen_page", "周二"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("t_gen_page", "周三"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("t_gen_page", "周四"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("t_gen_page", "周五"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("t_gen_page", "周六"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("t_gen_page", "周日"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pb_repro.setText(_translate("t_gen_page", "重新生成"))
        self.pb_clear.setText(_translate("t_gen_page", "清空"))
        self.pb_open_path.setText(_translate("t_gen_page", "打开文件位置"))
