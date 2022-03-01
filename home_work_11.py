# test_1
with open("test.txt", 'r') as file:
    string = file.readline()

string = string.replace('_', ' ')
print(string)
array = string.split(' ')
print(array)
result = 0

for i in array:
    if i.isdigit():
        result += int(i)

print(result)
print("__________________________________________________\n")


# test_2
with open("test2.txt", 'r') as file:
    array = file.readlines()

numbers = []
strings = []

for i in array:          # избавился от спец символа \n и разделил на два списка по типу данных
    if i.isdigit():
        i.replace('\n', '')
        numbers.append(int(i))
    if i.isalpha():
        i.replace('\n', '')
        strings.append(i)

strings.sort(key=len)
print(strings)
numbers.sort()
print(numbers)
result = numbers + strings
print(result)
print("__________________________________________________\n")


# test_3
with open("test3.txt", 'w') as file:
    while True:
        i = input("Enter something: ")
        if i == '':
            break
        file.write(i + '\n')
print("__________________________________________________\n")


# test_4
with open("test3.txt", 'r') as file:
    array = file.readlines()

print(array)
in_all_string = len(array)
number_string = 0
print(f"Amount string: {in_all_string}")

for i in array:
    number_string += 1
    length_string = len(i)
    print(f"In {number_string} string: {length_string} symbols")


# test_HW
array = ['34', '12', "teth", '87', '4', '100', "fgd", '4', "qre"]
numbers = []
strings = []

for i in array:
    if i.isdigit():
        numbers.append(int(i))
    if i.isalpha():
        strings.append(i)

strings.sort(key=len)
numbers.sort()

tmp = []
for j in numbers:
    tmp.append(str(j))


result = strings + tmp
result = ' '.join(result)

with open("test4.txt", 'w') as file:
    file.write(result)
