# -*- coding: utf-8 -*- 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *  
import pymysql.cursors
import sys  

class MyDialog(QWidget):  
    def __init__(self):  
        super(MyDialog, self).__init__() 

        self.setWindowTitle("生成表格")
        self.setGeometry(100,100,900,960)

        # Connect to the database
        connection = pymysql.connect(host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='temp',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        temp = connection.cursor()
        sql_search = "select * from final"
        temp.execute(sql_search)
        result = temp.fetchall()

        self.MyTable = QTableWidget(len(result),19)  
        self.MyTable.setHorizontalHeaderLabels(['项目编号','数据类型','设计费','自行','内部分包','外部分包','现场费用','大临','差旅费','办公费','业务招待费','车辆费用（油料）','零星材料','房租及后勤费用','其他','财务费用','税费','设备采购','分包'])  

        for i in range(len(result)):
            newItem = QTableWidgetItem(result[i]['项目编号'])  
            self.MyTable.setItem(i, 0, newItem) 
            newItem = QTableWidgetItem(result[i]['数据类型'])  
            self.MyTable.setItem(i, 1, newItem)  
            newItem = QTableWidgetItem(result[i]['设计费'])  
            self.MyTable.setItem(i, 2, newItem)   
            newItem = QTableWidgetItem(result[i]['自行'])  
            self.MyTable.setItem(i, 3, newItem)  
            newItem = QTableWidgetItem(result[i]['内部分包'])  
            self.MyTable.setItem(i, 4, newItem)  
            newItem = QTableWidgetItem(result[i]['外部分包'])  
            self.MyTable.setItem(i, 5, newItem)  
            newItem = QTableWidgetItem(result[i]['现场费用'])  
            self.MyTable.setItem(i, 6, newItem)  
            newItem = QTableWidgetItem(result[i]['大临'])  
            self.MyTable.setItem(i, 7, newItem)  
            newItem = QTableWidgetItem(result[i]['差旅费'])  
            self.MyTable.setItem(i, 8, newItem) 
            newItem = QTableWidgetItem(result[i]['办公费'])  
            self.MyTable.setItem(i, 9, newItem)  
            newItem = QTableWidgetItem(result[i]['业务招待费'])  
            self.MyTable.setItem(i, 10, newItem)  
            newItem = QTableWidgetItem(result[i]['车辆费用（油料）'])  
            self.MyTable.setItem(i, 11, newItem)   
            newItem = QTableWidgetItem(result[i]['零星材料'])  
            self.MyTable.setItem(i, 12, newItem)  
            newItem = QTableWidgetItem(result[i]['房租及后勤费用'])  
            self.MyTable.setItem(i, 13, newItem)  
            newItem = QTableWidgetItem(result[i]['其他'])  
            self.MyTable.setItem(i, 14, newItem)    
            newItem = QTableWidgetItem(result[i]['财务费用'])  
            self.MyTable.setItem(i, 15, newItem)  
            newItem = QTableWidgetItem(result[i]['税费'])  
            self.MyTable.setItem(i, 16, newItem)  
            newItem = QTableWidgetItem(result[i]['设备采购'])  
            self.MyTable.setItem(i, 17, newItem)   
            newItem = QTableWidgetItem(result[i]['分包'])  
            self.MyTable.setItem(i, 18, newItem)      
 

        layout = QHBoxLayout()  
        layout.addWidget(self.MyTable)  
        self.setLayout(layout)     
          
          
if __name__ == '__main__':  
    app = QApplication(sys.argv)  
    myWindow = MyDialog()  
    myWindow.show()  
    sys.exit(app.exec_())
