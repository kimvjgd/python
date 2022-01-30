# 액세스 Access - 멤버변수 접근 (r/w)
# 파이썬은 기본적으로 정보 은폐 기능 지원하지 않음
# def Human(age, name):
#     pass

# kim = Human(29, '김동현')
# kim.name = '정우성'
# kim.age = 46
# ㄴ이러면 전역변수처럼 사용하는 것이라 외부에서 변경되어도 어딘지 찾기 힘들다.

class Date:
    def __init__(self, month):
        self.inner_month = month
        self.__month = month
        
    # 방법 1
    @property                               # 데코레이터                                    # getter 함수 (불러올 때 호출되는 함수)
    def month(self):                        # property는 변수처럼 사용 가능하다!!
        return self.inner_month
    
    @month.setter                           # month라는 것 setting하는 것이다.                # setter 함수 (대입할 때 호출되는 함수)
    def month(self, month):
        if 1 <= month <= 12:                # 15는 조건에 안맞아서 업데이트가 안된다.
            self.inner_month = month
            
############################################################################################################################            
    # property 만드는 번거로움을 없애기 위해
    # 방법 2
    def getmonth(self):
        return self.__month
    
    def setmonth(self, month):
        if 1 <= month <= 12:
            self.__month = month
            
    month = property(getmonth, setmonth)

# 방법 1
today = Date(8)         # __init__
today.month = 15        # @month.setter로 가서 15를 전달
print(today.month)

# 방법 2
today.month = 11        # 얘로 하면 11로 업데이트 된다.
print(today.month)



tomorrow = Date(3)
tomorrow.month = 15

print(tomorrow.month)
# print(tomorrow.__month)   # 예외 발생 -> 프라이빗 멤버 변수 - 멤버 변수 앞에 __을 붙이면 외부에서 바로 접근 불가