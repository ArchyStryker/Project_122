import random

# test_1
tpl = tuple(random.randint(0, 100) for i in range(10))
print(tpl)
min_number = tpl[0]
max_number = tpl[0]
for j in range(len(tpl)):
    if min_number >= tpl[j]:
        min_number = tpl[j]
    if max_number <= tpl[j]:
        max_number = tpl[j]
print(f"{min_number = }; \n{max_number = }")
print("\n_________________________________")


# test_2
tpl_1 = tuple(random.randint(0, 5) for i in range(10))
tpl_2 = tuple(random.randint(-5, 0) for i in range(10))
tpl_3 = tpl_1 + tpl_2
print(f"{tpl_3} \nCount '0' = {tpl_3.count(0)}")
print("\n_________________________________")


# test_3
string_tpl = ''
tpl = (3007, "Artur", "Archy", True)
for i in tpl:
    string_tpl += str(i) + ', '

print(string_tpl[:-2])
print("\n_________________________________")


# test_4
A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
sum_A = 0
sum_B = 0
min_number_A = A[0]
min_number_B = B[0]
msg = ''
for i in range(len(A)):
    sum_A += A[i]
    if min_number_A >= A[i]:
        min_number_A = A[i]
for j in range(len(B)):
    sum_B += B[j]
    if min_number_B >= B[j]:
        min_number_B = B[j]
if sum_A > sum_B:
    msg = "Sum of elements A > sum of elements B."
elif sum_A < sum_B:
    msg = "Sum of elements A < sum of elements B"
else:
    msg = "Sum of elements A = sum of elements B"
print(f"{msg} \n{min_number_A = } \n{min_number_B = }")
print("\n_________________________________")


# test_HW
string = "Sauron, the Dark Lord, has accumulated to\
 him all the Rings of Power, the methods by which he plans to govern Middle-earth."
string_without_punctuation = ''
for i in string:
    if i in [',', '.', '"', "'", '-', ':', ';', '!', '?']:
        i = ''
    string_without_punctuation += i
lst_string = string_without_punctuation.split()

word = lst_string[0]
for i in range(len(lst_string)):
    if len(word) <= len(lst_string[i]):
        word = lst_string[i]

print(f"Longest word: {word} \n\n_________________________________\n{lst_string}")
