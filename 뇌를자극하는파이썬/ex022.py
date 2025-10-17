a = [1,2,3,4]

b = [*a , *a]
c = list()
c = a+a

c +=c

print(b)
print(c)

print(b==c)
print(a == c[0:4])