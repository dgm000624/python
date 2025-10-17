import random

def sort(lotto) :
    k = 0
    #check
    while 1:
        temp = set(lotto)
        if len(temp) == len(lotto):
            break
    #중복값 발생시 lotto에 값 재분배'
        else:
            index = 0
            while index < 6:
                lotto[index] = random.randint(1,num)
                index +=1

    lo = 0
    while k < len(lotto):
        min = 100
        i = k
        while i < len(lotto):
        #로또 리스트 내부 최솟값 찾기'
             if  lotto[i] < min:
                 min = lotto[i]
                 lo = i
             i +=1

        lotto[k], lotto[lo] = lotto[lo], lotto[k]

        k+=1
    return lotto

def mklotto(num) :
    a = [0,0,0,0,0,0]
    index = 0
    while index < 6:
        a[index] = random.randint(1,num)
        index +=1
    lotto = sort(a)
    return lotto

def cplotto(present, bundle) :
    all = present + bundle
    temp = set(all)
    cnt = len(all) - len(temp)
    return cnt

def print_result(present, bundle):
    cnt = 0

    print(f"이번 로또 번호는 {present} 입니다.\n")
    
    while cnt < len(bundle) :

        if cplotto(present, bundle[cnt]) == len(bundle[0]):
            print(f"축하합니다! {cnt+1}번째 로또의 당첨 숫자의 갯수는 {cplotto(present, bundle[cnt])}개 입니다.")
        else :
            print(f"{cnt+1}번째 로또의 당첨 숫자의 갯수는 {cplotto(present, bundle[cnt])}개 입니다.")
        cnt +=1

def sum_result(present, bundle):
    i = 0
    
    cp0, cp1, cp2, cp3, cp4, cp5, cp6 = 0,0,0,0,0,0,0
    
    while i < len(bundle):

        cnt = cplotto(present, bundle[i])

        if cnt == 0 :
            cp0 +=1

        elif cnt == 1 :
            cp1 +=1

        elif cnt == 2 :
            cp2 +=1
            
        elif cnt == 3 :
            cp3 +=1

        elif cnt == 4 :
            cp4 +=1

        elif cnt == 5 :
            cp5 +=1

        elif cnt == 6 :
            cp6 +=1

        else :
            
            print("오류 발생")

        i +=1
    dic = {0:cp0, 1:cp1, 2:cp2, 3:cp3, 4:cp4, 5:cp5, 6:cp6}

    return dic

def deter(text):
    
    while 1:
        if text == 'Y':
            break
        elif text == 'N':
            break
        else :
            print("Y 또는 N을 입력해주세요")
            text = input("")
            text = text.upper()

    return text

def isok(k):
    okay = 0
    while okay == 0:

        if k.isdigit():
            okay = 1
        
        else : 
            print("1이상의 숫자를 입력해주세요")
            k = input("")
    return k

def inrange(num, maxnum):
    okay = 0
    while okay == 0:

        if int(num) < maxnum :
            okay = 1
        
        else : 
            print("f{maxnum} 이하의 숫자를 입력해주세요")
            num = input("")
    return num

def selflotto(num, slotto, maxnum):
    for r in range(0, int(num)) :

        while 1:
            for t in range(0,6) :
                
                
                print(f"{r+1}번째 로또의 {t+1}번째 번호를 입력하세요.")
                cnt = input("")
                cnt = isok(cnt)
                cnt = inrange(cnt, maxnum)
                slotto[r][t] = int(cnt)

            if len(set(slotto[r])) < 6:
                print("같은 값은 2회 이상 사용 불가. 재입력해주세요.")
            else:
                break;
    for j in range (0, int(num)):
        slotto[j] = sort(slotto[j])        
    return slotto



# 여기서 부터 main 함수


print("로또를 몇장 구매하시겠습니까")
ltt = input("장수 입력\n")

#로또 번호 범위
num = 45

ltt = isok(ltt)
    
present = mklotto(num)

print("번호를 수기로 입력하시겠습니까? Y/N")
game = input("")
game = game.upper()
game = deter(game)

if game == 'Y':

    print("몇장을 수기로 입력하시겠습니까?")
    cnt1 = input("장수 입력\n")
    cnt1 = isok(cnt1)
        
    
elif game == 'N':
    print("모두 자동으로 입력합니다.\n")

cnt = 0
bundle = []

while cnt < int(ltt):
    bundle.append(mklotto(num))
    cnt +=1
    
cnt = 0
if game == 'Y':
    bundle = selflotto(cnt1, bundle, num) 

while cnt < len(bundle):
    print(f"{cnt+1}번째 로또 번호는{bundle[cnt]} 입니다.")
    cnt +=1

print("당첨 결과를 조회하시겠습니까? Y/N")
game0 = input("")
game0 = game0.upper()
game0 = deter(game0)
if game0 == 'Y':

    print("요약  결과를 조회하시겠습니까? Y/N")
    game2 = input("")
    game2 = game2.upper()
    game2 = deter(game2)
    
    if game2 == 'Y':
        dic = sum_result(present, bundle)
        print(f"0개 일치 : {dic[0]}, 1개 일치 : {dic[1]}, 2개 일치 : {dic[2]}, 3개 일치 : {dic[3]}, 4개 일치 : {dic[4]}, 5개 일치 : {dic[5]}, 6개 일치 : {dic[6]}")
        
        print("전체 결과를 조회하시겠습니까? Y/N")
        game3 = input("")
        game3 = game3.upper()
        game3 = deter(game3)
        if game3 == 'Y':

            print_result(present, bundle)
    
        elif game3 == 'N':
            print("종료")
        
    
    elif game2 == 'N':
        print_result(present, bundle)
    
elif game == 'N':
    print("종료")










    
    
