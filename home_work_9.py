# test_1
lst = []
while True:
    i = input("Enter element of list: ")
    if i == '':
        break
    lst.append(i)

st = set(lst)
if len(st) == len(lst):
    msg = "no contain duplicates"
else:
    msg = f"contain {len(lst) - len(st)} duplicates"

print(msg)
print("______________________________________________\n")


# test_2
dct = dict([("one", 1), ("two", 2), ("tree", 3), ("four", 4)])
print(dct)
dct["five"] = 5
print(dct)
dct[(3, 4)] = [3, 4]
print(dct)
print(dct.get((3, 4)))
dct.pop("five")
print(dct)
print(dct.keys())
print("______________________________________________\n")


# test_3
st = set("qwerasdf")
print(st)
fst = frozenset("erfghj")
print(fst)
print(st | fst)
print(st & fst)
