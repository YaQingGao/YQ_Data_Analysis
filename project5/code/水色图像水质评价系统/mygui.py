# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mygui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
import sys
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 417)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 571, 201))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 20, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(240, 20, 104, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 20, 71, 31))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.pushButton.clicked.connect(self.openimage)
        self.pushButton_2.clicked.connect(self.svmtest)
        self.path=''

    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(None, "导入图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
        self.path=imgName
        self.textEdit.setText('')

    def svmtest(self):
        from PIL import Image
        import numpy as np
        path=self.path
        img = Image.open(path)  # 读取图像
        im = img.split()  # 分离RGB颜色通道
        R = np.array(im[0]) / 255 * 40  # R通道
        row_1 = int(R.shape[0] / 2) - 50
        row_2 = int(R.shape[0] / 2) + 50
        con_1 = int(R.shape[1] / 2) - 50
        con_2 = int(R.shape[1] / 2) + 50
        R = R[row_1:row_2, con_1:con_2]
        G = np.array(im[1]) / 255 * 40  # G通道
        G = G[row_1:row_2, con_1:con_2]
        B = np.array(im[2]) / 255 * 40  # B通道
        B = B[row_1:row_2, con_1:con_2]
        # R,G,B一阶颜色矩
        r1 = np.mean(R)
        g1 = np.mean(G)
        b1 = np.mean(B)
        # R,G,B二阶颜色矩
        r2 = np.std(R)
        g2 = np.std(G)
        b2 = np.std(B)
        a = np.mean(abs(R - R.mean()) ** 3)
        b = np.mean(abs(G - G.mean()) ** 3)
        c = np.mean(abs(B - B.mean()) ** 3)
        # R,G,B三阶颜色矩
        r3 = a ** (1. / 3)
        g3 = b ** (1. / 3)
        b3 = c ** (1. / 3)
        x1=np.array([r1,g1,b1,r2,g2,b2,r3,g3,b3])
        from sklearn.svm import SVC
        X=np.load('X.npy')
        Y = np.load('Y.npy')
        clf = SVC(class_weight='balanced')  # 类标签平衡策略
        clf.fit(X, Y)
        y=clf.predict(x1.reshape(1,len(x1)))
        self.textEdit.setText(str(y[0]))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "水色图像水质评价系统"))
        self.pushButton.setText(_translate("MainWindow", "导入图片"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "水色识别"))
        self.label_2.setText(_translate("MainWindow", "类别"))

if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui_test=Ui_MainWindow()
    ui_test.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
