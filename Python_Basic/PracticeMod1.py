# PracticeMod1.py

PI = 3.141592

class Calc:
    def circ(self, r):
        return PI * (r ** 2)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

## if __name__ == "__main__":
# C:\doit>python mod1.py처럼 직접 이 파일을 실행했을 때는 
# __name__ == "__main__"이 참이 되어 if문 다음 문장이 수행된다. 
# 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 
# __name__ == "__main__"이 거짓이 되어 if문 다음 문장이 수행되지 않는다

if __name__ == "__main__":
    print(add(1,4))
    print(sub(4,2))