# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 't_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_t_page(object):
    def setupUi(self, t_page):
        t_page.setObjectName("t_page")
        t_page.resize(837, 296)
        self.verticalLayout = QtWidgets.QVBoxLayout(t_page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(t_page)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.tableWidget = QtWidgets.QTableWidget(t_page)
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
        self.pb_del = QtWidgets.QPushButton(t_page)
        self.pb_del.setMaximumSize(QtCore.QSize(150, 23))
        self.pb_del.setObjectName("pb_del")
        self.horizontalLayout.addWidget(self.pb_del)
        self.pb_del_all = QtWidgets.QPushButton(t_page)
        self.pb_del_all.setMaximumSize(QtCore.QSize(150, 23))
        self.pb_del_all.setObjectName("pb_del_all")
        self.horizontalLayout.addWidget(self.pb_del_all)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(t_page)
        self.comboBox.currentIndexChanged['QString'].connect(self.tableWidget.update)
        QtCore.QMetaObject.connectSlotsByName(t_page)

    def retranslateUi(self, t_page):
        _translate = QtCore.QCoreApplication.translate
        t_page.setWindowTitle(_translate("t_page", "Form"))
        self.comboBox.setItemText(0, _translate("t_page", "选择1"))
        self.comboBox.setItemText(1, _translate("t_page", "选择2"))
        self.comboBox.setItemText(2, _translate("t_page", "选择3"))
        self.comboBox.setItemText(3, _translate("t_page", "选择4"))
        self.comboBox.setItemText(4, _translate("t_page", "选择5"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("t_page", "1-2节"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("t_page", "3-4节"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("t_page", "5-6节"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("t_page", "7-8节"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("t_page", "9-10节"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("t_page", "周一"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("t_page", "周二"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("t_page", "周三"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("t_page", "周四"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("t_page", "周五"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("t_page", "周六"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("t_page", "周日"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pb_del.setText(_translate("t_page", "删除该表"))
        self.pb_del_all.setText(_translate("t_page", "删除全部表"))
