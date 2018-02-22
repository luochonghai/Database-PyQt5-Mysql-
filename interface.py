# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import inputData
import depictTable
import pymysql.cursors

searchData = ["项目编号","1"]

class MyTable(QTableWidget):
    def __init__(self,parent=None):
        super(MyTable, self).__init__(parent)
        self.setWindowTitle("我是一个表格")
        self.setWindowIcon(QIcon("liang.jpg"))
        self.resize(920, 240)
        self.setColumnCount(5)
        self.setRowCount(2)
        #设置表格有两行五列。
        self.setColumnWidth(0, 200)
        self.setColumnWidth(4, 200)
        self.setRowHeight(0, 100)
        #设置第一行高度为100px，第一列宽度为200px。

        self.table()

    def table(self):
        self.setItem(0,0,QTableWidgetItem("你的名字"))
        self.setItem(0,1,QTableWidgetItem("性别"))
        self.setItem(0,2,QTableWidgetItem("出生日期"))
        self.setItem(0,3, QTableWidgetItem("职业"))
        self.setItem(0,4, QTableWidgetItem("收入"))
        #添加表格的文字内容.
        self.setHorizontalHeaderLabels(["第一行", "第二行", "第三行", "第四行", "第五行"])
        self.setVerticalHeaderLabels(["第一列", "第二列"])
        #设置表头
        lbp = QLabel()
        lbp.setPixmap(QPixmap("Male.png"))
        self.setCellWidget(1,1,lbp)
        #在表中添加一张图片
        twi = QTableWidgetItem("新海诚")
        twi.setFont(QFont("Times", 10, ))
        self.setItem(1,0,twi)
        #添加一个自己设置了大小和类型的文字。
        dte = QDateTimeEdit()
        dte.setDateTime(QDateTime.currentDateTime())
        dte.setDisplayFormat("yyyy/MM/dd")
        dte.setCalendarPopup(True)
        self.setCellWidget(1,2,dte)
        #添加一个弹出的日期选择，设置默认值为当前日期,显示格式为年月日。
        cbw = QComboBox()
        cbw.addItem("医生")
        cbw.addItem("老师")
        cbw.addItem("律师")
        self.setCellWidget(1,3,cbw)
        #添加了一个下拉选择框
        sb = QSpinBox()
        sb.setRange(1000,10000)
        sb.setValue(5000)#设置最开始显示的数字
        sb.setDisplayIntegerBase(10)#这个是显示数字的进制，默认是十进制。
        sb.setSuffix("元")#设置后辍
        sb.setPrefix("RMB: ")#设置前辍
        sb.setSingleStep(100)
        self.setCellWidget(1,4,sb)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global searchData
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('空白部分<b>要什么注释</b> 。')
        
        mainLayout = QGridLayout()

        btn = QPushButton('查找数据',self)
        btn.clicked.connect(lambda:self.searchRes())
        btn.setToolTip('本按钮的功能是<b>查找数据</b> ')
        btn.resize(btn.sizeHint())
        mainLayout.addWidget(btn,3,0)
        #btn.move(280,150)

        stn = QPushButton('生成表格',self)
        #stn.clicked.connect(lambda: self.viewTable())
        stn.clicked.connect(lambda: self.showTable())
        stn.setToolTip('本按钮的功能是<b>生成表格</b> ')
        stn.resize(stn.sizeHint())
        mainLayout.addWidget(stn,0,1)
        #stn.move(200,50)

        # self.search_win = QLineEdit(self)
        # mainLayout.addWidget(self.search_win,2,0)
        # self.search_win.setText("1")
        # searchData[1] = self.search_win.text()
        # #self.search_win.move(40,150)
        self.nameLable = QLabel("请填写搜索内容")
        self.nameLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        mainLayout.addWidget(self.nameLable,2,0)

        self.styleLable = QLabel("项目编号")
        self.styleLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        mainLayout.addWidget(self.styleLable,1,0)
        #self.styleLable.move(240,100)

        select_type = QPushButton('选择',self)
        select_type.clicked.connect(self.select_one)
        mainLayout.addWidget(select_type,1,1)
        #select_type.move(200,150)

        select_type = QPushButton('搜索内容是？',self)
        select_type.clicked.connect(self.write_one)
        mainLayout.addWidget(select_type,2,1)

        ptn = QPushButton('输入数据',self)
        ptn.clicked.connect(lambda: self.InputData())
        ptn.setToolTip('本按钮的功能是<b>输入数据</b> ')
        ptn.resize(ptn.sizeHint())
        mainLayout.addWidget(ptn,0,0)
        self.setLayout(mainLayout)
        #ptn.move(40,50)
        self.setGeometry(300,300,200,220)
        self.setWindowTitle('初始界面')
        self.setWindowIcon(QIcon('liang.jpg'))
        self.show()

    def closeEvent(self,event):
        reply = QMessageBox.question(self,'Message',
            "Are you sure to quit?",QMessageBox.Yes|
            QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def viewTable(self):
        self.MyTable = MyTable()
        self.MyTable.show()

    def InputData(self):
    	self.IData = inputData.InputDialog()
    	self.IData.show()

    def showTable(self):
        self.myWindow = depictTable.MyDialog()
        self.myWindow.show()

    def searchRes(self):
        self.ResSer = searchResult()
        self.ResSer.show()

    def select_one(self):
        global searchData
        list = ['项目编号','合同名称','业主名称','业主性质','合同金额','合同性质','合同签订日','合同约定开工','合同约定日期','合同完工日','履约保证金','安全保证金','合同约定支付时间','合同约定退还时间','款项性质','收款条件','付款方式（银承、商承、电汇）','发票要求','收款其他条件（扣贴现息）','发票时间','发票金额','实际收款时间','实际收款金额','实际收款方式']
        style,ok = QInputDialog.getItem(self,"搜索类型","请选择搜索类型：",list)
        if ok :
            self.styleLable.setText(style)
            searchData[0] = style

    def write_one(self):
        global searchData
        name,ok = QInputDialog.getText(self,"搜索内容","输入搜索内容:",
                                       QLineEdit.Normal,self.nameLable.text())
        if ok and (len(name)!=0):
            self.nameLable.setText(name)
            searchData[1] = name


class searchResult(QDialog):  
    def __init__(self, parent=None):  
        super(searchResult, self).__init__(parent) 

        # Connect to the database
        connection = pymysql.connect(host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='temp',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        temp = connection.cursor()
        global searchData
        sql_search = "select * from project where "+searchData[0]+" = '%s'"
        temp.execute(sql_search%(searchData[1]))
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
    ex = Example()
    sys.exit(app.exec_())