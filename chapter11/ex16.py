def modify(x):
    # extra # x = [2,3,4,5]         == 참조를 바꿔라

    x[1] = 1000

    print(f'x: {x}')
    
def main():
    a = [10,20,30,40]
    modify(a)

    print(f'a: {a}')

main()

#ex15와 다르게 참조변수는 참조를 가져오기 떄문에 원본에 바로 적용이 된다.

# 2022/01/10 11:00~11:50 수업
# extra 로 x=[2,3,4,5]를 하면
# 새로운 참조값을 넣어라