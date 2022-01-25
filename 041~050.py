# 41
ticker = "btc_krw"
capital_ticker = ticker.upper()
print(capital_ticker)

# 42
ticker = "BTC_KRW"
small_letter_ticker = ticker.lower()
print(small_letter_ticker)

# 43
a = "hello"
A = a.capitalize()
print(A)

# 44. endswith() 모름!!!!!!!!
file_name = "보고서.xlsx"
check = file_name.endswith("xlsx")
print(check)
# string.endswith(value, start, end) : 문자열이 지정 문자열로 끝나는지를 체크. value 필수값, start(선택) 검색 시작 위치, end(선택) 검색 종료 위치

# 45. endswith() 모름!!!!! 공부!!
file_name = "보고서.xlsx"
check = file_name.endswith(("xlsx", "xls"))
print(check)
# 파일이름이 "xlsx" or "xls" 확인할 때 튜플로 감싸줘야함.

# 46. startswith
file_name = "2020_보고서.xlsx"
check = file_name.startswith("2020")
print(check)

# 47. split
a = "hello world"
b = a.split(" ")
print(b)
# 답은 a.split(). 괄호 안을 공백으로 두면, 공백을 기준으로 나눔.

# 48. 
ticker = "btc_krw"
s = ticker.split("_")
print(s)

# 49
date = "2020-05-01"
a = date.split("-")
print(a)
year = a[0]
month = a[1]
day = a[2]
print(f"연도: {year}, 월: {month}, 일: {day}")

# 50
data = "039490     "
a = data.rstrip()
print(a)
