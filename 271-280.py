# 271. 모름. 랜덤하게 숫자형성 random()을 사용하는 것 같은데 어떻게?. 확인하자.
import random

class Account():
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3) # '000'
        num2 = str(num2).zfill(2) # '00'
        num3 = str(num3).zfill(6) # '000000'
        self.account_number = num1 + "-" + num2 + "-" + num3

kim = Account("김민수", 100)
print(kim.account_holder, kim.balance, kim.bank, kim.account_number)

# 272. 모름. 생성된 계좌 계수 어떻게 저장? 확인하기.

import random

class Account():

    # class variable
    account_count = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3) # '000'
        num2 = str(num2).zfill(2) # '00'
        num3 = str(num3).zfill(6) # '000000'
        self.account_number = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1

kim = Account("김민수", 100)
print(Account.account_count)

lee = Account("이민수", 100)
print(Account.account_count)

# 273. 틀렸음 확인하기! 메서드가 객체인 self를 참조하는 것이 아니라 클래스를 참조해야함. 이 때 사용하는 게 "cls" 
import random

class Account():

    # class variable
    account_count = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3) # '000'
        num2 = str(num2).zfill(2) # '00'
        num3 = str(num3).zfill(6) # '000000'
        self.account_number = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1
    
    @classmethod # 클래스메서드 표기해줘야함.
    def get_account_number(cls):
        print(cls.account_count) # Account.account_count

kim = Account("김민수", 100)
lee = Account("이민수", 100)
kim.get_account_number() # 메서드에 kim 객체가 넘어가는 것이 아니라, cls = 클래스가 넘어간다.

# 274
import random

class Account():

    # class variable
    account_count = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3) # '000'
        num2 = str(num2).zfill(2) # '00'
        num3 = str(num3).zfill(6) # '000000'
        self.account_number = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1
    
    @classmethod # 클래스메서드 표기해줘야함.
    def get_account_number(cls):
        print(cls.account_count) # Account.account_count

    def deposit(self, cash):
        if cash >= 1:
            self.balance += cash

kim = Account("김민수", 100)
kim.deposit(1)
print(kim.balance)

# 275
import random

class Account():

    # class variable
    account_count = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3) # '000'
        num2 = str(num2).zfill(2) # '00'
        num3 = str(num3).zfill(6) # '000000'
        self.account_number = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1
    
    @classmethod # 클래스메서드 표기해줘야함.
    def get_account_number(cls):
        print(cls.account_count) # Account.account_count

    def deposit(self, cash):
        if cash >= 1:
            self.balance += cash

    def withdraw(self, cash):
        if cash <= self.balance:
            self.balance -= cash

kim = Account("김민수", 100)

kim.deposit(1)
print(kim.balance)
kim.withdraw(50)
print(kim.balance)

# 276
import random

class Account():

    # class variable
    account_count = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3) # '000'
        num2 = str(num2).zfill(2) # '00'
        num3 = str(num3).zfill(6) # '000000'
        self.account_number = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1
    
    @classmethod # 클래스메서드 표기해줘야함.
    def get_account_number(cls):
        print(cls.account_count) # Account.account_count

    def deposit(self, cash):
        if cash >= 1:
            self.balance += cash

    def withdraw(self, cash):
        if cash <= self.balance:
            self.balance -= cash

    def display_info(self):
        print(f"은행이름: {self.bank}")
        print(f"예금주: {self.account_holder}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔고: {self.balance}")

kim = Account("김민수", 1000)
kim.display_info()

# 277. 변수가 어디에 추가되어야 하는지 확인하기!!!
import random

class Account():

    # class variable
    account_count = 0

    def __init__(self, account_holder, balance):
        self.deposit_count = 0 # 객체가 생성될 때, count를 할 수 있는 변수가 있어야 함.

        self.account_holder = account_holder
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3) # '000'
        num2 = str(num2).zfill(2) # '00'
        num3 = str(num3).zfill(6) # '000000'
        self.account_number = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1
    
    @classmethod # 클래스메서드 표기해줘야함.
    def get_account_number(cls):
        print(cls.account_count) # Account.account_count

    def deposit(self, cash):
        if cash >= 1:
            self.balance += cash
            self.deposit_count += 1

        if self.deposit_count % 5 == 0:
            self.balance = int(self.balance) * 1.01
            print("입금횟수가 5회가 되어 이자가 추가되었습니다.")
            print(f"이자금 : {int(self.balance) * 0.01}, 현재 잔고 금액: {self.balance}")

    def withdraw(self, cash):
        if cash <= self.balance:
            self.balance -= cash

    def display_info(self):
        print(f"은행이름: {self.bank}")
        print(f"예금주: {self.account_holder}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔고: {self.balance}")

