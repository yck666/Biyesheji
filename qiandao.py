# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qiandao.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
import time
import requests
from json import JSONDecoder
from PyQt5.QtWidgets import QFileDialog,QMessageBox
import pymysql.cursors
import datetime
from time import strftime,gmtime
# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='311', db='facedata', 
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)



key = "XTq8uoG-Un_Nd0dAtnqOaEahqGOLjf6v" 
secret = "V0sVg5JBZi_nZt093W4bNshnr4-W8tH5"

outer_id = '18026284836'
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 238)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 50, 101, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 140, 101, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(170, 30, 311, 161))
        self.textEdit.setMinimumSize(QtCore.QSize(311, 161))
        self.textEdit.setMaximumSize(QtCore.QSize(311, 161))
        self.textEdit.setAcceptDrops(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 521, 241))
        self.label.setMinimumSize(QtCore.QSize(521, 241))
        self.label.setMaximumSize(QtCore.QSize(521, 241))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.textEdit.raise_()
        self.label.setPixmap(QtGui.QPixmap("/home/yck/faceIDbiyesheji/image/qiandao.jpg").scaled(self.label.width(),self.label.height()) )  


        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "签到界面"))
        self.pushButton.setText(_translate("Form", "开始签到"))
        self.pushButton_2.setText(_translate("Form", "退出"))

    def start(self):
        ttt=0
        aaa=0
        bbb=50
        cap = cv2.VideoCapture(0)#打开摄像头
        cascade = cv2.CascadeClassifier('/home/yck/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml')#这里是是自己的人脸识别xml路径
        while True:
            ret, frame = cap.read()#捕获图片
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#转为灰度图
            rect = cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5),flags=cv2.CASCADE_SCALE_IMAGE)  # 使用模板匹配图形
            for x, y, z, w in rect:
                cv2.rectangle(frame, (x, y), (x + z, y + w), (0, 0, 255), 2)# 函数的参数分别为：图像，左上角坐标，右下角坐标，颜色，宽度
            cv2.imshow("capture", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):#按下q拍照
                break
            lenrect=len(rect)
            aaa = lenrect+aaa
            if aaa >= bbb:
                path1="qiandao"+str(ttt)+".jpg"
                cv2.imwrite(path1,frame)
                ttt = int(ttt)+1
                bbb+=50

                http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
                data = {"api_key": key, "api_secret": secret, "return_landmark": "2"}
                files = {"image_file": open(path1, "rb")}
                response = requests.post(http_url, data=data, files=files)
                req_con = response.content.decode('utf-8')
                req_dict = JSONDecoder().decode(req_con)
                faces = req_dict["faces"]
                face_token = faces[0]['face_token']
                print(face_token)


                http_url = "https://api-cn.faceplusplus.com/facepp/v3/search"
                data = {"api_key": key, "api_secret": secret,"face_token":face_token,"outer_id": outer_id}
                response = requests.post(http_url, data=data)
                req_con = response.content.decode('utf-8')
                req_dict = JSONDecoder().decode(req_con)
                print(req_dict)
                if req_dict["results"][0]["confidence"]>=req_dict["thresholds"]["1e-5"]:
                    tmpp = []
                    tmpp.append(req_dict["results"][0]["face_token"])
                    
                    print(tmpp)
                    cursor = connection.cursor() 
                    sql = "SELECT * FROM facemessage WHERE facetoken=%s"
                    cursor.execute(sql,tmpp)

                    #查询数据库单条数据
                    result = cursor.fetchone()
                    nid = result["id"]
                    nname = result["name"]
                    # print(result)
                    # cursor.close()
                    ttime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    cursor = connection.cursor() 
                    sql = "INSERT INTO qiandao (id, name,qiandao_time) VALUES (%s,%s,%s)"
                    cursor.execute(sql,(nid,nname,ttime))
                    connection.commit()
                    cursor.close()



                    word = nname + "    "+ttime+"\n"
                    print(word)

                    # pyqt5 de textedit实时显示
                    cursor = self.textEdit.textCursor()  
                    cursor.movePosition(QtGui.QTextCursor.End)  
                    cursor.insertText(word)  
                    self.textEdit.setTextCursor(cursor)  
                    self.textEdit.ensureCursorVisible()  
                    
                else:
                    abc="没有此人信息!!!"
                    print("没有此人信息!!!")


         

                
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())