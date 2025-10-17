# r = input("반지름의 길이 : ")
# if r.isdigit() :
#     r = int(r)
#     area = 3.141592 * r ** 2
#     print("넓이는 ", area)
# else :
#     print("숫자를 넣어주세요")

try:
    r = int(input("반지름의 길이 : "))
    area = 3.141592 * r ** 2
    print("넓이는 ", area)

except:
    print("숫자만 입력")
