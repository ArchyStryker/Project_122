import random

# test_1
num = input("Enter 7 digit number: ")
count = 0
sum_ = 0
for i in range(7):
    sum_ += int(num[i])
    if int(num[i]) % 2 == 0:
        count += 1
prod = int(num[0]) * int(num[2]) * int(num[5])

if count > 3:
    print(sum_)
else:
    print(prod)
print("____________________________________\n")


# test_2
string = input("Enter some text: ").lower().replace(' ', '')
vowels_count = 0
vowels = ''
for i in string:
    if i in ['a', 'e', 'i', 'o', 'u', 'y']:
        vowels += i + ' '
        vowels_count += 1
consonants_count = len(string) - vowels_count

if consonants_count == vowels_count:
    print(vowels)
else:
    print(f"Vowels: {vowels_count} \nConsonants: {consonants_count}")
print("____________________________________\n")


# test_3
cc = 0
dd = 0
count = 0
i = 0
while i < 8:
    a = int(input("Enter first number from 1 to 20: "))
    b = int(input("Enter second number from 1 to 20: "))
    c = random.randrange(1, 21)
    d = random.randrange(1, 21)
    if a + b > c + d:
        count += 1
    if i == 3:
        cc += c
        dd += d
    i += 1
print(f"Random number: {7 - count} VS introduced number: {count} \nRandom number in 4 iteration: {cc}, {dd}")
print("____________________________________\n")


# test_4
num_count = int(input("Enter quantity numbers: "))
dig = (input("Enter found digit: "))
num_string = ''
count = 0
i = 0
while i < num_count:
    num = random.randrange(1, 1000)
    num_string += str(num) + ' '
    i += 1
print(num_string)
for j in num_string:
    if j == dig:
        count += 1
print(count)
print("____________________________________\n")


# test_5
numbers = ''
string = input("Enter some string: ")
for i in string:
    if i.isdigit():
        numbers += i + ' '
print(numbers)
print("____________________________________\n")


# test_6
word = input("Enter word: ")
i = 0
vowels_count = 0
upper_count = 0
lower_count = 0
while i < len(word):
    if word[i].islower() and word[i - 1].islower():
        lower_count += 1
        i += 1
    if word[i].isupper() and word[i - 1].isupper():
        upper_count += 1
        i += 1
    i += 1
for j in word:
    if j.lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
        vowels_count += 1
consonants_count = len(word) - vowels_count
print(f"Pairs of letters in uppercase: {upper_count} \nPairs of lowercase letters: {lower_count}"
      f"\nVowels letter: {vowels_count} \nConsonant letters: {consonants_count} \nWord length: {len(word)}")
