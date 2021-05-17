# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from SED import Ui_Dialog_SED
from SS import Ui_Dialog_SS	

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 582)
        MainWindow.setMaximumSize(QtCore.QSize(167772, 16777215))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 230, 541, 191))
        self.label.setStyleSheet("image: url(:/tupian/yanjiuluxian.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 60, 548, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.biaoti = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.biaoti.setFont(font)
        self.biaoti.setObjectName("biaoti")
        self.verticalLayout.addWidget(self.biaoti)
        self.renyuanjieshao = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.renyuanjieshao.setObjectName("renyuanjieshao")
        self.verticalLayout.addWidget(self.renyuanjieshao)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(150, 430, 160, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(390, 430, 206, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.setStyleSheet('''QWidget{background-color:rgb(245, 245, 245);}''')

        self.retranslateUi(MainWindow)
        #self.pushButton.clicked.connect(MainWindow.close)
        #self.pushButton_2.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.popWindow_SS)#打开声音分离窗口
        self.pushButton_2.clicked.connect(self.popWindow_SED)#打开声音事件检测窗口

    def popWindow_SED(self):
        self.form2 = QtWidgets.QWidget() 
        self.ui2 = Ui_Dialog_SED()
        self.ui2.setupUi(self.form2)
        self.form2.show()

    def popWindow_SS(self):
        self.form3 = QtWidgets.QWidget() 
        self.ui3 = Ui_Dialog_SS()
        self.ui3.setupUi(self.form3)
        self.form3.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.biaoti.setText(_translate("MainWindow", "融合声音分离的声音事件检测"))

        self.renyuanjieshao.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'隶书\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">答辩人:吉林大学 郭智方</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">指导老师:吉林大学 许芳</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">         中国科学院计算技术研究所 王向东</span></p></body></html>"))

        '''self.renyuanjieshao.setHtml(_translate("MainWindow",
"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'隶书\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">中国科学院 </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">计算技术研究所</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">泛在计算系统研究中心</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">人机交互组</span></p></body></html>"))'''

        self.label_3.setText(_translate("MainWindow", "声音分离"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.label_4.setText(_translate("MainWindow", "声音事件检测"))
        self.pushButton_2.setText(_translate("MainWindow", "确定"))
import picture_rc


import sys
class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())
