# UI 代码测试

测试主函数：

```python
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tran = QtWidgets.QMainWindow()
    ui = Ui_Tran()
    ui.setupUi(Tran)
    Tran.show()
    sys.exit(app.exec_())
```