# f.read()          : 파일 전체 내용
# f.read(n)         : n개의 내용
# f.readline()      : 한 줄
# f.readlines()     : 전체 라인 리스트 (각 라인의 끝에 개행 문자가 들어 있음)

def main():
    try:
        f = open('live.txt', 'rt', encoding='utf-8')
        text = f.read()
        lines = text.split('\n\n')

        for i, line in enumerate(lines, 1):     # 1부터 numbering하겠다.
            print(f'{i} - {line}')
        
        print(text)
    except FileNotFoundError:
        print('파일이 없습니다.')
    finally:
        f.close()
    
main()