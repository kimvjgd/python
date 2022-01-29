
# 데이터(명함)를 표현하는 클래스 -> 데이터 클래스, 모델 클래스
class NameCard:
    def __init__(self,name,phone,email,address) -> None:         # 리턴 값이 None이다
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        
    def __str__(self) -> str:
        return f'<NameCard name={self.name}, phone={self.phone}, email={self.email}, address={self.address}>'
    
    def __repr__(self) -> str:      # 나를 나타내는 대표 정보
        return f'<NameCard name={self.name}>'
    
    
def main():
    card1 = NameCard('김동현', '010-5471-0000', 'kimvjgd@naver.com', '향기로 77')
    card2 = NameCard('김베컴', '010-1234-0000', 'beckham@naver.com', '향기로 77')
    print(card1.name, card1.phone, card1.email, card1.address)
    print(card1)
    print(card2.name, card2.phone, card2.email, card2.address)
    print(card2)
    book = [card1, card2]           # __repr__ 가 실행된다. - collection으로 들어가면 대표정보만 return 된다. - represent
    print(book)
    
    book = []
    
    for i in range(100):
        card = NameCard(f'홍길동{i:03}', f'010-1111-{i:04}', f'hong{i:03}@naver.com', '서울시')
        book.append(card)
    print(book)

main()