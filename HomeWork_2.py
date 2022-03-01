# # test1
#
# number = int(input("Введите целое число: "))
#
# result = number % 2
#
# if result == 0:
#     print("Число целое")
# else:
#     print("Число нечетное")
#
#
# # test2
#
# print("Введите три целых числа: ")
#
# num_1 = int(input())
# num_2 = int(input())
# num_3 = int(input())
#
# if num_1 > num_2 and num_1 > num_3:
#     print(num_1, "- наибольшее число")
# elif num_2 > num_3:
#     print(num_2, "- наибольшее число")
# else:
#     print(num_3, "- наибольшее число")
#
#
# # test3
#
# operand_1 = float(input("Ввудите первый операнд: "))
# operand_2 = float(input("Введите второй операнд: "))
# simbol = input("Введите знак операции, допустимы '+', '-', '/', '*' ")
#
# if simbol == '+':
#     print("Результат:", operand_1 + operand_2)
# elif simbol == '-':
#     print("Результат:", operand_1 - operand_2)
# elif simbol == '/':
#     print("Результат:", operand_1 / operand_2)
# else:
#     print("Результат:", operand_1 * operand_2)
#
#
# # test4
#
# x = float(input("Задайте значение x для функции y = f(x): "))
#
# if x > 0:
#     print(2 * x - 10)
# elif x == 0:
#     print('0')
# else:
#     print(2 * abs(x) - 1)
#
#
# # test5
#
# print("Checking numbers for equality, please insert two numbers: ")
#
# number_1 = float(input())
# number_2 = float(input())
#
# result = number_1 == number_2
#
# if result:
#     print("Equals")
# else:
#     print("Not equals")
#
#
# # test1(HW)
#
# year = int(input("Insert year: "))
#
# if year % 4 == 0:
#     print("Year a leap")
# else:
#     print("Year not a leap")
#
#
# # test3(HW)
#
# print("Insert coordinates for point 'x' and 'y': ")
#
# coord_x = float(input())
# coord_y = float(input())
# radius = float(input("Insert radius of circle: "))
#
# if radius < abs(coord_x) or radius < abs(coord_y):
#     print("Point is not included in area of circle")
# else:
#     print("Point is included in area of circle")
#
# # test4
# time = int(input("What time is it now? "))
# day = input("What day of weeks? ")
# weather = input("it's sunny outside? Yes or No? ")
# def good_morning(time, day, weather):
#     """Функция принемает в качестве значение time - число обозначающее час
#     в качестве day - английское 3-ех буквенное сокращение дня недели Mon, Tue, Wen, Thu, Fri, Sat, Sun
#     в качестве weather - Yes или No"""
#     if (time >= 8 and (day != "Sat" or day != "Sun") and weather == "Yes") \
#             or (time >= 10 and (day == "Sat" or day == "Sun") and weather == "Yes"):
#         print("Good Morning!")
#     elif (time < 8 and (day != "Sat" or day != "Sun")) \
#             or (time < 10 and (day == "Sat" or day == "Sun")):
#         print("It's too early.")
#     elif (time >= 8 and (day != "Sat" or day != "Sun") and weather == "No") \
#             or (time >= 10 and (day == "Sat" or day == "Sun") and weather == "No"):
#         print("Good Morning! But it's cloudy outside.")
#     else:
#         print("Something goes wrong keep sleeping!")
#
# good_morning(time, day, weather)

S = "Skjgoi gja;lf76\n \b8LJfkN KFNL K"

print(S.count('g'))
