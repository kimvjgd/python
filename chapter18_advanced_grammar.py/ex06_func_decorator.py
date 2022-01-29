# 함수 데코레이터
# 이미 만들어진 함수에 동작을 추가하는 파이썬 기법
# 함수를 래핑(wrapping)하여 함수의 앞 또는 뒤에 코드를 추가

import time

def inner():
    print('결과를 출력합니다.')

def hello():
    print('안녕하세요')


########################################
def outer(func):
    print('-'*20)
    func()
    print('-'*20)

def elapse(func):
    start = time.time()
    func()
    end = time.time()
    
    print(end-start)


########################################
def main():
    outer(inner)
    outer(hello)

elapse(main)