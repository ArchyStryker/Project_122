# test_1
import random

M = int(input("Enter how many columns: "))
N = int(input("Enter how many rows: "))
matrix = [[0] * M for i in range(N)]

for i in range(N):
    for j in range(M):
        matrix[i][j] = random.randrange(100)
        print(matrix[i][j], end='\t')
    print()
print('______________________________\n')


# test_2
number = int(input("Enter the number: "))

for i in range(N):
    for j in range(M):
        if matrix[i][j] == number:
            print(f"matrix contains that number - [{i}][{j}] ")
print('______________________________\n')


# test_3
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
try:
    result = num_1 / num_2
except ZeroDivisionError:
    print("Error - zero divide")
else:
    print(result ** 2)
finally:
    print("Final")
print('______________________________\n')


# test_4
try:
    result = num_1 / num_2
except ZeroDivisionError:
    print("Error - zero divide")
except ValueError:
    print("Error - incorrect value")
except Exception as err:
    print(err)
else:
    print("All right!")
print('______________________________\n')


#  test_HW_1
matrix_5x5 = [[0] * 5 for i in range(5)]
max_value = sum(matrix_5x5[0])
max_index = 0

for i in range(5):
    for j in range(5):
        matrix_5x5[i][j] = random.randrange(100)
        print(matrix_5x5[i][j], end='\t')
    print()

max_value = sum(matrix_5x5[0])
max_index = 0

for i in range(1, 5):
    if max_value < sum(matrix_5x5[i]):
        max_value = sum(matrix_5x5[i])
        max_index = i

print(f"{max_index = }")


# test_HW_2

while True:
    try:
        num_one = float(input("Enter dividend: "))
        num_two = float(input("Enter divider: "))
        result = num_one / num_two
    except ValueError:
        print("Enter dividend and divider, having a numeric value and is not zero: ")
    except ZeroDivisionError:
        print("Enter divider that is not zero: ")
    else:
        print(result)
        break
