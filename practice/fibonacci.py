def fibonacchi(n):
    if n < 0 : return "error"

    if n ==1 : return 1
    if n == 0 : return 0

    return fibonacchi(n-1) + fibonacchi(n-2)

print(fibonacchi(5))