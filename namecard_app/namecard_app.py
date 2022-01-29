import random
import sys
from file_util import save_json, load_json

# 명함 관리 프로그램
# 관리할 명함 정보 : 이름, 전화번호, email, 주소 ==> 연라거(주소록) 관리

# 시작할 때 고려사항
# 1. 데이터를 어떻게 표현하고 관리할 것인가?
#   1- 한 사람의 정보 --> 사전
#   2- 여러명의 정보 --> 리스트
# 2. 어떤 기능을 제공할 것인가?
#   목록(검색), 추가, 수정, 삭제
#   CRUD 연산(Create Read Update Delete)
#   즐겨찾기, 그룹핑, 파일저장, 파일 로딩, ...  종료

books = []
FILE_NAME = 'book.json'

def create_card(name, phone, email, address):
    return {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }


def init(): # 초기화 함수
    global books                            # global 해줘야지 전역변수로 샤랄라!!!
    books = load_json(FILE_NAME)          # 주의!!!!!!!!!! 대입 연산자를 사용할때는 books가 지역변수이다!!
    # 처음에 아무런 데이터가 없을때 생성
    # for i in range(1, 101):
    #     card = create_card(f'홍길동{i:03}',f'010-1111-{i:04}',f'kimaaaa{i:03}@naver.com','서울시')
    #     books.append(card)                # 주의!!!!!!!!!!! 이럴때는 전역변수이다.
    # random.shuffle(books)           # 한번 섞어봐주자
    # books.sort(key=lambda card: card['name'])       # 이름으로 정렬해주고 싶으면 name

    # for card in books:
    #     print(card)

def print_menu():
    print()
    print('='*35)
    print('목록 || 검색 || 추가 || 수정 || 삭제 ||종료')
    print('='*35)

def add_card():
    name = input('이름 : ')
    phone = input('전화번호 : ')
    email = input('이메일 : ')
    address = input('주소 : ')
    card = create_card(name, phone, email, address)
    books.append(
        card
    )
    books.sort(key=lambda card: card['name'])

def print_card_list(card_list):
    for ix, card in enumerate(card_list):
        print(f'{ix:3}  {card["name"]} {card["phone"]}')
    print('-'*30)
    print(f'총: {len(card_list)}명')

# 목록 메뉴 실행 함수
def print_list():
    print_card_list(books)
# 검색 메뉴 실행 함수
def search():
    keyword = input('검색이름 : ')
    # 검색하고, 출력
    # 1) 직접 루프 돌려서 검색
    # result = []
    # for card in books:
    #     if keyword in card['name']:             # == 말고 in을 써야지 길동치면 100개가 다 나온다.
    #         result.append(card)
    
    # 2) filter로 검색
    result = list(filter(lambda card: keyword in card['name'], books))          # 연습하자!!!!!!!!! 이거 아직 많이 부족하다!!
    print_card_list(result)


def find_by_name(name):
    for ix, card in enumerate(books):           # 인덱스를 주기 위해 enumerate를 써야한다.
        if card['name'] == name:
            return ix
    return -1                   # for 밖에서 써줘야한다. for 문에서 else로 빼면 안맞자마자 -1로 함수가 끝나버린다.

    # 찾았으면 인덱스 리턴
    # 없으면 -1 리턴        -> False는 안된다, False는 0 index를 의미한다.




def update_card():
    # 이름입력 받기
    name = input('수정할 이름 : ')
    # 인덱스 찾기
    ix = find_by_name(name)
    # 있으면 ... 업데이트
    if ix != -1:
        #   기존 데이터 보여줌 이름(홍길동001):
        card = books[ix]            # 복사가 아니라 참조이다. 그래서 card를 수정해도 원본을 건드릴 수 있다. (card가 원본에 대한 참조변수이다.)
        name = input(f'이름({card["name"]}): ')
        if name != '':  # 무엇인가 값이 있다면
            card['name'] = name
            
        phone = input(f'전화번호({card["phone"]}): ')
        if phone != '':  # 무엇인가 값이 있다면
            card['phone'] = phone
            
        email = input(f'email({card["email"]}): ')
        if email != '':  # 무엇인가 값이 있다면
            card['email'] = email
            
        address = input(f'주소({card["address"]}): ')
        if address != '':  # 무엇인가 값이 있다면
            card['address'] = address
    
        print(f'{name} 항목을 수정했습니다.')
    else:
        print(f'{name} 항목이 없습니다.')    
        
    
    #   변경이 없으면 그냥 엔터
    #   변경할것이면 입력해서 수정처리
    # 없으면 ... 없음 출력
    
    
# 삭제 함수
def delete_card():
    name = input('삭제할 이름 : ')
    ix = find_by_name(name)
    if ix != -1:
        books.pop(ix)
        # or -> del books[ix]
        print(f'{name} 항목을 삭제했습니다.')
    else:
        print(f'{name} 항목이 없습니다.')

# 종료 메뉴 실행 함수
def exit():
    answer = input('종료 하시겠습니까? Y / n : ')
    # if answer in ['Y', 'y']:  이렇게 해도 된다.
    # if answer == 'Y' or answer == 'y':
    
    if(answer.lower() == 'y'):
        
        # book.json 파일로 저장하시오
        save_json(FILE_NAME, books)
        # print(load_json('book.json'))
        
        sys.exit(0)
   
   # json 파일을 command a로 모두 잡은 다음에 command k f 하면 json 형식으로 볼 수 있다. 
   



def main():
    init()
    while True:
        # 메뉴 출력
        print_menu()
        # 사용자가 메뉴를 입력
        menu_item = input("선택 > ")
        # 입력한 메뉴를 실행 / 결과 출력
        if(menu_item == '목록'):
            print_list()
        elif(menu_item == '검색'):
            search()
        elif(menu_item == '종료'):
            exit()
        elif(menu_item == '수정'):
            update_card()    
        elif(menu_item == '추가'):
            add_card()
        elif(menu_item == '삭제'):
            delete_card()
        else:
            print('잘못 입력한 메뉴입니다.')


    
main()