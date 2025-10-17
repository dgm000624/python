import datetime

num = datetime.datetime.now().month

if( 3<= num <=5) : print("봄")
elif( 6<= num <=8) : print("여름")
elif( 9<= num <=11) : print("가을")
else : print("겨울")