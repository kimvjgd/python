def flunk(s):
    return s < 60

def even(s):
    return s % 2 ==0

def elite(s):
    return s >= 90

# filter는 True와 False를 return 해준다.
# 원하는 데이터면 True를 return 해주고 아니면 False를 return 해준다.

def main():
    score = [45, 89, 82, 72, 53, 94]
    
    print('\n60미만')
    for s in filter(flunk, score):          
        print(s)
        
    print('\n짝수')
    for s in filter(even, score):
        print(s)
        
    print('\n90이상')
    for s in filter(elite, score):
        print(s)
        
    print('')
    
    high_scores = list(filter(elite,score))                 # 이렇게 따로 뺄 수 있다.
    print('{} 특별관리 대상\n\n'.format(high_scores))
        
    # filter 함수를 사용하지 말고 60점 미만 성적을 찾으세요.
    # new_list = []
    # for s in score:
    #     if(s<60):
    #         new_list.append(s)  
    # print(new_list)
    
    
      
main()




