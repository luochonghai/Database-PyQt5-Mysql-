# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class MyDialog(QDialog):  
    def __init__(self, parent=None):  
        super(MyDialog, self).__init__(parent) 

        # Connect to the database
        connection = pymysql.connect(host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='temp',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        temp = connection.cursor()
        sql_search = "select * from project where '%s' == '%s'"
        temp.execute(sql_search%())
        result = temp.fetchall()

        self.MyTable = QTableWidget(len(result),24)  
        self.MyTable.setHorizontalHeaderLabels(['项目编号','合同名称','业主名称','业主性质','合同金额','合同性质','合同签订日','合同约定开工','合同约定日期','合同完工日','履约保证金','安全保证金','合同约定支付时间','合同约定退还时间','款项性质','收款条件','付款方式（银承、商承、电汇）','发票要求','收款其他条件（扣贴现息）','发票时间','发票金额','实际收款时间','实际收款金额','实际收款方式'])  

        for i in range(len(result)):
            newItem = QTableWidgetItem(result[i]['项目编号'])  
            self.MyTable.setItem(i, 0, newItem)  
            newItem = QTableWidgetItem(result[i]['合同名称'])  
            self.MyTable.setItem(i, 1, newItem)  
            newItem = QTableWidgetItem(result[i]['业主名称'])  
            self.MyTable.setItem(i, 2, newItem)   
            newItem = QTableWidgetItem(result[i]['业主性质'])  
            self.MyTable.setItem(i, 3, newItem)  
            newItem = QTableWidgetItem(result[i]['合同金额'])  
            self.MyTable.setItem(i, 4, newItem)  
            newItem = QTableWidgetItem(result[i]['合同性质'])  
            self.MyTable.setItem(i, 5, newItem)  
            newItem = QTableWidgetItem(result[i]['合同签订日'])  
            self.MyTable.setItem(i, 6, newItem)  
            newItem = QTableWidgetItem(result[i]['合同约定开工'])  
            self.MyTable.setItem(i, 7, newItem)  
            newItem = QTableWidgetItem(result[i]['合同约定日期'])  
            self.MyTable.setItem(i, 8, newItem)   
            newItem = QTableWidgetItem(result[i]['合同完工日'])  
            self.MyTable.setItem(i, 9, newItem)  
            newItem = QTableWidgetItem(result[i]['履约保证金'])  
            self.MyTable.setItem(i, 10, newItem)  
            newItem = QTableWidgetItem(result[i]['安全保证金'])  
            self.MyTable.setItem(i, 11, newItem)    
            newItem = QTableWidgetItem(result[i]['合同约定支付时间'])  
            self.MyTable.setItem(i, 12, newItem)  
            newItem = QTableWidgetItem(result[i]['合同约定退还时间'])  
            self.MyTable.setItem(i, 13, newItem)  
            newItem = QTableWidgetItem(result[i]['款项性质'])  
            self.MyTable.setItem(i, 14, newItem)   
            newItem = QTableWidgetItem(result[i]['收款条件'])  
            self.MyTable.setItem(i, 15, newItem)  
            newItem = QTableWidgetItem(result[i]['付款方式（银承、商承、电汇）'])  
            self.MyTable.setItem(i, 16, newItem)  
            newItem = QTableWidgetItem(result[i]['发票要求'])  
            self.MyTable.setItem(i, 17, newItem)  
            newItem = QTableWidgetItem(result[i]['收款其他条件（扣贴现息）'])  
            self.MyTable.setItem(i, 18, newItem)  
            newItem = QTableWidgetItem(result[i]['发票时间'])  
            self.MyTable.setItem(i, 19, newItem)  
            newItem = QTableWidgetItem(result[i]['发票金额'])  
            self.MyTable.setItem(i, 20, newItem)   
            newItem = QTableWidgetItem(result[i]['实际收款时间'])  
            self.MyTable.setItem(i, 21, newItem)  
            newItem = QTableWidgetItem(result[i]['实际收款金额'])  
            self.MyTable.setItem(i, 22, newItem)  
            newItem = QTableWidgetItem(result[i]['实际收款方式'])  
            self.MyTable.setItem(i, 23, newItem)                      
        
        layout = QHBoxLayout()  
        layout.addWidget(self.MyTable)  
        self.setLayout(layout)            
          
if __name__ == '__main__':  
    app = QApplication(sys.argv)  
    myWindow = MyDialog()  
    myWindow.show()  
    sys.exit(app.exec_())