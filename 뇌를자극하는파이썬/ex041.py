def test():
    print("함수 호출")
    yield "TEST"

print("A 통과")
print(test())
print("B 통과")
print(test())