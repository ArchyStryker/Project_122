# test_1
lst = [3, 15, 41, 1, 2, 15]
lst_1 = []

for i in lst:
    if lst.count(i) == 1:
        lst_1.append(i)

print(lst_1)
print("___________________________________ \n")


# test_2
lst = [3, 15, 41, 1, 2, 15, 3, 2, 3, 15, 15, 41]
count = 0

while len(lst) != 0:
    a = lst[0]
    count += lst.count(a) // 2
    for i in lst:
        if i == a:
            lst.remove(i)

print(f"Amount pairs of numbers: {count}")
print("___________________________________ \n")


# test_3
c_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
c_2 = (45, 21, 124, 76, 5, 23, 91, 234)
sum_1 = sum(c_1)
index_max_1 = c_1.index(max(c_1))
index_min_1 = c_1.index(min(c_1))
sum_2 = sum(c_2)
index_max_2 = c_2.index(max(c_2))
index_min_2 = c_2.index(min(c_2))
msg = ("sum c_1 > sum c_2" if sum_1 > sum_2 else "sum c_1 < sum c_2")

print(f"{msg} \n{index_max_1 = } \n{index_min_1 = } \n{index_max_2 = } \n{index_min_2 = }")
print("___________________________________ \n")


# test_4
string = " An apple a day keeps the doctor away"
lst_keys = list(set(string.lower()))
lst_items = []

for i in lst_keys:
    lst_items.append(string.lower().count(i))

dct = dict(zip(lst_keys, lst_items))
print(dct)
print("___________________________________ \n")


# test_5
sweet_shop = {
    "cheesecake": [["cookies", "butter", "cream cheese", "sugar", "vanilla extract"], 2.5, 2500],
    "muffin": [["sugar", "flour", "egg", "milk", "cocoa powder"], 2.5, 1500],
    "cappuccino": [["espresso", "milk foam", "cinnamon"], 2.5, 5000]
}
while True:
    choice = input("Hello! What do you want?: ").lower()
    # choice takes values: "description", "cost", "amount", "all information" or "buy"
    match choice:
        case "description":
            for i in sweet_shop.keys():
                print(f"{i} - {', '.join(sweet_shop[i][0])};")
        case "cost":
            for i in sweet_shop.keys():
                print(f"{i} - {sweet_shop[i][1]} BYN;")
        case "amount":
            for i in sweet_shop.keys():
                print(f"{i} - {sweet_shop[i][2]} gr;")
        case "all information":
            for i in sweet_shop.keys():
                print(f"{i}: {', '.join(sweet_shop[i][0])}; "
                      f"cost - {sweet_shop[i][1]} BYN; "
                      f"weight - {sweet_shop[i][2]} gr;")
        case "buy":
            product = input("What would you like to buy: ").lower()
            while True:
                try:
                    how_much = int(input("How much do you want to buy(gr): "))
                except ValueError:
                    print("Wrong weight entered!")
                else:
                    break
            while True:
                match product:
                    case "cheesecake":
                        if how_much > sweet_shop[product][2]:
                            print("Sorry! We don't have that much!")
                            break
                        print(f"Price: {sweet_shop[product][1] * (how_much / 100)} BYN")
                        sweet_shop[product][2] -= how_much
                        break
                    case "muffin":
                        if how_much > sweet_shop[product][2]:
                            print("Sorry! We don't have that much!")
                            break
                        print(f"Price: {sweet_shop[product][1] * (how_much / 100)} BYN")
                        sweet_shop[product][2] -= how_much
                        break
                    case "cappuccino":
                        if how_much > sweet_shop[product][2]:
                            print("Sorry! We don't have that much!")
                            break
                        print(f"Price: {sweet_shop[product][1] * (how_much / 100)} BYN")
                        sweet_shop[product][2] -= how_much
                        break
                    case "end":
                        print("Goodbye")
                        break
                    case _:
                        print("Invalid name product!")
                        break
        case "bye":
            print("Have a good day!")
            break
print("___________________________________ \n")


# test_6
lst_1 = [i for i in range(1, 10)]
lst_2 = [i for i in range(5, 15)]

st_1 = set(lst_1)
st_2 = set(lst_2)
st_3 = st_1 & st_2

print(len(st_3))
print("___________________________________ \n")


# test_7
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
    finally:
        print("The End!")
print("___________________________________ \n")


# test_8
with open("test.txt", 'r', encoding='utf-8') as file:
    array = file.readlines()

print(array)

average_mark = 0
count = 0
loser = []

for i in array:
    count += 1
    if i[-1].isspace():
        i = i[:-1]
    print(i)
    average_mark += int(i[-2])
    if int(i[-2]) < 3:
        loser.append(i)

print(f"Loser: {' '.join(loser)} \nAverage mark: {average_mark / count}")
