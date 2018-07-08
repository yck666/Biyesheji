# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui
import sys
import cv2
import os
import time
import numpy as np
import requests
from json import JSONDecoder
from laoshijiemian import Ui_Form3
from xuesheng import Ui_Form2
from denglu import Ui_Form   # 导入生成first.py里生成的类
from PyQt5.QtWidgets import QFileDialog,QMessageBox
import pymysql.cursors
from PyQt5.QtCore import pyqtSignal
# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='311', db='facedata', 
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)



key = "XTq8uoG-Un_Nd0dAtnqOaEahqGOLjf6v" 
secret = "V0sVg5JBZi_nZt093W4bNshnr4-W8tH5"

outer_id = '18026284836'

class mywindow(QtWidgets.QWidget,Ui_Form):
    close_signal = pyqtSignal()
    close_signal2 = pyqtSignal()

    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        
        

    def zhuce(self):
        


        tmp=[]
        name  = self.lineEdit.text()
        number  = self.lineEdit_2.text()
        if self.radioButton.isChecked():
            shenfen = "student"
        else:
            shenfen = "teacher"
        print(shenfen)

        if (name == "") or (number == ""):
            QMessageBox.warning(self,"Tip","你有信息未填写！！！")
            print(name)
            print(number)

        else:
            print(222)
            http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"

            data = {"api_key": key, "api_secret": secret, "return_landmark": "2"}
            files = {"image_file": open("tmpe.jpg", "rb")}
            response = requests.post(http_url, data=data, files=files)
            req_con = response.content.decode('utf-8')
            req_dict = JSONDecoder().decode(req_con)
            if 'error_message' in req_dict:
                QMessageBox.warning(self,"Tip","人脸识别返回错误！！")
            else:
                faces = req_dict["faces"]
                img = cv2.imread("tmpe.jpg")
               

                face_token = faces[0]['face_token']
                print(face_token)
                face_rectangle = faces[0]['face_rectangle']
                print(face_rectangle)

                width =  face_rectangle['width']
                top =  face_rectangle['top']
                left =  face_rectangle['left']
                height =  face_rectangle['height']
                # crop_img = img[left:left+width,top:top+height]
                # cv2.imwrite("image/abc.jpg",crop_img)
                start = (left, top)
                end = (left+width, top+height)
                
                
                cv2.rectangle(img,start,end,(255,0,0),2)
                
                # photopath = "image/"+number+".jpg"
                
                # cv2.imwrite(photopath,crop_img)
                crop_img = img[top:top+height,left:left+width]
                # cv2.imshow("imad",crop_img)
                # cv2.waitKey(0)
                photopath = "faceimg/"+number+".jpg"
                # print(photopath)
                cv2.imwrite(photopath,crop_img)
                # print("ok")
                tmp.append(number)
                tmp.append(name)
                tmp.append(face_token)
                tmp.append(photopath)
                tmp.append(shenfen)

                http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/addface"
                data = {"api_key": key, "api_secret": secret, "outer_id": outer_id,"face_tokens":face_token}
                response = requests.post(http_url, data=data)
                req_con = response.content.decode('utf-8')
                req_dict = JSONDecoder().decode(req_con)
                if 'error_message' in req_dict:
                    QMessageBox.warning(self,"Tip","facetoken 加入失败！！")
                    print("facetoken 加入失败！！！")
                else:
                    QMessageBox.about(self,"Tip","注册成功！！！")

                    print("添加成功！！！")
                # self.close()

                print(tmp)
                # 通过cursor创建游标
                cursor = connection.cursor() 
                sql = "INSERT INTO facemessage (id, name,facetoken,facepath,shenfen) VALUES (%s,%s, %s,%s,%s)"
                cursor.execute(sql,tmp)

                # 提交SQL
                connection.commit()

                cursor.close()



    def opensxt(self):

        print(222)

        # face_cascade = cv2.CascadeClassifier('/home/yck/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        while True:
            ret,img = cap.read()
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            # for (x,y,w,h) in faces:
            #     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imshow('img',img)       
            if cv2.waitKey(1) &0xFF == ord('q'):
                
                cv2.imwrite("tmpe.jpg",img)
                self.label.setPixmap(QtGui.QPixmap("tmpe.jpg").scaled(self.label.width(),self.label.height()) )  

                break
        cap.release()
        cv2.destroyAllWindows()
			



    def denglu(self):
        print(333)
        aaa=0
        cap = cv2.VideoCapture(0)
        cascade = cv2.CascadeClassifier('/home/yck/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml')
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            rect = cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5),flags=cv2.CASCADE_SCALE_IMAGE)
            for x, y, z, w in rect:
                cv2.rectangle(frame, (x, y), (x + z, y + w), (0, 0, 255), 2)
            cv2.imshow("capture", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            lenrect=len(rect)
            aaa = lenrect+aaa
            if aaa >= 50:
                cv2.imwrite("text.jpg",frame) 
                break
        cap.release()
        cv2.destroyAllWindows()


        http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
        data = {"api_key": key, "api_secret": secret, "return_landmark": "2"}
        files = {"image_file": open("text.jpg", "rb")}
        response = requests.post(http_url, data=data, files=files)
        req_con = response.content.decode('utf-8')
        req_dict = JSONDecoder().decode(req_con)
        print(req_dict)
        faces = req_dict["faces"]
        print(faces)
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
            print(result["name"])
            # print(result)
            # cursor.close()
            global resultname
            resultid = result["id"]
            resultname=result["name"]
            if result["shenfen"] == 'student':
                message  = resultname + "  " +"欢迎来到学生界面！ "
                QMessageBox.about(self,"Tip",message)
                # self.close_signal.emit()
                self.close()
                self.newwin = xueshengwin()
                self.newwin.show()
                self.newwin.setWindowTitle(resultname)  #设置窗口标题  

                cursor = connection.cursor() 

                sql = "SELECT * FROM qiandao WHERE id=%s"
                cursor.execute(sql,resultid)

                # 提交SQL
                reaaa = cursor.fetchall()
                print(len(reaaa))
                cursor.close()
                for i in range(len(reaaa)):
                    word = reaaa[i]["qiandao_time"] + "\n"
                # for i in reaaa[i]["qiandao_time"]:
                #     # # # pyqt5 de textedit实时显示
                    cursor = self.newwin.textEdit.textCursor()  
                    cursor.movePosition(QtGui.QTextCursor.End)  
                    cursor.insertText(word)  
                    self.newwin.textEdit.setTextCursor(cursor)  
                    self.newwin.textEdit.ensureCursorVisible()  




            else:
                message  = resultname + "  " +"欢迎来到老师界面！ "
                QMessageBox.about(self,"Tip",message)
                # self.close_signal2.emit()
                self.close()
                self.newwin = laoshiwin()
                self.newwin.show()
                self.newwin.setWindowTitle(resultname) 
                # self.newwin.pushButton_2.clicked.connect(self.kaoqin)
                # self.newwin.pushButton_3.clicked.connect(self.daochu)
                # self.newwin.pushButton_4.clicked.connect(self.tupian)

                
                
                        



                # def kaoqin(self):
                #     pass
                # def daochu(self):
                #     pass

                # def tupian(self):
                #     pass
                            
                        

        else:
            abc="没有此人信息!!!"
            print("没有此人信息!!!")
            QMessageBox.about(self,"Tip","登录失败！！！！！")

        



class xueshengwin(QtWidgets.QWidget,Ui_Form2):
    def __init__(self):
        super(xueshengwin,self).__init__()
        self.setupUi(self)
    

class laoshiwin(QtWidgets.QWidget,Ui_Form3):
    def __init__(self):
        super(laoshiwin,self).__init__()
        self.setupUi(self)
#     def show_w1(self):
#         self.show()







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()


    # w1=xueshengwin()

    # w2=laoshiwin()
    ui.show()
    # ui.close_signal.connect(w1.show_w1)

    # ui.close_signal2.connect(w2.show_w1)

    sys.exit(app.exec_())