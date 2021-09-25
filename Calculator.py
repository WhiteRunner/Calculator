from PyQt5.Qt import *
from PyQt5 import QtGui
from Function import cal_100m_score
import sys

class Window(QWidget):
    def __init__(self,title):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(500, 500)
        self.setup_ui()


    def setup_ui(self):
        pass



# 创建一个应用程序对象
app = QApplication(sys.argv)

# 创建控件作为窗口控件
window = Window('标题')



# 展示控件 只有窗口控件需要show,其子控件自动展示
window.show()

# 执行程序并在执行结束后返回退出码
sys.exit(app.exec_())