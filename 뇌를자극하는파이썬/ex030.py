numbers = [1,3,14,5,2]

iterator = reversed(numbers)
print(iterator)
print("첫번째 호출")
for number in iterator:
    print(number, end = " ")
print("\n두번째 호출")
for number in iterator:
    print(number, end = " ")

iterator2 = reversed(numbers)
print("\n세번째 호출")
for number in iterator2:
    print(number, end = " ")

