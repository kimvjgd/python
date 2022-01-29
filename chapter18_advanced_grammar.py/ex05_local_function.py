# 지역 함수
# 함수 안에 함수를 정의
# 함수가 정의된 함수 내에서만 사용 가능 -> 함수의 이름 충돌을 방지
# 지역함수를 리턴한 경우 -> 함수 밖에서도 사용 가능하다.


# def calcsum(n):
#     def add(a, b):
#         return a+b

#     total = 0
#     for i in range(n+1):
#         total = add(total, i)
#     return total

# def main():
#     print('~10 = ', calcsum(10))
#     # print(add(10, 20))            # 지역 함수는 함수 밖에서 사용 불가 

# main()

def makeHello(message):
    def hello(name):
        print(message + ", " + name)
    return hello


enghello = makeHello('Good Morning')
kohello = makeHello('안녕하세요')

print(enghello)

enghello("Mr Kim")
kohello("홍길동")

print(enghello)

