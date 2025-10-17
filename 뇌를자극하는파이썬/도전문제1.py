dictionary = dict()
numbers = [1,2,3,4,1,2,3,1,4,1,2,3]
for number in numbers :
    dictionary[number] = numbers.count(number)

print(f"사용된 숫자의 종류는 {len(dictionary.keys())}")
print(f"참고 : {dictionary}")