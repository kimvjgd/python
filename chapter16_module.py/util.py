INCH = 2.54

def calcsum(n):
    sum = 0
    
    for num in range(n+1):
        sum += num
    return sum

# print('@@util.py', __name__)          여기다 쓰면 실행문에 있어서 다른곳에서 import 하면 저절로 실행된다.


if __name__ == "__main__":          # 모듈 테스트하기 위해서 만들었다.   여기서 실행하면 돌고 다른곳에서 실행하면 돌지 않는다.
    print('@@util.py', __name__)
    print(INCH)
    print(calcsum(100))
