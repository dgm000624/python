Honggildong = {"이름" : "홍길동", "직업":"의적", "성별":"남성", "나이":"불명"}

print(Honggildong.items())

hong = list(Honggildong)

print(Honggildong.values())

print(Honggildong.get("이름"))

if "이름" in Honggildong :
    print("Right")

elif "이름" not in Honggildong :
    print("Left")