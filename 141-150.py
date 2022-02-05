# 141
리스트 = [100, 200, 300]
for i in 리스트:
    print(i + 10)

# 142
리스트 = ["김밥", "라면", "튀김"]
for i in 리스트:
    print("오늘의 메뉴:", i)
    
# 143
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
    print(len(i))
    
# 144
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i, len(i))
    
# 145
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i[0])
    
# 146
리스트 = [1, 2, 3]
for i in 리스트:
    print("3 x", i)
    
# 147
리스트 = [1, 2, 3]
for i in 리스트:
    print("3 x", i,"=", 3*i)
    
# 148. 모르겠다 확인!
리스트 = ["가", "나", "다", "라"]
for i in 리스트[1:]:
    print(i)
    
# 149
리스트 = ["가", "나", "다", "라"]
가다 = 리스트[0] + 리스트[2]
for i in 가다:
    print(i)
    
# 149 답안. 증감폭 이용하기
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::2]:
    print(i)
    
# 150
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::-1]:
    print(i)
