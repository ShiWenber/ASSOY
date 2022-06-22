"""
信号量定义为类的方法是为了和其他界面通信，如果仅仅在页面内部使用信号量，则可以直接connect()方法
"""
from re import U
from turtle import clear

from zmq import EVENT_ALL_V1
from ui.ui_start_page import Ui_MainWindow
from ui.ui_t_page import Ui_t_page  # 表格展示界面
from ui.ui_t_gen_page import Ui_t_gen_page  # 表格生成界面
from functions import *

import sys
from PyQt5 import QtCore, QtWidgets, QtCore
from shutil import copy
import os


# 主窗口
class Start_page(QtWidgets.QMainWindow, Ui_MainWindow):
    switch_view_t = QtCore.pyqtSignal()  # 跳转信号, 在主界面跳转到表格查看
    switch_view_free_t = QtCore.pyqtSignal()  # 跳转信号, 在主界面跳转到空闲表
    switch_gen_duty_t = QtCore.pyqtSignal()  # 跳转信号, 在主界面跳转到排班表
    switch_gen_free_t = QtCore.pyqtSignal()  # 跳转信号, 在主界面跳转到空闲表生成

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_view_t.clicked.connect(self.go_t_page)
        self.pb_view_free_t.clicked.connect(self.go_t_page)
        self.pb_gen_free_t.clicked.connect(self.go_t_gen_page)
        self.pb_gen_duty_t.clicked.connect(self.go_t_gen_page)

        self.pb_import_t.clicked.connect(self.pop_up_open_files_windows)

    def go_t_page(self):
        self.switch_view_t.emit()

    def go_t_gen_page(self):
        self.switch_gen_free_t.emit()

    def pop_up_open_files_windows(self):
        fileNames, fileType = QtWidgets.QFileDialog.getOpenFileNames(self, "选取文件", os.getcwd(),
                                                                     "Excel Files(*.xlsx)")
        print("geted:")
        print(fileNames)
        print(fileType)

        # 将文件复制到input中
        for i in fileNames:
            copy(i, "./input")
            print("copyed:" + i.split("/")[-1])


# 查看课表窗口
class T_page(QtWidgets.QWidget, Ui_t_page):
    switch_view_start_page = QtCore.pyqtSignal()  # 跳转信号, 在表格查看界面跳转到主界面
    # switch_del = QtCore.pyqtSignal()  # 信号, 删除当前课表
    # switch_del_all = QtCore.pyqtSignal()  # 信号, 删除全部课表
    current_student_index = 0
    students = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_del.clicked.connect(self.del_t)
        self.pb_del_all.clicked.connect(self.del_all_t)

        self.refresh_page()

    def refresh_page(self):
        self.comboBox.clear()
        self.students = getStudentsList()
        self.comboBox.addItems([i.getName() for i in self.students])
        self.comboBox.currentIndexChanged.connect(self.show_t)

    def del_t(self):
        base = os.getcwd()
        print(self.current_student.getName() + ".xlsx")
        for i in os.listdir(base + "\\strTable"):
            if i.endswith(".xlsx") and i == self.current_student.getName() + ".xlsx":
                print("del:strTable\\" + i)
                os.remove(base + "\\strTable\\" + i)
                return
        for i in os.listdir(base + "\\input"):
            if i.endswith(".xlsx") and i == self.current_student.getName() + ".xlsx":
                print("del: " + i)
                os.remove(base + "\\input\\" + i)
                return
        for i in os.listdir(base + "\\numTable"):
            if i.endswith(".xlsx") and i == self.current_student.getName() + ".xlsx":
                print("del: " + i)
                os.remove(base + "\\numTable\\" + i)
                return

        self.refresh_page()
        # 刷新列表元素

    def del_all_t(self):
        base = os.getcwd()
        clearOutFile()

        for i in os.listdir(base + "\\input"):
            if (i.endswith(".xlsx")):
                print("del: " + i)
                os.remove(base + "\\input\\" + i)
            return

        self.refresh_page()

    def closeEvent(self, event):
        """重写closeEvent方法，实现窗口关闭时选择是否返回主界面

        Args:
            event (_type_): _description_
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "返回主界面？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:

            self.go_start_page()
            event.accept()  # 接受关闭信号
        else:
            event.accept()  # 接受关闭信号

        event.accept()

    def show_t(self, i):
        t = getStudentsList()[i].getStrTable()
        self.current_student = getStudentsList()[i]
        print("------------------------------------------------")
        print(t)
        print(len(t))
        print(len(t.iloc[:, 0]))
        print("------------------------------------------------")
        print(t.iloc[0, 0])

        for i in range(5):
            for j in range(7):
                self.tableWidget.setItem(
                    i, j, QtWidgets.QTableWidgetItem(t.iloc[i, j]))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def go_start_page(self):
        self.switch_view_start_page.emit()


# 生成排班表窗口
class T_gen_page(QtWidgets.QWidget, Ui_t_gen_page):
    switch_view_start_page = QtCore.pyqtSignal()  # 跳转信号, 在表格查看界面跳转到主界面

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        """重写closeEvent方法，实现窗口关闭时询问是否返回主界面

        Args:
            event (_type_): _description_
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               "本程序",
                                               "返回主界面？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.go_start_page()
            event.accept()  # 接受关闭信号
        else:
            event.accept()  # 接受关闭信号

    def go_start_page(self):
        self.switch_view_start_page.emit()


class Controller:
    """页面跳转控制器
    """

    def __init__(self):
        pass

    # 跳转到 主 窗口
    def show_start_page(self):
        self.start_page = Start_page()
        self.start_page.switch_view_t.connect(self.show_t_page)
        self.start_page.switch_gen_free_t.connect(self.show_t_gen_page)
        self.start_page.show()

    # 跳转到 查看课表 窗口, 关闭原窗口
    def show_t_page(self):
        self.t_page = T_page()
        self.start_page.close()  # 关闭主窗口
        self.t_page.switch_view_start_page.connect(
            self.show_start_page)  # 通过t_page的信号连接到start_page的槽, 实现返回主界面
        self.t_page.show()
        # self.show_start_page()

    # 跳转到 生成排班表 窗口
    def show_t_gen_page(self):
        self.t_gen_page = T_gen_page()
        self.start_page.close()
        self.t_page.switch_view_start_page.connect(
            self.show_start_page)  # 通过t_page的信号连接到start_page的槽, 实现返回主界面
        self.t_gen_page.show()
