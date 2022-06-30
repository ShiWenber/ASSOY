"""
信号量定义为类的方法是为了和其他界面通信，如果仅仅在页面内部使用信号量，则可以直接connect()方法
"""
from locale import currency
from msilib.schema import ComboBox
from re import U
from turtle import clear
from matplotlib.pyplot import show

from zmq import EVENT_ALL_V1
from ui.ui_start_page import Ui_MainWindow
from ui.ui_t_page import Ui_t_page  # 表格展示界面
from ui.ui_t_gen_page import Ui_t_gen_page  # 表格生成界面
from ui.ui_free_t_page import Ui_free_t_page  # 空闲表界面
from functions import *

import sys
from PyQt5 import QtCore, QtWidgets, QtCore
from shutil import copy
import os


# 主窗口
class Start_page(QtWidgets.QMainWindow, Ui_MainWindow):
    """主页面类

    Args:
        QtWidgets (_type_): _description_
        Ui_MainWindow (_type_): 自定义图像界面类
    """
    switch_view_t = QtCore.pyqtSignal()  # 跳转信号, 在主界面跳转到表格查看
    switch_gen_duty_t = QtCore.pyqtSignal()  # 跳转信号, 在主界面跳转到排班表
    switch_gen_free_t = QtCore.pyqtSignal()  # 跳转信号, 在主界面跳转到空闲表生成

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_view_t.clicked.connect(self.go_t_page)
        self.pb_gen_free_t.clicked.connect(self.go_free_t_page)
        self.pb_gen_duty_t.clicked.connect(self.go_t_gen_page)

        self.pb_import_t.clicked.connect(self.pop_up_open_files_windows)

    def go_t_page(self):
        self.switch_view_t.emit()

    def go_t_gen_page(self):
        self.switch_gen_duty_t.emit()

    def go_free_t_page(self):
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

        initFiles()


# 查看课表窗口
class T_page(QtWidgets.QWidget, Ui_t_page):
    """查看课表窗口类

    Args:
        QtWidgets (_type_): _description_
        Ui_t_page (_type_): 自定义图形界面类
    """
    switch_view_start_page = QtCore.pyqtSignal()  # 跳转信号, 在表格查看界面跳转到主界面
    # switch_del = QtCore.pyqtSignal()  # 信号, 删除当前课表
    # switch_del_all = QtCore.pyqtSignal()  # 信号, 删除全部课表
    current_student_index = int()
    students = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current_student_index = 0
        self.students = getStudentsList()

        self.comboBox.clear()
        self.comboBox.addItem("请选择学生")
        self.tableWidget.clearContents()

        self.pb_del.clicked.connect(self.del_t)
        self.pb_del_all.clicked.connect(self.del_all_t)

        self.comboBox.addItems([i.getName() for i in self.students])
        self.comboBox.currentIndexChanged.connect(self.show_t)

    def refresh_page(self):
        self.current_student_index = 0
        self.students = getStudentsList()

        self.comboBox.clear()
        self.comboBox.addItem("请选择学生")
        self.tableWidget.clearContents()
        self.comboBox.addItems([i.getName() for i in self.students])
        self.comboBox.currentIndexChanged.connect(self.show_t)

    def del_t(self):
        base = os.getcwd()
        print(self.students[self.current_student_index].getName() + ".xlsx")
        for i in os.listdir(base + "\\strTable"):
            if i.endswith(".xlsx") and i == self.students[self.current_student_index].getName() + ".xlsx":
                print("del:strTable\\" + i)
                os.remove(base + "\\strTable\\" + i)
        for i in os.listdir(base + "\\input"):
            if i.endswith(".xlsx") and i == self.students[self.current_student_index].getName() + ".xlsx":
                print("del: " + i)
                os.remove(base + "\\input\\" + i)
        for i in os.listdir(base + "\\numTable"):
            if i.endswith(".xlsx") and i == self.students[self.current_student_index].getName() + ".xlsx":
                print("del: " + i)
                os.remove(base + "\\numTable\\" + i)

        # 刷新列表元素
        self.refresh_page()

    def del_all_t(self):
        base = os.getcwd()
        clearOutFile()

        for i in os.listdir(base + "\\input"):
            if (i.endswith(".xlsx")):
                print("del: " + i)
                os.remove(base + "\\input\\" + i)

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
        if i <= 0:
            print("show_t: " + str(i))
            self.tableWidget.clearContents()
            # 是否需要对self.current_student_index进行更新？
        else:
            print("show_t: " + str(i))
            self.current_student_index = i - 1
            t = self.students[self.current_student_index].getStrTable()
            # print("------------------------------------------------")
            # print(t)
            # print(len(t))
            # print(len(t.iloc[:, 0]))
            # print("------------------------------------------------")
            # print(t.iloc[0, 0])

            for i in range(5):
                for j in range(7):
                    self.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(t.iloc[i, j]))

            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()

    def go_start_page(self):
        self.switch_view_start_page.emit()


