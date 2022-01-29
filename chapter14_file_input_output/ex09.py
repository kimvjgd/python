def main():
    datas = [12, 34, 56, 78, 90]
    # datas element들을 int에서 str으로 형변환
    # 1 data_list = [str(i) for i in datas]         comprehension이용 변환
    # 2 data_list = list(map(str, datas))           map이용 변환

    content = list(map(str, datas))
    
    # 리스트 --> '12,34,56,78,90'
    content = ','.join(content)

    

    
    
    
    # 리스트를 내용을 data.txt 파일로 저장하세요.
    
    try:
        with open('data.txt', 'wt') as file:            # 숫자만 있어서 encoding = utf-8을 해줄 필요가 없다.
            file.write(content)
    except Exception as e:
        print(e)


main()