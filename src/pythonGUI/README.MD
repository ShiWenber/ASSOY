# pythonGUI学习日志
通过C语言编译的dll加上python代码实现混合语言编程，用python实现图形界面，调用c来实现函数

```
gitpod /workspace/a-work-for-python-class $ /home/gitpod/.pyenv/versions/3.8.12/bin/python /workspace/a-work-for-python-class/pythonGUI/GUI.pyTraceback (most recent call last):
  File "/workspace/a-work-for-python-class/pythonGUI/GUI.py", line 2, in <module>
    from PyQt5 import QtCore, QtWidgets
```
上述问题的出现解决方法(仅仅适用于gitpod类型的在线编译器，在本机上应该考虑是否是使用错了编译路径，pip安装的默认路径是python官方的，不是minGW提供的python编译路径)：
https://blog.csdn.net/Felaim/article/details/108726908

使用pyqt5的designer能够用图形化的方式进行页面设计，更便捷，可以将业务逻辑代码和ui界面代码分成两个页面

 unable to access 'https://github.com/wenboshicn/a-work-for-python-class.git/': OpenSSL SSL_read: Connection was reset, errno 10054
 解决方式：
 https://blog.csdn.net/weixin_43883666/article/details/114738288



.ui文件由pyqt5中的designer制作
.ui文件为.py的输出方式（命令行）：
`python -m PyQt5.uic.pyuic demo.ui -o demo.py`


pyqt5 模板：
```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class MainWindow(QMainWindow):
    def __init__(self,parent = None):
        super(MainWindow, self).__init__(parent)
        self.resize(600, 300)
        self.status = self.statusBar()
        self.status.showMessage("这是状态提示", 10000)
        self.setWindowTitle("MainWindow界面")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

————————————————
版权声明：本文为CSDN博主「勤奋的大熊猫」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/u011699626/article/details/113698939
 
 