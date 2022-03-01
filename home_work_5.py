# test_1
i = 1
while i < 10:
    print(i ** 2)
    i += 1
print("_______________________________________")

# test_2
i = 1
j = 1
while i < 125:
    if i % 2 == 0:
        j *= i
    i += 1
print(j)
print("_______________________________________")


# test_3
i = 15
while i > 0:
    print(i, end=' ')
    i -= 1
print('\n'"_______________________________________")


# test_4
num_one = int(input("Enter first number: "))
num_two = int(input("Enter second number: "))
if num_one > num_two:
    num_one, num_two = num_two, num_one
array = [i for i in range(num_one, num_two, 1)]

i = 1
while i != len(array):
    if array[i] < 0:
        print(array[i], end=' ')
    i += 1
else:
    print("Final")
print('\n'"_______________________________________")


# test_5
i = 0
array = []

while i < 98:
    i += 7
    array.append(i)
    print(i, end=' ')
print(f"length the array {len(array)}")
print("_______________________________________")



# test_6
while True:
    i = int(input("Enter first number: "))
    j = int(input("Enter second number: "))
    sign = input("Enter arithmetic sign (+, -, *, /): ")

    if sign == '+':
        print(i + j)
    elif sign == '-':
        print(i - j)
    elif sign == '*':
        print(i * j)
    elif sign == '/':
        if j != 0:
            print(i / j)
        else:
            print("Cannot be divided 0")

    final = int(input("Enter '1' to continue or '0' for exit: "))
    if final == 0:
        break
print("_______________________________________")


# test_7
array = [5, 19, 4, 18, 3, 24, 71]
i = j = k = 0
while k < 7:
    if array[k] % 2 == 0:
        i += 1
    else:
        j += 1
    k += 1

k = 0
result = 0
if i > j:
    while k < 7:
        result += array[k]
        k += 1
    print(result)
else:
    result = array[0] * array[2] * array[5]
    print(result)
print("_______________________________________")


# test_HW
import random

number = random.randint(1, 10)
color = random.randint(0, 1)
if color == 0:
    color = "red"
else:
    color = "black"

i = 0
while i < 5:
    user_number = int(input("Enter a number from 1 to 10: "))
    user_color = (input("Enter color 'red' or 'black': "))
    if user_number == number and user_color == color:
        print("You Winner!")
        break
    else:
        print("Try again!")
        i += 1
else:
    print("You loss!")
