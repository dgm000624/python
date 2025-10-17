import datetime
import time

now_time = datetime.time()

print(now_time)

future_time = now_time
number = 0

while time.time() < future_time:
    number+=1

print(number)