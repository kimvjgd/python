# 모듈
# 변수와 함수를 모두 한파일에 정의하면 관리가 힘들어진다.
# 비슷한 성격의 변수, 함수들을 파일 별로 나눠 정의
# 이렇게 정의한 파일을 모듈이라고 함
# 파일명이 모듈명이 된다.

import util

print('1inch = ', util.INCH)
print('~10 = ', util.calcsum(10))

# import util                   # 한번더 import 한다고 한들 위에서 import 한번만한다.

print('@@ex01.py', __name__)

# __name__ : 모듈명을 저장하고 있는 변수
# __main__ 으로 나온다.
# 실행의 주체가 되는 파일 -> __main__


# if __name__ == "__main__" :
    # 모듈 테스트 코드
# 모듈이 실행의 주체일때만 실행되게
# 만약 파일이 모듈로 쓸 것인데 테스트 하려면 여기 