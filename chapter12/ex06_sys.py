import sys
def main():
    print("버전 : ", sys.version)
    print('플랫폼 : ', sys.platform)
    print('바이트 순서 : ', sys.byteorder)
    print('모듈 경로 : ', sys.path)

    for p in sys.path:
        print(p)

    sys.exit(0)                     # 이 중 우리가 가장 많이 쓸 것 - 프로그램을 종료시킨다.
                                    # exit안의 0은 정상종료를 나타냄 - 다른 숫자들은 비정상적인 종료를 나타낸다.
    print('종료합니다.')               # 프로그램이 이미 종료돼서 실행이 안된다.
    
main()