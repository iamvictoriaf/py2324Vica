d1 = {'elizaveta':'89213651412','julia':'89773215678','vladimir':'89345672134'}

d2 = {
    'igor':'89324564376',
    'svetlana':'9874563245',
    'vera':'89623773123'
}

while True:
    name = input('Введите имя: ')
    print(f'Телефон абонента {name} - {d1[name]}')

except KeyError:
    print(f'Телефон абонента {name} - не найден')
#d1.update(d2)
#print(d1)

#print(d1.items())
#print(d1.keys())
#print(d1.values())