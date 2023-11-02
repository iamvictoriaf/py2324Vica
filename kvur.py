from math import sqrt
print("Программа для решения квадратных уравнений!")

bad_data = True

while bad_data == True:
    try:
        a = int(input("Введите число a: "))
        b = int(input("Введите число b: "))
        c = int(input("Введите число c: "))
        bad_data = False
    except ValueError:
        print("Данные не привести к числу")

D = (b * b) - (4 * a * c)
print('Дискриминант равен: ',D,'!')

if D > 0:
    d = koren(D)
    x1 = ((-b) + d) / (2 * a)
    x2 = ((-b) - d) / (2 * a)
    print(f'Уравнение имеет 2 корня. X1 ={X1}, X2={X2}')
