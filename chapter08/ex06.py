def main():
    names = ['홍길동', '고길동', '둘리', '또치']
    search_name = input("검색 이름 > ")
    name_list = []
        
    for name in names:
        if search_name in name:
            name_list.append(name)
    
    print(name_list)
    
    
main()