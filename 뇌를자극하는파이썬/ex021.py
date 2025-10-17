import random

for _ in range(6):
    random.shuffle(balls)
    choice_balls.append(balls.pop())

print(choice_balls)
choice_balls.sort()
print(choice_balls)