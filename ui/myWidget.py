import typing

from PyQt5 import QtCore
from PyQt5.Qt import *


class EqualBtn(QPushButton):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)

    def keyPressEvent(self, evt):
        if evt.key() == Qt.Key_Enter or evt.key()==Qt.Key_Return:
            self.click()

class MyModel(QSqlTableModel):
    def data(self, idx: QtCore.QModelIndex, role: int = ...) -> typing.Any:
        value = super().data(idx, role)
        # 对齐方式
        if Qt.TextAlignmentRole == role:
            return Qt.AlignCenter | Qt.AlignHCenter
        # # 前景色(字体颜色)
        # if Qt.ForegroundRole == role:
        #     if 3 == idx.column():
        #         return QColor(255, 144, 144)
        # # 字体
        # if Qt.FontRole == role:
        #     return QFont('微软雅黑',pointSize=10,weight=500,italic=True)
        return value