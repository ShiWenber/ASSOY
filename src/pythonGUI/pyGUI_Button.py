import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QPushButtonDemo(QDialog):
    # pyqt_clicked1 = pyqtSignal()
    # pyqt_clicked2 = pyqtSignal()
    def __init__(self):
        super(QPushButtonDemo , self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('QPushButton Demo')
        layout = QVBoxLayout()
        self.button1 = QPushButton('first')   # 初始化的时候设置button的字符
        self.button1.setText('第一个')  # 用setText方法设置button字符
        self.button1.setCheckable(True)    # 
        self.button1.toggle()
        
        # 下一句将信号连接到槽
        self.button1.clicked.connect( lambda:self.whichButton(self.button1))  
        # 当使用QPushButton.clicked.connect(lambda:self.信号槽方法)。connect方法传参数时，需要加上“lambda:”
        layout.addWidget(self.button1)
        self.setLayout(layout)
        
        
    #多个信号使用同一槽
    def whichButton(self,btn):
        print('被单击的按钮是'+btn.text())  # 获得button的文本
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())
    # 以上四行是标准用法框架