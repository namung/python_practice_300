# 231
# 정의된 result가 없다고 나옴.

# 232
def make_url(a):
    return "www."+a+".com"

a = make_url("naver")
print(a)

# 233
def make_list(string):
    list = []
    for i in string:
        list.append(i)
    return list

a = make_list("abcd")
print(a)

# 234
def pickup_even(num_list):
    result_list = []
    for i in num_list:
        if i % 2 == 0:
            result_list.append(i)
    return result_list

a = pickup_even([3, 4, 5, 6, 7, 8])
print(a)

# 235
def convert_int(num_string):
    num_string = int(num_string.replace(",",""))
    return num_string

a = convert_int("1,234,567")
print(a)

# 236
# 22

# 237
# 22

# 238
# 140

# 239
# 16

# 240
# 28
