from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets

# 该按钮可以被小键盘和大键盘的enter触发
class EqualBtn(QPushButton):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.grabKeyboard() # 捕获键盘
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key()==Qt.Key_Enter or a0.key()==Qt.Key_Return:
            self.click()