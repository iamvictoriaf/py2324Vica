f = open('users.txt','r')

for line in f:
    line = line.strip()
    split_line = line.split(':')
    #print(split_line)
    name = split_line[0]
    surname = split_line[1]
    sex = split_line[2]
    phone = split_line[3]

    print(f'Привет, меня зовут {name}, моя фамилия {surname}, пол {sex}, а телефон {phone}')
    #insert into telsprav values ("kirill","morozov","m","89113456789")
    #insert into telsprav values = "elizaveta","ivanova","f","89213651412"

    insert_string = f'insert into telsprav values("{name}","{surname}","{sex}","{phone}")'

f.close()