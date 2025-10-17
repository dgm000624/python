import random

def mk_lotto() :
    lotto = set()

    while len(lotto) <=5:
        num = random.randint(1,45)
        lotto.add(num)

    return lotto

def sort_lotto(lotto) :
    lotto = list(lotto)
    lotto = sorted(lotto)
    return lotto

def buy_lotto(num, result_lotto) :
    for i in range(0, num) :
        lotto = sort_lotto(mk_lotto())
        cp = compare_lotto(lotto, result_lotto)
        print(f"{lotto}\t 맞은 갯수 : {cp}")

def compare_lotto(lotto, result_lotto) :
    lotto = set(lotto)
    cp = lotto & result_lotto
    return len(cp)


a = sort_lotto(mk_lotto())
a = set(a)
bonus = 0
while len(a)==6 :
    bonus = random.randint(0,45)
    a.add(bonus)

a.remove(bonus)

print(f"이번 주의 로또 숫자 : {sort_lotto(a)} , 이번 주의 보너스 숫자 : {bonus}")

a.add(bonus)

buy_lotto(100, a)