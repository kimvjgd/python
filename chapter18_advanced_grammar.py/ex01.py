# 2022 / 01 / 17 

# 열거 가능 객체
# for 반본문의 순회 대상 객체

# for x in xxx:                                   # xxx.__iter__() 처음에 xxx나올때 객체 생성
#     x = it.__next__()                           # 루프를 돌때마다   -> 매 루프마다 __next__()함수를 통해 다음 요소를 추출
                                                  # 더이상 return 할 것이 없으면 예외 발생   -> StopIteration예외가 발생하고 for 문을 끝낸다.
                                                  
nums = [11,22,33]

it = iter(nums)             #-> __iter__() -> 일반함수 iter()    
while True:
    try: 
        num = next(it)      #-> __next__() -> 일반함수 next()
    except StopIteration:
        break
    print(num)
    
