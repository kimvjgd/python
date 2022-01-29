def main():
    
    # 디렉토리 구분자
    #   윈도우즈 : \
        # 근데 \는 escape문자이다   \\라고 써야하는데 그건 귀찮으니 그냥 / 도 되게함 ㅎㅎ
    #   맥, 리눅스: /
    
    # path(경로) : 파일 위치를 기술하는 문자열
    
    # 상대경로(relative path) - 현재 디렉토리를 기준으로 시작함
    # f = open('live.txt','rt',encoding='utf-8') 
    # f = open('data/live.txt','rt',encoding='utf-8')   #data folder에 있는 것
    
    # 절대경로 (absolute path)- 과거 디렉토리를 기준으로 시작함 -> 최상위 디렉토리를 (루트 디렉토리)리고 부른다.
    f = open('/Users/kimdonghyun/Documents/test/live.txt', 'rt', encoding='utf-8')

    
    rows = f.readlines()

    # print(rows)

    for row in rows:
        print(row, end="")

    f.close()
    
main()

# f = open('live.txt', 'rt', encoding='utf-8')

# for line in f:
#     print(line, end='')
    
# f.close()
# 이렇게 읽을 수도 있다.