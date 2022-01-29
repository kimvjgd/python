# assert - 주장하다, 단정하다, 단정문

# assert 조건, 메시지
# 조건이 True면 통과, 아니면 에러 메시지
def main():
    try:
        score = 128
        assert score <= 100, "점수는 100 이하여야 합니다."
        print(score)
    except Exception as e:
        print(f'error message : {e}')

    # score = 128
    # assert score <= 100, "점수는 100 이하여야 합니다."
    # print(score)
    # try 문으로 안넣어주면 밑에 있는 코드가 진행이 되지 않는다.
    
    print('그 다음 진행')
        
main()



# 예외 처리는 습관을 중요시 해야한다.

