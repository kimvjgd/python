class Seq:
    def __init__(self, data):
        self.data = data
        self.index = -2
        
    def __iter__(self):             # 루프 시작할때 - 호출된다.
        self.index = -2             # 한번 다 돌때 초기화 해준다.
        return self
    
    def __next__(self):
        self.index += 2
        if self.index >= len(self.data):
            raise StopIteration                 # 얘 없으면 계속 루프가 돌게 된다.

        return self.data[self.index:self.index+2]
    
    
def main():        
    solarterm = Seq("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")

    for k in solarterm:
        print(k, end=',')
    print()
    print('-'*60)
        
    for k in solarterm:                         # 두번째 돌릴때 아무 데이터도 나오지 않는다.    -> Seq class에서 __iter__에서 index초기화 해줘야한다.
        print(k, end=',')
    print()
    print('-'*60) 
        
main()