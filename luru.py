# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'luru.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui
import cv2
import os
import requests
from json import JSONDecoder
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QFileDialog,QMessageBox

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 30, 101, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 250, 101, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 260, 51, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 260, 51, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 261, 301))
        self.label.setMinimumSize(QtCore.QSize(261, 301))
        self.label.setMaximumSize(QtCore.QSize(261, 301))
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 160, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(260, 210, 41, 17))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(300, 150, 91, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 200, 91, 27))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 60, 101, 27))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(270, 100, 121, 21))
        self.label_4.setMinimumSize(QtCore.QSize(121, 21))
        self.label_4.setMaximumSize(QtCore.QSize(121, 21))
        self.label_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.pushButton_5.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_3.raise_()

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(Form.close)
        self.pushButton.clicked.connect(self.openimage)
        self.pushButton_2.clicked.connect(self.opensxt)
        self.pushButton_4.clicked.connect(self.rllr)
        self.pushButton_5.clicked.connect(self.savephoto)
        
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "信息录入"))
        self.pushButton.setText(_translate("Form", "上传照片"))
        self.pushButton_2.setText(_translate("Form", "打开摄像头"))
        self.pushButton_3.setText(_translate("Form", "退出"))
        self.pushButton_4.setText(_translate("Form", "录入"))
        self.label_2.setText(_translate("Form", "姓名"))
        self.label_3.setText(_translate("Form", "   ID"))
        self.pushButton_5.setText(_translate("Form", "拍照"))


    def openimage(self):
        print(111)
        # 打开文件路径
         #设置文件扩展名过滤,注意用双分号间隔
        global imgName
        imgName,imgType= QFileDialog.getOpenFileName(None,
                                    "打开图片",
                                    "",
                                    "Image Files(*.jpg *.png *.jpeg)")

        print(imgName)
        crop_imgimg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(crop_imgimg)
        #利用qlabel显示图片
        # png = QtGui.QPixmap(imgName).scaled(self.label_3.width(), self.label_3.height())
        # self.label_3.setPixmap(png)吴亦凡

    def opensxt(self):
        print(222)
        QMessageBox.about(self,"Tip","facetoken 加入失败！！")


    def rllr(self):
        print(444)
    def savephoto(self):
        print(555)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())