# test_1
string = input("Enter string: ")
symbol = input("Enter a symbol contained in this string: ")

for char in string:
    if char == symbol:
        continue
    print(char, end='')
print('\n''_____________________________')


# test_2
start = int(input("Enter first number: "))
stop = int(input("Enter last number: "))
step = int(input("Enter the step sequence: "))

for i in range(start, stop + 1, step):
    print(i, end=' ')
print('\n''_____________________________')


# test_3
for i in range(54, 9184):
    if i % 5 == 0:
        print(i)
print('\n''_____________________________')


# test_4
dinner = ["Bread", "Fish", "Pasta", "Vegetable", "Beef", "Cheese"]
# dinner.pop(1)

for food in dinner:
    if food == "Fish":
        print("I'm don't eat fish.")
        break
else:
    print("It was delicious!")
print('\n''_____________________________')


# test_5
numbers = [4, 9, 13, 18, 27]
amount = 0
multip = 1

for i in numbers:
    amount += i
    multip *= i
else:
    print(f"Sum of array numbers: {amount}")
    print(f"Multiplication of array numbers: {multip}")
print('\n''_____________________________')

# test_6
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end=' ')
    print()
print('\n,_____________________________')


# test_HW
multipl = 1

for i in range(1, 100):
    if i % 2 != 0:
        multipl *= i
else:
    print(f"Multiplication equal: {multipl}")
print('\n''_____________________________')


array = []

for i in range(500):
    if i % 5 == 0:
        array.append(i)
else:
    print(array)
print('\n''_____________________________')


for i in range(1, 497):
    if i % 2 == 0:
        print(i)
print('\n''_____________________________')


lst = [13, 22, 7, 6, 4, 5, 14, 22, 5]
lst_2 = []
n = len(lst)

for i in range(n):
    for j in range(i + 1, n):
        if lst[i] == lst[j]:
            lst_2.append(lst[i])
else:
    print(lst_2)
