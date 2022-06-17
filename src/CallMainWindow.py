# https://blog.csdn.net/qq_41398808/article/details/102813181
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from fileopen import Ui_MainWindow
import sys
import os
from shutil import copy
 
class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.actionfileopen.triggered.connect(self.open_files) # 连接按钮的信号与槽（将控件与方法相连）
 
    def open_files(self):
        # fileName,fileType = QtWidgets.QFileDialog.getOpenFileNames(self, "选取文件", os.getcwd(), 
        # "All Files(*);;Text Files(*.txt);;Excel Files(*.xlsx)")

        fileNames,fileType = QtWidgets.QFileDialog.getOpenFileNames(self, "选取文件", os.getcwd(), 
        "Excel Files(*.xlsx)")
        print("geted:")
        print(fileNames)
        print(fileType)

        # 将文件复制到input中
        for i in fileNames:
            copy(i, "./input")
            print("copyed:" + i.split("/")[-1])
            



        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())