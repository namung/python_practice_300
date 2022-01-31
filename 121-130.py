# 121
user = input("영문자 하나를 입력하세요: ")
if user.islower():
    print(user.upper())
else:
    print(user.lower())
    
# 122
score = int(input("학점을 입력하세요: "))
if score >= 81:
    print("grade is A")
elif score >= 61:
    print("grade is B")
elif score >= 41:
    print("grade is C")
elif score >= 21:
    print("grade is D")
else:
    print("grade is E")
    
# 123
user = input("금액을 입력하세요: ")
user = user.split()
price = float(user[0])
currency = user[1]

print(f"입력: {price} {currency}")
if currency == "달러":
    print(price * 1167, currency)
elif currency == "엔":
    print(price * 1.096, currency)
elif currency == "유로":
    print(price * 1268, currency)
else:
    print(price * 171, currency)
    
# 123. 답 코드
# 위에서 내가 한 것도 정답이지만, 딕셔너리를 사용해 좀 더 코드를 간단하게 만들 수 있다.
환율 = {"달러":1167,
     "엔":1.096,
     "유로":1268,
     "위안":171}
user = input("금액을 입력하세요: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")

# 124
number1 = int(input("number1: "))
number2 = int(input("number2: "))
number3 = int(input("number3: "))
if number1 >= number2 >= number3 or number1 >= number3 >= number2:
    print(number1)
elif number2 >= number1 >= number3 or number2 >= number3 >= number1:
    print(number2)
else:
    print(number3)
    
# 125
tell = {"011":"SKT",
      "016":"KT",
      "019":"LGU",
      "010":"알수없음"}
user = input("휴대전화 번호 입력: ")
if user[:3] in tell:
    print("당신은", tell[user[:3]], "사용자입니다.")

# 126
zip_code ={}
for a in range(0,3):
    zip_code[a] = "강북구"
for a in range(3,6):
    zip_code[a] = "도봉구"
for a in range(6,10):
    zip_code[a] = "노원구"

user = input("우편번호: ")
user_gu = int(user[2])
if user_gu in zip_code:
    print(f"{zip_code[user_gu]}")
# 앞의 01 숫자도 포함해야 함.

# 126. 답안 방법
우편번호 = input("우편번호: ")
우편번호 = 우편번호[:3]
if 우편번호 in ["010", "011", "012"]:
    print("강북구")
elif 우편번호 in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")

# 127
user = input("주민등록번호: ")
user_split = user.split("-")
code = user_split[1][0]
if code == "1" or code == "3":
    print("남자")
else:
    print("여자")
    
# 128
user = input("주민등록번호: ")
user_code = user.split("-")
birth_code = user_code[1][1:3]
if birth_code in ["00","01","02","03","04","05","06","07","08"]:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")

# 129
user = input("주민등록번호: ")
user_split = user.split("-")
code1 = user_split[0]
code2 = user_split[1]
num = int(code1[0])*2 + int(code1[1])*3 + int(code1[2])*4\
+ int(code1[3])*5 + int(code1[4])*6 + int(code1[5])*7\
+ int(code2[0])*8 + int(code2[1])*9 + int(code2[2])*2\
+ int(code2[3])*3 + int(code2[4])*4 + int(code2[5])* 5
num2 = num % 11
lastnum = 11 - num2
if lastnum == int(code2[6]):
    print("유효한 주민번호입니다.")
else:
    print("유효하지 않은 주민번호입니다.")

# 130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
fluctuation = float(btc['max_price']) - float(btc['min_price'])
benchmark = float(btc['opening_price']) + fluctuation
if fluctuation > benchmark:
    print("상승장")
else:
    print("하락장")
