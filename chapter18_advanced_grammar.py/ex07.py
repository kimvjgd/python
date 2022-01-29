import time

def inner():
    print('결과를 출력합니다')
    
def outer(func):            # 1) 장식자 함수는 내부 함수를 리턴    2) 원래함수 이름으로 내부함수를 다시 바꾼다. 
    def wrapper():
        print('-'*20)
        func()
        print('-'*20)
    return wrapper

# inner = outer(inner)    # -> return wrapper(내장 함수 리턴)                 outer안에 있는 inner를 다시 inner로 바꿔준다.
# inner()             #-> wrapper를 호출한다.

def elapse(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        
        print(f'{func.__name__} 함수 실행 시간: {end-start}')           # func.__name__실제 함수의 이름을 나타냄
    return wrapper


# 13번째 줄을 아래와 같이 쓸 수 있다.!!!!!!!!!
@outer          #  inner = outer(inner)
def inner():
    print('결과를 출력합니다.')

@elapse
@outer                              # 이렇게 데코레이터를 여러개 붙힐 수 있다.      inner = elapse(outer(inner))
def inner1():
    print('결과를 출력합니다.')

print('\n\n\n')
inner()
print('\n\n\n')
inner1()
print('\n\n\n')