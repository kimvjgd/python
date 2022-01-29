def modify(x):
    x = 1000
    print(f'x: {x}')
    
    
def main():

    a=10
    modify(a)   # x = a 가 실행된다.
    
    print(f'a:{a}')


# 매개변수로 전달된 값은 원본으로 전달되지 않는다.
# a는 어떠한 곳에 저장되어있고 x도 어떠한 곳에 저장되어있다.
# x에 a의 값 복사를 한다.
# 그러니 a에는 전혀 영향이 없다.

# 원본을 바꾸고 싶으면 modify function 에서 return x하고 
# a = modify(a) 로 해줘야한다.



main()