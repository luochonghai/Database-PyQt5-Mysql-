# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import inputData
import inputFinal
import depictTable
import depictFinal
import pymysql.cursors

searchData = ["项目编号","1"]
searchFinal = ["项目编号","1"]
modifyProject = ["项目编号",""]
modifyTemp = ["项目编号","",""]
showlist = ["" for i in range(28)]

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

        ptn = QPushButton('合同台帐',self)
        ptn.clicked.connect(lambda: self.InputData())
        ptn.setToolTip('本按钮的功能是<b>输入合同台帐</b> ')
        ptn.resize(ptn.sizeHint())
        mainLayout.addWidget(ptn,0,0)
        self.setLayout(mainLayout)

        stn = QPushButton('生成表格（合同台帐）',self)
        stn.clicked.connect(lambda: self.showTable())
        stn.setToolTip('本按钮的功能是<b>生成表格</b> ')
        stn.resize(stn.sizeHint())
        mainLayout.addWidget(stn,0,1)

        ctn = QPushButton('成本明细',self)
        ctn.clicked.connect(lambda: self.InputFinal())
        ctn.setToolTip('本按钮的功能是<b>输入成本明细</b> ')
        ctn.resize(ctn.sizeHint())
        mainLayout.addWidget(ctn,0,2)
        self.setLayout(mainLayout) 

        sctn = QPushButton('生成表格（成本明细）',self)
        sctn.clicked.connect(lambda: self.showFinal())
        sctn.setToolTip('本按钮的功能是<b>生成表格</b> ')
        sctn.resize(sctn.sizeHint())
        mainLayout.addWidget(sctn,0,3)               

        self.styleLable = QLabel("项目编号（合同台帐）")
        self.styleLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        mainLayout.addWidget(self.styleLable,1,0)

        select_type = QPushButton('选择',self)
        select_type.clicked.connect(self.select_one)
        mainLayout.addWidget(select_type,1,1)

        self.styleLable1 = QLabel("项目编号（成本明细）")
        self.styleLable1.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        mainLayout.addWidget(self.styleLable1,1,2)

        select_type1 = QPushButton('选择',self)
        select_type1.clicked.connect(self.select_one)
        mainLayout.addWidget(select_type1,1,3)

        self.nameLable = QLabel("请填写搜索内容")
        self.nameLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        mainLayout.addWidget(self.nameLable,2,0)

        select_type = QPushButton('搜索内容是？',self)
        select_type.clicked.connect(self.write_one)
        mainLayout.addWidget(select_type,2,1)

        self.nameLable1 = QLabel("请填写搜索内容")
        self.nameLable1.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        mainLayout.addWidget(self.nameLable1,2,2)

        select_type2 = QPushButton('搜索内容是？',self)
        select_type2.clicked.connect(self.write_two)
        mainLayout.addWidget(select_type2,2,3)

        btn = QPushButton('查找数据',self)
        btn.clicked.connect(lambda:self.searchRes())
        btn.setToolTip('本按钮的功能是<b>查找数据</b> ')
        btn.resize(btn.sizeHint())
        mainLayout.addWidget(btn,3,0)

        rtn = QPushButton('查找数据',self)
        rtn.clicked.connect(lambda:self.searchT())
        rtn.setToolTip('本按钮的功能是<b>查找数据</b> ')
        rtn.resize(rtn.sizeHint())
        mainLayout.addWidget(rtn,3,2)

        self.modifyLable = QLabel("请输入项目编号")
        self.modifyLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        mainLayout.addWidget(self.modifyLable,4,0)

        ttn = QPushButton('修改数据',self)
        ttn.clicked.connect(lambda:self.modifyInput())
        ttn.resize(ttn.sizeHint())
        mainLayout.addWidget(ttn,4,1)

        self.modifyLable1 = QLabel("请输入项目编号")
        self.modifyLable1.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        mainLayout.addWidget(self.modifyLable1,4,2)

        self.modifyLable2 = QLabel("请输入数据类型")
        self.modifyLable2.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        mainLayout.addWidget(self.modifyLable2,4,3)

        sttn = QPushButton('修改数据',self)
        sttn.clicked.connect(lambda:self.modifyFinal())
        sttn.resize(sttn.sizeHint())
        mainLayout.addWidget(sttn,5,3)

        ltn = QPushButton('点击修改',self)
        ltn.clicked.connect(lambda:self.modifyData())
        ltn.resize(ltn.sizeHint())
        mainLayout.addWidget(ltn,5,0)

        sltn = QPushButton('点击修改',self)
        sltn.clicked.connect(lambda:self.modifyData1())
        sltn.resize(sltn.sizeHint())
        mainLayout.addWidget(sltn,5,2)

        sumbtn = QPushButton('求和',self)
        sumbtn.clicked.connect(lambda: self.SumOfData())
        sumbtn.resize(sumbtn.sizeHint())
        mainLayout.addWidget(sumbtn,6,2)
        
        self.setGeometry(300,300,400,220)
        self.setWindowTitle('初始界面')
        self.setWindowIcon(QIcon('liang.jpg'))
        self.show()

    def SumOfData(self):
        self.SumData = SumFunc()
        self.SumData.show()

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

    def InputFinal(self):
        self.FData = inputFinal.InputDialog()
        self.FData.show()    

    def showTable(self):
        self.myWindow = depictTable.MyDialog()
        self.myWindow.show()

    def showFinal(self):
        self.myWindow = depictFinal.MyDialog()
        self.myWindow.show()

    def searchRes(self):
        self.ResSer = searchResult()
        self.ResSer.show()

    def searchT(self):
        self.ResSer = searchTemp()
        self.ResSer.show()   

    def modifyData(self):
        self.modify = OutputDialog()
        self.modify.show()

    def modifyData1(self):
        self.modify = OutputFinal()
        self.modify.show()

    def select_one(self):
        global searchData
        list = ['项目编号','合同名称','业主名称','业主性质','合同金额','合同性质','合同签订日','合同约定开工','合同约定日期','合同完工日','履约保证金','安全保证金','合同约定支付时间','合同约定退还时间','款项性质','收款条件','付款方式（银承、商承、电汇）','发票要求','收款其他条件（扣贴现息）','发票时间','发票金额','实际收款时间','实际收款金额','实际收款方式','所属部门','E','P','C']
        style,ok = QInputDialog.getItem(self,"搜索类型","请选择搜索类型：",list)
        if ok :
            self.styleLable.setText(style)
            searchData[0] = style

    def modifyInput(self):
        global modifyProject
        name,ok = QInputDialog.getText(self,"修改对象","输入项目编号:",
                                       QLineEdit.Normal,self.modifyLable.text())
        if ok and (len(name)!=0):
            self.modifyLable.setText(name)
            modifyProject[1] = name

    def modifyFinal(self):
        global modifyTemp
        name,ok = QInputDialog.getText(self,"修改对象","输入项目编号:",
                                       QLineEdit.Normal,self.modifyLable1.text())
        names,oks = QInputDialog.getText(self,"修改对象","输入数据类型:",
                                       QLineEdit.Normal,self.modifyLable2.text())
        if ok and (len(name)!=0):
            self.modifyLable1.setText(name)
            modifyTemp[1] = name  
        if oks and (len(names)!=0):        
            self.modifyLable2.setText(names)
            modifyTemp[2] = names  

    def write_one(self):
        global searchData
        name,ok = QInputDialog.getText(self,"搜索内容","输入搜索内容:",
                                       QLineEdit.Normal,self.nameLable.text())
        if ok and (len(name)!=0):
            self.nameLable.setText(name)
            searchData[1] = name

    def write_two(self):
        global searchFinal
        name,ok = QInputDialog.getText(self,"搜索内容","输入搜索内容:",
                                       QLineEdit.Normal,self.nameLable1.text())
        if ok and (len(name)!=0):
            self.nameLable1.setText(name)
            searchFinal[1] = name

