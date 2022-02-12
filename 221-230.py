# 221
def print_reverse(a):
    a = a[::-1]
    print(a)

print_reverse("python")

# 222 내가 작성한 코드
def print_score(score):
    sum = 0
    for i in score:
        sum += i
    print(sum/len(score))

print_score([1,2,3])

# 222 답안코드
# list 형태는 sum() 사용 가능함.
def print_score(score):
    print(sum(score)/len(score))

print_score([1,2,3])

# 223
def print_even(args):
    for i in args:
        if i % 2 == 0:
            print(i)

print_even ([1, 3, 2, 10, 12, 11, 15])

# 224. 내가 한 답안. 하나씩 꺼내는 걸 수행x. 확인하기!!
def print_keys(args):
    keys = list(args.keys())
    print(keys)

print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# 224. 답안코드
def print_keys(args):
    for key in args.keys():
        print(key)

print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# 225
my_dict = {"10/26" : [100, 130, 100, 100],
            "10/27" : [10, 12, 10, 11]}

def print_value_by_key(dict, key):
    print(dict[key])

print_value_by_key(my_dict, "10/26")

# 226. 내가 짠 코드. 그냥 앞 뒤로 숫자 5 기준으로 한 번씩만 나눔. 잘 모르겠다. 답안코드 확인!
def print_5xn(string):
    print(string[:5] + "\n" + string[5:])

print_5xn("아이엠어보이유알어걸")

# 226. 답안코드. 어렵다. 해설코드도 같이 확인!!
def print_5xn(line):
    chunk_num = int(len(line)/5)
    for x in range(chunk_num+1):
        print(line[x*5: x*5+5]) # 남은 단어까지만 가져옴.

# 227
def print_mxn(string, num):
    times = int(len(string) / num) + 1 # +1 은 나머지까지 챙기기 위해서.
    for i in range(times):
        print(string[num * i : num * i + 3])    

print_mxn("아이엠어보이유알어걸", 3)

# 228
def calc_monthly_salary(annual_salary):
    monthly_salary = int(annual_salary / 12)
    print(monthly_salary)

calc_monthly_salary(12000000)

# 229
# 왼쪽: 100
# 오른쪽: 200

# 230
# 왼쪽: 200
# 오른쪽: 100
