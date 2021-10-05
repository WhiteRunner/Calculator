from PyQt5.Qt import *
from PyQt5 import QtGui
from ui.calculator_ui  import Ui_Form

class Window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 将layoutWidget上的布局转移到每个tab上
        self.tab1.setLayout(self.gridLayout)

        self.set_style()
        self.press_equal = False


    def resizeEvent(self, re: QtGui.QResizeEvent) -> None:
        self.tabWidget.resize(self.width(), self.height())


    def set_style(self):
        # 加载qss样式
        with open(r"style\tabWidget.qss", "r", encoding='utf8') as f:
            self.setStyleSheet(f.read())
        with open("style\calculator.qss", "r", encoding='utf8') as f:
            self.tab1.setStyleSheet(f.read())

    '''
    1.可使用键盘操作,等号可以被大小键盘的enter触发
    2.显示%并参与计算
    3.对于计算出的结果,如果继续使用运算符号,会接着运算,否则重置
    4.显示屏数字0常驻
    5.可使用括号
    6.数字过多会缩小字体,最后禁止输入,数字减少会恢复字体大小
    7.整数不会显示x.0的形式
    '''
    def clickBtnOnCalculator(self):

        text_org = self.let1.text()
        text_new = self.sender().text()
        width = self.tab1.width()

        # 如果上一次按=号，以下值在清空editline后输入
        if self.press_equal==True and text_new in ['0','1','2','3','4','5','6','7','8','9','(',')','.']:
            if text_new=='.':
                self.let1.setText('0'+text_new)
            else:
                self.let1.setText(text_new)
            self.press_equal = False
            return
        self.press_equal = False

        if text_org=='0' and text_new  in ['0','1','2','3','4','5','6','7','8','9','(',')']:
            self.let1.setText(text_new)
        elif text_new=='←':
            length = len(text_org)
            expression = text_org[0:length - 1]
            if width / length > 40:
                self.let1.setStyleSheet("font-size: 60px;")
            if expression == '':
                self.let1.setText('0')
            else:
                self.let1.setText(expression)
        elif text_new == 'C':
            self.let1.setText('0')
            self.let1.setStyleSheet("font-size: 60px;")
        elif text_new == '=':
            try:
                # 后面加个空格防止和后面的数字连起来
                text_rep=text_org.replace('%','/100 ')
                result = round(eval(str(text_rep)),8)
                # 数字最后一位是0的转化为整数
                result = int(result) if str(result)[-1]=='0' else result
                self.let1.setText(str(result))
                if width / len(str(result)) > 40:
                    self.let1.setStyleSheet("font-size: 60px;")
                self.press_equal = True
            except Exception:
                # =号运算发生异常editline文本保持原状不变
                self.let1.setText(text_org)
        else:
            text_update = text_org + text_new
            numbers = len(text_update)
            # 显示屏放不下就把字变小
            if width/numbers  < 40:
                self.let1.setStyleSheet("font-size: 45px;")
            # 再放不下就不让输入
            if width/numbers  < 30:
                self.let1.setText(text_org)
            else:
                # 正常输入
                self.let1.setText(text_update)







if __name__ == "__main__":
    import sys

    # 创建一个应用程序对象
    app = QApplication(sys.argv)

    # 创建控件作为窗口控件
    window = Window()

    # 展示控件
    window.show()

    # 执行程序
    sys.exit(app.exec_())


