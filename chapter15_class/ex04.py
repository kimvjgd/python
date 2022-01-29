# def xxx():
#     pass

# a = xxx              # xxx의 참조를 대입
# a = xxx()            # xxx의 리턴값을 대입

# 객체 = 객체명(인수)      # 인스턴스에대한 참조
# 객체 = 객체명           # 클래스 정의에 대한 참조




# 스택 개념
#
#   추상화!!!!(astract) : (스택 개념에 맞게 클래스를 설계하는 과정)
#
#   클래스 설계 : 다루는 데이터가 무엇인가? (데이터 타입?, 단일/여러개?)
#              그 데이터를 어떻게 처리(운영)하는가? (어떤 메서드가 필요한가?)
#                   저장, 데이터 꺼냄, 꺼내지않고 top 읽기


class Stack:
    def __init__(self) -> None:
        self.data = []
    
    def push(self, value):
        self.data.append(value)

    def pop(self):
        assert len(self.data) > 0, '스택이 비었습니다.'
        return self.data.pop()
    
    def read_top(self):
        assert len(self.data) > 0, '스택이 비었습니다.'
        top = self.data[-1]
        return top
    
    def is_empty(self):
        return len(self.data) == 0
    
    
    
def main():
    stack1 = Stack()
    
    stack1.push(10)
    stack1.push('홍길동')
    stack1.push(10)
    stack1.pop()
    stack1.pop()
    stack1.pop()
    
    stack2 = Stack()
    
    stack2.push(10)
    stack2.push('홍길동')
    stack2.push(10)
    stack1.pop()
    stack1.pop()
    stack2.pop()

    
    print(id(stack1.read_top()))
    print(id(stack2.read_top()))
    
    
main()