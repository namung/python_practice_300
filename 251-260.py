# 251
# 클래스 : 빵의 틀 같은 것. 객체나 인스턴스의 설계도
# 객체 : 클래서로 생성된 것. "빵"이라는 결과물.
# 인스턴스 : 클래스와 객체의 관계성을 나타낼 때 사용. "a 객체는 b클래스의 인스턴스이다."

# # 252
# class Human():
#     pass

# # 253
# class Human():
#     pass

# areum = Human()

# # 254
# class Human():
#     def __init__(self):
#         print("응애응애")

# areum = Human()

# # 255
# class Human():
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human("아름", 25, "여자")

# # 256
# print(f"이름: {areum.name}, 나이: {areum.age}, 성별: {areum.sex}")

# # 257. 메서드 안에 self 꼭 들어가야함.
# class Human():
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
    
#     def who(self):
#         print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.sex}")

# areum = Human("아름", 25, "여자")
# areum.who()

# 258
class Human():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.sex}")

    def setinfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")
areum.setinfo("현진", 24, "여자")
areum.who()

# 259. 소멸자가 뭐지?? 공부하자.
class Human():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.sex}")

    def setinfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def __del__(self):
        print("나의 죽음을 적에게 알리지 말라")

areum = Human("아름", 25, "여자")
del areum

# 260
# 클래스는 기본적으로 매개변수 self가 있어야한다. self = 클래스 본인을 가리키는 것. self가 지정되지 않으면 오류가 발생한다.
# 위 해설 정확하지 x. 아래 답변을 참고하자.

# 260. 답안
class OMG : 
    def print() :
        print("Oh my god")

myStock = OMG()
myStock.print()     # OMF.print(myStock). 클래스 OMG의 메소드 print()에는 인자가 정의되지 않았는데 인자가 넘어가니 오류가 발생한 것.
# 자동으로 객체가 self로 넘어감.
