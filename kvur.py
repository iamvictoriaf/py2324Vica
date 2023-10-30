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

