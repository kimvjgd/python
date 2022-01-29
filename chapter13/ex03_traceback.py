import traceback

mode = 'DEV'        # 'DEV' or 'PRODUCT'       - 개발모드냐 아니면 실제 운영하고 있는 운영모드냐             


def convert(value):
    return int(value)

def work():
    str = "89점"
    score = convert(str)
    print(score)


def main():
    try:
        work()
    except Exception as e:              # 모든 예외에 대해 처리
        print(e)
        if mode == 'DEV':
            traceback.print_exc()           # 트레이스로 볼 수 있다.     터미널의 에러창에서 몇번째 라인에서 오류가 난지 command 클릭하면 거기로 간다.
        
    print('작업완료')

main()