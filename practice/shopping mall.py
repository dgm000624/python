# 상품명 : 재고 및 속성
sell_list = {"chicken" : [3, "meat"], "cola" : [10, "beverage"], "pizza" : [2, "fast_food"]}

boundary = list()

chickens = 0
colas = 0
pizzas = 0
while 1:
    print(f"남은 재고  치킨 : {sell_list.get("chicken")[0] - boundary.count(1)} "
          f"콜라 : {sell_list.get("cola")[0] - boundary.count(2)} "
          f"피자 : {sell_list.get("pizza")[0] - boundary.count(3)}")
    print("무엇을 구매하시겠습니까.\n 1. 치킨, 2. 콜라, 3. 피자, 0. 구매확정")
    num = int(input())

    if num ==1:
        if sell_list.get("chicken")[0] == boundary.count(1) :
            print("추가 구매 불가")
            continue
        boundary.append(1)
    elif num==2:
        if sell_list.get("cola")[0] == boundary.count(2) :
            print("추가 구매 불가")
            continue
        boundary.append(2)
    elif num==3:
        if sell_list.get("pizza")[0] == boundary.count(3) :
            print("추가 구매 불가")
            continue
        boundary.append(3)
    elif num==0:
        chickens = boundary.count(1)
        colas = boundary.count(2)
        pizzas = boundary.count(3)
        print(f"치킨 {chickens}개와 콜라 {colas}개와 피자 {pizzas}개를 구매했습니다")
        sell_list["chicken"] = [sell_list.get("chicken")[0] - boundary.count(1),sell_list.get("chicken")[1]]
        sell_list["cola"] = [sell_list.get("cola")[0] - boundary.count(2), sell_list.get("cola")[1]]
        sell_list["pizza"] = [sell_list.get("pizza")[0] - boundary.count(3), sell_list.get("pizza")[1]]

        print(f"남은 재고  치킨 : {sell_list.get("chicken")[0]} "
              f"콜라 : {sell_list.get("cola")[0]} "
              f"피자 : {sell_list.get("pizza")[0]}")

        break



    else :
        print("해당하는 상품이 없습니다.")