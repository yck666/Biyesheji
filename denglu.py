# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'denglu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(445, 449)
        Form.setMinimumSize(QtCore.QSize(445, 449))
        Form.setMaximumSize(QtCore.QSize(445, 449))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 445, 331))
        self.label.setMinimumSize(QtCore.QSize(381, 331))
        self.label.setMaximumSize(QtCore.QSize(445, 331))
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 360, 31, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 400, 21, 17))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(60, 350, 113, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 390, 113, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 350, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 390, 101, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 300, 101, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(60, 420, 119, 22))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.label.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.radioButton.raise_()
        self.pushButton_3.raise_()
        self.label.setPixmap(QtGui.QPixmap("/home/yck/faceIDbiyesheji/image/jiemian.jpg").scaled(self.label.width(),self.label.height()) )  

        self.pushButton.clicked.connect(self.zhuce)
        self.pushButton_2.clicked.connect(self.denglu)
        self.pushButton_3.clicked.connect(self.opensxt)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "人脸识别界面"))
        self.label_2.setText(_translate("Form", "姓名"))
        self.label_3.setText(_translate("Form", "ID"))
        self.pushButton.setText(_translate("Form", "注册"))
        self.pushButton_2.setText(_translate("Form", "登录"))
        self.pushButton_3.setText(_translate("Form", "打开摄像头"))
        self.radioButton.setText(_translate("Form", "student"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())