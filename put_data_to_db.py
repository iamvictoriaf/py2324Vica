import pymysql

connection = pymysql.connect(host="nadejnei.net", user="student", password="1q2w#E$R", database="test", port=33306)

cursor = connection.cursor()

for line in f:
    line = line.strip()
    split_line = line.split(':')
    name = split_line[0]
    surname = split_line[1]
    sex = split_line[2]
    phone = split_line[3]
    cursor.execute("f'insert into telsprav values("{vica}", "{frank}", "{f}", "{89116543456}")')

connection.commit()


