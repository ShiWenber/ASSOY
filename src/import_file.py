# 创建一个只有按钮的页面

from sre_parse import SubPattern


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
