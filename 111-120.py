# 111
a = input()
print(a*2)
    
# 112
num = input("숫자를 입력하세요: ")
print(int(num)+10)

# 113
num = input()
if int(num) % 2 == 0:
    print("짝수")
else:
    print("홀수")
    
# 114
num = input()
if int(num) <= 255:
    print(int(num) + 20)
else:
    print(255)
    
# 115
num = input("값을 입력하세요:")
result = int(num) - 20
if result < 0:
    print(0)
elif result > 255:
    print(255)
else:
    print(result)
    
# 116
time = input("현재 시각을 입력하세요: ")
time_split = time.split(":")
sharp = time_split[1]
if sharp[0] and sharp[1] == str(0): 
    print("정각입니다.")
else:
    print("정각이 아닙니다.")
    
# 116. 답
# 입력받은 값에서 마지막 2개의 값만 가져오면 됨. time[-2:] == "00"을 쓰면 코드가 더 간단해짐.

# 117
user = input("과일을 하나 입력하세요: ")
fruit = ["사과", "포도", "홍시"]
if user in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")
    
# 118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user = input("투자 종목을 하나 입력하세요. 위험 종목이면 알려드립니다.\n")
if user in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")
    
# 119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
season = list(fruit.keys())
user = input("좋아하는 계절은: ")
if user in season:
    print("정답입니다.")
else:
    print("오답입니다.")
    
# 120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은? ")
if user in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")
