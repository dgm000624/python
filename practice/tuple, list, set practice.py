from traceback import print_tb

a = list()
a.extend([1,2,4])
print(a)

a = tuple(a)
print(a)

a = set(a)
print(a)

a = list(a)
a.append([1,2])
print(a)

a = tuple(a)
print(a)
a = set(a)
print(a)