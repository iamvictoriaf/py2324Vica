import pymysql

connection = pymysql.connect(host="10.10.101.161", user="pyuser", password="123456", database="test")

cursor = connection.cursor()

cursor.execute("insert into telsprav values("vica", "frank", "f", "89213456754")")

connection.commit()


