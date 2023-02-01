#encoding=utf-8
from selenium import webdriver
import sys
import os
from PyQt5 import QtGui,QtCore
from ID_Number import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import re
import Area
import random
from PyQt5.QtCore import QVariant

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.setupUi(self)
        self.province.clear()
        self.province.addItem('请选择')
        self.city.clear()
        self.city.addItem('请选择')
        self.county.clear()
        self.county.addItem('请选择')
        self.getprovince()
        self.man.click()
        self.province.activated.connect(self.add_city)
        self.city.activated.connect(self.add_county)
        self.CreateId.clicked.connect(self.CreatId)



    def CreatId(self):
        pro=self.province.currentIndex()
        city=self.city.currentIndex()
        conuty=self.county.currentIndex()
        num=self.Num.text()
        if pro==0:
            QMessageBox.information(None, '提示框', '未选择省份')
        elif city==0:
            QMessageBox.information(None, '提示框', '未选择市区')
        elif conuty==0:
            QMessageBox.information(None, '提示框', '未选择乡村')
        elif len(num)!=0:
            try:
                int(num)
            except ValueError:
                QMessageBox.information(None,'提示框','请输入数字')
            else:
                self.ShowId.clear()
                self.show_info()
        elif len(num)==0:
            self.ShowId.clear()
            self.show_info()


    #显示身份证号
    def show_info(self):
        num = self.Num.text()
        if len(num) == 0:
            num = 1
        try:
            idcard = self.gennerator(num)
        except Exception as e:
            print(e)
        for i in idcard:
            self.ShowId.append(i)




    #初始化省份
    def getprovince(self):
        province=Area.dictProvince.values()

        for key,value in Area.dictProvince.items():
            self.province.addItem(value,key)

    #根据省份显示市
    def add_city(self,index):
        pro_code=self.province.itemData(index)
        city=Area.dictCity.get(pro_code,dict())
        self.city.clear()
        self.city.addItem('请选择')
        self.county.clear()
        self.county.addItem('请选择')
        if self.city.currentData()!='请选择':
            for key,value in city.items():
                self.city.addItem(value,key)

    #根据市添加乡村
    def add_county(self,index):
        city_code=self.city.itemData(index)
        country=Area.dictCounty.get(city_code,dict())
        #print(country)
        self.county.clear()
        self.county.addItem('请选择')
        if self.county.currentData()!='请选择':
            for key,value in country.items():
                self.county.addItem(value,key)

    #生成身份证号
    def gennerator(self,num):
        conuty = self.county.currentIndex()
        townid = self.county.itemData(conuty)
        date=self.dateEdit.text()
        dateid=date.replace('-','')
        idcard=[]
        count=0
        sex=self.sigle_btn()
        try:
            for i in range(int(num)):
                id = str(townid) + str(dateid)
                if sex==1:
                   rad=(random.randint(0,499)*2+1)
                   if rad<10:
                        rad='00'+str(rad)
                   elif 10<=rad<100:
                        rad='0'+str(rad)
                   else:
                        rad=str(rad)
                   id=id+rad
                else:
                    rad=(random.randint(0, 499)*2)
                    if rad<10:
                        rad ='00'+str(rad)
                    elif 10<= rad<100:
                        rad='0'+str(rad)
                    else:
                        rad=str(rad)
                    id=id+rad
                weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  #权重项
                checkcode ={'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'4','9':'3','10':'2'}
                try:
                    count=0
                    for c in range(0, len(id)):
                        count =count +int(id[c]) * weight[c]
                except Exception as e:
                    print('异常错误2:' + str(e),id)
                id = id + checkcode[str(count % 11)]  # 算出校验码
                idcard.append(id)
        except Exception as e:
            print('异常错误1:'+ str(e))
        return idcard

    def sigle_btn(self):
        if self.man.isChecked():
            sex=1
        else:
            sex=2
        return sex


if __name__ == "__main__":
    app=QApplication(sys.argv)
    #MainWindow=QMainWindow()
    ui=MyApp()
    #ui.setupUi(mainwindow)
    ui.show()
    sys.exit(app.exec_())

