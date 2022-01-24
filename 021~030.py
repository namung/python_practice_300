# 21
letters = 'python'
print(letters[0],letters[2])

# 22
license_plate = "24가 2210"
print(license_plate[-4:])

# 23
string = "홀짝홀짝홀짝"
print(string[0]+string[2]+string[4])

# 23  답
print(string[::2]) # [시작인덱스:끝인덱스:오프셋(간격)

# 24 답. 체크.
string = "PYTHON"
print(string[::-1])

# 25 내가 한 것.
phone_number = "010-1111-2222"
print(phone_number.split("-")) # 오답! split은 한 list 안에 "-" 를 제외한 숫자를 "따로" 저장함.

# 25 답
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-"," ")
print(phone_number1)

# 26
phone_number2 = phone_number1.replace(" ", "")
print(phone_number2)

# 27
url = "http://sharebook.kr"
print(url[-2:])

# 27 답
url_split = url.split(".")
print(url_split[-1])

# 28. 문자열을 수정 불가능!. 할당할 수 없다.

# 29. 
string = 'abcdfe2a354a32a'
print(string.replace('a','A'))

# 30
# aBcd. 오답. 답은 abcd 그대로 유지.
# 문자열은 변경 불가능 -> replace 메서드는 원본을 그대로 둔 채 새로운 문자열 객체를 리턴함. 아무것도 바인딩 하지 않으면 메모리에서 사라짐. 문제에서는 아무것도 바인딩 하지 않음.
