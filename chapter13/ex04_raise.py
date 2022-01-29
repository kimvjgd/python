# raise
# 개발자에 의해 임의로 예외를 발생시킴

def calcsum(n):
    if n<0:
        raise ValueError
    
    total = 0
    for i in range(n+1):
        total += i
    return total

try:
    print("~10 = ", calcsum(10))
    print("~-5 = ", calcsum(-5))
except ValueError:
    print('입력값이 잘못되었습니다.')


try:
    print('네트워크 접속')
    a = 2/0
    print('네트워크 통신 수행')
except Exception as e:
    print(e)
finally:
    print('접속해제')    


# print('접속해제')    이렇게 하면 되지 않냐 왜 굳이 finally를 쓰냐?
# 밑에 작업을 성공한 경우에만 처리하려고 할때  finally를 사용해야한다. 아래에 예제가 있다.

print('작업완료')
# finally

def comm():
    try:
        print('네트워크 접속')
        a = 2/0
        print('네트워크 통신 수행')
    except Exception as e:
        print(e)
        return
    finally:
        print('접속해제')  

comm()

# 이런 경우에 cleanup 작업으로 finally가 쓰여야한다.
# 아니면 코드를 한눈에 보기 힘들 수 있다.