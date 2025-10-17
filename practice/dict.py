ex_list = ["요소A", "요소B","요소C"]

print("# 단순 출력")
print(ex_list)
print()

print("# enumerate() 함수 적용 출력")
print(enumerate(ex_list))
print()

print("# list() 함수로 강제 변환 출력")
print(list(enumerate(ex_list)))
print()

print("# 반복문과 조합하기")
for i, value in enumerate(ex_list):
    print("{}번째 요소는 {}입니다.".format(i,value))