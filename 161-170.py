# # 161
# for i in range(0,100):
#     print(i)
    
# # 162
# for i in range(2002,2051,4):
#     print(i)

# # 163
# for i in range(1,31):
#     if i % 3 == 0:
#         print(i)
        
# # 163. 답안
# for i in range(3,31,3):
#     print(i)
    
# # 164
# for i in range(0,100,-1):
#     print(i)
    
# 165. 모르겠당 확인!
for i in range(1,10):
    print(i/10)

# 166
for i in range(1,10):
    print(f"3 x {i} = {3*i}")
    
# 167
for i in range(1,10):
    if i % 3 == 0:
        print(f"3 x {i} = {3*i}")

# 168
result = 0
for i in range(1,11):
    result += i
print(result)

# 169
result = 0
for i in range(1,11):
    if i % 2 == 1:
        result += i
print(result)

# 169. 답안 코드
result = 0
for i in range(1,11,2):
    result += i
print(result)

# 170
result = 1
for i in range(1,11):
    result *= i
print(result)