kim = Account("김민수", 1000)
kim.deposit(1000)
kim.deposit(1000)
kim.deposit(1000)
kim.deposit(1000)
kim.deposit(1000)

# 278
import random

class Account():

    # class variable
    account_count = 0

    def __init__(self, account_holder, balance):
        self.deposit_count = 0 # 객체가 생성될 때, count를 할 수 있는 변수가 있어야 함.

        self.account_holder = account_holder
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3) # '000'
        num2 = str(num2).zfill(2) # '00'
        num3 = str(num3).zfill(6) # '000000'
        self.account_number = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1
    
    @classmethod # 클래스메서드 표기해줘야함.
    def get_account_number(cls):
        print(cls.account_count) # Account.account_count

    def deposit(self, cash):
        if cash >= 1:
            self.balance += cash
            self.deposit_count += 1

        if self.deposit_count % 5 == 0:
            self.balance = int(self.balance) * 1.01
            print("입금횟수가 5회가 되어 이자가 추가되었습니다.")
            print(f"이자금 : {int(self.balance) * 0.01}, 현재 잔고 금액: {self.balance}")

    def withdraw(self, cash):
        if cash <= self.balance:
            self.balance -= cash

    def display_info(self):
        print(f"은행이름: {self.bank}")
        print(f"예금주: {self.account_holder}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔고: {self.balance}")

kim = Account("김민수", 100)
lee = Account("이민수", 200)
nam = Account("남민수", 300)

list = []
list.append(kim)
list.append(lee)
list.append(nam)

print(list)

# 279
import random

class Account():

    # class variable
    account_count = 0

    def __init__(self, account_holder, balance):
        self.deposit_count = 0 # 객체가 생성될 때, count를 할 수 있는 변수가 있어야 함.

        self.account_holder = account_holder
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3) # '000'
        num2 = str(num2).zfill(2) # '00'
        num3 = str(num3).zfill(6) # '000000'
        self.account_number = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1
    
    @classmethod # 클래스메서드 표기해줘야함.
    def get_account_number(cls):
        print(cls.account_count) # Account.account_count

    def deposit(self, cash):
        if cash >= 1:
            self.balance += cash
            self.deposit_count += 1

        if self.deposit_count % 5 == 0:
            self.balance = int(self.balance) * 1.01
            print("입금횟수가 5회가 되어 이자가 추가되었습니다.")
            print(f"이자금 : {int(self.balance) * 0.01}, 현재 잔고 금액: {self.balance}")

    def withdraw(self, cash):
        if cash <= self.balance:
            self.balance -= cash

    def display_info(self):
        print(f"은행이름: {self.bank}")
        print(f"예금주: {self.account_holder}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔고: {self.balance}")

kim = Account("김민수", 1000000)
lee = Account("이민수", 200)
nam = Account("남민수", 30000)

list = []
list.append(kim)
list.append(lee)
list.append(nam)

for i in list:
    if i.balance >= 1000000:
        i.display_info()

# 280. 모르겠다 확인!
import random

class Account():

    # class variable
    account_count = 0

    def __init__(self, account_holder, balance):
        self.deposit_count = 0 # 객체가 생성될 때, count를 할 수 있는 변수가 있어야 함.

        self.deposit_log = []
        self.withdraw_log = []

        self.account_holder = account_holder
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3) # '000'
        num2 = str(num2).zfill(2) # '00'
        num3 = str(num3).zfill(6) # '000000'
        self.account_number = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1
    
    @classmethod # 클래스메서드 표기해줘야함.
    def get_account_number(cls):
        print(cls.account_count) # Account.account_count

    def deposit(self, cash):
        if cash >= 1:
            self.deposit_log.append(cash)

            self.balance += cash
            self.deposit_count += 1

        if self.deposit_count % 5 == 0:
            self.balance = int(self.balance) * 1.01
            print("입금횟수가 5회가 되어 이자가 추가되었습니다.")
            print(f"이자금 : {int(self.balance) * 0.01}, 현재 잔고 금액: {self.balance}")

    def withdraw(self, cash):
        if cash <= self.balance:
            self.withdraw_log.append(cash)

            self.balance -= cash

    def display_info(self):
        print(f"은행이름: {self.bank}")
        print(f"예금주: {self.account_holder}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔고: {self.balance}")

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)

    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)
        
kim = Account("김민수", 1000)
kim.deposit(100)
kim.deposit(200)
kim.deposit(300)
kim.deposit_history()

kim.withdraw(300)
kim.withdraw(200)
kim.withdraw(100)
kim.withdraw_history()
