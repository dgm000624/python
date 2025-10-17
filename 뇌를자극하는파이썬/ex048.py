list_number = [52,273,32,72,100]

try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소 : {}".format(number_input, list_number[number_input]))
except ValueError as exception :
    print("정수를 입력하세요")
except IndexError as exception :
    print("리스트 인덱스 벗어남")
