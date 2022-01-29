from namecard import NameCardBook
import random

def main():
    book = NameCardBook()
    
    # 200개 데이터를 구성해서 book.dat로 저장

    addresses = ['서울', '부산', '대구', '광주', '인천','성남','제주']
    for i in range(1, 101):
        address = random.choice(addresses)
        book.add(f'홍길동{i:03}', f'010-0000-{i:04}', f'hong{i:03}@naver.com',address)    

    print(book.book)
    book.save('book.dat')

    # book.book을 orderby 변수값을 기준으로 정렬하세요.
    
    print('*'*50)
    # 주소부분으로 정렬하라
    orderby = 'address'
    book.book.sort(key=lambda card : card[orderby])         # card['address]
    print(book.book)
    
    # 이름부분으로 정렬하라
    orderby = 'name'
    book.book.sort(key=lambda card : card[orderby])         # card['address]
    print(book.book)
    
    
main()    