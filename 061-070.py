# 61
price = ['20180728', 100, 130, 140, 150, 160, 170]
price = price[1:]
print(price)

# 62
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 63
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

# 64 오답. 확인!!!
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 65
interest = ['삼성전자', 'LG전자', 'Naver']
print(f"{interest[0]} {interest[2]}")
# 난 문자열로 감쌌는데 리스트 안의 값을 꺼낼 때는 굳이 문자열로 안 감싸도 됨.
# 답은 print(interest[0], interest[2])

# 66. join() 메서드. 모름!!!!!!
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
result = ' '.join(interest)
print(result)
# ' '.join(list) : 리스트의 각 요소를 문자열로 붙여줌. 앞에 공백을 두고 합쳐라는 뜻.

# 67. 
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
result = "/".join(interest)
print(result)

# 68. 
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
result = "\n".join(interest)
print(result)

# 69
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

# # 70
# data = [2, 4, 3, 1, 5, 10, 9]
# data = data.sort()
# print(data)

# 오답!!!! data.sort()는 바인딩 불가능. 원본 데이터 그대로 변경함. 바인딩하려면 data2 = sorted(data) 방법을 사용해야함.

# 70 답
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

# 70 답2
data = [2, 4, 3, 1, 5, 10, 9]
data2 = sorted(data)
print(data2)
