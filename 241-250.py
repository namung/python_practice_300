# 241. 모름 확인!
import datetime

now = datetime.datetime.now()
print(now)

# 242
import datetime

now = datetime.datetime.now()
print(type(now))

# 243
from datetime import datetime, timedelta 

now = datetime.now()
for i in range(5,0,-1):
    delta = now - timedelta(i)
    print(f"오늘로부터 {i}일 전의 날짜: {delta}")

# 244. 모름 확인!
import datetime

now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))

# 245. 모름 확인!
import datetime

time = "2020-05-04"
time2 = datetime.datetime.strptime(time, "%Y-%m-%d")
print(time2, type(time2))

# 246
import datetime, time

while True:
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)

# 247. 확인하기!!
# 1. import os
# 2. from os import rename
# 4. from os import *
# 5. import os as myos (myos.함수()) <- 형태로 사용 가능

# 248
import os

print(os.getcwd())

# 249
import os

os.rename("새 파일.txt", "new file.txt")

# 250. 내가 한 코드
import numpy as np

a = np.arange(0.0,5.1,0.1) # numpy의 arange는 실수단위로 증가 가능하다.
print(a, type(a))

# 250. 답안 코드
import numpy as np

for i in np.arange(0,5.1,0.1):
    print(i)
