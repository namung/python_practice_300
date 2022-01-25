# 51
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

# 52
movie_rank.append("배트맨")
print(movie_rank)

# 53. insert() 모름!!!!
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)
# list.insert(인덱스, 원소) : 인덱스 위치에 원소 추가. 

# 54. del 모름!!
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)

# 55 오답.
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# del movie_rank[2][3]
# print(movie_rank)
# del을 이용하여 해당 인덱스의 값을 삭제할 수 있음. 원소에 직접 접근해 삭제 불가능. 즉, 순차적으로 새로 삭제해야함.

# 55 답.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# 56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2
print(langs)

# 57 오답. 활용법 체크.
# nums = [1, 2, 3, 4, 5, 6, 7]
# m = nums.max()
# n = nums.min()
# print("max:\t%d" % m)
# print("min:\t%d" % m)

# 57 답
nums = [1, 2, 3, 4, 5, 6, 7]
m = max(nums)
n = min(nums)
print("max:\t%d" % m)
print("min:\t%d" % n)

# 58 체크!!
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 60
nums = [1, 2, 3, 4, 5]
average = sum(nums) / len(nums)
print(average)
