import random

# test_1
import math


def number_of_digits(numb = int(input("Enter integer number: "))):
    count = 0
    while numb > 1:
        numb //= 10
        count += 1
    return count


# test_2
def area_figure(figure = input("Change figure: treangle - 1; square - 2; cicle - 3: ")):
    match figure:
        case '1':
            treangle = lambda p, a, b, c: math.sqrt(p * (p - a) * (p - b) * (p - c))
            a = float(input("Enter edge A: "))
            b = float(input("Enter edge B: "))
            c = float(input("Enter edge C: "))
            p = (a + b + c) / 2
            area = treangle(p, a, b, c)
        case '2':
            square = lambda a: a ** 2
            a = float(input("Enter edge: "))
            area = square(a)
        case '3':
            cicle = lambda r: math.pi * r ** 2
            r = float(input("Enter radius: "))
            area = cicle(r)
        case _:
            area = "Incorect data: "
    return area


# test_3
def random_number(start:int, stop:int):
    array = []
    for i in range(6):
        array.append(random.randrange(start, stop + 1))
    return array


# test_4
def second_converter(seconds:int):
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minuts = seconds // 60
    seconds %= 60
    return f"{days=}; {hours=}; {minuts=}; {seconds=}"


# test_5
def letter_counter(string = input("Enter word(s), without digits: ")):
    vowels = 0
    consonants = 0
    for i in string:
        if i.isalpha():
            if i in "aeiouy":
                vowels +=1
            else:
                consonants += 1
    return f"String contains: {vowels=}: {consonants=}"


# test_6
def func(num = input("Enter digit: ")):
    return int(num) + int(num * 2) + int(num * 3)


# test_7
def multi_function(x = random.randrange(-10, 11)):
    if x < -5:
        result = 2 * abs(x) - 1
    elif x > 5:
        result = 2 * x
    else:
        result = x ** 2
    return f"{x = } \n{result}"


# test_HW
def count(value):

    result = 0
    letters = 0
    numbers = 0

    if type(value) is tuple:
        for i in value:
            result += len(str(i))
    elif type(value) is list:
        for i in value:
            if type(i) is str:
                for j in i:
                    if j.isalpha():
                        letters += 1
                    elif j.isdigit():
                        numbers += 1
            if type(i) is int or type(i) is float:
                numbers += 1
        result = f"{letters = }; {numbers = }"
    elif type(value) is int or type(value) is float:
        for i in str(value):
            if i.isdigit():
                if int(i) % 2 != 0:
                    result += 1
    elif type(value) is str:
        for i in value:
            if i.isalpha():
                result += 1

    return result


tpl = ("yhi", 3578, "_bgdh 34")
lst = ["yhi", 3578, "_bgdh 34"]
str_ = "_bgdh 34"
int_ = 3578
array = [tpl, lst, str_, int]

if __name__ == "__main__":
    number_of_digits()
    area_figure()
    random_number(2, 8)
    second_converter(1234)
    letter_counter()
    func()
    multi_function()
    count(34.56777)
