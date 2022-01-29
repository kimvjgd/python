def calcscore(name, *score, **option):
    print(name)
    total = 0
    for s in score:

        total += s
    
    print("총점 ; ",total)
    # if(option['avg'] == True):
    if option.get('avg'):            # 'avg' 키가 없으면 None -> 디폴트 False 처리가 된다.
        print("평균 ; ", total/len(score))
    print()



def main():
    # calcscore('홍길동', 88, 99, 77, avg=True)
    # calcscore('고길동', 99, 88, 75, 34, avg=False)
    # calcscore('김동현',100,100)
    
    hong_score = [88, 99, 77]
    go_score = [99, 8, 65, 43]
    
    option = {
        'avg' : True,
        'total': True,
    }
    calcscore('aa',*hong_score, avg=True)           # 아!! hong_score가 하나가 통째로 간다. 튜플중 1개가 리스트 *로 풀어줘야한다.
    calcscore('bb', *go_score, **option)            # dictionary를 펼치는 건 ** 이다. list 펼치는 게 * 이다.
main()