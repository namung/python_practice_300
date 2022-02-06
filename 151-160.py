# 151
리스트 = [3, -20, -3, 44]
for i in 리스트:
    if i < 0:
        print(i)

# 152
리스트 = [3, 100, 23, 44]
for i in 리스트:
    if i % 3 == 0:
        print(i)

# 153
리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
    if (i < 20) and (i % 3 == 0):
        print(i)
        
# 154
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
    if len(i) >= 3:
        print(i)
        
# 155
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
    if 변수.isupper():
        print(변수)
        
# 156
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
    if 변수.islower():
        print(변수)

# 157
리스트 = ['dog', 'cat', 'parrot']
for a in 리스트:
    A = a[0].upper()
    print(A + a[1:])
    
# 158
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']

for i in 리스트:
    print(i.split(".")[0])
    
# 159
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    if i.split(".")[1] == "h":
        print(i)
        
# 160
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    스플릿 = i.split(".")[1]
    if (스플릿 == "h") or (스플릿 == "c"):
        print(i)
