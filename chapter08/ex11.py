def main():
    # s='._.'
    # l='동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세'

    # print(s.join(l))
    
    names = ['또치', '둘리', '홍길동', '고길동']
    # names의 각이름을 한줄에 하나씩 출력하라
    print('\n'.join(names))
    
    # 각각을 하나의 문자열로 만들어라
    list = ','.join(names)
    print(list)
    
main()