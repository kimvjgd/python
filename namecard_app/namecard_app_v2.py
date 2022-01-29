# 필요한 클래스
# NameCard      : 데이터클래스(모델 클래스)
# NameCardBook  : NameCard모델의 컬렉션 클래스

# Application 운영 클래스
#   데이터 : 앱타이틀, NameCardBook, 파일명
#   기능 : 초기화, 목록, 추가, 수정, 삭제, 검색, a종료

from namecard import NameCardBook
from baseapp import Application
from paging import Paginator

class NameCardBookApp(Application):
    
    def __init__(self) -> None:
        super().__init__('명함관리앱')
        self.book = NameCardBook()
        self.FILE_PATH = 'book.dat'
        

    def init(self):
        super().init()  # 메뉴구성
        self.book.load(self.FILE_PATH)
    
    def print_card_list(self, card_list, start = 0):
        print('-'*40)
        for ix, card in enumerate(card_list, start):
            print(f'{ix:3}  {card["name"]} {card["phone"]}')
        print('-'*40)

    

    def print(self):
        while True:
            # 페이지 단위로 출력
            page_num = int(input('페이지번호:'))
            if page_num == -1:  # -1 or 0 아무거나
                break   # or return 
            
            # 헤딩 페이지를 출력
            page_obj = self.book.get_page(page_num)
            print(f'aaaa{id(page_obj)}')
            self.print_card_list(page_obj.page, page_obj.start)
            print(f'[{page_num}/{page_obj.total_page}] 총{page_obj.total_count}건')


    def add(self):
        name = input('이름: ')
        phone = input('전화번호: ')
        email = input('email: ')
        address = input('주소: ')
        self.book.add(name, phone, email, address)
    
    def get_field(self, card, key, title):
        value = input(f'{title}({card[key]}): ')    # NameCard에서 __getitem__, __setitem__을 만들어놓았기에 attribute 접근이 가능
        if value == '':  # 무엇인가 값이 있다면
            # card[key] = value         원본을 외부에서 고치는 것은 비권장한다.
            value = card[key]   # 그냥 엔터를 치면 기존값으로 value를 준다.
        return value


    
    def update(self):
        name = input('수정할 이름: ')
        # name올 검색해서 card의 참조 취득
        ix = self.book.find(name)
        if ix != -1:
            card = self.book.get(ix)
            # card = self.book.book[ix] 가능은 하나 권장하지 않음(이유: 객체 지향에서는 비권장)
            name = self.get_field(card, 'name', '이름')
            phone = self.get_field(card, 'phone', '전화번호')
            email = self.get_field(card, 'email', 'email')
            address = self.get_field(card, 'address', '주소')
            self.book.update(ix, name, phone, email, address)
        else:
            print(f'{name}은/는 없는 항목에 이름입니다.')
    
    def search(self):
        name = input('검색할 이름: ')
        result = self.book.search(name)
        self.print_card_list(result)
        print(f'총 {len(result)}건')


    def remove(self):
        name = input('삭제할 이름: ')
        ix = self.book.find(name)
        if ix != -1:
            self.book.remove(ix)
            print(f'{name}을/를 삭제했습니다.')
        else:
            print(f'{name}은/는 존재하지 않습니다.')
            
    def exit(self):
        super().exit(lambda : self.book.save(self.FILE_PATH))
        pass
    
    def create_menu(self):
        self.menu.add_menu('목록',self.print)
        self.menu.add_menu('추가',self.add)
        self.menu.add_menu('수정',self.update)
        self.menu.add_menu('검색',self.search)
        self.menu.add_menu('삭제',self.remove)
        self.menu.add_menu('종료',self.exit) 
        
    
def main():
    app = NameCardBookApp()
    app.run()
    
main()