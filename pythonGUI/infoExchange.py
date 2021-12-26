from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QApplication, QFormLayout, QDialog
import sys
 
 
class sub(QDialog): #创建一个dialog,用作被调用类
    changeValue = pyqtSignal(str) #创建槽信号,str指定接收参数为str类型(字符串类型)
    def __init__(self, parent=None):
        super(sub, self).__init__(parent)
        self.initUi()
 
    def initUi(self):
        self.setWindowTitle('子窗口')
        self.lineEdit = QLineEdit()
        self.formlayout = QFormLayout()
        self.formlayout.addRow('输入', self.lineEdit)
        self.lineEdit.textChanged.connect(self.setValue)
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.formlayout)
        self.setLayout(self.vbox)
        self.resize(200, 200)
        self.show()
    def setValue(self):
        self.changeValue.emit(str(self.lineEdit.text())) #发送带参数的信号,信号为本类中的lineEdit.text(),即lineEdit的内容
 
class mainwin(QWidget):
    def __init__(self):
        super(mainwin, self).__init__()
        self.ex = sub(self) #调用子类dialog,这一步一定要在self.initUi前面,不然initUi中不能调用没有实例化的changeValue这个槽信号
        self.initUi()
 
    def initUi(self):
        self.setWindowTitle('主窗口')
        self.lineEdit = QLineEdit()
        self.formlayout = QFormLayout()
        self.formlayout.addRow('输出', self.lineEdit)
        self.ex.changeValue.connect(self.getValue) #调用sub类中的changeValue槽信号并绑定信号到getValue这个方法
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.formlayout)
        self.setLayout(self.vbox)
        self.resize(400, 400)
        self.show()
 
    def getValue(self, val): #接收信号的函数,并且接收参数
        self.lineEdit.setText(val)#将参数传递给本类lineEdit
        # self.lineEdit.setText(self.ex.lineEdit.text()) #将sub的lineEdit中的内容传递给mainwin本类中的lineEdit中
        print(val)  # 观察控制台可以发现每次改变文本框内的字符都会输出到控制台，可以肯定参数已经通过connect传递给了getValue函数


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = mainwin()
    sys.exit(app.exec_())