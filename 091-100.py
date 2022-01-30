# 91
inventory = {'메로나':[300, 20],
            '비비빅':[400, 3],
            '죠스바':[250, 100]}
print(inventory)

# 92
print(inventory['메로나'][0], "원")

# 93
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print(inventory['메로나'][1], "개")

# 94
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
inventory["월드콘"] = [500, 7]
print(inventory)

# 95
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(list(icecream.keys()))
           
# 96
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(list(icecream.values()))

# 97
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
price = list(icecream.values())
print(sum(price))

# 98. 모름!!!!  확인
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)
# 또다른 딕셔너리에 추가하는 메서드 : ".update()"

# 99. 모름!!! 확인
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
print(dict(zip(keys, vals)))
# zip() 함수는 두 개의 리스트 혹은 튜플을 쌍으로 묶어줌.


#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)
