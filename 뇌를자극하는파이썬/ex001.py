import random
from time import sleep


def censor(a:int,b):
    if a > b:
        return a
    else:
        return b

a, b= 10, 20

c = 10 + 30j

a, b = b, a
k = random.randint(0, 100)

print(c.real)
print(c.imag)
t = random.randrange(5,10)
print(censor(a,k))

while 1:
    print(t)
    t = random.randrange(5, 10)
    sleep(1)