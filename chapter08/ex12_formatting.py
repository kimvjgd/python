def main():
    # s = '독도는 일본땅, 대마도는 일본땅'
    # print(s.replace('일본','한국'))
    
    # message = '안녕하세요. 김동현입니다.'
    # print(message.center(30))               # 30칸 중에 센터로 모아준다.
    
    # s = '독도는 한국땅, 대마도는 한국땅'
    # 중간에 있는 모든 공백을 제거하라.
    # '독도는한국땅,대마도는한국땅
    # print(s.replace(' ', ''))

    s = '억대연봉 일'
    print(f'나는 하고 싶은 {s}을 하면서 살고싶다.')
    
    hour = 7
    print(f'나는 {hour}시에 밥 먹을 거야')
    
    s1 = 'left'
    result1 = f'|{s1:<10}|'
    print(result1)
    
    s2 = 'mid'
    result2 = f'|{s2:^10}|'
    print(result2)
    
    s3 = 'right'
    result3 = f'|{s3:>10}|'
    print(result3)
    
main()