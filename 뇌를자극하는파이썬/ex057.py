class Student:
    count = 0
    def __init__(self, name, korean = 0, math = 0, english = 0, science = 0):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count +=1
        print("{}번째 학생이 생성되었습니다".format(self.count))

    def countup(self):
        self.count +=1

Students = [
    Student("A1", 20, 40, 50,20),
    Student("A2", 30, 40),
    Student("A3", science = 30),
    Student("A4", 20, 40, 50,20),
    Student("A5", 30, 40),
    Student("A6", science = 30)
]

Students[0].korean = 100
Students[0].countup()


print("총 학생의 수는 {}입니다".format(Student.count))
print("총 학생의 수는 {}입니다".format(Students[0].acount))