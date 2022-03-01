# test_1
lst = [i for i in range(12)]
lst.reverse()
print(lst)
print("_______________________________________")


# test_2
n = 20
lst = ['a', 'c', 14, 20, "front", 1917, 20, 'W']
lst.insert(lst.index(n), 200)
lst.pop(lst.index(n))
print(lst)
print("_______________________________________")


# test_3
lst = [3, 14, 15, 18, 16, 11, 2]
even = []
not_even = []
n = 0
for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        not_even.append(i)

if len(even) > len(not_even):
    for i in range(7):
        n += lst[i]
else:
    n = lst[0] * lst[2] * lst[5]
print(n)
print("_______________________________________")


# test_4
a = [5, [1, 2], 2, 'r', 4, "ee"]
b = [4, "we", "ee", 3, [1,2]]
lst = []

for i in a:
    for j in b:
        if i == j:
            lst.append(i)

print(lst)
print("_______________________________________")


# test_5
a = [4, 6, "py", "tell", 78]
b = [44, "hello", 56, "exept", 3]
a.extend(b)
print(a)

a.insert(3, 6)
print(a)

for i in a:
    if type(i) is str:
        a.remove(i)
print(a)

print(len(a))
print("_______________________________________")


# test_HW
lst = [15, 48, "hello", 6, 19, "world"]
n = 0
vowels = 0
consonants = 0
word = ''
for i in range(len(lst)):
    if type(lst[i]) is int:
        if lst[i] % 2 == 0:
            n += lst[i]
        else:
            lst[i] = 1
    else:
        word += lst[i]

word = list(word)
vowels = word.count('o')
vowels += word.count('e')
consonants = len(word) - vowels
print(lst, n)
print(f"vowels: {vowels} \nconsonants: {consonants}")
