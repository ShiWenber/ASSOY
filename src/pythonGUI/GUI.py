import helloworld

import ctypes
import sys

from typing import Literal
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow, QLabel, QGridLayout, QWidget, QApplication
from PyQt5.QtCore import QSize
# from ctypes import *

# def pyStrToCStr(pystr):
#     # str_tmp = pystr.encode('utf-8') # 先将py字符串转换为utf-8格式
#     return POINTER(c_char_p(pystr) # ctypes中的格式转换方法



        
# def transfer(inputstr):
#     ll = cdll.LoadLibrary
#     lib = ll(".\C\stringtransfer.dll")
#     strlen = len(inputstr)
#     temp_p = pyStrToCStr(inputstr) # 转成C string
#     lib.transfer(temp_p)
#     pystr = []
#     return temp_p[:strlen]

class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320,240))
        self.setWindowTitle("Hello world")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        
        inputs = "Hello World from PyQt"
        title = QLabel(inputs,self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(title,0,0)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)   #固定写法，传入参数
    mainWin = HelloWindow()   # 创建主窗口对象
    mainWin.show()   # 用ui变量存对象
    
    app.exec_()    #  结束app对象
    ################################
    
    app2 = QApplication(sys.argv)  #固定写法，传入参数
    mainWindow = QMainWindow()   # 创建主窗口对象
    ui = helloworld.Ui_MainWindow()   # 用ui变量存对象
    ui.setupUi(mainWindow) # 创建所有组件
    mainWindow.show()
    sys.exit(app2.exec_())   # 结束整个程序
    