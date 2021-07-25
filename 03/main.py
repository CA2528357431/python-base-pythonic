array = ["A", "B", None, True, (1, 4)]
enu1 = list(enumerate(array))
enu11 = dict(enumerate(array))
print(enu1)
print(enu11)
print()

tup = ("A", "B", None, True, (1, 4))
enu2 = list(enumerate(tup))
enu22 = dict(enumerate(tup))
print(enu2)
print(enu22)
print()

dic = {"a": [1, 3], "b": "hello", "c": None, "d": True}
enu3 = list(enumerate(dic))
enu33 = dict(enumerate(dic))
print(enu3)
print(enu33)
print()