class searchResult(QWidget): 
    def __init__(self, parent=None):  
        super(searchResult, self).__init__(parent) 

        self.setWindowTitle("搜索结果")
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
        global searchData
        sql_search = "select * from project where "+searchData[0]+" = '%s'"
        #temp.execute(sql_search%(searchData[1]))
        #result = temp.fetchall()

        try:
            templist = ['项目编号','合同名称','业主名称','业主性质','合同金额','合同性质','E','P','C','合同签订日','合同约定开工','合同约定日期','合同完工日','履约保证金','安全保证金','合同约定支付时间','合同约定退还时间','款项性质','收款条件','付款方式（银承、商承、电汇）','发票要求','收款其他条件（扣贴现息）','发票时间','发票金额','实际收款时间','实际收款金额','实际收款方式','所属部门']
            if searchData[0] not in templist:
                self.setWindowTitle("报错窗口")
                self.setGeometry(100,100,200,50)
                QLabel('not existed',self).move(50,25)
                return
            temp.execute(sql_search%(searchData[1]))
            result = temp.fetchall()
            if len(result) == 0:
                self.setWindowTitle("报错窗口")
                self.setGeometry(100,100,200,50)
                QLabel('not existed',self).move(50,25)
            else:
                self.MyTable = QTableWidget(len(result),28)  
                self.MyTable.setHorizontalHeaderLabels(['项目编号','合同名称','业主名称','业主性质','合同金额','合同性质','E','P','C','合同签订日','合同约定开工','合同约定日期','合同完工日','履约保证金','安全保证金','合同约定支付时间','合同约定退还时间','款项性质','收款条件','付款方式（银承、商承、电汇）','发票要求','收款其他条件（扣贴现息）','发票时间','发票金额','实际收款时间','实际收款金额','实际收款方式','所属部门'])  

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
                    newItem = QTableWidgetItem(result[i]['所属部门'])  
                    self.MyTable.setItem(i, 6, newItem)      
                    newItem = QTableWidgetItem(result[i]['E'])  
                    self.MyTable.setItem(i, 7, newItem)      
                    newItem = QTableWidgetItem(result[i]['P'])  
                    self.MyTable.setItem(i, 8, newItem)  
                    newItem = QTableWidgetItem(result[i]['合同签订日'])  
                    self.MyTable.setItem(i, 9, newItem)  
                    newItem = QTableWidgetItem(result[i]['合同约定开工'])  
                    self.MyTable.setItem(i, 10, newItem)  
                    newItem = QTableWidgetItem(result[i]['合同约定日期'])  
                    self.MyTable.setItem(i, 11, newItem)   
                    newItem = QTableWidgetItem(result[i]['合同完工日'])  
                    self.MyTable.setItem(i, 12, newItem)  
                    newItem = QTableWidgetItem(result[i]['履约保证金'])  
                    self.MyTable.setItem(i, 13, newItem)  
                    newItem = QTableWidgetItem(result[i]['安全保证金'])  
                    self.MyTable.setItem(i, 14, newItem)    
                    newItem = QTableWidgetItem(result[i]['合同约定支付时间'])  
                    self.MyTable.setItem(i, 15, newItem)  
                    newItem = QTableWidgetItem(result[i]['合同约定退还时间'])  
                    self.MyTable.setItem(i, 16, newItem)  
                    newItem = QTableWidgetItem(result[i]['款项性质'])  
                    self.MyTable.setItem(i, 17, newItem)   
                    newItem = QTableWidgetItem(result[i]['收款条件'])  
                    self.MyTable.setItem(i, 18, newItem)  
                    newItem = QTableWidgetItem(result[i]['付款方式（银承、商承、电汇）'])  
                    self.MyTable.setItem(i, 19, newItem)  
                    newItem = QTableWidgetItem(result[i]['发票要求'])  
                    self.MyTable.setItem(i, 20, newItem)  
                    newItem = QTableWidgetItem(result[i]['收款其他条件（扣贴现息）'])  
                    self.MyTable.setItem(i, 21, newItem)  
                    newItem = QTableWidgetItem(result[i]['发票时间'])  
                    self.MyTable.setItem(i, 22, newItem)  
                    newItem = QTableWidgetItem(result[i]['发票金额'])  
                    self.MyTable.setItem(i, 23, newItem)   
                    newItem = QTableWidgetItem(result[i]['实际收款时间'])  
                    self.MyTable.setItem(i, 24, newItem)  
                    newItem = QTableWidgetItem(result[i]['实际收款金额'])  
                    self.MyTable.setItem(i, 25, newItem)  
                    newItem = QTableWidgetItem(result[i]['实际收款方式'])  
                    self.MyTable.setItem(i, 26, newItem)       
                    newItem = QTableWidgetItem(result[i]['C'])  
                    self.MyTable.setItem(i, 27, newItem)          
  
                layout = QHBoxLayout()  
                layout.addWidget(self.MyTable)  
                self.setLayout(layout)  

        except Exception as e:
            raise e            

