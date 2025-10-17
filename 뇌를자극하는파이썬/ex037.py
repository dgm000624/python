def square(x:int):
    return x * 2

print(square(x=2))
v1 = [1,2,3,4]
print(square(x=v1))
result = map(square , v1)
print(result)
for i in result:
    print(i, end = " ")

print()
need1 = lambda x: x**2
result2 = map(need1, [2,4,6,8])
print(result2)