# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pymysql.cursors

class IniDialog():  
	def __init__(self):  
		super().__init__() 
		# Connect to the database
		connection = pymysql.connect(host='127.0.0.1',
		                             port=3306,
		                             user='root',
		                             password='123456',
		                             db='temp',
		                             charset='utf8mb4',
		                             cursorclass=pymysql.cursors.DictCursor)
		temp = connection.cursor()
		#to search first
		sign_exist = 0
		sign_e_ = 0
		sql_show_db = "show databases;"
		result = temp.execute(sql_show_db)
		result = temp.fetchall()
		for i in range(len(result)):
		    if result[i]['Database'] == 'temp':
		        sign_exist = 1
		        break
		if sign_exist == 0:
		    sql_create = "create database temp;"
		    sql_use = "use temp3;"
		    sql_table_project = "create table project(项目编号 varchar(50),合同名称 varchar(50),业主名称 varchar(50),业主性质 varchar(50),合同金额 varchar(50),合同性质 varchar(50),合同签订日 varchar(50),合同约定开工 varchar(50),合同约定日期 varchar(50),合同完工日 varchar(50),履约保证金 varchar(50),安全保证金 varchar(50),合同约定支付时间 varchar(50),合同约定退还时间 varchar(50),款项性质 varchar(50),收款条件 varchar(50),付款方式（银承、商承、电汇） varchar(50),发票要求 varchar(50),收款其他条件（扣贴现息） varchar(50),发票时间 varchar(50),发票金额 varchar(50),实际收款时间 varchar(50),实际收款方式 varchar(50),所属部门 varchar(50),E varchar(50),P varchar(50),C varchar(50),primary key(项目编号))"
		    result = temp.execute(sql_create)
		    result = temp.execute(sql_use)
		    result = temp.execute(sql_table_project)

		    #sql_use_table = "use temp;"
		    sql_table_final = "create table final(项目编号 varchar(50),数据类型 varchar(50),设计费 varchar(50),自行 varchar(50),内部分包 varchar(50),外部分包 varchar(50),现场费用 varchar(50),大临 varchar(50),差旅费 varchar(50),办公费 varchar(50),业务招待费 varchar(50),车辆费用（油料） varchar(50),零星材料 varchar(50),房租及后勤费用 varchar(50),其他 varchar(50),财务费用 varchar(50),税费 varchar(50),设备采购 varchar(50),分包 varchar(50),primary key(项目编号,数据类型))"
		    #result = temp.execute(sql_create_table)
		    result = temp.execute(sql_table_final)
