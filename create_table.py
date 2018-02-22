import pymysql.cursors
 
# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='123456',
                             db='temp',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
temp = connection.cursor()

sql_search = "desc project"
temp.execute(sql_search)
result = temp.fetchall()
print(result)