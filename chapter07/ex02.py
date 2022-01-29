# 가변 인수
# 인수의 수가 고정되지 않음
# 호출시 원하는 만큼 인수를 지정
# 함수에서는 튜플 변수로 받음
# 일반 인수 뒤에만 올 수 있음
# 하나만 사용 가능

def calrange(*ints):
    total = 0
    print('type',type(ints))            # 튜플로 저장된다.
    for num in ints:
        total += num
    return total
print(calrange(1,2,3,4))
print(calrange(1,2,3,4,5,6,7,8,9,10))

