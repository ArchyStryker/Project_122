# test 1
import math, random

int_num_one = int(input("Введите первое целое число"))
int_num_two = int(input("Введите второе целое число"))
str_val = input("Напишите что-нибудь")
float_num = float(input("Введите дробное число"))

summ = int_num_one + int_num_two + float_num

print(str_val, summ, '\n', '\n')
print(str_val, summ, '\n', '\n')


# test 2
cathet_one = int(input("Значение первого катета:"))
cathet_two = int(input("Значение первого катета:"))
hypot = math.hypot(cathet_one, cathet_two)


area = (cathet_one * cathet_two) / 2
perimeter = cathet_one + cathet_two + hypot

print(' ' + "Площадь треугольника:", area, '\n', "Периметр треугольника:", perimeter, '\n', '\n')


# test 3
int_var = 365
float_var = 0.25
str_var = "Insignia"
bool_var = True

print("Преобразование в целочисленное:", int(float_var), int(bool_var))
print("Преобразование в дробное:", float(int_var), float(bool_var))
print("Преобразование в строку:", str(int_var), str(float_var), str(bool_var))
print("Преобразование в логическое:", bool(int_var), bool(float_var), bool(str_var), '\n', '\n')


# test 4
surname = input("Введите Вашу фамилию:")
name = input("Введите Ваше имя:")
patronymic = input("Введите Ваше отчество:")
try:
    age = int(input("Ваш возраст:"))
except:
    print("Возраст введен не верно, введите корректные данные")
    age = int(input("Ваш возраст:"))
    city = input("Город вашего проживания:")
else:
    city = input("Город вашего проживания:")
finally:
    print('\n', surname, name, patronymic, '\n', "Возраст:", age, '\n', "Город:", city)


# test 5
num_one = 49
num_two = 3.6
num_tree = 19

result = ((num_two + num_tree) - num_one * num_two) % ((num_two / num_two) ** num_one)

print('\n', '\n', result)
