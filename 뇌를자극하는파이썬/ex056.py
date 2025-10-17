class Student:
    def __init__(self, name, korean = 0, math = 0, english = 0, science = 0):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def print_subject(self):
        print(self.name + "의 국어 점수는 " + str(self.korean) + "이고 수학 점수는 " + str(self. math) +
              "이고 영어 점수는 " + str(self.english) + "이고 과학 점수는" + str(self.science) + "입니다.", end=" " )

    def __del__(self):
        print("파괴됨")

    def sum(self):
        return self.korean+self.math+self.science+self.english

    def average(self):
        return self.sum()/4

    @classmethod
    def print(cls):
        print(student)

Students = [
    Student("A1", 20, 40, 50,20),
    Student("A2", 30, 40),
    Student("A3", science = 30)
]

Students[0].korean = 100

for i in Students:
    i.print_subject()
    print("{} , {}".format(i.sum(), i.average()))
