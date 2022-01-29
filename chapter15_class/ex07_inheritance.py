# 모든 클래스는 object 클래스의 자식이다.
# __str__ 나 __expr__ 같은 object의 메서드를 이용할 수 있다.


class Human:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def intro(self):
        print(str(self.age)+"살 " + self.name + "입니다.")
    
    def eat(self):                                         # 자식에 없어도 자식에서 호출 가능 -> 
        print('식사를 합니다.')
    
    def __str__(self):                                      # object의 __str__을 오버라이딩 한거다
        return f'Human(name={self.name}, age={self.age})'
    
class Student(Human):
    def __init__(self, name, age, stunum) -> None:
        super().__init__(name, age)                         # super은 부모 인스턴스 참조 (부모꺼를 수정해서 쓰고 싶을때 override시켜준다.)
        self.stunum = stunum
        
    def intro(self):
        super().intro()
        print("학번: " + str(self.stunum))
        
    def study(self):
        print('하늘천 따지 검을현 누를황')

# 선생님 : Teacher
# 데이터는: 이름, 나이
# 기능: 소개, 식사하기, 가르치기
class Teacher(Human):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
    def teach(self):
        print('가르치기')


kim = Human('김동현', 27)
kim.intro()
kim.eat()
print(kim)

lee = Student('이승우', 20, 200011)
lee.intro()
lee.study()
lee.eat()
print(lee)

park = Teacher('홍길동', 50)
park.intro()
park.eat()
park.teach()
print(park)

# park.study()

