# 데코레이터
# 일급시민
# 함수도 일반 변수와 동일한 특성을 갖는다

# 이름을 가진다
# 다른 변수에 대입할 수 있다
# 인수로 전달할 수 있다
# 리턴값이 될 수 있다.
# 컬렉션에 저장할 수 있다.
# -> 위와 같은 특성을 가지는 것을 일급시민이라고 함.

# 클래스, 일반함수도 일급시민이다.

# def add(a, b):
#     print(a+b)
    
# plus = add
# plus(1, 2)


def calc(op, a, b, c):              # 함수를 인자로 전달받을 수 있다. 
    op(a, b, c)
    
def add(a, b, c):
    print(a + b + c)

def multi(a, b, c):
    print(a * b * c)

calc(add, 1, 2, 3)
calc(multi, 3, 4, 5)