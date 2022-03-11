# # test_1
# import math
#
# array_1 = [1, 3, 14, 67, 34]
#
#
# def sum_array(array):
#     sum_ = 0
#     for i in array:
#         if str(i).isdigit():
#             sum_ += int(i)
#     return sum_
#
#
# # test_2
# def is_year_leap(year=int(input("Enter year(YYYY): "))):
#     return year % 400 == 0 or year % 4 == 0 and year % 100 != 0
#
#
# # test_3
# def square(a=int(input("Enter length side of the square: "))):
#     p = 4 * a
#     s = a ** 2
#     d = math.sqrt(2) * a
#     return p, s, d
#
#
# # test_4
# def season(month=int(input("Enter number month of the year: "))):
#     if month in [3, 4, 5]:
#         message = "Spring"
#     elif month in [6, 7, 8]:
#         message = "Summer"
#     elif month in [9, 10, 11]:
#         message = "Autumn"
#     elif month in [1, 2, 12]:
#         message = "Winter"
#     else:
#         message = "Undefined month"
#     return message
#
#
# # test_5
# def is_prime(num=int(input("Enter number 0 to 1000: "))):
#     """Return 'True' if number prime and return false if not."""
#     div = 2
#     if 0 <= num >= 1000:
#         message = "Incorrect number"
#     else:
#         while num % div != 0:
#             div += 1
#         message = num == div
#     return message
#
#
# # test_6
# def average_number(array):
#     return sum(array) / len(array)


# test_HW
def calculator(expression=input("Enter number, sign(+, -, *, /) and second number through a space: "
                                "\n\t(To exit enter '0')\n")):
    if expression == '0':
        return "Quit"
    result = 0
    values = expression.split(' ')
    try:
        match values[1]:
            case '+':
                result = float(values[0]) + float(values[2])
            case '-':
                result = float(values[0]) - float(values[2])
            case '*':
                result = float(values[0]) * float(values[2])
            case '/':
                result = float(values[0]) / float(values[2])
            case _:
                result = "Incorrect data entered"
    except ZeroDivisionError:
        print("Enter divider that is not zero: ")
    except ValueError:
        print("Incorrect data entered")
    finally:
        return result


if __name__ == "__main__":
    print(calculator())
    # sum_array(array_1)
    # is_year_leap()
    # square()
    # season()
    # is_prime()
    # average_number(array_1)
