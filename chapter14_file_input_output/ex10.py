# data.txt 파일을 읽어서
# datas = [12,34,56,78,90] 리스트로 복원하라


def main():
    with open('data.txt', 'rt') as file:
        content = file.read()
        print(content)
    datas = content.split(',')
    datas = list(map(int, datas))
    print(datas)
    
    
main()