# 291. 내가 한 답
f = open("C:/Users/nam/desktop/매수종목1.txt", "w")
f.write("005930\n")
f.write("005380\n")
f.write("035420\n")
f.close()

# 291.답안
f = open("C:/Users/nam/desktop/매수종목1.txt", mode = "wt", encoding = "utf-8")
f.write("005930\n")
f.write("005380\n")
f.write("035420\n")
f.close()

# 292
f = open("C:/Users/nam/desktop/매수종목2.txt", mode = "wt", encoding = "utf-8")
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER\n")
f.close()

# 293. csv 파일 작성법 모름! 확인하기!
import csv

f = open("C:/Users/nam/desktop/매수종목.csv", "wt", encoding = "cp949", newline = "") # newline = "" 으로 설정하면 새로운 라인이 없어짐. 즉  \n이 제거됨. csv엔 \n 이 자동으로 저장되어 있어서 설정해주어야함.

writer = csv.writer(f)
writer.writerow(["종목명","종목코드","PER"]) # writerow() : 리스트를 인수로 두면 그 해당 값을 셀에 저장한다.
writer.writerow(["삼성전자","005930",15.79])
writer.writerow(["NAVER","035420",55.82])

f.close()

# 294. 내가 짠 코드. 공백 제거 안되었음.
list = []
f = open("C:/Users/nam/desktop/매수종목1.txt", "r")
for i in f.readlines():
    print(i)
f.close()

# 294 답안 코드
f = open("C:/Users/nam/desktop/매수종목1.txt", "r", encoding = "utf-8")
lines = f.readlines()
# print(lines, type(lines))

list = []
for line in lines:
    code = line.strip() # strip()은 문자열에서 사용 가능. 리스트에서 불가능.
    list.append(code)

print(list)

f.close()

# 295. dict 저장법 모르겠음 확인!
f = open("C:/Users/nam/desktop/매수종목2.txt", "r", encoding = "utf-8")
lines = f.readlines()

data = {}
for line in lines:
    line = line.strip() # 공백제거
    k, v = line.split() # split() : 인자를 아무것도 작성 안하면 공백을 기준으로 한다는 뜻.
    # print(k, v)
    data[k] = v # 딕셔너리 값 추가!!! index를 주고 value를 주면 값 출력됨.
print(data)

f.close()

# 296. 다시 체크하기. try 위치 확인.
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)

# 297. 내가 짠 코드.
per = ["10.31", "", "8.00"]
list = []

for i in per:
    try:
        list.append(float(i))
    except:
        pass

print(list)

# 297. 답안 코드
per = ["10.31", "", "8.00"]
list = []

for i in per:
    try:
        v = float(i)
    except:
        v = 0
    list.append(v)

print(list)

# 298
try:
    a = 2/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

# 299. 내가 짠 코드. 반복문 밖에서 실행하는 게 아님.
data = [1, 2, 3]

try:
    for i in range(5):
        print(data[i])
except IndexError as e:
    print(e)

# 299. 답안 코드
data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print("e")

# 300.
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료.")
