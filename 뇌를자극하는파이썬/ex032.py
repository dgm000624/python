def print3_times() -> None:
    for _ in range(3) :
        print("안녕하세요")
    return

print3_times()

def print_n_times(value="None", n:int = 1):
    for _ in range(n):
        print(value, end="")

print_n_times("안녕", 2)
print_n_times(n=5, value="tlqk")
print_n_times()