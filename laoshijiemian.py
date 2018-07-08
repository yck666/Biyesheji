# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laoshijiemian.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QFileDialog,QMessageBox
import pymysql.cursors
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
from PyQt5.QtWidgets import QFileDialog  
import xlwt
import datetime 
from time import strftime,gmtime
import requests
import cv2
import numpy as np
from json import JSONDecoder

key = "XTq8uoG-Un_Nd0dAtnqOaEahqGOLjf6v" 
secret = "V0sVg5JBZi_nZt093W4bNshnr4-W8tH5"

outer_id = '18026284836'
class Ui_Form3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(280, 283)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(52, 40, 101, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 90, 101, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 140, 101, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 190, 101, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 230, 31, 31))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 230, 171, 31))
        self.label.setObjectName("label")
        self.pushButton.clicked.connect(self.jianbiao)
        self.pushButton_2.clicked.connect(self.kaoqin)
        self.pushButton_3.clicked.connect(self.daochu)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "创建班级表"))
        self.pushButton_2.setText(_translate("Form", "开始考勤"))
        self.pushButton_3.setText(_translate("Form", "导出Excel"))
        self.label.setText(_translate("Form", "宏观了解学校学习氛围图："))

    def jianbiao(self):
        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='311', db='facedata', 
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

        texttext=self.lineEdit.text()

        if texttext == "":
            QMessageBox.about(self,"Tip","请先输入要建的班级名字格式为：dx141")
        else:
            wintitle = self.windowTitle()
            biaoname = wintitle + "_" + texttext
            print(biaoname)
            cursor = connection.cursor() 
            sql = "create table if not exists "+biaoname+" select * from "+texttext+";"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            print("建表成功")

            # print(sql)


    def kaoqin(self):
        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='311', db='facedata', 
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

        ttime=datetime.datetime.now().strftime('%Y年%m月%d日%H时%M分%S秒')        # ttimes = "KQ"+ttime
        print(ttime)
        texttext=self.lineEdit.text()
        if texttext == "":
            QMessageBox.about(self,"Tip","请先输入要考勤的班级名字格式为：dx141")
        else:
            wintitle = self.windowTitle()
            biaoname = wintitle + "_" + texttext
            fieldtype = "VARCHAR(5)"
            # print(biaoname)
            cursor = connection.cursor() 
            sql = "alter table "+biaoname+" add "+ttime+" "+fieldtype+";"
            print(sql)
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            # print(sql)
            # print(sql)


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
                        dao = '"Y"'
                        cursor = connection.cursor() 
                        sql = "update "+biaoname+" set "+ttime+"="+dao+" where id="+nid+";"
                        print("qiandao de sql\n"+sql)
                        cursor.execute(sql)
                        connection.commit()
                        cursor.close()


  
                        
                    else:
                        abc="没有此人信息!!!"
                        print("没有此人信息!!!")


             

                    
            cap.release()
            cv2.destroyAllWindows()


    def daochu(self):
        texttext=self.lineEdit.text()
        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='311', db='facedata', 
                             charset='utf8mb4')

        if texttext == "":
            QMessageBox.about(self,"Tip","请先输入要导出的班级名字格式为：dx141")
        else:
            # texttext=self.lineEdit.text()
            wintitle = self.windowTitle()
            biaoname = wintitle + "_" + texttext
            directory1 = QFileDialog.getExistingDirectory(self,  
                                        "选取文件夹",  
                                        "") 
            print(directory1)
            path = directory1+ "/"+biaoname+".xls"
            sql = "select * from "+biaoname+";"
            cursor = connection.cursor() 
            count=cursor.execute(sql)

            cursor.scroll(0,mode='absolute')
            results=cursor.fetchall()
            # print(re/sult)
            fields = cursor.description
            workbook= xlwt.Workbook()
            sheet = workbook.add_sheet('table_'+biaoname,cell_overwrite_ok=True)
            for field in range(0,len(fields)):
                sheet.write(0,field,fields[field][0])

            row = 1
            col=0
            for row in range(1,len(results)+1):
                for col in range(0,len(fields)):
                    sheet.write(row, col, u'%s' % results[row-1][col])

            workbook.save(path)
            QMessageBox.about(self,"Tip","success!")





