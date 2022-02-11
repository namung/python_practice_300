# 171. 모르겠다 확인!!
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])
    
# 172
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(i, price_list[i])

# 172 답안코드
for i, data in enumerate(price_list):
    print(i, data)
# enumerate() : 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환

# 173. 모르겠다 확인!!
for i in range(len(price_list)):
    print((len(price_list) -1) - i, price_list[i])
# 전체 리스트 길이에서 1을 뺀 값에서 시작하는 인덱스(i = 0부터!)을 빼면 리스트의 마지막 인덱스를 나타냄을 이용.

# 174. 모르겠다 확인!
for i in range(1,4):
    print(90 + 10 * i, price_list[i])
    
# 175
my_list = ["가", "나", "다", "라"]
for i in range(4):
    if 0 <= i < 3: 
        print(my_list[i], my_list[i+1])
    else:
        pass

# 175 답안 코드
for i in range(len(my_list)-1):
    print(my_list[i], my_list[i+1])
    
# 176
my_list = ["가", "나", "다", "라", "마"]
for i in range(len(my_list)-2):
    print(my_list[i], my_list[i+1], my_list[i+2])
    
# 177
my_list = ["가", "나", "다", "라"]

for i in range(len(my_list) - 1):
    print(my_list[len(my_list) - 1 - i], my_list[len(my_list) - 2 - i])

# 178
my_list = [100, 200, 400, 800]
for i in range(len(my_list) - 1):
    print(my_list[i+1] - my_list[i])

# 179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(len(my_list) - 2):
    result = (my_list[i]+my_list[i+1]+my_list[i+2])/(len(my_list) - 3)
    print(result)
# abs() : 절대값 함수

# 179 답안
for i in range(1, len(my_list) - 1): # 1, 2, 3, 4
    print(abs(my_list[i-1] + my_list[i] + my_list[i+1]) / 3 )

# 180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)):
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)
