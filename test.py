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
result = temp.execute("select * from city")
print(result)