from PyQt5.Qt import *
from PyQt5 import QtGui, QtCore
from qtui import Ui_Form
import sys

class Window(QMainWindow,Ui_Form):
    def __init__(self,title):
        super().__init__()
        self.setWindowTitle(title)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)


    def resizeEvent(self, re: QtGui.QResizeEvent) -> None:
        super().resizeEvent(re)
        width=self.width()
        height=self.height()
        # self.tabWidget.setGeometry(QtCore.QRect(0, 0, width, height))
        self.tabWidget.resize(width, height)
        self.tab1.resize(width-10, height-25)
        self.tab2.resize(width-10, height-25)
        self.tab3.resize(width-10, height-25)
        self.calculator_resize(self.tab1)




# 创建一个应用程序对象
app = QApplication(sys.argv)

# 创建控件作为窗口控件
window = Window('标题')

# 展示控件 只有窗口控件需要show,其子控件自动展示
window.show()

# 执行程序并在执行结束后返回退出码
sys.exit(app.exec_())