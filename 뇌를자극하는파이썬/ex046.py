try :
    num = int(input("반지름 입력"))
except : print("숫자만 입력")
else : print(f"원의 넓이는 {3.14*num**2}")
finally : print("종료")