def work():
    str = "89점"
    score = int(str)
    print(score)


def main():
    try:
    #     work()
    # except ValueError as e:
    #     print(e)
    # except IndexError as e:
    #     print(e)
        work()
    except Exception as e:              # 모든 예외에 대해 처리
        print(e)
    
    print('작업완료')

main()