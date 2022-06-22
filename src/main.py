from mimetypes import init
from page_controller import Controller
from PyQt5 import QtCore, QtWidgets, QtCore
from functions import *
import sys


def main():
    initFiles()

    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()  # 控制器实例
    controller.show_start_page()  # 默认展示的是 start_page 页面
    print('UI start')
    sys.exit(app.exec_())


if __name__ == '__main__':
    print('开始运行')
    main()
