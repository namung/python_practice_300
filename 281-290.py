# 281
class 차():
    def __init__(self, wheel, price):
        self.바퀴 = wheel
        self.가격 = price

car = 차(2, 1000)
print(car.바퀴)
print(car.가격)

# 282
class 차():
    def __init__(self, wheel, price):
        self.바퀴 = wheel
        self.가격 = price

class 자전차(차):
    pass

# 283
class 차():
    def __init__(self, wheel, price):
        self.바퀴 = wheel
        self.가격 = price

class 자전차(차):
    def __init__(self, wheel, price):
        self.바퀴 = wheel
        self.가격 = price

bicycle = 자전차(2, 100)
print(bicycle.가격)

# 284
class 차():
    def __init__(self, wheel, price):
        self.바퀴 = wheel
        self.가격 = price

class 자전차(차):
    def __init__(self, wheel, price, drivetrain):
        # super().__init__(wheel, price) # 파이썬에선 부모클래스를 가져오는 걸 "super()"라고 해준다. 그리고 생성자 안에 3개의 인자를 자동으로 가져온다. 그래서 굳이 self는 적어주지 않아도 된다.
        차.__init__(self, wheel, price) # "차" 클래스 생성자에게 넘겨준다. 무엇을? 자전차 클래스의 인스턴스, 즉 self를. 그래서 self 작성이 필요하다. 보통은 super() 권장.
        self.구동계 = drivetrain

bicycle = 자전차(2, 100, "시마노")
print(bicycle.구동계)
print(bicycle.바퀴)

# 285
class 차():
    def __init__(self, wheel, price):
        self.바퀴 = wheel
        self.가격 = price

class 자동차(차):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)
    
    def 정보(self):
        print(f"바퀴수 {self.바퀴}")
        print(f"바퀴수 {self.가격}")

car = 자동차(4, 1000)
car.정보()

# 286
class 차():
    def __init__(self, wheel, price):
        self.바퀴 = wheel
        self.가격 = price
    
    def 정보(self):
        print(f"바퀴수 {self.바퀴}")
        print(f"바퀴수 {self.가격}")

class 자동차(차):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)

class 자전차(차):
    def __init__(self, wheel, price, drivetrain):
        super().__init__(wheel, price)
        self.구동계 = drivetrain

bicycle = 자전차(2, 100, "시마노")
bicycle.정보()

# 287
class 차():
    def __init__(self, wheel, price):
        self.바퀴 = wheel
        self.가격 = price
    
    def 정보(self):
        print(f"바퀴수 {self.바퀴}")
        print(f"바퀴수 {self.가격}")

class 자동차(차):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)

class 자전차(차):
    def __init__(self, wheel, price, drivetrain):
        super().__init__(wheel, price)
        self.구동계 = drivetrain
    
    def 정보(self):
        super().정보() # super() 는 self 명시 안함! 자동으로 넘어감.
        print(f"구동계 {self.구동계}")

bicycle = 자전차(2, 100, "시마노")
bicycle.정보()

# 288
# 자식호출

# 289
# 자식생성

# 290
# 자식생성
# 부모생성
