import cv2
import numpy as np
import time
# cap = cv2.VideoCapture(0)
# while(1):
#             # get a frame
#     ret, frame = cap.read()
#         # show a frame
#     cv2.imshow("capture", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows() 


#从摄像头读取图片并保存

# cap = cv2.VideoCapture(0)#打开摄像头
# cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")#这里是是自己的人脸识别xml路径
# while True:
#     # get a frame
#     ret, frame = cap.read()#捕获图片
#     # show a frame
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#转为灰度图
#     rect = cascade.detectMultiScale(gray,  1.2, 2, cv2.CASCADE_SCALE_IMAGE, (20, 20))  # 使用模板匹配图形
#     for x, y, z, w in rect:
#         cv2.rectangle(frame, (x, y), (x + z, y + w), (0, 0, 255), 2)# 函数的参数分别为：图像，左上角坐标，右下角坐标，颜色，宽度
#     cv2.imshow("capture", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):#按下q拍照
#         cv2.imwrite("images\client.jpg", frame)#相对路径，储存图片
#         break
# cap.release()
# cv2.destroyAllWindows()

# aaa=0
# cap = cv2.VideoCapture(0)#打开摄像头
# cascade = cv2.CascadeClassifier('/home/yck/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml')#这里是是自己的人脸识别xml路径
# while True:
#     # get a frame
#     ret, frame = cap.read()#捕获图片
#     # show a frame
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#转为灰度图
#     rect = cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5),flags=cv2.CASCADE_SCALE_IMAGE)  # 使用模板匹配图形
#     # print(max(rect))
#     for x, y, z, w in rect:
#         cv2.rectangle(frame, (x, y), (x + z, y + w), (0, 0, 255), 2)# 函数的参数分别为：图像，左上角坐标，右下角坐标，颜色，宽度
#     cv2.imshow("capture", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):#按下q拍照
#         # cv2.imwrite("images/client.jpg", frame)#相对路径，储存图片
#         break
     
#     # while rect>=[[1000 1000 1000 1000]]:
#     #     cv2.imwrite("text.jpg",frame)
    
#     lenrect=len(rect)
#     aaa = lenrect+aaa

#     if aaa >= 100:
#         cv2.imwrite("text.jpg",frame) 
#         break
    
    
    
#         # cv2.imwrite("text.jpg",frame)
#         # time.sleep(3)
#         # break

# cap.release()
# cv2.destroyAllWindows()


# import numpy as np
# import cv2

# face_cascade = cv2.CascadeClassifier('/home/yck/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml')
# cap = cv2.VideoCapture(0)
# while True:
#     ret,img = cap.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#     cv2.imshow('img',img)       
#     if cv2.waitKey(1) &0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
# img = cv2.imread("/home/yck/faceIDbiyesheji/tmpe.jpg")

 


 

# # img = cv2.imshow("tmpg",img)
# top = 212
# left= 187
# width=214
# height=214
# start = (left, top)
# end = (left+width, top+height)
# color = (255,0,0)
# thickness = 3
# cv2.rectangle(img, start, end, color, thickness)
# cv2.imshow("image",img)
# cv2.waitKey(0)


# create table qiandao(
#    qiandao_id INT NOT NULL AUTO_INCREMENT,
#    id VARCHAR(20) NOT NULL,
#    name VARCHAR(60) NOT NULL,
#    qiandao_time VARCHAR(50) NOT NULL,
#    submission_date DATE,
#    PRIMARY KEY ( qiandao_id )
# );


# create table dx141(
#    dx141_id INT NOT NULL AUTO_INCREMENT,
#    id int(50) NOT NULL,
#    name VARCHAR(20) NOT NULL,
#    PRIMARY KEY ( dx141_id )
# );

# create table dx131(
#    dx131_id INT NOT NULL AUTO_INCREMENT,
#    id int(50) NOT NULL,
#    name VARCHAR(20) NOT NULL,
#    PRIMARY KEY ( dx131_id )
# # );
# from PyQt5 import QtWidgets, QtGui
# import sys
# import cv2
# import os
# import time
# import numpy as np
# import requests
# from json import JSONDecoder
# from PyQt5.QtWidgets import QFileDialog,QMessageBox
# import pymysql.cursors

# # QMessageBox.information(self,"Tip","facetoken 加入失败！！")
# import pymysql.cursors
# import xlwt
# connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='311', db='facedata', 
#                              charset='utf8mb4')
# name='张忠海'
# id = '14034490141'
# tmp = []
# tmp.append(id)
# tmp.append(name)
# path = "/home/yck/faceIDbiyesheji/aaa.xls"
# cursor = connection.cursor() 
# sql = "select * from dx141;"
# count=cursor.execute(sql)
# # print(count)
# cursor.scroll(0,mode='absolute')
# results = cursor.fetchall()
# print(results)
# fields = cursor.description
# # print(fields)
# workbook= xlwt.Workbook()
# sheet = workbook.add_sheet('table_me',cell_overwrite_ok=True)
# for field in range(0,len(fields)):
#     sheet.write(0,field,fields[field][0])
# print(results[0][0])
# row=1
# col=0
# for row in range(1,len(results)+1):
#     for col in range(0,len(fields)):
#         sheet.write(row, col, u'%s' % results[row-1][col])
#         print(results[row-1][col])

# workbook.save(path)


# print(reee)
# cursor.close()


# create table facemessage(
#     nid int(10) unsigned primary key auto_increment,
#     name VARCHAR(60) NOT NULL,
#     id VARCHAR(20) NOT NULL,
#     shenfen VARCHAR(20) NOT NULL,
#     facetoken VARCHAR(100) NOT NULL,
#     facepath VARCHAR(100) NOT NULL)default character set utf8;


# create table qiandao(
#     nid int(10) unsigned primary key auto_increment,
#     name VARCHAR(60) NOT NULL,
#     id VARCHAR(20) NOT NULL,
#     qiandao_time VARCHAR(50) NOT NULL)default character set utf8;

# create table dx141(
#     nid int(10) unsigned primary key auto_increment,
#     name VARCHAR(60) NOT NULL,
#     id VARCHAR(20) NOT NULL)default character set utf8;

# create table dx131(
#     nid int(10) unsigned primary key auto_increment,
#     name VARCHAR(60) NOT NULL,
#     id VARCHAR(20) NOT NULL)default character set utf8;

# a = "xjp"
# b = "dx141"
# word = a + "_" + b
# print(word)

# create table if not exists dx131 select * from dx141;
import datetime
import time 
from time import strftime,gmtime
# sql = "update "tablename" set "fieldname1"="new_value" where "filename2"="value";"
ttime=datetime.datetime.now().strftime('%Y年%m月%d日%H时%M分%S秒')#现在
print(nowTime)

ttime=strftime("%Y年%m月%d日%H时%M分%S秒", gmtime())
print(ttime)