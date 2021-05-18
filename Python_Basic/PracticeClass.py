#%%
# Default Class Form
class Calculator:
    pass

# %%
# Class Without __init__
class Calculator1:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
# %%
a = Calculator1()
# %%
a.setdata(6,3)
# %%
a.add()
# %%
# Calculator1에는 __init__ 메소드가 없으므로
# setdata를 호출하지 않고는 그 다음을 수행할 수 없다.
# 이 때 a = Calculator()의 괄호 안에 
# 바로 변수 지정해줄 수 있게 하는 도구가 __init__ 메소드 인듯하다.

# %%
# Class with __init__

class Calculator2:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def multi(self):
        result = self.first * self.second
        return result

# %%
a = Calculator2(3,4)
# %%
a.multi()
# 3 * 4
# %%
# 상속(Inheritance)

class MoreCalculator2(Calculator2):
    def power(self):
        result = self.first ** self.second
        return result
# %%
a = MoreCalculator2(2,4)
# %%
a.multi()
# 2 * 4
# %%
a.power()
# 2^4
# %%
