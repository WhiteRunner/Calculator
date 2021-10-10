from PyQt5 import QtGui
from PyQt5.QtCore import QTime
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QWidget, QDoubleSpinBox, QSizePolicy, QButtonGroup, QHeaderView, QListView, QComboBox, \
    QMessageBox, QFileDialog
from ui.calculator_ui import Ui_Form
from ui.raceData import raceData
from utils.athletics_function import *
from ui.myWidget import *
from utils.file_path import *
import datetime


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0) # 设置默认打开第一页

        # 0.实现tabWidget
        # 将layoutWidget上的布局转移到每个tab上
        self.tab1.setLayout(self.gridLayout)
        self.tab2.setLayout(self.verticalLayout)
        self.tab3.setLayout(self.verticalLayout_2)
        # 实现表的展示与数据库的关联
        self.showTableView()

        # 1.实现tab1
        self.press_equal = False

        # 2.实现tab2
        self.raceName.addItems(raceData.keys())

        # 3.实现tab3
        # 设置正在使用的score1
        self.inUseScore1=self.timeScore1
        # 创建输入浮点数的score1
        self.doubleScore1=QDoubleSpinBox()
        self.doubleScore1.setSuffix('米')
        self.doubleScore1.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        # 添加下拉框选项
        events = [['100m', '100m'], ['200m', '200m'], ['400m', '400m'], ['800m', '800m'], ['1000m', '1000m'],
                  ['100m栏', '100mH'], ['110m栏', '110mH'], ['跳高', 'highJump'], ['跳远', 'longJump'],
                  ['三级跳', 'tripleJump'], ['撑杆跳', 'poleVault'], ['标枪', 'Javelin'], ['铅球', 'shotPut']]
        for i, item in enumerate(events):
            self.event1.addItem(item[0], item[1])
            self.event2.addItem(item[0], item[1])
        # 设置性别选项组
        self.sexGroup1,self.sexGroup2=QButtonGroup(self),QButtonGroup(self)
        self.sexGroup1.addButton(self.men1,1)
        self.sexGroup1.addButton(self.women1,2)
        self.sexGroup2.addButton(self.men2,1)
        self.sexGroup2.addButton(self.women2,2)
        self.men1.setChecked(True)
        self.men2.setChecked(True)


        # 4.设置样式
        self.set_style()




    def resizeEvent(self, re: QtGui.QResizeEvent) -> None:
        # 设置tabWidget跟随窗口尺寸变化,使布局可以根据窗口大小自适应
        self.tabWidget.resize(self.width(), self.height())

    # 关联数据库,展示两张表
    def showTableView(self):
        # 0.切换到exe解压到的临时目录/工程目录
        os.chdir(tmd)
        # 1.创建并连接数据库
        self.database = QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName('./db/record.db')
        self.database.open()

        # 2.创建tab2数据模型
        fields1 = ['ID', '项目', '道次', '性别', '风速', '海拔', '原成绩', '修正后成绩']
        self.fixScoreModel=self.createModel('fixScore',fields1)
        # 2.创建tab2数据模型
        fields2 = ['ID', '项目1', '性别1', '成绩1', '项目2', '性别2', '成绩2', '分数']
        self.compareScoreModel = self.createModel('compareScore',fields2)

        # 3.创建tab3视图
        self.createView(self.fixScoreView,self.fixScoreModel)
        # 3.创建tab3视图
        self.createView(self.compareScoreView, self.compareScoreModel)

    def createModel(self,name,fields):
        # 使用继承的QSqlTableModel,使得表中数据居中
        model = MyModel()
        model.setTable(name)
        # 表中数据变化时写入数据库
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        # 读取数据库数据
        model.select()
        # 设置数据模型行标题
        for i, field in enumerate(fields):
            model.setHeaderData(i, Qt.Horizontal, field)
        return model

    def createView(self,view,model):
        # 设置视图使用的模型
        view.setModel(model)
        # 按照id逆序排列
        view.sortByColumn(0, Qt.DescendingOrder)
        # 设置id列隐藏
        view.setColumnHidden(0, True)
        # 设置可拉伸列宽
        for i in range(1, model.columnCount()):
            view.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

    # 切换页面的槽,使得等号按钮在计算器页面时可以grabKeyboard
    def changeTab(self, curr):
        if curr == 0:
            self.equal.grabKeyboard()
        else:
            self.equal.releaseKeyboard()

    def set_style(self):
        # 0.切换工作目录
        os.chdir(tmd)
        # 启用对背景的样式设置
        self.tabWidget.setAttribute(Qt.WA_StyledBackground)
        # 设置表格头的名字(用于qss)
        self.fixScoreView.horizontalHeader().setObjectName("fix_hHeader")
        self.fixScoreView.verticalHeader().setObjectName("fix_vHeader")
        # 设置下拉框的View(用于qss)
        for item in self.tabWidget.findChildren(QComboBox):
            item.setView(QListView())
        # 加载qss样式
        with open(r"style/tabWidget.qss", "r", encoding='utf8') as f1, \
                open(r"style/calculator.qss", "r", encoding='utf8') as f2, \
                open(r"style/calScore.qss", "r", encoding='utf8') as f3:
            self.setStyleSheet(f1.read())
            self.tab1.setStyleSheet(f2.read())
            f3=f3.read()
            self.tab3.setStyleSheet(f3)
            self.tab2.setStyleSheet(f3)

    # 处理对表格操作的通用槽函数
    def handleView(self,sender,delBtn,clearBtn,refreshBtn,outputBtn,model,view):
        if sender == delBtn:
            res = QMessageBox.information(self, '提示', '是否删除选中', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if res == QMessageBox.Yes:
                selectedRows = set()
                # item:QModelIndex
                for item in view.selectedIndexes():
                    selectedRows.add(item.row())
                for i in selectedRows:
                    model.removeRow(i)
                # 重新读取数据
                model.select()
        elif sender == clearBtn:
            res = QMessageBox.information(self, '提示', '是否清空数据', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if res == QMessageBox.Yes:
                for i in range(0, model.rowCount()):
                    model.removeRow(i)
                model.select()
        elif sender == refreshBtn:
            model.select()
            # 按照id倒序排列,也即按照时间顺序排列
            view.sortByColumn(0, Qt.DescendingOrder)
        elif sender == outputBtn:
            col_cnt = model.columnCount()
            row_cnt = model.rowCount()
            fields = []
            output = [] # 保存输出的字符串
            for i in range(1, col_cnt):
                fields.append(model.headerData(i,Qt.Horizontal))
            output.append(' '.join(fields))
            for i in range(0, row_cnt):
                row_values = []
                for j in range(1, col_cnt): # 不需要id字段
                    row_values.append(str(model.record(i).value(j)))
                output.append(' '.join(row_values))
            # 导出文件
            os.chdir(cwd) # 切换到当前所在路径
            result = QFileDialog.getSaveFileName(self, "选择导出路径", "./", "文本文件(*.txt)", "文本文件(*.txt)")
            path = result[0]
            if path != '':
                with open(path, 'w') as f:
                    for s in output:
                        f.write(s + '\n')
                QMessageBox.information(self, '保存状态', '保存成功')


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
        if self.press_equal == True and text_new in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '.']:
            if text_new == '.':
                self.let1.setText('0' + text_new)
            else:
                self.let1.setText(text_new)
            self.press_equal = False
            return
        self.press_equal = False

        if text_org == '0' and text_new in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')']:
            self.let1.setText(text_new)
        elif text_new == '←':
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
                text_rep = text_org.replace('%', '/100 ')
                result = round(eval(str(text_rep)), 8)
                # 数字最后一位是0的转化为整数
                result = int(result) if str(result)[-1] == '0' else result
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
            if width / numbers < 40:
                self.let1.setStyleSheet("font-size: 45px;")
            # 再放不下就不让输入
            if width / numbers < 30:
                self.let1.setText(text_org)
            else:
                # 正常输入
                self.let1.setText(text_update)




    '''
    1.输入项目,道次,性别,原始成绩,风速和海拔,计算真实成绩
    2.可选择比赛项目和年份自动填入风速和海拔
    3.将计算出来的成绩保存到数据库,并显示在表格中
    4.表格可以删除选中列,清空,刷新,导出数据
    '''
    def handleFixScore(self, val):
        # print(val)
        if self.sender() == self.length:
            # if val in ['50m', '60m']:
            #     self.lane.setEnabled(False)
            #     self.men.setEnabled(False)
            #     self.women.setEnabled(False)
            #     self.windSpeed.setEnabled(True)
            # elif val in ['100m', '400m']:
            #     self.windSpeed.setEnabled(True)
            #     if val == '400m':
            #         self.windSpeed.setEnabled(False)
            #     self.lane.setEnabled(False)
            #     self.men.setEnabled(False)
            #     self.women.setEnabled(False)
            #     self.raceName.setEnabled(True)
            #     self.year.setEnabled(True)
            # elif val == '200m':
            #     self.lane.setEnabled(True)
            #     self.men.setEnabled(True)
            #     self.women.setEnabled(True)
            #     self.raceName.setEnabled(True)
            #     self.year.setEnabled(True)
            #     self.windSpeed.setEnabled(True)
            if val == '400m':
                self.windSpeed.setEnabled(False)
            if val == '100m':
                self.windSpeed.setText(self.factorData[0])
            elif val == '200m':
                self.windSpeed.setText(self.factorData[1])
        elif self.sender() == self.resetFix:
            self.length.setCurrentIndex(2)
            self.lane.setCurrentIndex(0)
            self.oldScore.setText("")
            self.raceName.setCurrentIndex(0)
            self.year.setCurrentIndex(0)
            self.men.setChecked(True)
            self.correctedScore.setText("")
        elif self.sender() == self.raceName:
            yearData = raceData[val]
            # 阻止clear动作发出信号
            self.year.blockSignals(True)
            self.year.clear()
            self.year.blockSignals(False)
            for key, val in yearData.items():
                # clear后add使得index改变,发出信号
                self.year.addItem(key, val)
        elif self.sender() == self.year:
            raceLength = self.length.itemText(self.length.currentIndex())
            self.factorData = self.year.itemData(self.year.currentIndex())
            # 将下拉框选择的比赛和日期对应的风速海拔填入文本框
            if raceLength == '100m':
                self.windSpeed.setText(self.factorData[0])
            elif raceLength == '200m':
                self.windSpeed.setText(self.factorData[1])
            self.altitude.setText(self.factorData[2])
        elif self.sender() == self.fixScore:
            try:
                # 计算修正后的成绩
                race_length = int(self.length.itemText(self.length.currentIndex())[0:-1])
                lane_num = int(self.lane.itemText(self.lane.currentIndex()))
                sex = 'women' if self.women.isChecked() else 'men'
                old_score = float(self.oldScore.text())
                wind_speed = float(self.windSpeed.text()) if self.windSpeed.text() else 0
                altitude = float(self.altitude.text())
                # print(race_length, lane_num, sex, old_score, wind_speed, altitude)
                new_score = round(cal_score(old_score, wind_speed, altitude, race_length, lane_num, sex), 2)
                self.correctedScore.setText(str(new_score))
                # 插入到数据模型中
                newRecord = self.fixScoreModel.record()
                newRecord.setValue('race', str(race_length) + 'm')
                newRecord.setValue('altitude', altitude)
                newRecord.setValue('oldScore', old_score)
                newRecord.setValue('newScore', new_score)
                newRecord.setValue('wind', wind_speed)
                newRecord.setValue('lane', lane_num)
                newRecord.setValue('sex', '男' if sex == 'men' else '女')
                if race_length != 400:
                    newRecord.setValue('wind', wind_speed)
                self.fixScoreModel.insertRecord(0, newRecord)
                self.fixScoreModel.select()
            except Exception:
                QMessageBox.information(self, '提示', '请输入正确的数据')

    def handleFixScoreView(self):
        self.handleView(self.sender(),self.delSelected,self.clear,self.refresh,self.outputData,
                        self.fixScoreModel,self.fixScoreView)





    '''
    1.选择一个项目1,输入性别和成绩,计算出分数和对应的项目2成绩
    2.选择不同的项目输入成绩的控件会不同
    3.将计算出来的成绩保存到数据库,并显示在表格中
    4.表格可以删除选中列,清空,刷新,导出数据
    '''
    def handleCompareScore(self, val):
        # print(val)
        if self.sender() == self.event1:
            self.autoChecked(self.event1, val, self.men1, self.women1)
            # 根据选中的项目决定输入成绩的控件
            if val in range(0,7) and self.inUseScore1==self.doubleScore1:
                self.inUseScore1.hide()
                self.score1Layout.replaceWidget(self.inUseScore1, self.timeScore1)
                self.inUseScore1 = self.timeScore1
                self.timeScore1.show()
                self.scoreLabel1.setText("成绩1(min:s:ms)")
            elif val in range(7,13) and self.inUseScore1==self.timeScore1:
                self.inUseScore1.hide()
                self.score1Layout.replaceWidget(self.inUseScore1,self.doubleScore1)
                self.inUseScore1 = self.doubleScore1
                self.doubleScore1.show()
                self.scoreLabel1.setText("成绩1")
        elif self.sender() == self.event2:
            self.autoChecked(self.event2, val, self.men2, self.women2)
        elif self.sender() == self.resetCompare:
            # print("reset")
            self.event1.setCurrentIndex(0)
            self.event2.setCurrentIndex(0)
            self.timeScore1.setTime(QTime(0,0))
            self.doubleScore1.setValue(0)
            self.score2.setText("")
            self.points.setText("")
            self.men1.setChecked(True)
            self.men2.setChecked(True)
        elif self.sender()==self.compareScore:
            # 1.计算项目1的points
            points=0
            score1=0
            event1=self.event1.currentData()
            gender1='men' if self.men1.isChecked() else 'women'
            minutes1=self.timeScore1.time().minute()
            seconds1=self.timeScore1.time().second()
            mSec1=self.timeScore1.time().msec()
            seconds1=seconds1+mSec1/1000
            meters1=self.doubleScore1.value()
            if self.event1.currentIndex() in range(0, 7):
                points=cal_points(event1,gender1,seconds1,minutes1)
                score1=minutes1*60+seconds1
                score1=self.timeScore2Str(score1)
            if self.event1.currentIndex() in range(7, 13):
                points = cal_points(event1, gender1, meters1)
                score1=self.doubleScore1.text()+"米"
            points_str=str(round(points,2))
            self.points.setText(points_str)
            # 2.根据项目1的points计算项目2的成绩
            gender2 = 'men' if self.men2.isChecked() else 'women'
            event2 = self.event2.currentData()
            score2=cal_points2score(event2,gender2,points)
            if self.event2.currentIndex() in range(0, 7):
                score2=self.timeScore2Str(score2)
                self.score2.setText(score2)
            else:
                score2 = str(round(score2,2))+'米'
                self.score2.setText(score2)
            # 3.输出到数据模型,也即数据库
            newRecord=self.compareScoreModel.record()
            newRecord.setValue('event1',self.event1.currentText())
            newRecord.setValue('gender1','男' if gender1 == 'men' else '女')
            newRecord.setValue('score1',score1)
            newRecord.setValue('event2',self.event2.currentText())
            newRecord.setValue('gender2','男' if gender2 == 'men' else '女')
            newRecord.setValue('score2',score2)
            newRecord.setValue('points',round(points,2))
            self.compareScoreModel.insertRecord(0,newRecord)
            self.compareScoreModel.select()

    # 将秒转换为字符串
    def timeScore2Str(self,score):
        score = round(score, 2)
        if score > 60:
            score = str(datetime.timedelta(seconds=score))[2:10]
            score = score[0:2] + "分" + score[3:8] + "秒"
            if score[0]=='0':
                score=score[1:]
        else:
            score = str(score) + "秒"
        return score

    # 根据赛事自动选择性别
    def autoChecked(self, evt, val, rb1, rb2):
        eventChosen = evt.itemData(val)
        if eventChosen in ['100mH', '110mH']:
            rb1.setEnabled(False)
            rb2.setEnabled(False)
            if eventChosen == '100mH':
                rb2.setChecked(True)
            else:
                rb1.setChecked(True)
        else:
            rb1.setEnabled(True)
            rb2.setEnabled(True)

    def handleCompareScoreView(self):
        self.handleView(self.sender(),self.delSelected2,self.clear2,self.refresh2,self.outputData2,
                        self.compareScoreModel,self.compareScoreView)


