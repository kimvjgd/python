# 클래스
# 관련 정보와 정보의 조작 함수(메서드)를 묶어서 관리
# 사용하기 위해서는 인스턴스를 생성한 후 사용

# ___뭐뭐뭐뭐___  : python 내부적으로 사용하는 함수, 변수

# class 내부의 모든 첫번째 인자는 self인자이고 그 뒤가 일반인자



# Heap이라는 영역에 관리정보가 입력이 된다. 그것에 대한 참조가 self이다.
class Account:
    def __init__(self, balance):    # 초기화를 담당하는 생성자 함수     # self는 인스턴스에 대한 참조 변수 - 파이썬이 자동으로 넣어준다.
        self.balance = balance      # heap에 있는 관리정보의 참조를 가져와서 거기에 일반인자 balance를 넣어준다.
                                    # 여기서 return self로 되어서 account instance에 참조값이 담긴다.
    
    def deposit(self, money):       # 여기서의 self는 참조값을 담고있는 account이다.
        self.balance += money
        
    def inquire(self):
        print(f"잔액은 {self.balance}원 입니다." )
                                    
                                    # 메서드는 Account 정보를 담고있는 메모리에 있고 다른 인스턴스에서 필요할때 공유해서 돌려쓴다.

def main():
    account = Account(8000)       # Account class의 인스턴스 생성     # 이때 자동으로 __init__함수가 호출된다.
    account.deposit(1000)
    account.inquire()

    donghyun = Account(8000)
    donghyun.deposit(10009000000000)
    donghyun.inquire()
    
    nonghyup = Account(1200000)
    nonghyup.inquire()
    
main()