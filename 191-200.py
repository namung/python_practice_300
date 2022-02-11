# 191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

for row in data:
    for col in row:
        print(col + (col * 0.00014))

# 191 답안
for row in data:
    for col in row:
        print(col * 1.00014)

# 192 
for row in data:
    for col in row:
        print(col * 1.00014)
    print("-"*4)

# 193
result = []
for row in data:
    for col in row:
        result.append(col * 1.00014)
print(result)

# 194. 모르겠다! 2차원 배열로 어떻게 저장하는지 확인
result = []
for row in data:
    sub = []
    for col in row:
        sub.append(col * 1.00014)
    result.append(sub)
print(result)

# 195. 반복문 어떻게 활용? 모르겠다 확인하기.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for row in ohlc[1:]:
    print(row[3])

# 196
for row in ohlc[1:]:
    if row[3] > 150:
        print(row[3])

# 197
for row in ohlc[1:]:
    if row[3] >= row[0]:
        print(row[3])

# 198
volatility = []
for row in ohlc[1:]:
    volatility.append(row[1]-row[2])
print(volatility)

# 199
for row in ohlc[1:]:
    if row[3] > row[0]:
        print(row[1]-row[2])

# 200
result = 0
for row in ohlc[1:]: 
    result += row[3]-row[0]
print(result)
