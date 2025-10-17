import random

with open("students.csv", 'w', encoding= 'cp949') as excel :
    list = list("가나다라마바사아자차카타파하")
    for i in range(0,99):
        excel.write(str(i) + "," + str(random.choice(list))+ str(random.choice(list))+"," + str(random.randint(10,20)) + "\n")

with open("students.csv", 'r', encoding='cp949') as file :
    for line in file :
        (line, name, age) = line.split(',')
        print(f'{int(line)+1}번째 학생의 이름은 {name}이고 나이는 {age}입니다\n')
        if not line or not name or not age :
            continue



