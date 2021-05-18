# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SS.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pyqtgraph as pg
import numpy as np
#from try_show import win
import os
import soundfile as sf
from playsound import playsound



'''# 3) Plot in chunks, adding one new plot curve for every 100 samples
chunkSize = 100
# Remove chunks after we have 10
maxChunks = 10
startTime = pg.ptime.time()

curves = []
data5 = np.empty((chunkSize + 1, 2))
ptr5 = 0'''
mode = 0

class Ui_Dialog_SS(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(562, 446)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(100, 60, 347, 90))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.biaoti = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.biaoti.setFont(font)
        self.biaoti.setAlignment(QtCore.Qt.AlignCenter)
        self.biaoti.setObjectName("biaoti")
        self.verticalLayout_2.addWidget(self.biaoti)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.xuhao = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.xuhao.setObjectName("xuhao")
        self.horizontalLayout.addWidget(self.xuhao)
        self.bofang = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.bofang.setObjectName("bofang")
        self.horizontalLayout.addWidget(self.bofang)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.fanhui = QtWidgets.QPushButton(Dialog)
        self.fanhui.setGeometry(QtCore.QRect(230, 350, 93, 28))
        font = QtGui.QFont()
        font.setFamily("隶书")
        self.fanhui.setFont(font)
        self.fanhui.setObjectName("fanhui")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(200, 190, 160, 100))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.qianjing = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.qianjing.setObjectName("qianjing")
        self.verticalLayout_4.addWidget(self.qianjing)
        self.beijing = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.beijing.setObjectName("beijing")
        self.verticalLayout_4.addWidget(self.beijing)
        self.hunhe = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.hunhe.setObjectName("hunhe")
        self.verticalLayout_4.addWidget(self.hunhe)

        #self.setStyleSheet('''QWidget{background-color:rgb(245, 245, 245);}''')

        self.retranslateUi(Dialog)
        self.fanhui.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.qianjing.clicked.connect(self.popWindow_try1)
        self.beijing.clicked.connect(self.popWindow_try2)
        self.hunhe.clicked.connect(self.popWindow_try3)
        self.bofang.clicked.connect(self.popWindow_try4)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.biaoti.setText(_translate("Dialog", "声音分离"))
        self.label.setText(_translate("Dialog", "测试音频序号"))
        self.bofang.setText(_translate("Dialog", "播放"))
        self.fanhui.setText(_translate("Dialog", "返回"))
        self.qianjing.setText(_translate("Dialog", "DESED混合前景声源"))
        self.beijing.setText(_translate("Dialog", "DESED背景声源"))
        self.hunhe.setText(_translate("Dialog", "FUSS混合声源"))

    def popWindow_try1(self):
        #os.remove("stereo_file.wav")
        mode = 1
        num=self.xuhao.value()
        #input = np.load("source.npy")
        #input = input[num*3+mode-1]
        #samplerate = 16000
        #sf.write('stereo_file.wav', input, samplerate, subtype='PCM_24')
        #playsound("stereo_file.wav",False)#在playsound的43行增加winCommand(‘close’, alias)
        os.system(r"python -m try %d %d" % (mode,num))
        #playsound("stereo_file.wav", False)

    def popWindow_try2(self):
        mode = 2
        num = self.xuhao.value()
        os.system(r"python -m try %d %d" % (mode, num))


    def popWindow_try3(self):
        mode = 3
        num = self.xuhao.value()
        os.system(r"python -m try %d %d" % (mode, num))

    def popWindow_try4(self):
        os.remove("stereo_file.wav")
        input = np.load("mix.npy")
        num = self.xuhao.value()
        input = input[num]
        samplerate = 16000
        sf.write('stereo_file.wav', input, samplerate, subtype='PCM_24')
        playsound("stereo_file.wav")
        os.remove("stereo_file.wav")

    '''def update3(self):
        global p5, data5, ptr5, curves
        now = pg.ptime.time()
        for c in curves:
            c.setPos(-(now - startTime), 0)

        i = ptr5 % chunkSize
        if i == 0:
            curve = p5.plot()
            curves.append(curve)
            last = data5[-1]
            data5 = np.empty((chunkSize + 1, 2))
            data5[0] = last
            while len(curves) > maxChunks:
                c = curves.pop(0)
                p5.removeItem(c)
        else:
            curve = curves[-1]
        data5[i + 1, 0] = now - startTime
        data5[i + 1, 1] = np.random.normal()
        curve.setData(x=data5[:i + 2, 0], y=data5[:i + 2, 1])
        ptr5 += 1'''

    #def popWindow_try(self):
    ''''win = pg.GraphicsLayoutWidget(show=True)
        win.setWindowTitle('pyqtgraph example: Scrolling Plots')
        win.nextRow()
        p5 = win.addPlot(colspan=2)
        p5.setLabel('bottom', 'Time', 's')
        p5.setXRange(-10, 0)
        def update():
            self.update3()
        timer = pg.QtCore.QTimer()
        timer.timeout.connect(update)
        timer.start(50)
        pg.mkQApp().exec_()'''
        #self.form2 = QtWidgets.QWidget()
        #self.ui2 = win()
        #self.ui2.setupUi(self.form2)
        #self.form2.show()
        #x = np.random.rand(10000)
        #os.system(r"python -m try %d" % mode)
        #os.system('import pyqtgraph')

        #self.app = QtWidgets.QApplication(sys.argv)
        #self.mywindow = win()
        #self.mywindow.show()
        #self.sys.exit(app.exec_())


import sys
class MyWindow(QtWidgets.QMainWindow, Ui_Dialog_SS):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())
