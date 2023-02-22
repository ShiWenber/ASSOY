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
    # 如果不存在就创建文件夹
    if (not os.path.exists('./input')):
        os.mkdir('./input')
    if (not os.path.exists('./numTable')):
        os.mkdir('./numTable')
    if (not os.path.exists('./strTable')):
        os.mkdir('./strTable')
    if (not os.path.exists('./dutyTable')):
        os.mkdir('./dutyTable')
    main()

    
    # # -----------调用自动做系统图的工具
    # from pycallgraph import PyCallGraph
    # from pycallgraph.output import GraphvizOutput
    # from pycallgraph import Config
    # from pycallgraph import GlobbingFilter

  
    # ----------使用自动调用系统图工具
    # config = Config()
    # # 添加需要绘制的函数名或类名
    # config.trace_filter = GlobbingFilter(include=[
    #     'main',
    #     # 'ui.*',
    #     'functions.*',
    #     'page_controller.*',
    # ])
    # # 以下添加需要剔除的函数名或类名
    # # config.trace_filter = GlobbingFilter(exclude=[])

    # graphviz = GraphvizOutput()
    # graphviz.output_file = './graph/calling_graph'+'.png'   # 要保存的路径名和文件名
    # with PyCallGraph(output=graphviz, config=config):
    #     main()
