from math import sqrt
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 700)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.tabWidget.setObjectName("tabWidget")

        self.tab1 = QtWidgets.QWidget()
        # self.tab1.resize(590, 675)
        self.tab1.setObjectName("tab1")
        self.tabWidget.addTab(self.tab1, "")

        self.tab2 = QtWidgets.QWidget()
        # self.tab2.resize(590, 675)
        self.tab2.setObjectName("tab2")
        self.tabWidget.addTab(self.tab2, "")

        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        # self.tab3.resize(590, 675)
        self.tabWidget.addTab(self.tab3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.press_equal=False
        self.calculator_init(self.tab1)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "田径计算器"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Form", "计算器"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("Form", "短跑硬实力计算"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("Form", "跨赛事对比"))

    def calculator_init(self,target):
        self.let1 = QLineEdit(target)
        self.let1.setReadOnly(True)
        self.let1.setAlignment(Qt.AlignRight)

        self.btn1 = QPushButton(target)
        self.btn1.setText('7')
        self.btn1.clicked.connect(self.clickNum)

        self.btn2 = QPushButton(target)
        self.btn2.setText('8')
        self.btn2.clicked.connect(self.clickNum)

        self.btn3 = QPushButton(target)
        self.btn3.setText('9')
        self.btn3.clicked.connect(self.clickNum)

        self.btn4 = QPushButton(target)
        self.btn4.setText('4')
        self.btn4.clicked.connect(self.clickNum)

        self.btn5 = QPushButton(target)
        self.btn5.setText('5')
        self.btn5.clicked.connect(self.clickNum)

        self.btn6 = QPushButton(target)
        self.btn6.setText('6')
        self.btn6.clicked.connect(self.clickNum)

        self.btn7 = QPushButton(target)
        self.btn7.setText('1')
        self.btn7.clicked.connect(self.clickNum)

        self.btn8 = QPushButton(target)
        self.btn8.setText('2')
        self.btn8.clicked.connect(self.clickNum)

        self.btn9 = QPushButton(target)
        self.btn9.setText('3')
        self.btn9.clicked.connect(self.clickNum)

        self.btn10 = QPushButton(target)
        self.btn10.setText('0')
        self.btn10.clicked.connect(self.clickNum)

        self.btn11 = QPushButton(target)
        self.btn11.setText('C')
        self.btn11.setObjectName('C')
        self.btn11.clicked.connect(self.clickNum)

        self.btn12 = QPushButton(target)
        self.btn12.setText('.')
        self.btn12.clicked.connect(self.clickNum)

        self.btn13 = QPushButton(target)
        self.btn13.setText('+')
        self.btn13.clicked.connect(self.clickNum)

        self.btn14 = QPushButton(target)
        self.btn14.setText('-')
        self.btn14.clicked.connect(self.clickNum)

        self.btn15 = QPushButton(target)
        self.btn15.setText('*')
        self.btn15.clicked.connect(self.clickNum)

        self.btn16 = QPushButton(target)
        self.btn16.setText('/')
        self.btn16.clicked.connect(self.clickNum)

        self.btn17 = QPushButton(target)
        self.btn17.setText('=')
        self.btn17.setObjectName('equal')
        self.btn17.clicked.connect(self.clickNum)

        self.btn18 = QPushButton(target)
        self.btn18.setText('(')
        self.btn18.clicked.connect(self.clickNum)

        self.btn19 = QPushButton(target)
        self.btn19.setText(')')
        self.btn19.clicked.connect(self.clickNum)

        self.btn20 = QPushButton(target)
        self.btn20.setText('←')
        self.btn20.clicked.connect(self.backspace)

        self.btn21 = QPushButton(target)
        self.btn21.setText('sqrt(')
        self.btn21.setObjectName('sqrt')
        self.btn21.clicked.connect(self.clickNum)

        with open("style/calculator.qss", "r") as f:
            target.setStyleSheet(f.read())

        self.calculator_resize(self.tab1)

    def calculator_resize(self,target):
        height = target.height()
        width = target.width()
        quarter_width=width/4
        half_width=width/2
        let_height=5*height/29
        btn_height=4*height/29

        self.let1.move(1.5, 0)
        self.btn1.move(0, let_height+btn_height)
        self.btn2.move(quarter_width, let_height+btn_height)
        self.btn3.move(half_width, let_height+btn_height)
        self.btn4.move(0, let_height+btn_height*2)
        self.btn5.move(quarter_width, let_height+btn_height*2)
        self.btn6.move(half_width, let_height+btn_height*2)
        self.btn7.move(0, let_height+btn_height*3)
        self.btn8.move(quarter_width, let_height+btn_height*3)
        self.btn9.move(half_width, let_height+btn_height*3)
        self.btn10.move(quarter_width, let_height+btn_height*4)
        self.btn11.move(0, let_height)
        self.btn12.move(half_width, let_height+btn_height*5)
        self.btn13.move(3*quarter_width, let_height+btn_height*4)
        self.btn14.move(3*quarter_width, let_height+btn_height*3)
        self.btn15.move(3*quarter_width, let_height+btn_height*2)
        self.btn16.move(3*quarter_width, let_height+btn_height)
        self.btn17.move(0, let_height+btn_height*5)
        self.btn18.move(0, let_height+btn_height*4)
        self.btn19.move(half_width, let_height+btn_height*4)
        self.btn20.move(quarter_width, let_height)
        self.btn21.move(3*quarter_width, let_height)

        self.let1.resize(width-3, let_height)
        self.btn1.resize(quarter_width, btn_height)
        self.btn2.resize(quarter_width, btn_height)
        self.btn3.resize(quarter_width, btn_height)
        self.btn4.resize(quarter_width, btn_height)
        self.btn5.resize(quarter_width, btn_height)
        self.btn6.resize(quarter_width, btn_height)
        self.btn7.resize(quarter_width, btn_height)
        self.btn8.resize(quarter_width, btn_height)
        self.btn9.resize(quarter_width, btn_height)
        self.btn10.resize(quarter_width, btn_height)
        self.btn11.resize(quarter_width, btn_height)
        self.btn12.resize(quarter_width, btn_height)
        self.btn13.resize(quarter_width, btn_height*2)
        self.btn14.resize(quarter_width, btn_height)
        self.btn15.resize(quarter_width, btn_height)
        self.btn16.resize(quarter_width, btn_height)
        self.btn17.resize(half_width, btn_height)
        self.btn18.resize(quarter_width, btn_height)
        self.btn19.resize(quarter_width, btn_height)
        self.btn20.resize(half_width, btn_height)
        self.btn21.resize(quarter_width, btn_height)


    def clickNum(self):


        text_org = self.let1.text()
        new_text = self.sender().text()

        # 如果上一次按=号，以下值在清空editline后输入
        if self.press_equal==True and new_text in ['0','1','2','3','4','5','6','7','8','9','0','(',')','sqrt(','.']:
            self.let1.setText(new_text)
            self.press_equal = False
            return
        self.press_equal = False

        if new_text not in ['C','=']:
            self.let1.setText(text_org + new_text)
        elif new_text == 'C':
            self.let1.setText('')
        # =号运算发生异常editline文本保持原状不变
        elif new_text == '=':
            try:
                result = round(eval(str(text_org)),4)
                self.let1.setText(str(result))
                self.press_equal = True
            except Exception:
                self.let1.setText(text_org)

    def backspace(self):
        expression = self.let1.text()
        length = len(expression)
        expression = expression[0:length - 1]
        self.let1.setText(expression)
