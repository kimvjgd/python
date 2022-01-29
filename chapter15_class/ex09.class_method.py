# 클래스 메드

# 멤버변수나 메서드는 항상 인스턴스가 필요했다.
# 인스턴스 참조.xxx(self)

# 클래스 메서드
# 일반적으로 메서드는 인턴스 메서드

# 클래스 메서드는 인스턴스와 무관하게 존재
# 인스턴스 없이도 클래스명을 통해 접근 가능
# 첫 번째 인자는 클래스에 대한 참조
# @ classmethod로 정의 <- 데코레이터


# 클래스 멤버변수
# class 안에서 self와 무관하게 정의되는 멤버변수
# 인스턴스와 무관하게 존재하며 모든 인스턴스가 공유하는 정보




# class Car:
#     count = 0
    
#     def __init__(self, name) -> None:
#         self.name = name
#         Car.count += 1
        
#     @classmethod
#     def outcount(cls):          # cls 는 클래스의 약자
#         print(cls.count)
        
# pride = Car('프라이드')
# korando = Car('코란도')
# Car.outcount()






# 정적 메서드
# 클래스 내에 정의된 일반 함수  - 메서드가 아니다
# 메서드의 첫번째 인자는 인스턴스에 대한 참조 = self
# 메서드와 비슷한 성격으로 함수를 묶어서 관리하는 역할

# class Car:
#     @staticmethod
#     def hello():
#         print('hihi')
#     count = 0
    
#     def __init__(self, name) -> None:
#         self.name = name
#         Car.count += 1
        
#     @classmethod
#     def outcount(cls):
#         print(cls.count)
        
# Car.hello()
# aaa = Car('aa')
# aaa.hello()



# 연산자 메서드
# == : __eq__
# != : __ne__
# 등등등등 너무 많아서 다 못적었다.

# ex
# h1 = H()
# h2 = H()
# 이럴떄 h1과 h2는 다르다(참조 값이 다르다)


# class Human:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
        
#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age

# kim = Human('김상형', 29)
# sang = Human('김상형', 29)
# moon = Human('문종민', 44)
# print(kim == sang)
# print(kim == moon)



