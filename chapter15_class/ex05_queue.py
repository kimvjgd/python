# 큐, Queue : First In First Out
# 클래스 설계
#   클래스명 : Queue
#       데이터: 리스트
#       기능: 추가, 꺼내기, 꺼내지 않고 읽기, 비었는지 검사


# 클래스 설계 원칙 : SRP: 단일 책임의 원칙
class Queue:
    def __init__(self) -> None:
        self.data = []
        
    def put(self, value):
        self.data.append(value)
        
    def get(self):
        assert not self.is_empty(), '큐가 비었습니다.'
        return self.data.pop(0)
    
    def read_front(self):
        assert not self.is_empty(), '큐가 비었습니다.'
        return self.data[0]
    
    def is_empty(self):
        return len(self.data) == 0

def main():
    q = Queue()
    q.put(1)
    q.put(10)
    q.put(100)
    q.put(1000)
    
    # 무조건 꺼내는 것(예외 발생할 수 있다.)
    print(q.get())
    print(q.get())
    print(q.get())

    # 데이터가 있는지 검사해서 꺼내겠다
    if(not q.is_empty()):
        print(q.get())
    
    
main()
