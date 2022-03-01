# test_1
name = input("What is your name? ")
print("Hello, " + name + '!')
print((name + '! ') * 3)


# test_2
num = input("Введите число: ")
result = 0
for i in range(len(num)):
    result += int(num[i])
print(f"Сумма всех цифр числа = {result}")
# print(int(num[0]) + int(num[1]) + int(num[2]))


# test_3
string_3 = "KSLlfdJKJafd"
print(string_3[::3])
print(string_3[0] + string_3[-1])
print(string_3.upper())
print(string_3[-1::-1])
print("True") if string_3.isdigit() else print("False")


# test_4
string_4 = "Ww eE Ee wW"
string_affter = string_4.replace(' ', '')
if string_affter == string_affter[-1::-1]:
    print("This is a palindrome")
else:
    print("This is not a palindrome")


# test_HW
string_5 = "KSLlfdJKJafd"

print(string_5[2])
print(string_5[-2])
print(string_5[:5])
print(string_5[:-2])
print(string_5[::2])
print(string_5[1::2])
print(string_5[-1::-1])
print(string_5[-1::-2])
print(len(string_5))
