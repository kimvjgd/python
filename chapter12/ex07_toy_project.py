import random
import sys
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

def create_card(name, phone, email, address):
    return {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }


def init(): # 초기화 함수
    for i in range(1, 101):
        card = create_card(f'홍길동{i:03}',f'010-1111-{i:04}',f'kimaaaa{i:03}@naver.com','서울시')
        books.append(card)
    random.shuffle(books)           # 한번 섞어봐주자
    books.sort(key=lambda card: card['name'])       # 이름으로 정렬해주고 싶으면 name

    # for card in books:
    #     print(card)

def print_menu():
    print()
    print('='*30)
    print('목록 || 검색 || 추가 || 종료')
    print('='*30)

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


    



# 종료 메뉴 실행 함수
def exit():
    answer = input('종료 하시겠습니까? Y / n : ')
    # if answer in ['Y', 'y']:  이렇게 해도 된다.
    # if answer == 'Y' or answer == 'y':
    
    if(answer.lower() == 'y'):
        sys.exit(0)
    elif(answer.lower() == 'n'):
        pass
    else:
        print('Y/n 중 하나를 입력해주세요.')



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
        elif(menu_item == '추가'):
            add_card()
        else:
            print('잘못 입력한 메뉴입니다.')


    
main()