class searchTemp(QWidget): 
    def __init__(self, parent=None):  
        super(searchTemp, self).__init__(parent) 

        self.setWindowTitle("搜索结果")
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
        global searchFinal
        sql_search = "select * from final where "+searchFinal[0]+" = '%s'"
        #temp.execute(sql_search%(searchFinal[1]))
        #result = temp.fetchall()

        try:
            templist = ['项目编号','数据类型','设计费','自行','内部分包','外部分包','现场费用','大临','差旅费','办公费','业务招待费','车辆费用（油料）','零星材料','房租及后勤费用','其他','财务费用','税费','设备采购','分包']
            if searchFinal[0] not in templist:
                self.setWindowTitle("报错窗口")
                self.setGeometry(100,100,200,50)
                QLabel('not existed',self).move(50,25)
                return
            temp.execute(sql_search%(searchFinal[1]))
            result = temp.fetchall()

            if len(result) == 0:
                self.setWindowTitle("报错窗口")
                self.setGeometry(100,100,200,50)
                QLabel('not existed',self).move(50,25)
            else:
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
                
        except Exception as e:
            raise e      

class OutputDialog(QWidget):
    def __init__(self):       
        super(OutputDialog,self).__init__()
        self.setWindowTitle("修改窗口")
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
        global searchData
        sql_search = "select * from project where "+modifyProject[0]+" = '%s'"
        # temp.execute(sql_search%(modifyProject[1]))
        # result = temp.fetchall()
        try:
            temp.execute(sql_search%(modifyProject[1]))
            result = temp.fetchall()
            if len(result) == 0:
                self.setWindowTitle("报错窗口")
                self.setGeometry(100,100,200,50)
                QLabel('not existed',self).move(50,25)
                #connection.commit()
            else:
                label1=QLabel("项目编号:")
                label2=QLabel("合同名称:")
                label3=QLabel("业主名称:")
                label4=QLabel("业主性质:")
                label5=QLabel("合同金额:")
                label6=QLabel("合同性质:")
                label7=QLabel("合同签订日:")
                label8=QLabel("合同约定开工:")
                label9=QLabel("合同约定日期:")
                label10=QLabel("合同完工日:")
                label11=QLabel("履约保证金:")
                label12=QLabel("安全保证金:")
                label13=QLabel("合同约定支付时间:")
                label14=QLabel("合同约定退还时间:")
                label15=QLabel("款项性质:")
                label16=QLabel("收款条件:")
                label17=QLabel("付款方式（银承、商承、电汇）:")
                label18=QLabel("发票要求:")
                label19=QLabel("收款其他条件（扣贴现息）:")
                label20=QLabel("发票时间:")
                label21=QLabel("发票金额:")
                label22=QLabel("实际收款时间:")
                label23=QLabel("实际收款金额:")
                label24=QLabel("实际收款方式:")
                label25=QLabel("所属部门:")
                label26=QLabel("E:")
                label27=QLabel("P:")
                label28=QLabel("C:")

                nextButton = QPushButton("修改")
                nextButton.clicked.connect(lambda: self.nextPage())

                mainLayout=QGridLayout()
                mainLayout.addWidget(label1,0,0)
                self.text1 = QLineEdit(result[0]['项目编号'],self)
                mainLayout.addWidget(self.text1,0,1)
                mainLayout.addWidget(label2,1,0)
                self.text2 = QLineEdit(result[0]['合同名称'],self)
                mainLayout.addWidget(self.text2,1,1)
                mainLayout.addWidget(label3,2,0)
                self.text3 = QLineEdit(result[0]['业主名称'],self)
                mainLayout.addWidget(self.text3,2,1)
                mainLayout.addWidget(label4,3,0)
                self.text4 = QLineEdit(result[0]['业主性质'],self)  
                mainLayout.addWidget(self.text4,3,1)  
                mainLayout.addWidget(label5,4,0)
                self.text5 = QLineEdit(result[0]['合同金额'],self)
                mainLayout.addWidget(self.text5,4,1)
                mainLayout.addWidget(label6,5,0)
                
                self.text6 = QComboBox()
                self.text6.insertItem(0,self.tr("EPC"))
                self.text6.insertItem(1,self.tr("EP"))
                self.text6.insertItem(2,self.tr("EC"))
                self.text6.insertItem(3,self.tr("PC"))
                self.text6.insertItem(4,self.tr("E"))
                self.text6.insertItem(5,self.tr("P"))
                self.text6.insertItem(6,self.tr("C"))

                mainLayout.addWidget(self.text6,5,1)
                mainLayout.addWidget(label7,6,0)
                self.text7 = QDateTimeEdit(self)
                self.text7.setDateTime(QDateTime.currentDateTime())
                self.text7.setDisplayFormat("yyyy/MM/dd")
                self.text7.setCalendarPopup(True)
                mainLayout.addWidget(self.text7,6,1)
                mainLayout.addWidget(label8,7,0)
                self.text8 = QDateTimeEdit(self)
                self.text8.setDateTime(QDateTime.currentDateTime())
                self.text8.setDisplayFormat("yyyy/MM/dd")
                self.text8.setCalendarPopup(True)
                mainLayout.addWidget(self.text8,7,1)
                mainLayout.addWidget(label9,8,0)
                self.text9 = QDateTimeEdit(self)
                self.text9.setDateTime(QDateTime.currentDateTime())
                self.text9.setDisplayFormat("yyyy/MM/dd")
                self.text9.setCalendarPopup(True)
                mainLayout.addWidget(self.text9,8,1)
                mainLayout.addWidget(label10,9,0)
                self.text10 = QDateTimeEdit(self)
                self.text10.setDateTime(QDateTime.currentDateTime())
                self.text10.setDisplayFormat("yyyy/MM/dd")
                self.text10.setCalendarPopup(True)
                mainLayout.addWidget(self.text10,9,1)
                mainLayout.addWidget(label11,10,0)
                self.text11 = QLineEdit(result[0]['履约保证金'],self)
                mainLayout.addWidget(self.text11,10,1)
                mainLayout.addWidget(label12,11,0)
                self.text12 = QLineEdit(result[0]['安全保证金'],self)   
                mainLayout.addWidget(self.text12,11,1) 

                mainLayout.addWidget(label25,12,0)
                self.text28 = QComboBox()
                mainLayout.addWidget(self.text28,12,1)
                self.text28.insertItem(0,self.tr("冶金事业部"))
                self.text28.insertItem(1,self.tr("市政事业部"))
                self.text28.insertItem(2,self.tr("铁合金事业部"))
                self.text28.insertItem(3,self.tr("自动化事业部"))
                self.text28.insertItem(4,self.tr("建工所"))
                self.text28.insertItem(5,self.tr("翻译中心"))
                self.text28.insertItem(6,self.tr("青海分公司"))
                self.text28.insertItem(7,self.tr("包头分院"))
                self.text28.insertItem(8,self.tr("公司"))

                mainLayout.addWidget(label26,12,3)
                self.text25 = QLineEdit(result[0]['E'],self)
                mainLayout.addWidget(self.text25,12,4)
                mainLayout.addWidget(label27,13,0)
                self.text26 = QLineEdit(result[0]['P'],self)
                mainLayout.addWidget(self.text26,13,1)
                mainLayout.addWidget(label28,13,3)
                self.text27 = QLineEdit(result[0]['C'],self)
                mainLayout.addWidget(self.text27,13,4)

                mainLayout.addWidget(label13,0,3)
                self.text13 = QDateTimeEdit(self)
                self.text13.setDateTime(QDateTime.currentDateTime())
                self.text13.setDisplayFormat("yyyy/MM/dd")
                self.text13.setCalendarPopup(True)
                mainLayout.addWidget(self.text13,0,4)
                mainLayout.addWidget(label14,1,3)
                self.text14 = QDateTimeEdit(self)
                self.text14.setDateTime(QDateTime.currentDateTime())
                self.text14.setDisplayFormat("yyyy/MM/dd")
                self.text14.setCalendarPopup(True)
                mainLayout.addWidget(self.text14,1,4)
                mainLayout.addWidget(label15,2,3)
                self.text15 = QComboBox()

                self.text15.insertItem(0,self.tr("预付款（第一笔款）"))
                self.text15.insertItem(1,self.tr("第二笔款")) 
                self.text15.insertItem(2,self.tr("第三笔款"))
                self.text15.insertItem(3,self.tr("第四笔款"))
                self.text15.insertItem(4,self.tr("第五笔款"))
                self.text15.insertItem(5,self.tr("第六笔款"))
                self.text15.insertItem(6,self.tr("质保金"))   
                self.text15.insertItem(7,self.tr("······"))    

                mainLayout.addWidget(self.text15,2,4)
                mainLayout.addWidget(label16,3,3)
                self.text16 = QLineEdit(result[0]['收款条件'],self)
                mainLayout.addWidget(self.text16,3,4)
                mainLayout.addWidget(label17,4,3)
                self.text17 = QComboBox()

                self.text17.insertItem(0,self.tr("银承"))
                self.text17.insertItem(1,self.tr("商承"))
                self.text17.insertItem(2,self.tr("电汇"))

                mainLayout.addWidget(self.text17,4,4)
                mainLayout.addWidget(label18,5,3)
                self.text18 = QLineEdit(result[0]['发票要求'],self)
                mainLayout.addWidget(self.text18,5,4)
                mainLayout.addWidget(label19,6,3)
                self.text19 = QLineEdit(result[0]['收款其他条件（扣贴现息）'],self)
                mainLayout.addWidget(self.text19,6,4)
                mainLayout.addWidget(label20,7,3)
                self.text20 = QDateTimeEdit(self)
                self.text20.setDateTime(QDateTime.currentDateTime())
                self.text20.setDisplayFormat("yyyy/MM/dd")
                self.text20.setCalendarPopup(True)    
                mainLayout.addWidget(self.text20,7,4)
                mainLayout.addWidget(label21,8,3)
                self.text21 = QLineEdit(result[0]['发票金额'],self)
                mainLayout.addWidget(self.text21,8,4)
                mainLayout.addWidget(label22,9,3)
                self.text22 = QDateTimeEdit(self)
                self.text22.setDateTime(QDateTime.currentDateTime())
                self.text22.setDisplayFormat("yyyy/MM/dd")
                self.text22.setCalendarPopup(True)
                mainLayout.addWidget(self.text22,9,4)
                mainLayout.addWidget(label23,10,3)
                self.text23 = QLineEdit(result[0]['实际收款金额'],self)
                mainLayout.addWidget(self.text23,10,4)
                mainLayout.addWidget(label24,11,3)
                self.text24 = QLineEdit(result[0]['实际收款方式'],self)  
                mainLayout.addWidget(self.text24,11,4)  
                mainLayout.addWidget(nextButton,14,1)
                self.setLayout(mainLayout)
        except Exception as e:
            raise e


    def nextPage(self):   
        global showlist
        # Connect to the database
        connection = pymysql.connect(host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='temp',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        temp = connection.cursor()
        sql_insert = "update project set 合同名称 = '%s',业主名称 = '%s',业主性质 = '%s',合同金额 = '%s',合同性质 = '%s',合同签订日 = '%s',合同约定开工 = '%s',合同约定日期 = '%s',合同完工日 = '%s',履约保证金 = '%s',安全保证金 = '%s',合同约定支付时间 = '%s',合同约定退还时间 = '%s',款项性质 = '%s',收款条件 = '%s',付款方式（银承、商承、电汇） = '%s',发票要求 = '%s',收款其他条件（扣贴现息） = '%s',发票时间 = '%s',发票金额 = '%s',实际收款时间 = '%s',实际收款金额 = '%s',实际收款方式 = '%s',所属部门 = '%s',E = '%s',P = '%s',C = '%s' where 项目编号 = '%s'"
        showlist[0] = self.text1.text()
        showlist[1] = self.text2.text()
        showlist[2] = self.text3.text()
        showlist[3] = self.text4.text()
        showlist[4] = self.text5.text()
        showlist[5] = self.text6.currentText()
        showlist[6] = self.text7.text()
        showlist[7] = self.text8.text()
        showlist[8] = self.text9.text()
        showlist[9] = self.text10.text()
        showlist[10] = self.text11.text()
        showlist[11] = self.text12.text()
        showlist[12] = self.text13.text()
        showlist[13] = self.text14.text()
        showlist[14] = self.text15.currentText()
        showlist[15] = self.text16.text()
        showlist[16] = self.text17.currentText()
        showlist[17] = self.text18.text()
        showlist[18] = self.text19.text()
        showlist[19] = self.text20.text()
        showlist[20] = self.text21.text()
        showlist[21] = self.text22.text()
        showlist[22] = self.text23.text()
        showlist[23] = self.text24.text()
        showlist[24] = self.text25.text()
        showlist[25] = self.text26.text()
        showlist[26] = self.text27.text()
        showlist[27] = self.text28.currentText()

        try:
            temp.execute(sql_insert%(showlist[1],showlist[2],showlist[3],showlist[4],showlist[5],showlist[6],showlist[7],showlist[8],showlist[9],showlist[10],showlist[11],showlist[12],showlist[13],showlist[14],showlist[15],showlist[16],showlist[17],showlist[18],showlist[19],showlist[20],showlist[21],showlist[22],showlist[23],showlist[24],showlist[25],showlist[26],showlist[27],showlist[0]))
            connection.commit()
        except Exception as e:
            raise e
        finally:
            connection.close()

class OutputFinal(QWidget):
    def __init__(self):       
        super(OutputFinal,self).__init__()
        global modifyTemp
        #self.setWindowTitle("修改窗口")
        #self.setGeometry(100,100,900,960)

        # Connect to the database
        connection = pymysql.connect(host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='temp',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        temp = connection.cursor()
        sql_search = "select * from final where "+modifyTemp[0]+" = '%s' and 数据类型 = '%s'"
        # temp.execute(sql_search%(modifyTemp[1]))
        # result = temp.fetchall()
        try:
            temp.execute(sql_search%(modifyTemp[1],modifyTemp[2]))
            result = temp.fetchall()
            if len(result) == 0:
                self.setWindowTitle("报错窗口")
                self.setGeometry(100,100,200,50)
                QLabel('not existed',self).move(50,25)
                
                #connection.commit()
            else:
                self.setWindowTitle("修改窗口")
                self.setGeometry(100,100,900,960)
                label1=QLabel("项目编号:")
                label2=QLabel("数据类型:")
                label3=QLabel("设计费:")
                label4=QLabel("自行:")
                label5=QLabel("内部分包:")
                label6=QLabel("外部分包:")
                label7=QLabel("现场费用:")
                label8=QLabel("大临:")
                label9=QLabel("差旅费:")
                label10=QLabel("办公费:")
                label11=QLabel("业务招待费:")
                label12=QLabel("车辆费用（油料）:")
                label13=QLabel("零星材料:")
                label14=QLabel("房租及后勤费用:")
                label15=QLabel("其他:")
                label16=QLabel("财务费用:")
                label17=QLabel("税费:")
                label18=QLabel("设备采购:")
                label19=QLabel("分包:")

                nextButton = QPushButton("修改")
                nextButton.clicked.connect(lambda: self.nextPage())

                mainLayout=QGridLayout()
                mainLayout.addWidget(label1,0,0)
                self.text1 = QLineEdit(result[0]['项目编号'],self)
                mainLayout.addWidget(self.text1,0,1)
                mainLayout.addWidget(label2,1,0)
                self.text2 = QLineEdit(result[0]['数据类型'],self)
                mainLayout.addWidget(self.text2,1,1)
                mainLayout.addWidget(label3,2,0)
                self.text3 = QLineEdit(result[0]['设计费'],self)
                mainLayout.addWidget(self.text3,2,1)
                mainLayout.addWidget(label4,3,0)
                self.text4 = QLineEdit(result[0]['自行'],self)  
                mainLayout.addWidget(self.text4,3,1)  
                mainLayout.addWidget(label5,4,0)
                self.text5 = QLineEdit(result[0]['内部分包'],self)
                mainLayout.addWidget(self.text5,4,1)
                mainLayout.addWidget(label6,5,0)
                self.text6 = QLineEdit(result[0]['外部分包'],self)
                mainLayout.addWidget(self.text6,5,1)
                mainLayout.addWidget(label7,6,0)
                self.text7 = QLineEdit(result[0]['现场费用'],self)
                mainLayout.addWidget(self.text7,6,1)
                mainLayout.addWidget(label8,7,0)
                self.text8 = QLineEdit(result[0]['大临'],self)
                mainLayout.addWidget(self.text8,7,1)
                mainLayout.addWidget(label9,8,0)
                self.text9 = QLineEdit(result[0]['差旅费'],self)
                mainLayout.addWidget(self.text9,8,1)
                mainLayout.addWidget(label10,9,0)
                self.text10 = QLineEdit(result[0]['办公费'],self)
                mainLayout.addWidget(self.text10,9,1)

                mainLayout.addWidget(label11,0,3)
                self.text11 = QLineEdit(result[0]['业务招待费'],self) 
                mainLayout.addWidget(self.text11,0,4)
                mainLayout.addWidget(label12,1,3)
                self.text12 = QLineEdit(result[0]['车辆费用（油料）'],self)
                mainLayout.addWidget(self.text12,1,4)
                mainLayout.addWidget(label13,2,3)
                self.text13 = QLineEdit(result[0]['零星材料'],self)
                mainLayout.addWidget(self.text13,2,4)  
                mainLayout.addWidget(label14,3,3)
                self.text14 = QLineEdit(result[0]['房租及后勤费用'],self)
                mainLayout.addWidget(self.text14,3,4)
                mainLayout.addWidget(label15,4,3)
                self.text15 = QLineEdit(result[0]['其他'],self)
                mainLayout.addWidget(self.text15,4,4)
                mainLayout.addWidget(label16,5,3)
                self.text16 = QLineEdit(result[0]['财务费用'],self)
                mainLayout.addWidget(self.text16,5,4)
                mainLayout.addWidget(label17,6,3)
                self.text17 = QLineEdit(result[0]['税费'],self)
                mainLayout.addWidget(self.text17,6,4)  
                mainLayout.addWidget(label18,7,3)
                self.text18 = QLineEdit(result[0]['设备采购'],self)
                mainLayout.addWidget(self.text18,7,4)
                mainLayout.addWidget(label19,8,3)
                self.text19 = QLineEdit(result[0]['分包'],self)
                mainLayout.addWidget(self.text19,8,4)      
                mainLayout.addWidget(nextButton,9,4)
                self.setLayout(mainLayout)

        except Exception as e:
            raise e
        finally:
            connection.close()

    def nextPage(self):   
        global showlist
        # Connect to the database
        connection = pymysql.connect(host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='temp',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        temp = connection.cursor()
        sql_insert = "update final set 设计费 = '%s',自行 = '%s',内部分包 = '%s',外部分包 = '%s',现场费用 = '%s',大临 = '%s',差旅费 = '%s',办公费 = '%s',业务招待费 = '%s',车辆费用（油料） = '%s',零星材料 = '%s',房租及后勤费用 = '%s',其他 = '%s',财务费用 = '%s',税费 = '%s',设备采购 = '%s',分包 = '%s' where 项目编号 = '%s' and 数据类型 = '%s'"
        showlist[0] = self.text1.text()
        showlist[1] = self.text2.text()
        showlist[2] = self.text3.text()
        showlist[3] = self.text4.text()
        showlist[4] = self.text5.text()
        showlist[5] = self.text6.text()
        showlist[6] = self.text7.text()
        showlist[7] = self.text8.text()
        showlist[8] = self.text9.text()
        showlist[9] = self.text10.text()
        showlist[10] = self.text11.text()
        showlist[11] = self.text12.text()
        showlist[12] = self.text13.text()
        showlist[13] = self.text14.text()
        showlist[14] = self.text15.text()
        showlist[15] = self.text16.text()
        showlist[16] = self.text17.text()
        showlist[17] = self.text18.text()
        showlist[18] = self.text19.text()

        try:
            temp.execute(sql_insert%(showlist[2],showlist[3],showlist[4],showlist[5],showlist[6],showlist[7],showlist[8],showlist[9],showlist[10],showlist[11],showlist[12],showlist[13],showlist[14],showlist[15],showlist[16],showlist[17],showlist[18],showlist[0],showlist[1]))
            connection.commit()
        except Exception as e:
            raise e
        finally:
            connection.close()

class SumFunc(QWidget): 
    def __init__(self, parent=None):  
        super(SumFunc, self).__init__(parent) 

        self.setWindowTitle("求和")
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
        sum_list = ['项目编号','数据类型','设计费','自行','内部分包','外部分包','现场费用','大临','差旅费','办公费','业务招待费','车辆费用（油料）','零星材料','房租及后勤费用','其他','财务费用','税费','设备采购','分包']
        modify_show = ["",""]
        sql_list = ["" for i in range(17)]
        for i in range(17):
            sql_list[i] = "select sum(TEMP.fee) as FEE,TEMP.type as TYPE from (select (case when temp. 数据类型 like '%月' then '月份总和' when temp.数据类型 = '费控指标'then '费控指标'else 'error' end) as type,fee from (select "+sum_list[i+2]+" as fee,数据类型 from final where  项目编号 = "+modifyTemp[1]+") as temp) as TEMP group by type;"
        """sumdata:[value of 月份总和,value of 费控指标]"""
        sumdata = [["",""] for i in range(17)]

        #to check whether the 项目编号 exist or not
        try:
            sql_check = "select distinct 项目编号 from final"
            #to record how many types of 数据类型 exist in the database
            result_len = 0
            temp.execute(sql_check)
            result = temp.fetchall()
            pj_num = len(result)
            pj_name = ["" for i in range(pj_num)]
            for j in range(pj_num):
                pj_name[j] = result[j]['项目编号']

            if modifyTemp[1] not in pj_name:
                self.setWindowTitle("报错窗口")
                self.setGeometry(100,100,200,50)
                QLabel('not existed',self).move(50,25)
                return
            else:
                #to calculate how many types of 数据类型 exist in the database
                sql_cal = "select distinct (case when temp.数据类型 like '%月' then '月份总和' when temp.数据类型 = '费控指标' then '费控指标' else 'error' end) as type from (select 设计费 as fee,数据类型 from final where 项目编号 = "+modifyTemp[1]+") as temp;"
                temp.execute(sql_cal)
                result = temp.fetchall()
                result_len = len(result)
                for j in range(min(result_len,2)):
                    for i in range(17):
                        result = temp.execute(sql_list[i])
                        result = temp.fetchall()
                        sumdata[i][j] = result[j]['FEE']
                        sumdata[i][j] = str(sumdata[i][j])
                        if i == 0:
                            modify_show[j] = result[j]['TYPE']
                        """notice here:only type string can be shown on the QTableWidgetItem"""

                self.MyTable = QTableWidget(min(result_len,2),19)  
                self.MyTable.setHorizontalHeaderLabels(sum_list)  

                for i in range(min(result_len,2)):
                    newItem = QTableWidgetItem(modifyTemp[1])  
                    self.MyTable.setItem(i, 0, newItem) 
                    newItem = QTableWidgetItem(modify_show[i])  
                    self.MyTable.setItem(i, 1, newItem)  
                    newItem = QTableWidgetItem(sumdata[0][i])  
                    self.MyTable.setItem(i, 2, newItem)   
                    newItem = QTableWidgetItem(sumdata[1][i])  
                    self.MyTable.setItem(i, 3, newItem)  
                    newItem = QTableWidgetItem(sumdata[2][i])  
                    self.MyTable.setItem(i, 4, newItem)  
                    newItem = QTableWidgetItem(sumdata[3][i])  
                    self.MyTable.setItem(i, 5, newItem)  
                    newItem = QTableWidgetItem(sumdata[4][i])  
                    self.MyTable.setItem(i, 6, newItem)  
                    newItem = QTableWidgetItem(sumdata[5][i])  
                    self.MyTable.setItem(i, 7, newItem)  
                    newItem = QTableWidgetItem(sumdata[6][i])  
                    self.MyTable.setItem(i, 8, newItem) 
                    newItem = QTableWidgetItem(sumdata[7][i])  
                    self.MyTable.setItem(i, 9, newItem)  
                    newItem = QTableWidgetItem(sumdata[8][i])  
                    self.MyTable.setItem(i, 10, newItem)  
                    newItem = QTableWidgetItem(sumdata[9][i])  
                    self.MyTable.setItem(i, 11, newItem)   
                    newItem = QTableWidgetItem(sumdata[10][i])  
                    self.MyTable.setItem(i, 12, newItem)  
                    newItem = QTableWidgetItem(sumdata[11][i])  
                    self.MyTable.setItem(i, 13, newItem)  
                    newItem = QTableWidgetItem(sumdata[12][i])  
                    self.MyTable.setItem(i, 14, newItem)    
                    newItem = QTableWidgetItem(sumdata[13][i])  
                    self.MyTable.setItem(i, 15, newItem)  
                    newItem = QTableWidgetItem(sumdata[14][i])  
                    self.MyTable.setItem(i, 16, newItem)  
                    newItem = QTableWidgetItem(sumdata[15][i])  
                    self.MyTable.setItem(i, 17, newItem)   
                    newItem = QTableWidgetItem(sumdata[16][i])  
                    self.MyTable.setItem(i, 18, newItem)         
             
                layout = QHBoxLayout()  
                layout.addWidget(self.MyTable)  
                self.setLayout(layout)     
        except Exception as e:
            raise e      

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
