# 181
apart = [["101호", "102호"],["201호", "202호"],["301호", "302호"]]

# 182
stock = [["시가", 100, 200, 300],["종가", 80, 210, 330]]

# 183
stock = {"시가":[100, 200, 300], "종가":[80, 210, 330]}

# 184
stock = {"10/10":[80, 110, 70, 90], "10/11":[210,230, 190, 200]}

# 185
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in range(len(apart)):
    print(apart[i][0], "호")
    print(apart[i][1], "호")

# 185 답안
for row in apart:
    for col in row:
        print(col, "호")

# 186 
apart = [ [101, 102], [201, 202], [301, 302] ]
apart = list(reversed(apart))
for reverse in apart:
    for i in list(reversed(reverse)):
        print(i, "호")

# 186 답안
for row in apart[::-1]:
    for col in row:
        print(col, "호")

# 187
for row in apart[::-1]:
    for col in row[::-1]:
        print(col, "호")

# 188
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
        print("-"*5)

# 189
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
    print("-"*5)

# 180
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
print("-"*5)
