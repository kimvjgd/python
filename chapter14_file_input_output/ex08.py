# 텍스트 파일을 읽어서 내용을 리턴하는 함수를 작성하세요.
# 매개변수: 파일명
# 리턴값: 파일의 내용
def load(filename):
    try:
        with open(filename, 'rt', encoding='utf-8') as file:
            content = file.read()
            return content
    except:
        return ''
        
def save(filename, content):
    with open(filename, 'wt', encoding='utf-8') as file:
        file.write(content)
    
    
def main():
    try:    
        file_name = 'live.txt'
        content = load(file_name)
        print(content)
        
        # save('live2.txt', content)        #<- 이건 파일 복사
        
        
        # 파일 수정후
        text = input('추가할 내용 : ')
        content += text + '\n'
        save(file_name, content)
        # save(filename)
    except Exception as e:
        print(e)
main()