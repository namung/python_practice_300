# 211
# "안녕"
# "Hi"

# 212
# 7
# 15

# 213
# 정의한 함수는 매개변수(argument) "문자열"이 정의되어 있는데, 함수를 호출할 때 그 인수(parameter)를 작성하지 않았기 때문에 error 발생

# 214
# "+" 연산자는 같은 type 끼리만 가능. str 과 int를 함께 사용하는 건 불가능.

# 215
def print_with_smile(x):
    print(str(x) + ":D")

# 216
print_with_smile("안녕하세요")

# 217
def print_upper_price(price):
    print(price * 1.3)

# 218
def print_sum(a,b):
    print(a+b)

# 219
def print_arithmetic_operation(a, b):
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} * {b} = {a*b}")
    print(f"{a} / {b} = {a/b}")

# 220. 내가 작성한 코드
def print_max(a, b, c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)

# 220. 답안 코드
def print_max(a, b, c):
    max_val = 0
    if a > max_val:
        max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    print(max_val)
