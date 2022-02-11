# 71
my_varible = ()
print(type(my_varible))

# 72
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

# 73. 개념 체크!
num1 = (1)
print(type(num1), num1)
# 튜플 안에 숫자 하나만 넣는 경우 int로 인식함.
num2 = (1, )
print(type(num2), num2)
#  데이터 하나만 입력할 때 int가 아닌 tuple로 인식하려면, (1, ) 처럼 안에 쉼표를 넣어줘야 함.

# 74
# 튜플은 데이터 변환을 할 수 없음.

# 75
# t = 1, 2, 3, 4 형태는 튜플 형태로 값이 저장된다.

# 76. 체크!!!!!!
t = ('a', 'b', 'c')
t = ('A', 'b', 'c') 
print(t)

# 77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(interest)
# 오답. 튜플에서 리스트로 "데이터 타입 변환"은 가능하다.

# 77 답
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest)

# 78
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(interest)

# 79
# apple, banana, cake 출력

# 80
print(tuple(range(2,100,2)))
