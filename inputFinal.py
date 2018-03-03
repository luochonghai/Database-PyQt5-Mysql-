#-*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import inputCheck
import pymysql.cursors

showlist = ["" for i in range(19)]

class InputDialog(QWidget):
    def __init__(self):       
        super(InputDialog,self).__init__()
    #     self.initUi()

    # def initUi(self):
        self.setWindowTitle("项目成本信息")
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

        nextButton = QPushButton("保存")
        nextButton.clicked.connect(lambda: self.nextPage())

        mainLayout=QGridLayout()
        mainLayout.addWidget(label1,0,0)
        self.text1 = QLineEdit(self)
        mainLayout.addWidget(self.text1,0,1)
        mainLayout.addWidget(label2,1,0)
        self.text2 = QComboBox()
        self.text2.insertItem(0,self.tr("费控指标"))
        self.text2.insertItem(1,self.tr("1月"))
        self.text2.insertItem(2,self.tr("2月"))
        self.text2.insertItem(3,self.tr("3月"))
        self.text2.insertItem(4,self.tr("4月"))
        self.text2.insertItem(5,self.tr("5月"))
        self.text2.insertItem(6,self.tr("6月"))
        self.text2.insertItem(7,self.tr("7月"))
        self.text2.insertItem(8,self.tr("8月"))
        self.text2.insertItem(9,self.tr("9月"))
        self.text2.insertItem(10,self.tr("10月"))
        self.text2.insertItem(11,self.tr("11月"))
        self.text2.insertItem(12,self.tr("12月"))        
        mainLayout.addWidget(self.text2,1,1)
        mainLayout.addWidget(label3,2,0)
        self.text3 = QLineEdit(self)
        mainLayout.addWidget(self.text3,2,1)
        mainLayout.addWidget(label4,3,0)
        self.text4 = QLineEdit(self)  
        mainLayout.addWidget(self.text4,3,1)  
        mainLayout.addWidget(label5,4,0)
        self.text5 = QLineEdit(self)
        mainLayout.addWidget(self.text5,4,1)
        mainLayout.addWidget(label6,5,0)
        self.text6 = QLineEdit(self)
        mainLayout.addWidget(self.text6,5,1)
        mainLayout.addWidget(label7,6,0)
        self.text7 = QLineEdit(self)
        mainLayout.addWidget(self.text7,6,1)
        mainLayout.addWidget(label8,7,0)
        self.text8 = QLineEdit(self)
        mainLayout.addWidget(self.text8,7,1)
        mainLayout.addWidget(label9,8,0)
        self.text9 = QLineEdit(self)
        mainLayout.addWidget(self.text9,8,1)
        mainLayout.addWidget(label10,9,0)
        self.text10 = QLineEdit(self)  
        mainLayout.addWidget(self.text10,9,1)

        mainLayout.addWidget(label11,0,3)
        self.text11 = QLineEdit(self)  
        mainLayout.addWidget(self.text11,0,4)
        mainLayout.addWidget(label12,1,3)
        self.text12 = QLineEdit(self)
        mainLayout.addWidget(self.text12,1,4)
        mainLayout.addWidget(label13,2,3)
        self.text13 = QLineEdit(self)  
        mainLayout.addWidget(self.text13,2,4)  
        mainLayout.addWidget(label14,3,3)
        self.text14 = QLineEdit(self)
        mainLayout.addWidget(self.text14,3,4)
        mainLayout.addWidget(label15,4,3)
        self.text15 = QLineEdit(self)  
        mainLayout.addWidget(self.text15,4,4)
        mainLayout.addWidget(label16,5,3)
        self.text16 = QLineEdit(self)
        mainLayout.addWidget(self.text16,5,4)
        mainLayout.addWidget(label17,6,3)
        self.text17 = QLineEdit(self)  
        mainLayout.addWidget(self.text17,6,4)  
        mainLayout.addWidget(label18,7,3)
        self.text18 = QLineEdit(self)
        mainLayout.addWidget(self.text18,7,4)
        mainLayout.addWidget(label19,8,3)
        self.text19 = QLineEdit(self)  
        mainLayout.addWidget(self.text19,8,4)     
        mainLayout.addWidget(nextButton,9,4)
        self.setLayout(mainLayout)

    def nextPage(self):   
        # Connect to the database
        connection = pymysql.connect(host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='temp',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        temp = connection.cursor()
        sql_ser = "select * from final where 项目编号 = '%s' and 数据类型 = '%s'"
        sql_insert = "insert into final(项目编号,数据类型,设计费,自行,内部分包,外部分包,现场费用,大临,差旅费,办公费,业务招待费,车辆费用（油料）,零星材料,房租及后勤费用,其他,财务费用,税费,设备采购,分包) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        global showlist
        showlist[0] = self.text1.text()
        showlist[1] = self.text2.currentText()
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
            #add the function of checking input 
            for i in range(2,19):
                str_temp = inputCheck.str_check(showlist[i])
                if str_temp == -1:
                    QMessageBox.critical(self, 'Error', 'Strange characters.')
                    return
                elif str_temp == -2:
                    QMessageBox.critical(self, 'Error', 'The length of decimal is longer then 2.')
                    return
                elif str_temp == -3:
                    QMessageBox.critical(self, 'Error', 'Empty input.')
                    return
            temp.execute(sql_ser%(showlist[0],showlist[1]))
            res_ser = temp.fetchall()
            if len(res_ser) == 0:
                temp.execute(sql_insert%(showlist[0],showlist[1],showlist[2],showlist[3],showlist[4],showlist[5],showlist[6],showlist[7],showlist[8],showlist[9],showlist[10],showlist[11],showlist[12],showlist[13],showlist[14],showlist[15],showlist[16],showlist[17],showlist[18]))
                connection.commit()
            else:
                QMessageBox.critical(self, 'Error', 'Already existed.')
                # 如果用户名和密码正确，关闭对话框，accept()关闭后，如果增加一个取消按钮调用reject()
        except Exception as e:
            raise e
        finally:
            connection.close()

if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    myshow=InputDialog()
    myshow.show()
    sys.exit(app.exec_())
