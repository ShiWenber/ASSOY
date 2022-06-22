import imp
from ui_start_page import Ui_MainWindow as START_Ui   # 主菜单界面的库
from ui_t_page import Ui_t_page as T_Ui
from ui_t_gen_table import Ui_t_gen_page as Tgen_Ui
# from ui_t_page import Ui_MainWindow as T_Ui           # 查看课表界面的库
# from ui_t_gen_table import Ui_MainWindow as Tgen_Ui  # 生成值班表界面的库

import sys
from PyQt5 import QtCore, QtWidgets, QtCore

# 主窗口
class STARTWindow(QtWidgets.QMainWindow, START_Ui):
    switch_window1 = QtCore.pyqtSignal() # 跳转信号
    switch_window2 = QtCore.pyqtSignal() # 跳转信号
    switch_window3 = QtCore.pyqtSignal() # 跳转信号
    def __init__(self):
        super(STARTWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.goT)
        self.pushButton_3.clicked.connect(self.goTgen)
    def goT(self):
        self.switch_window1.emit()
    def goTgen(self):
        self.switch_window2.emit()
    def goImport(self):
        self.switch_window3.emit()

# 查看课表窗口
class TWindow(QtWidgets.QMainWindow, T_Ui):
    def __init__(self):
        super(TWindow, self).__init__()
        self.setupUi(self)

# 生成排班表窗口
class TgenWindow(QtWidgets.QMainWindow, Tgen_Ui):
    def __init__(self):
        super(TgenWindow, self).__init__()
        self.setupUi(self)


# 利用一个控制器来控制页面的跳转
class Controller:
    def __init__(self):
        pass
    # 跳转到 主 窗口
    def show_START(self):
        self.START = STARTWindow()
        self.START.switch_window1.connect(self.show_T)
        self.START.switch_window2.connect(self.show_Tgen)
        self.START.show()
    # 跳转到 查看课表 窗口
    def show_T(self):
        self.T = TWindow()
        self.START.close()
        self.T.show()
    # 跳转到 生成排班表 窗口
    def show_Tgen(self):
        self.Tgen = TgenWindow()
        self.START.close()
        self.Tgen.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller() # 控制器实例
    controller.show_START() # 默认展示的是 START 页面
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



