# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eval.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 30, 256, 491))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, " ")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(290, 90, 471, 431))
        self.tableView.setObjectName("tableView")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(290, 30, 131, 31))
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox.addItems(['2016', '2017','2018'])
        self.comboBox.activated[str].connect(self.select_value)
        self.comboBox.currentIndexChanged[str].connect(self.chg_value)

        sw=pd.read_excel('sw.xlsx')
        ind=sw.iloc[:,0].value_counts()
        indname=list(ind.index)
        root = QTreeWidgetItem(self.treeWidget)
        root.setText(0, '申银万国行业分类')
        root.setText(1, '0')
        for i in range(len(indname)):
           child = QTreeWidgetItem(root)
           child.setText(0, indname[i])
           child.setText(1, str(i))

        self.treeWidget.clicked.connect(self.selectname)
        self.chg_i='2016'
        self.select=0

    def selectname(self):
        self.select=1
        self.eval_fun('2016')
        if self.chg_i!='2016':
            self.eval_fun(self.chg_i)

    def select_value(self,i):
        if self.select!=0:
           self.eval_fun(i)

    def chg_value(self,i):
        self.chg_i=i

    def eval_fun(self,year):
        import fun
        item = self.treeWidget.currentItem()
        data = pd.read_excel('Data'+year+'.xlsx')
        code = []
        for i in range(len(data)):
            code.append(data.iloc[i, 0][:6])
        sw = pd.read_excel('sw.xlsx', dtype=str)
        code1 = list(sw.iloc[sw['行业名称'].values == item.text(0), 1].values)
        index = []
        for c in code1:
            a = c in code
            if a == True:
                index.append(code.index(c))

        dt = data.iloc[index, :]
        r = fun.Fr(dt)
        s1 = r[1]
        if len(s1) > 0:
            self.model = QStandardItemModel(len(s1), 2)
            self.model.setHorizontalHeaderLabels(['公司简称', '综合得分排名'])
            for row in range(len(s1)):
                for column in range(2):
                    if column == 0:
                        a = QStandardItem(s1.index[row])
                    else:
                        a = QStandardItem(str(s1[row]))
                    self.model.setItem(row, column, a)

            self.tableView.setModel(self.model)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "上市公司综合评价"))

if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui_test=Ui_MainWindow()
    ui_test.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())