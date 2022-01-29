# 방법 1
# class NameCard:
#     def __init__(self, name, phone, email, address='') -> None:           # address에 default값을 부여할 수 있다.
#         self.name = name
#         self.phone = phone
#         self.email = email
#         self.address = address
    
#     def __repr__(self):                     # 콜렉션 같은 곳에서 쓸때 나를 대표해서 나타난다.
#         return f'NameCard(name={self.name})'

#     def __str__(self):
#         return f'NameCard(name={self.name}, phone={self.phone}, email={self.email}, adderss={self.address})'

# represent 뺴고는 위와 똑같다!
from dataclasses import dataclass
from itertools import count
import os
# from file_util import load,save
import file_util        # 아래의 함수와 save가 이름이 겹쳐서 그냥 import 로
import math
from paging import Paginator

# 방법 2
@dataclass   # --> 생성자 정의, __repr__(), __str__() 자동 추가된다.
class NameCard:
    name: str
    phone: str
    email: str
    address: str = ''    # Default 값을 배정할 수 있다.

    def __getitem__(self, key):                 # 이 코드가 있어야 밖에서 card[key] 이렇게 쓸수 있는 것이다. namecard_app_v2.py안에 있는 get_field에서 확인해보자
        return getattr(self, key)
        
    
    def __setitem__(self, key, value):
        return setattr(self, key,value)
    
    # json 모듈: 파이썬 표준 모듈만 처리 가능.
    
# NameCardBook 클래스   SRP: 단일책임의 원칙            #single responsibility priciple
#   NameCard 모델 클래스의 콜렉션 역할
#   데이터: NameCard 목록
#   기능 : 추가, 수정, 삭제, 검색
    
    
class NameCardBook:
    
    def __init__(self) -> None:
        self.book = []
    
    # 페이지 목록 추출
    def get_page(self, page_num, count_per_page=10):            # count_per_page : 한 페이지에 몇개로 할꺼냐? 디폴트는 10
        # 리턴값: 해당 페이지의 데이터 목록, 전체 페이지 수를 리턴할 것이다.
        page_obj = Paginator(self.book, page_num, count_per_page)
        
        return page_obj

    
    
    def add(self, name, phone, email, address):
        card = NameCard(name, phone, email, address)
        self.book.append(card)
        self.book.sort(key= lambda card: card.name)

        
    def update(self, ix, name, phone, email, address):
        card = self.book[ix]
        card.name = name
        card.phone = phone
        card.email = email
        card.address = address
    
    def remove(self, ix):           # delete라는 예약어가 있을 떄가 있다.   그것과 충돌을 막기위해 삭제는 이제 remove를 사용하는 것을 권장한다.
        # ix = self.find(name)      # parameter에 ix대신 name 넣을 수 있다.. <- 난 이게 더 좋은 것 같은데.. 힝
        if ix != -1:
            self.book.pop(ix)

    def search(self, name):     # 포함으로 검색, 리스트 리턴
        result = list(filter(lambda card: name in card.name, self.book))          # 연습하자!!!!!!!!! 이거 아직 많이 부족하다!!
        return result
    
    def find(self, name):                   # 있으면 index값을 반환하고 없으면 -1을 return
        for ix, card in enumerate(self.book):           # 인덱스를 주기 위해 enumerate를 써야한다.
            if card.name == name:
                return ix
        return -1
    
    # 인덱스로 참조값을 얻는 메서드
    def get(self, ix):
        return self.book[ix]
    
    def load(self, file_path):          # json말고 이번에 pickle 관리하겠다. -> json으로 저장하기 위해서는 따로 라이브러리를 사용해야한다.
        # file_path의 파일이 실제 존재하는지 검사
        if os.path.exists(file_path):
            self.book = file_util.load(file_path)
        else:   # 파일이 없는경우
            self.book = []

    def save(self, file_path):
        file_util.save(file_path, self.book)
        
if __name__ == "__main__":          # 모듈 테스트
    import random       # 테스트 과정에서만 쓰여서 여기에다가 배정을 했다.
    
    card = NameCard('홍길동', '010-5471-0000','kimvjgd@naver.com','서울특별시 서대문구 연희동')
    print(card)
    print([card])
    
    book = NameCardBook()
    book.add('홍길동3', '010-1111-1111', 'hong1@naver.com','서울시')
    book.add('홍길동2', '010-1111-1111', 'hong1@naver.com','서울시')
    book.add('홍길동4', '010-1111-1111', 'hong1@naver.com','서울시')
    book.add('홍길동1', '010-1111-11112', 'hong1@naver.com2','서울시')
    print(book.book)

    print('검색 테스트')
    result = book.search('길동')
    print(result)
    result = book.search('동1')
    print(result)
    
    print('find 검색 테스트')
    ix = book.find('홍길동2')
    print(ix)
    ix = book.find('홍길동3')
    print(ix)
    
    print('삭제 테스트')
    book.remove(0)
    print(book.book)
    
    # print('저장 테스트')
    # book.save('book.dat')
    
    # print('로딩 테스트')
    # book.load('test.dat')           # 파일이 존재하지 않는 경우
    # print(book.book)
    # book.load('book.dat')           # 파일이 존재하는 경우
    # print(book.book)
    
    # book.book = []
    # addresses = ['서울', '부산', '대구', '광주', '인천','성남','제주']
    # for i in range(1, 101):
    #     address = random.choice(addresses)
    #     book.add(f'홍길동{i:03}', f'010-0000-{i:04}', f'hong{i:03}@naver.com',address)    

    # print(book.book)
    # book.save('book.dat')
    
    # # print('*'*50)
    # # 주소부분으로 정렬하라
    # # orderby = 'address'
    # # book.book.sort(key=lambda card : card[orderby])         # card['address]
    # # print(book.book)
    
    # # 이름부분으로 정렬하라
    # # orderby = 'name'
    # # book.book.sort(key=lambda card : card[orderby])         # card['address]
    # # print(book.book)