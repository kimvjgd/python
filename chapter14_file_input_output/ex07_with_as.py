# open() 함수와 함께 with ~ as 문을 사용하면 명시적으로 close() 함수를 호출하지 않아도 파일이 항상 닫힘 (auto close기능 제공)


# file = open('live.txt','rt',encoding='utf-8')


def main():
    try:
        with open('live.txt', 'rt', encoding='utf-8') as file:
            str= file.read()
            print(str)
            # file.close()
    except Exception as e:
        print(e)
        
main()