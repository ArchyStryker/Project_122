# test_1
import random

a_num = 23
b_num = 34.7


class Example:

    first_static = 34
    second_static = 7

    def __init__(self, first_dinamic: int, second_dinamic: int):
        self.first_dimanic = first_dinamic
        self.second_dinamic = second_dinamic

    def print_some_var(self):
        i = random.randrange(15)
        print(i)

    def sum_num(self):
        return a_num + b_num

    def pow_dinamic(self):
        return self.first_dimanic ** self.second_dinamic


# test_2
class Calculate:

    def __init__(self):
        self.var_input()

    def var_input(self):
        self.a = float(input("Enter first number: "))
        self.b = float(input("Enter second number: "))

    def sum_(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


# test_HW
class DefCalc:

    result = ''
    len_ = 0

    def __init__(self):
        self.definition()

    def definition(self):
        self.variable = input("Enter string or number: ")
        if self.variable.isdigit():
            self.result = "numbers"
        else:
            self.result = "string"
        return self.result

    def length(self):
        self.len_ = len(self.variable)
        return self.len_

    def calculation(self):
        count_vowels = 0
        count_consonants = 0
        even = 0
        vowels = []
        consonants = []
        message = ''

        if self.result == "string":
            for i in self.variable:
                if i in "aeiouy":
                    count_vowels += 1
                    vowels.append(i)
                else:
                    count_consonants += 1
                    consonants.append(i)
            if count_vowels * count_consonants <= self.len_:
                message = ''.join(vowels)
            else:
                message = ''.join(consonants)

        if self.result == "numbers":
            for i in self.variable:
                if int(i) % 2 == 0:
                    even += int(i)
            message = even * self.len_

        return message
