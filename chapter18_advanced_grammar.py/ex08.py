from dataclasses import dataclass

@dataclass   # --> 생성자 정의, __repr__(), __str__() 자동 추가된다.
class NameCard:
    name: str
    phone: str = ''
    email: str = ''
    address: str = ''
    
    def print(self):
        print(self.name)
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        return setattr(self, key, value)


def main():
    card = NameCard('김동현', '010-5471-0000')
    print(card)             # 여기의 print는 그냥 python의 print
    
    name = getattr(card, 'name')        # attribute가 객체의 속성       # name = card.name과 같은 동작이다.
    print(name)
    
    setattr(card, 'email', 'dong@naver.com')        # card.email = 'dong@naver.com'
    print(card)
    
    func = getattr(card, 'print')       # 이건 method를 불러옴
    func()
    
    key = 'name'
    value = getattr(card, key)
    print(value)
    print(card[key])          # 이렇게 읽고 싶으면 __getitem__(self, key) 호출됨
    
    key = 'address'
    value = '서울시'
    setattr(card, key, value)
    card[key] = '서울시'        # 이렇게 쓰고 싶다면 __setitem__(self, key, value) 호출됨
    
    print(card)
    
    print()
    # print(card['name'])
    print(card.name)
    
main()

