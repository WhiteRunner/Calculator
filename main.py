from PyQt5.Qt import *
import sys
from calculator_impl import Window

# 创建一个应用程序对象
app = QApplication(sys.argv)

# 创建控件作为窗口控件
window = Window()


# 展示控件
window.show()

# 执行程序
sys.exit(app.exec_())