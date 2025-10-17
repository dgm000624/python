def print_all(*values, n = 2) :
    for _ in range(n):
        for arg in values:
            print(arg)

print_all(1,True,"Avc","32")
