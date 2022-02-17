# 261
class Stock():
    pass

# 261. 답안
class Stock:
    pass
# 속성이 없음 -> "()"도 업음.

# 262
class Stock():
    def __init__(self, name, code):
        self.name = name
        self.code = code

삼성 = Stock("삼성전자", "005930")
print(삼성.name, 삼성.code)

# 263
class Stock():
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

a = Stock(None, None)
a.set_name("삼성전자")
print(a.name)

# 264
class Stock():
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

a = Stock(None, None)
a.set_code("005930")
print(a.code)

# 265
class Stock():
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code
    
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code

삼성 = Stock("삼성전자", "005930")
name = 삼성.get_name()
code = 삼성.get_code()
print(name, code)

# 266
class Stock():
    def __init__(self, name, code, per, pbr, dividend_yield):
        self.name = name
        self.code = code
        self.per = float(per)
        self.pbr = float(pbr)
        self.dividend_yield = float(dividend_yield)

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code
    
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code

# 267
class Stock():
    def __init__(self, name, code, per, pbr, dividend_yield):
        self.name = name
        self.code = code
        self.per = float(per)
        self.pbr = float(pbr)
        self.dividend_yield = float(dividend_yield)

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code
    
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code

a = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(a.dividend_yield)

# 268
class Stock():
    def __init__(self, name, code, per, pbr, dividend_yield):
        self.name = name
        self.code = code
        self.per = float(per)
        self.pbr = float(pbr)
        self.dividend_yield = float(dividend_yield)

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code
    
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = float(per)
    
    def set_pbr(self, pbr):
        self.pbr = float(pbr)

    def set_dividend_yield(self, dividend_yield):
        self.dividend_yield = float(dividend_yield)

# 269
class Stock():
    def __init__(self, name, code, per, pbr, dividend_yield):
        self.name = name
        self.code = code
        self.per = float(per)
        self.pbr = float(pbr)
        self.dividend_yield = float(dividend_yield)

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code
    
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = float(per)
    
    def set_pbr(self, pbr):
        self.pbr = float(pbr)

    def set_dividend_yield(self, dividend_yield):
        self.dividend_yield = float(dividend_yield)

samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
samsung.set_per(12.75)
print(samsung.per)

# 270. 리스트 만드는 법 유의해서 확인!!
class Stock():
    def __init__(self, name, code, per, pbr, dividend_yield):
        self.name = name
        self.code = code
        self.per = float(per)
        self.pbr = float(pbr)
        self.dividend_yield = float(dividend_yield)

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code
    
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = float(per)
    
    def set_pbr(self, pbr):
        self.pbr = float(pbr)

    def set_dividend_yield(self, dividend_yield):
        self.dividend_yield = float(dividend_yield)

삼성전자 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

a = []
a.append(삼성전자)
a.append(현대차)
a.append(LG전자)
# print(a, type(a))

for i in a:
    print(i.code, i.per)
