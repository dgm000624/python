def mul(*values):
    total = 1
    for i in values :
        total *=i

    return total


print(mul(5,7,9,10))




def f1(x) :
    return x
def f2(x) :
    return 2*x +1
def f3(x) :
    return x**2 + 2*x + 1

print(f1(5))
print(f2(5))
print(f3(5))
