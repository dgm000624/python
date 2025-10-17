num = input("숫자 입력하쇼")

if int(num) == 0: print("0은 ?")
elif int (num) < 0: print("음수는 x")

num = num[-1]

if int(num) % 2: print("홀수")
elif (int(num) + 1)%2: print("짝수")
else : print("오류")