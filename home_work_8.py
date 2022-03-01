# test_1
person = {"name": "Artur", "age": 32, "city": "Minsk"}
print(person["age"])
print("_______________________________\n")


# test_2
cars = {"BMW": ["X3", "X5", "X7"], "Tesla": ["Model S", "Model X", "Cybertruck"]}

print(f"{cars['BMW'][0]}, {cars['BMW'][-1]}; \n{cars['Tesla'][0]}, {cars['Tesla'][-1]}.")
print("_______________________________\n")


# test_3
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

print(d1['b'] == d2['b'])
print("_______________________________\n")


# test_4
multiple = 1
num_dict = {1: 41, 2: 8, 14: 12, 5: 3, 0: 33}

for i in num_dict.values():
    multiple *= i

print(f"{multiple = }")
print("_______________________________\n")


# test_5
one_lst = ["one", "two", "tree", "four", "five"]
two_lst = [1, 2, 3, 4, 5]

print(dict(zip(one_lst, two_lst)))
print("_______________________________\n")


# test_6
key_lst = []
value_lst = []
string = "pythonist"
for i in string:
    key_lst.append(i)
    value_lst.append(string.count(i))

print(dict(zip(key_lst, value_lst)))
print("_______________________________\n")


# test_HW
price_list = ''
cost = 0
amount_goods = 0
goods = {"table": [350, 4], "chair": [400, 11], "commode": [380, 3], "bed": [420, 6]}

for i in goods:
    price_list += i + ' - ' + str(goods[i][0]) + ' - ' + str(goods[i][1]) + '\n'
    cost += goods[i][0]
    amount_goods += goods[i][1]

print(f"{price_list} \n{cost = } \n{amount_goods = }")
