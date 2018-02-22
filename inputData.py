#-*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pymysql.cursors

showlist = ["" for i in range(24)]

class InputDialog(QWidget):
    def __init__(self):       
        super(InputDialog,self).__init__()
    #     self.initUi()

    # def initUi(self):
        self.setWindowTitle("项目信息")
        self.setGeometry(400,400,900,960)

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

        self.nameLable = QLabel("")
        self.nameLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.styleLable = QLabel("")
        self.styleLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.numberLable = QLabel("")
        self.numberLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.costLable = QLabel("")
        self.costLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.introductionLable = QLabel("")
        self.introductionLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._6Lable = QLabel("")
        self._6Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._7Lable = QLabel("")
        self._7Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._8Lable = QLabel("")
        self._8Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._9Lable = QLabel("")
        self._9Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._10Lable = QLabel("")
        self._10Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._11Lable = QLabel("")
        self._11Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._12Lable = QLabel("")
        self._12Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._13Lable = QLabel("")
        self._13Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._14Lable = QLabel("")
        self._14Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._15Lable = QLabel("")
        self._15Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._16Lable = QLabel("")
        self._16Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._17Lable = QLabel("")
        self._17Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._18Lable = QLabel("")
        self._18Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._19Lable = QLabel("")
        self._19Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._20Lable = QLabel("")
        self._20Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._21Lable = QLabel("")
        self._21Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._22Lable = QLabel("")
        self._22Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._23Lable = QLabel("")
        self._23Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self._24Lable = QLabel("")
        self._24Lable.setFrameStyle(QFrame.Panel|QFrame.Sunken)

        nameButton=QPushButton("修改")
        nameButton.clicked.connect(self.selectName)
        styleButton=QPushButton("修改")
        styleButton.clicked.connect(self.selectStyle)
        numberButton=QPushButton("修改")
        numberButton.clicked.connect(self.selectNumber)
        costButton=QPushButton("修改")
        costButton.clicked.connect(self.selectCost)
        introductionButton=QPushButton("修改")
        introductionButton.clicked.connect(self.selectIntroduction)
        _6Button = QPushButton("修改")
        _6Button.clicked.connect(self.select6)
        _7Button = QPushButton("修改")
        _7Button.clicked.connect(self.select7)
        _8Button = QPushButton("修改")
        _8Button.clicked.connect(self.select8)
        _9Button = QPushButton("修改")
        _9Button.clicked.connect(self.select9)
        _10Button = QPushButton("修改")
        _10Button.clicked.connect(self.select10)
        _11Button = QPushButton("修改")
        _11Button.clicked.connect(self.select11)
        _12Button = QPushButton("修改")
        _12Button.clicked.connect(self.select12)
        _13Button = QPushButton("修改")
        _13Button.clicked.connect(self.select13)
        _14Button = QPushButton("修改")
        _14Button.clicked.connect(self.select14)
        _15Button = QPushButton("修改")
        _15Button.clicked.connect(self.select15)
        _16Button = QPushButton("修改")
        _16Button.clicked.connect(self.select16)
        _17Button = QPushButton("修改")
        _17Button.clicked.connect(self.select17)
        _18Button = QPushButton("修改")
        _18Button.clicked.connect(self.select18)
        _19Button = QPushButton("修改")
        _19Button.clicked.connect(self.select19)
        _20Button = QPushButton("修改")
        _20Button.clicked.connect(self.select20)
        _21Button = QPushButton("修改")
        _21Button.clicked.connect(self.select21)
        _22Button = QPushButton("修改")
        _22Button.clicked.connect(self.select22)
        _23Button = QPushButton("修改")
        _23Button.clicked.connect(self.select23)
        _24Button = QPushButton("修改")
        _24Button.clicked.connect(self.select24)

        nextButton = QPushButton("保存")
        nextButton.clicked.connect(lambda: self.nextPage())

        mainLayout=QGridLayout()
        mainLayout.addWidget(label1,0,0)
        mainLayout.addWidget(self.nameLable,0,1)
        mainLayout.addWidget(nameButton,0,2)
        mainLayout.addWidget(label2,1,0)
        mainLayout.addWidget(self.styleLable,1,1)
        mainLayout.addWidget(styleButton,1,2)
        mainLayout.addWidget(label3,2,0)
        mainLayout.addWidget(self.numberLable,2,1)
        mainLayout.addWidget(numberButton,2,2)
        mainLayout.addWidget(label4,3,0)
        mainLayout.addWidget(self.costLable,3,1)
        mainLayout.addWidget(costButton,3,2)
        mainLayout.addWidget(label5,4,0)
        mainLayout.addWidget(self.introductionLable,4,1)
        mainLayout.addWidget(introductionButton,4,2)
        mainLayout.addWidget(label6,5,0)
        mainLayout.addWidget(self._6Lable,5,1)
        mainLayout.addWidget(_6Button,5,2)
        mainLayout.addWidget(label7,6,0)
        mainLayout.addWidget(self._7Lable,6,1)
        mainLayout.addWidget(_7Button,6,2)
        mainLayout.addWidget(label8,7,0)
        mainLayout.addWidget(self._8Lable,7,1)
        mainLayout.addWidget(_8Button,7,2)
        mainLayout.addWidget(label9,8,0)
        mainLayout.addWidget(self._9Lable,8,1)
        mainLayout.addWidget(_9Button,8,2)
        mainLayout.addWidget(label10,9,0)
        mainLayout.addWidget(self._10Lable,9,1)
        mainLayout.addWidget(_10Button,9,2)
        mainLayout.addWidget(label11,10,0)
        mainLayout.addWidget(self._11Lable,10,1)
        mainLayout.addWidget(_11Button,10,2)
        mainLayout.addWidget(label12,11,0)
        mainLayout.addWidget(self._12Lable,11,1)
        mainLayout.addWidget(_12Button,11,2)
        mainLayout.addWidget(label13,0,3)
        mainLayout.addWidget(self._13Lable,0,4)
        mainLayout.addWidget(_13Button,0,5)
        mainLayout.addWidget(label14,1,3)
        mainLayout.addWidget(self._14Lable,1,4)
        mainLayout.addWidget(_14Button,1,5)
        mainLayout.addWidget(label15,2,3)
        mainLayout.addWidget(self._15Lable,2,4)
        mainLayout.addWidget(_15Button,2,5)
        mainLayout.addWidget(label16,3,3)
        mainLayout.addWidget(self._16Lable,3,4)
        mainLayout.addWidget(_16Button,3,5)
        mainLayout.addWidget(label17,4,3)
        mainLayout.addWidget(self._17Lable,4,4)
        mainLayout.addWidget(_17Button,4,5)
        mainLayout.addWidget(label18,5,3)
        mainLayout.addWidget(self._18Lable,5,4)
        mainLayout.addWidget(_18Button,5,5)
        mainLayout.addWidget(label19,6,3)
        mainLayout.addWidget(self._19Lable,6,4)
        mainLayout.addWidget(_19Button,6,5)
        mainLayout.addWidget(label20,7,3)
        mainLayout.addWidget(self._20Lable,7,4)
        mainLayout.addWidget(_20Button,7,5)
        mainLayout.addWidget(label21,8,3)
        mainLayout.addWidget(self._21Lable,8,4)
        mainLayout.addWidget(_21Button,8,5)
        mainLayout.addWidget(label22,9,3)
        mainLayout.addWidget(self._22Lable,9,4)
        mainLayout.addWidget(_22Button,9,5)
        mainLayout.addWidget(label23,10,3)
        mainLayout.addWidget(self._23Lable,10,4)
        mainLayout.addWidget(_23Button,10,5)
        mainLayout.addWidget(label24,11,3)
        mainLayout.addWidget(self._24Lable,11,4)
        mainLayout.addWidget(_24Button,11,5)
        mainLayout.addWidget(nextButton,12,1)

        self.setLayout(mainLayout)



    def selectName(self):
        global showlist
        name,ok = QInputDialog.getText(self,"项目编号","输入项目编号:",
                                       QLineEdit.Normal,self.nameLable.text())
        if ok and (len(name)!=0):
            self.nameLable.setText(name)
            showlist[0] = name

    def selectStyle(self):
        global showlist
        name,ok = QInputDialog.getText(self,"合同名称","输入合同名称:",
                                       QLineEdit.Normal,self.styleLable.text())
        if ok and (len(name)!=0):
            self.styleLable.setText(name)   
            showlist[1] = name

    def selectNumber(self):
        global showlist
        name,ok = QInputDialog.getText(self,"业主名称","输入业主名称:",
                                       QLineEdit.Normal,self.numberLable.text())
        if ok and (len(name)!=0):
            self.numberLable.setText(name) 
            showlist[2] = name

    def selectCost(self):
        global showlist
        name,ok = QInputDialog.getText(self,"业主性质","输入业主性质:",
                                       QLineEdit.Normal,self.costLable.text())
        if ok and (len(name)!=0):
            self.costLable.setText(name)
            showlist[3] = name

    def selectIntroduction(self):
        global showlist
        name,ok = QInputDialog.getText(self,"合同金额","输入合同金额:",
                                       QLineEdit.Normal,self.introductionLable.text())
        if ok and (len(name)!=0):
            self.introductionLable.setText(name)
            showlist[4] = name

    def select6(self):
        global showlist
        name,ok = QInputDialog.getText(self,"合同性质","输入合同性质:",
                                       QLineEdit.Normal,self._6Lable.text())
        if ok and (len(name)!=0):
            self._6Lable.setText(name)
            showlist[5] = name

    def select7(self):
        global showlist
        name,ok = QInputDialog.getText(self,"合同签订日","输入合同签订日:",
                                       QLineEdit.Normal,self._7Lable.text())
        if ok and (len(name)!=0):
            self._7Lable.setText(name)
            showlist[6] = name

    def select8(self):
        global showlist
        name,ok = QInputDialog.getText(self,"合同约定开工","输入合同约定开工:",
                                       QLineEdit.Normal,self._8Lable.text())
        if ok and (len(name)!=0):
            self._8Lable.setText(name)
            showlist[7] = name

    def select9(self):
        global showlist
        name,ok = QInputDialog.getText(self,"合同约定日期","输入合同约定日期:",
                                       QLineEdit.Normal,self._9Lable.text())
        if ok and (len(name)!=0):
            self._9Lable.setText(name)
            showlist[8] = name

    def select10(self):
        global showlist
        name,ok = QInputDialog.getText(self,"合同完工日","输入合同完工日:",
                                       QLineEdit.Normal,self._10Lable.text())
        if ok and (len(name)!=0):
            self._10Lable.setText(name)
            showlist[9] = name

    def select11(self):
        global showlist
        name,ok = QInputDialog.getText(self,"履约保证金","输入履约保证金:",
                                       QLineEdit.Normal,self._11Lable.text())
        if ok and (len(name)!=0):
            self._11Lable.setText(name)
            showlist[10] = name

    def select12(self):
        global showlist
        name,ok = QInputDialog.getText(self,"安全保证金","输入安全保证金:",
                                       QLineEdit.Normal,self._12Lable.text())
        if ok and (len(name)!=0):
            self._12Lable.setText(name)
            showlist[11] = name

    def select13(self):
        global showlist
        name,ok = QInputDialog.getText(self,"合同约定支付时间","输入合同约定支付时间:",
                                       QLineEdit.Normal,self._13Lable.text())
        if ok and (len(name)!=0):
            self._13Lable.setText(name)
            showlist[12] = name

    def select14(self):
        global showlist
        name,ok = QInputDialog.getText(self,"合同约定退还时间","输入合同约定退还时间:",
                                       QLineEdit.Normal,self._14Lable.text())
        if ok and (len(name)!=0):
            self._14Lable.setText(name)
            showlist[13] = name

    def select15(self):
        global showlist
        name,ok = QInputDialog.getText(self,"款项性质","输入款项性质:",
                                       QLineEdit.Normal,self._15Lable.text())
        if ok and (len(name)!=0):
            self._15Lable.setText(name)
            showlist[14] = name

    def select16(self):
        global showlist
        name,ok = QInputDialog.getText(self,"收款条件","输入收款条件:",
                                       QLineEdit.Normal,self._16Lable.text())
        if ok and (len(name)!=0):
            self._16Lable.setText(name)
            showlist[15] = name

    def select17(self):
        global showlist
        name,ok = QInputDialog.getText(self,"付款方式（银承、商承、电汇）","输入付款方式:",
                                       QLineEdit.Normal,self._17Lable.text())
        if ok and (len(name)!=0):
            self._17Lable.setText(name)
            showlist[16] = name

    def select18(self):
        global showlist
        name,ok = QInputDialog.getText(self,"发票要求","输入发票要求:",
                                       QLineEdit.Normal,self._18Lable.text())
        if ok and (len(name)!=0):
            self._18Lable.setText(name)
            showlist[17] = name

    def select19(self):
        global showlist
        name,ok = QInputDialog.getText(self,"收款其他条件（扣贴现息）","输入收款其他条件:",
                                       QLineEdit.Normal,self._19Lable.text())
        if ok and (len(name)!=0):
            self._19Lable.setText(name)
            showlist[18] = name

    def select20(self):
        global showlist
        name,ok = QInputDialog.getText(self,"发票时间","输入发票时间:",
                                       QLineEdit.Normal,self._20Lable.text())
        if ok and (len(name)!=0):
            self._20Lable.setText(name)
            showlist[19] = name

    def select21(self):
        global showlist
        name,ok = QInputDialog.getText(self,"发票金额","输入发票金额:",
                                       QLineEdit.Normal,self._21Lable.text())
        if ok and (len(name)!=0):
            self._21Lable.setText(name)
            showlist[20] = name

    def select22(self):
        global showlist
        name,ok = QInputDialog.getText(self,"实际收款时间","输入实际收款时间:",
                                       QLineEdit.Normal,self._22Lable.text())
        if ok and (len(name)!=0):
            self._22Lable.setText(name)
            showlist[21] = name

    def select23(self):
        global showlist
        name,ok = QInputDialog.getText(self,"实际收款金额","输入实际收款金额:",
                                       QLineEdit.Normal,self._23Lable.text())
        if ok and (len(name)!=0):
            self._23Lable.setText(name)
            showlist[22] = name

    def select24(self):
        global showlist
        name,ok = QInputDialog.getText(self,"实际收款方式","输入实际收款方式:",
                                       QLineEdit.Normal,self._24Lable.text())
        if ok and (len(name)!=0):
            self._24Lable.setText(name)
            showlist[23] = name
    # def selectStyle(self):
    #     list = ["外包","自研"]

    #     style,ok = QInputDialog.getItem(self,"项目性质","请选择项目性质：",list)
    #     if ok :
    #         self.styleLable.setText(style)

    # def selectNumber(self):
    #     number,ok = QInputDialog.getInt(self,"项目成员","请输入项目成员人数：",int(self.numberLable.text()),20,100,2)
    #     if ok :
    #         self.numberLable.setText(str(number))

    # def selectCost(self):
    #     cost,ok = QInputDialog.getDouble(self,"项目成本","请输入项目成员人数：",float(self.costLable.text()),100.00,500.00,2)
    #     if ok :
    #         self.costLable.setText(str(cost))

    # def selectIntroduction(self):
    #     introduction,ok = QInputDialog.getMultiLineText(self,"项目介绍","介绍：","服务外包第三方公司 \nPython project")
    #     if ok :
    #         self.introductionLable.setText(introduction)
 
    # def nextPage(self):
    #     self.nextbut = inputData2.InputDialog()
    #     self.nextbut.show()
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
        sql_ser = "select * from project where 项目编号 = '%s'"
        sql_insert = "insert into project(项目编号,合同名称,业主名称,业主性质,合同金额,合同性质,合同签订日,合同约定开工,合同约定日期,合同完工日,履约保证金,安全保证金,合同约定支付时间,合同约定退还时间,款项性质,收款条件,付款方式（银承、商承、电汇）,发票要求,收款其他条件（扣贴现息）,发票时间,发票金额,实际收款时间,实际收款金额,实际收款方式) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        try:
            temp.execute(sql_ser%(showlist[0]))
            res_ser = temp.fetchall()
            if len(res_ser) == 0:
                temp.execute(sql_insert%(showlist[0],showlist[1],showlist[2],showlist[3],showlist[4],showlist[5],showlist[6],showlist[7],showlist[8],showlist[9],showlist[10],showlist[11],showlist[12],showlist[13],showlist[14],showlist[15],showlist[16],showlist[17],showlist[18],showlist[19],showlist[20],showlist[21],showlist[22],showlist[23]))
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