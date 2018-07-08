# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xuesheng.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QFileDialog,QMessageBox

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(563, 407)
        Form.setMinimumSize(QtCore.QSize(563, 407))
        Form.setMaximumSize(QtCore.QSize(563, 407))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 16, 141, 21))
        self.label.setStyleSheet("font: italic 16pt \"Ubuntu\";")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 261, 331))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 16, 191, 21))
        self.label_2.setStyleSheet("font: italic 16pt \"Ubuntu\";")
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(300, 50, 241, 261))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(370, 340, 101, 27))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 561, 411))
        self.label_3.setMinimumSize(QtCore.QSize(561, 411))
        self.label_3.setMaximumSize(QtCore.QSize(561, 411))
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.textEdit.raise_()
        self.pushButton.raise_()
        self.textEdit_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        # self.label_3.setPixmap(QtGui.QPixmap("/home/yck/faceIDbiyesheji/image/qiandao.jpg").scaled(self.label_3.width(),self.label_3.height()) )  
        self.pushButton.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "学生界面"))
        self.label.setText(_translate("Form", "历史签到记录："))
        self.label_2.setText(_translate("Form", "我不服，我要上诉："))
        self.pushButton.setText(_translate("Form", "确定"))
        # self.label_3.setText(_translate("Form", "TextLabel"))





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())