# 生成排班表窗口
# 获取(x,y)的值
# self.tableWidget.cellWidget(x,y).currentText()
# self.tableWidget.item(d_row,d_col).text()#获取某行某列item中的x信息

class T_gen_page(QtWidgets.QWidget, Ui_t_gen_page):
    switch_view_start_page = QtCore.pyqtSignal()  # 跳转信号, 在表格查看界面跳转到主界面
    students = []
    freeTable_str = []
    freeTable_obj = []
    dutylist = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_repro.clicked.connect(self.repro)
        self.pb_clear.clicked.connect(self.clearTable)

        self.students = getStudentsList()
        self.freeTable_str, self.freeTable_obj = to_freeTable(self.students)

        # combox = QtWidgets.QComboBox()
        # combox.addItem("请选择学生")

        self.dutylist, self.students = to_dutyTable(self.students)

        print(self.dutylist)
        # 打印值班表
        exist = 0
        for i in range(5):
            for j in range(7):
                for k in self.dutylist:
                    if k[0] == i and k[1] == j:
                        # print(k[2].getName(), end=' ')
                        self.tableWidget.setItem(
                            i, j, QtWidgets.QTableWidgetItem(k[2].getName()))
                        self.dutylist.remove(k)
                        exist = 1
                        break
                if exist == 0:
                    # print('-', end=' ')
                    self.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem('无'))
                else:
                    exist = 0
            print()

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def clearTable(self):
        self.tableWidget.clearContents()

    def repro(self):
        self.students = getStudentsList()
        self.freeTable_str, self.freeTable_obj = to_freeTable(self.students)

        # combox = QtWidgets.QComboBox()
        # combox.addItem("请选择学生")

        self.dutylist, self.students = to_dutyTable(self.students)

        print(self.dutylist)
        # 打印值班表
        exist = 0
        for i in range(5):
            for j in range(7):
                for k in self.dutylist:
                    if k[0] == i and k[1] == j:
                        # print(k[2].getName(), end=' ')
                        self.tableWidget.setItem(
                            i, j, QtWidgets.QTableWidgetItem(k[2].getName()))
                        self.dutylist.remove(k)
                        exist = 1
                        break
                if exist == 0:
                    # print('-', end=' ')
                    self.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem('无'))
                else:
                    exist = 0
            print()

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

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

# 生成空闲表


class Free_t_page(QtWidgets.QWidget, Ui_free_t_page):
    """生成空闲表

    Args:
        QtWidgets (Qtwidgets): form父类
        Ui_free_t_page (Ui_free_t_page): 自定义图形界面类
    """
    switch_view_start_page = QtCore.pyqtSignal()  # 跳转信号, 在表格查看界面跳转到主界面

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current_student_index = 0
        self.students = getStudentsList()

        self.tableWidget.clearContents()

        self.pb_del.clicked.connect(self.del_t)
        self.pb_open_path.clicked.connect(self.open_path)

        t, freeTable_obj = to_freeTable(self.students)
        print(t)
        for i in range(5):
            for j in range(7):
                self.tableWidget.setItem(
                    i, j, QtWidgets.QTableWidgetItem(t.iloc[i, j]))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def refresh_page(self):
        self.current_student_index = 0
        self.students = getStudentsList()

        self.tableWidget.clearContents()

    def del_t(self):
        base = os.getcwd()
        print(self.students[self.current_student_index].getName() + ".xlsx")
        for i in os.listdir(base + "\\freeTable"):
            if i.endswith(".xlsx") and i == self.students[self.current_student_index].getName() + ".xlsx":
                print("del:freeTable\\" + i)
                os.remove(base + "\\freeTable\\" + i)

        self.refresh_page()

    def show_t(self):
        t, freeTable_obj = to_freeTable(self.students)
        print(t)
        for i in range(5):
            for j in range(7):
                self.tableWidget.setItem(
                    i, j, QtWidgets.QTableWidgetItem(t.iloc[i, j]))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def open_path(self):
        os.popen("explorer.exe " + ".\\freeTable")

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
        self.start_page.switch_gen_free_t.connect(self.show_free_t_page)
        self.start_page.switch_gen_duty_t.connect(self.show_t_gen_page)
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
        self.t_gen_page.switch_view_start_page.connect(
            self.show_start_page)  # 通过t_page的信号连接到start_page的槽, 实现返回主界面
        self.t_gen_page.show()

    # 跳转到 空闲表 窗口
    def show_free_t_page(self):
        self.free_t_page = Free_t_page()
        self.start_page.close()
        self.free_t_page.switch_view_start_page.connect(
            self.show_start_page)
        self.free_t_page.show()
