import sys

print(sys.argv)

sum = 0
for i in sys.argv[1:] :
    print(i)
    sum +=int(i)

print(sum)