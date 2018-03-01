# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import interface
import test
import pymysql.cursors

class LoginDialog(QDialog):   
    def __init__(self, parent=None):   
        QDialog.__init__(self, parent)   
        self.setWindowTitle('login')  
        self.title_user = QLabel("username:",self)
        self.title_user.move(10,20)
        self.user = QLineEdit(self)   
        self.user.move(65, 20)   
        self.user.setText('admin') 

        self.title_pwd = QLabel("password:",self)
        self.title_pwd.move(10,60)

        self.pwd = QLineEdit(self)   
        self.pwd.move(65, 60)   
        self.pwd.setText('admin')   
        self.pwd.setEchoMode(QLineEdit.Password)   
        self.loginBtn = QPushButton('Login', self)   
        self.loginBtn.move(100, 90)   
        self.loginBtn.clicked.connect(self.login) # 绑定方法判断用户名和密码   
        self.loginBtn.clicked.connect(self.testing)
    def login(self):   
        # Connect to the database
        connection = pymysql.connect(host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='temp',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        temp = connection.cursor()

        sql_search = "select * from userpwd where username = '%s'"
        try:
            temp.execute(sql_search%(self.user.text()))
            res_search = temp.fetchall()
            if len(res_search) == 0:
                QMessageBox.critical(self, 'Error', 'User name or password error')
            elif res_search[0]['password'] != self.pwd.text():
                QMessageBox.critical(self, 'Error', 'User name or password error')
            else:
                # 如果用户名和密码正确，关闭对话框，accept()关闭后，如果增加一个取消按钮调用reject()
                self.accept()
        except Exception as e:
            raise e
        finally:
            connection.close()
    
    def testing(self):
        self.IData = test.IniDialog()
        #self.IData.show()

  
if __name__ == '__main__':   
    app = QApplication(sys.argv)   
    dialog = LoginDialog()   
    if dialog.exec_():    
        ex = interface.Example()
        sys.exit(app.exec_())   
