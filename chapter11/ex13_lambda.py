lambda x: x+ 1          # 앞의 x가 매개변수 1개, x+1이 본문이고 자동으로 return 된다.
# def increase(x):
#     return x+1           -> lambda x: x+1



# 람다 함수는 한줄로 구현 가능한 코드를 매개변수로 전달하는 상황에서 쓰인다.

score = [45,89,72,53,94]
for s in filter(lambda x: x<60, score):
    print(s)
    
print('\ncheck high score')
for s in filter(lambda x: x>=90, score):
        print(s)
        
for s in map(lambda x: x/2, score):
    print(s, end = ", ")
    
print('\n')
# def div2(x):
#     return x/2
# for s in map(div2, score):
#     print(s, end= ', ')