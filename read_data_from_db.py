import pymysql

connection = pymysql.connect(host="nadejnei.net", user="student", password="1q2w#E$R", database="test", port=33306)
cursor = connection.cursor()

cursor.execute=("select name, phone from telsprav")

data = cursor.fetchall()
print(data)
telsprav={}
for element in data:
    print(element)
    #telsprav[]
    name = element[0]
    phone = element[1]
    telsprav[name]=phone

print(telsprav)