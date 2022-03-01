import math, random

# test1
name = input("Ваше имя: ")
age = input("Ваш возраст: ")
country = input("Страна где Вы живете: ")
city = input("Город в котором Вы живете: ")

if int(age[-2]) == 1 and int(age[-1]) != 0:
    age_grad = "лет"
elif int(age[-1]) > 1:
    age_grad = "годa"
elif int(age[-1]) > 4 or int(age[-1]) == 0:
    age_grad = "лет"
else:
    age_grad = "год"

message = "Привет, " + name + "! Вам " + age + ' ' + age_grad + ". Вы живете в городе " + city + ", это " + country

print(message)


# test2
# переменными ab, bc, ca - обозначены стороны треугольника,
# r - радиус окружности, R - радиус сферы, a - сторона квадрата, A - сторона куба
# S_sq, S_tr, S_cir, S_cub и S_sph - площади квадрата, треугольника, окружности, куба и сферы соответственно
# P_sq, P_tr, P_cir - периметры
# V_cub, V_sph - обьёмы
Pi = 3.14
ab = int(input("Первая сторона треугольника: "))
bc = int(input("Вторая сторона треугольника: "))
ca = int(input("Третья сторона треугольника: "))
a = int(input("Сторона квадрата: "))
r = int(input("Радиус круга: "))
A = int(input("Сторона куба: "))
R = int(input("Радиус сферы: "))

S_sq = a ** 2
p = (ab + bc + ca) / 2
S_tr = math.sqrt(p * (p - ab) * (p - bc) * (p - ca))
S_cir = Pi * r ** 2
P_sq = 4 * a
P_tr = ab + bc + ca
P_cir = 2 * Pi * r
S_cub = 6 * A ** 2
S_sph = 4 * Pi * R ** 2
V_cub = A ** 3
V_sph = 4 / 3 * Pi * R ** 3

print("Площадь квадрата, треугольника, круга, куба и сферы соответственно: ",
      S_sq, "  ", S_tr, "  ", S_cir, "  ", S_cub, "  ", S_sph, '\n',
      "Периметр квадрата, треугольника, длина окружности: ", P_sq, "  ", P_tr, "  ", P_cir, '\n',
      "Обьемы куба и сферы: ", V_cub, "  ", V_sph)
